# Docker Deployment and Daily Scheduled Synchronization

## Purpose

This deployment runs the complete scraper and Vector Store delta sync
automatically once per day. The job is packaged as a one-shot Docker image and
scheduled by GitHub Actions. No permanently running web server is required: a
container starts, performs one synchronization, emits logs/reports, and exits.

## Deployment architecture

```text
GitHub Actions scheduler / manual dispatch
                  |
                  v
        Ubuntu hosted runner
                  |
                  v
       docker build from Dockerfile
                  |
                  v
   one-shot non-root application container
                  |
      +-----------+------------------+
      |                              |
      v                              v
OptiSigns Zendesk API       OpenAI Vector Store API
      |                              |
      +---------------+--------------+
                      v
          console log + JSON report
                      |
                      v
       GitHub Actions artifact (30 days)
```

GitHub Actions supplies compute and scheduling. Docker supplies a repeatable
runtime. Docker Desktop is only needed to build and run that same image on a
developer workstation.

## Docker image

### Base and runtime behavior

The `Dockerfile` uses `python:3.13-slim`, sets `/app` as the working directory,
and enables:

- immediate unbuffered logs;
- no generated Python bytecode;
- no pip download cache in the final image.

Dependencies are installed from `requirements.txt` before application code is
copied, allowing Docker to reuse the dependency layer when only source code
changes.

### Security and included data

The image creates and runs as the unprivileged `app` user. It copies:

- `main.py`;
- the `src/` Python package;
- `data/markdown/` as the baseline used to bootstrap legacy Vector Store file
  attributes.

Secrets are not baked into the image. `.env`, local state, tests, Git history,
PDFs, caches, and generated artifacts are excluded by `.dockerignore`.

### One-shot command

The container entry point is:

```text
python main.py
```

and its default argument is `--all`. Therefore, running the image without extra
arguments performs one complete corpus sync and then exits.

Local Docker verification:

```powershell
# Build the image from the repository root.
docker build -t optibot-daily-sync .

# Run one full sync using secrets from the local .env file.
docker run --rm --env-file .env optibot-daily-sync --all

# Optional safe comparison against an existing Vector Store.
docker run --rm --env-file .env optibot-daily-sync --all --dry-run
```

`--rm` deletes the stopped container, not the image and not the remote Vector
Store. In Docker Desktop, the image appears under **Images** while a running
invocation temporarily appears under **Containers**. Because this is a
one-shot job, the container normally disappears after completion.

For example, after `docker build`, Docker Desktop keeps an image named
`optibot-daily-sync`. When `docker run` starts, a temporary container executes
`python main.py --all`. A successful process exits with code 0; `--rm` then
removes that container while the reusable image remains available for the next
run.

## GitHub Actions workflow

### Triggers and schedule

The workflow supports two triggers:

- `workflow_dispatch` for manual testing from the Actions tab;
- `schedule` for automatic daily execution.

The cron expression is:

```yaml
cron: "17 2 * * *"
timezone: "Asia/Ho_Chi_Minh"
```

This means once per day at **02:17 Vietnam time**. The non-round minute reduces
contention near the top of the hour. Scheduled jobs can start a little later
when GitHub-hosted runners are busy, so the Actions run history is the source
of truth for actual start time.

Reading the five cron fields from left to right makes the expression explicit:

```text
17  2  *  *  *
|   |  |  |  +-- every day of the week
|   |  |  +----- every month
|   |  +-------- every day of the month
|   +----------- hour 02
+--------------- minute 17
```

For example, a run listed as `schedule` at approximately 02:17 on Wednesday is
an automatic cron run. A run listed as `workflow_dispatch` at 15:00 was started
manually and does not, by itself, prove that the scheduler fired.

### Permissions, concurrency, and timeout

- Repository permission is restricted to `contents: read`.
- The job runs on `ubuntu-latest`.
- `timeout-minutes: 30` prevents an indefinitely stuck sync.
- Concurrency group `daily-optibot-sync` allows only one active daily sync.
- `cancel-in-progress: false` lets the current data mutation finish instead of
  replacing it with a newer trigger halfway through.

### Secrets

The repository must define these GitHub Actions secrets:

```text
OPENAI_API_KEY
OPENAI_VECTOR_STORE_ID
```

They are injected as environment variables at runtime. The workflow explicitly
validates both before building/running the job. The Vector Store ID should be
the same store connected to the OptiBot Assistant.

### Job pipeline

Each run performs these steps:

1. **Check out repository** using `actions/checkout@v6`.
2. **Validate deployment secrets** and fail early when either is absent.
3. **Build one-shot job image** as `optibot-daily-sync`.
4. **Create writable artifact directories** on the runner.
5. **Run the container**, forwarding only the two required environment
   variables.
6. **Mount `$GITHUB_WORKSPACE/artifacts` at `/app/artifacts`** so reports and
   logs survive container removal.
7. **Pipe stdout/stderr through `tee`** into
   `artifacts/logs/daily-sync.log` while retaining live Actions output.
8. **Publish the JSON report and log** using `actions/upload-artifact@v7`, even
   when an earlier step fails.

`set -o pipefail` is important: without it, `tee` could return success and hide
a failed container exit code.

Example success flow:

```text
GitHub scheduler fires
  -> checkout succeeds
  -> both secrets are present
  -> Docker image builds
  -> container reports added=0 updated=0 skipped=402 removed=0
  -> container exits 0
  -> log and JSON report are uploaded
  -> workflow receives a green check
```

An all-skipped delta is still a useful successful run: it proves the source was
checked and the Vector Store was already current.

### Artifacts and observability

The uploaded artifact is named:

```text
daily-sync-<run number>-<run attempt>
```

Including the attempt avoids collisions when a run is retried. Artifacts are
retained for 30 days and contain, when available:

```text
artifacts/logs/daily-sync.log
artifacts/run_reports/daily_sync_<UTC timestamp>.json
```

The console log shows pagination, delta counts, Vector Store ID, chunk estimate,
and final result. The JSON report is the structured audit record for scrape,
delta, chunking, uploads, removals, duplicates, and Vector Store usage.

For run number 12, attempt 2, the artifact name is `daily-sync-12-2`. It differs
from `daily-sync-12-1`, so diagnostics from the original failed attempt are not
overwritten by the rerun.

## How to verify the cron

1. Open the repository's **Actions** tab.
2. Select **Daily OptiBot Sync**.
3. Confirm a run appears with event `schedule`, rather than only
   `workflow_dispatch`.
4. Open the `sync` job and verify every step is green.
5. Download the artifact and inspect both the log and JSON report.
6. Confirm the report timestamp and delta counts match the expected daily run.

A successful manual run proves the image, credentials, API access, and pipeline
work. A later run marked as scheduled proves the cron trigger itself works.

## State model in CI

The GitHub runner and container are ephemeral. `data/state` is not persisted by
the workflow, and it is not required in CI because
`OPENAI_VECTOR_STORE_ID` identifies the target store while remote file
attributes act as the synchronization manifest.

`data/markdown` inside the image provides a bootstrap baseline for older remote
files without attributes. The newly scraped mirror exists only for that run;
the durable operational outputs are the remote Vector Store and uploaded
Actions artifacts.

## Failure and retry behavior

- Missing secrets fail before any container execution.
- Docker build errors fail the job.
- Scraper/OpenAI failures propagate through the container exit code and
  `pipefail`.
- The artifact step uses `if: always()`, preserving whatever diagnostics were
  produced before failure.
- GitHub does not automatically retry this workflow; use **Re-run jobs** or
  `workflow_dispatch` after correcting the cause.
- Application-level HTTP/OpenAI retries remain active inside the container.
- Delta sync idempotency makes reruns safe: unchanged files are skipped and
  eventually consistent duplicate copies are cleaned up.

## Related files

| File | Responsibility |
| --- | --- |
| [`.github/workflows/daily-sync.yml`](../.github/workflows/daily-sync.yml) | Daily/manual triggers, secrets, Docker execution, logging, and artifacts. |
| [`Dockerfile`](../Dockerfile) | Reproducible Python image and one-shot non-root runtime. |
| [`.dockerignore`](../.dockerignore) | Excludes secrets, local tooling, state, tests, and generated output from build context. |
| [`.env.example`](../.env.example) | Documents the two runtime variables without containing real secrets. |
| [`main.py`](../main.py) | Process entry point used by the Docker image. |
| [`requirements.txt`](../requirements.txt) | Locked major-version ranges installed during image build. |
| [`src/support_ingestion/pipeline/daily_sync.py`](../src/support_ingestion/pipeline/daily_sync.py) | One-shot application workflow executed by the scheduled container. |
| `artifacts/logs/` (generated at runtime) | Local/mounted plain-text execution logs. |
| [`artifacts/run_reports/`](../artifacts/run_reports/) | Structured per-run JSON reports uploaded by GitHub Actions. |
| [`README.md`](../README.md) | Short setup, local/Docker commands, job links, and Assistant screenshot. |
