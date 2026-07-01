# RAG Ingestion, Chunking, and Vector Store Synchronization

## Purpose

This pipeline turns the scraped Markdown corpus into the knowledge base used by
the OptiBot Assistant. It estimates token/chunk volume, compares the newest
corpus with the files already indexed in an OpenAI Vector Store, and applies
only the changed files.

The implementation is an idempotent file-level delta sync. Re-running an
unchanged corpus should classify every document as `skipped`, avoid duplicate
uploads, and leave retrieval data unchanged.

## What RAG means here

RAG stands for **Retrieval-Augmented Generation**. Instead of expecting the
language model to remember every OptiSigns support article, the system first
retrieves small relevant passages from the uploaded knowledge base. It then
adds those passages to the model's context before the model writes the answer.

```text
Retrieval:  find relevant support passages for the user's question
Augmented:  place those passages in the model's temporary input context
Generation: write a grounded answer from that retrieved context
```

This creates two separate pipelines:

1. **Ingestion/indexing pipeline**, run by the daily synchronization job when
   documents are added or changed.
2. **Question-answering pipeline**, run by File Search whenever a user asks the
   Assistant a question.

The daily job does not generate customer answers. The Assistant does not
rescrape Zendesk. They meet at the OpenAI Vector Store.

## Ingestion and indexing pipeline

```text
Zendesk JSON article
        |
        v
HTML parser and cleaner
        |
        v
Normalized UTF-8 Markdown
        |
        v
Local manifest: Article ID + filename + SHA-256
        |
        v
Delta planner: added / updated / skipped / removed
        |
        v
OpenAI File object (only added or updated files)
        |
        v
Vector Store attachment with attributes + chunking strategy
        |
        v
Hosted Markdown parsing -> token chunks -> embeddings -> vector index
        |
        v
Searchable knowledge base
```

### 1. Source parsing and normalization

The first parser is local and explicit. `ZendeskClient` returns a JSON article;
`converter.py` parses the article's HTML body with BeautifulSoup, removes page
chrome, and converts the remaining content to Markdown. Metadata is placed at
the top of the same document:

```markdown
# How to use YouTube with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/...
Article ID: 360051014713
Last Updated: 2026-06-30T10:00:00Z

## Add the YouTube app

Open Files/Assets and select YouTube...
```

Markdown is useful here because headings, lists, links, and code remain
readable while navigation and decorative HTML have already been removed. The
file is UTF-8, a format accepted by Vector Store ingestion.

The second parsing stage is hosted. After upload, OpenAI reads the Markdown
file and extracts indexable text. Its internal parser implementation is not
part of this repository; the application observes ingestion status such as
`completed` rather than receiving the parser's internal syntax tree.

### 2. File-level change detection before indexing

The local pipeline extracts the stable `Article ID` and hashes the exact file
bytes. It compares those values with attributes on the existing remote file.
This check happens before chunking so unchanged articles never need to be
uploaded and re-embedded.

Example:

```text
Yesterday: article_id=42, sha256=AAA, filename=install-player.md
Today:     article_id=42, sha256=AAA, filename=install-player.md
Result:    skipped; no parsing, chunking, embedding, or indexing request
```

If the hash changes to `BBB`, the complete Markdown file is treated as an
updated version. Chunk-level diffing is not attempted: OpenAI indexes the new
file, and the old file is removed only after the replacement is ready.

### 3. Hosted chunk creation

A long document cannot be placed into retrieval as one indivisible block. The
Vector Store therefore splits its parsed text into overlapping token windows.
This project sends a static strategy of 1,200 tokens per chunk with 200 tokens
of overlap.

```text
Document tokens: 1 ................................................. 2201

Chunk 1:         [1 -------------------------- 1200]
Chunk 2:                         [1001 ------------------------ 2200]
Chunk 3:                                           [2001 ---- 2201]
                                  ^ 200-token overlap ^
```

The 1,000-token stride is `1,200 - 200`. Overlap preserves context across a
boundary. For example, if a setup instruction begins at token 1,150 and ends
at token 1,230, both halves are available together in Chunk 2.

The estimate in `chunking.py` predicts how many chunks this strategy should
produce for reporting. The real chunks are created asynchronously by OpenAI
when `create_and_poll()` attaches the file.

### 4. Embedding generation

An embedding is a numeric vector that represents the meaning of a text chunk.
Conceptually, a chunk becomes a long list of numbers:

```text
"Paste the YouTube URL and click Save"
    -> [0.018, -0.421, 0.073, ..., 0.206]
```

The numbers above are illustrative, not real output. Texts with related meaning
are positioned closer together in vector space even when they do not contain
exactly the same words. That is why a query containing "show a YouTube clip"
can still retrieve a passage that says "add a YouTube video".

With hosted File Search, the application does not select an embedding model,
request raw embedding arrays, or store those arrays itself. OpenAI performs
embedding as part of Vector Store ingestion. The repository stores only the
source file identity and synchronization attributes.

### 5. Vector index construction

The Vector Store acts as the searchable index. Each indexed chunk remains
associated with its source `file_id`, filename, and file attributes. At a
conceptual level it contains records like:

```text
chunk text + embedding vector + source file association + attributes
```

The exact internal index structure is managed by OpenAI and is not exposed as
a local FAISS, Chroma, or Pinecone database. The application waits until every
file in the batch reports `completed`; only then can the new chunks be assumed
ready for retrieval.

## Repository synchronization pipeline

### 1. Resolve the Vector Store

`main.py` resolves the Vector Store ID in this order:

1. `--vector-store-id` command-line argument;
2. `OPENAI_VECTOR_STORE_ID` loaded from `.env` or the process environment;
3. `vector_store_id` from `data/state/vector_store.json`;
4. create a new store when none is available.

New stores are named `OptiBot Support Knowledge Base` and record corpus and
chunking metadata. `OPENAI_API_KEY` is mandatory for all non-scrape-only runs.
The OpenAI client uses four retries and a 90-second timeout.

For example, this invocation wins over both `.env` and the state file because
the explicit CLI value has the highest priority:

```powershell
python main.py --all --vector-store-id vs_cli_example
```

Without that argument, `OPENAI_VECTOR_STORE_ID=vs_env_example` is used. If the
environment variable is also absent, the resolver can reuse the ID recorded in
the local state JSON.

### 2. Load the remote manifest

Each attached Vector Store file is expected to have these attributes:

```text
article_id = stable Zendesk article ID
filename   = generated Markdown filename
sha256     = hash of the exact Markdown bytes
```

The synchronizer pages through all remote files and requires each file status
to be `completed`. The manifest is keyed by `article_id`, which remains stable
even when an article title and filename change.

One remote manifest entry conceptually looks like this:

```json
{
  "article_id": "360051014713",
  "filename": "how-to-use-youtube-with-optisigns.md",
  "sha256": "f8d8...64-hex-characters...",
  "file_id": "file_abc123"
}
```

If the title later changes, the filename may change, but article
`360051014713` is still recognized as the same logical document.

For files uploaded before attributes were introduced, the synchronizer can
bootstrap metadata by matching the remote filename with `data/markdown`. If no
safe local match exists, it stops rather than guessing document identity.

Because OpenAI deletion can be eventually consistent, two completed files for
the same article may temporarily appear. The newest `(created_at, file_id)` is
kept as current and stale copies are queued for cleanup.

### 3. Build the local manifest

The full daily job first runs the scraper into a temporary directory. It then:

- requires at least 30 non-empty `.md` files;
- extracts `Article ID:` with a strict multiline pattern;
- rejects missing or duplicate article IDs;
- hashes the exact file bytes with SHA-256;
- stores `article_id`, `filename`, `sha256`, and local path.

Sorted input paths make planning and reports deterministic.

For example, suppose a new Markdown file contains:

```markdown
# How to use YouTube with OptiSigns

Article ID: 360051014713
```

The local manifest uses `360051014713` as its key and calculates SHA-256 from
the exact UTF-8 file bytes. A one-character body change therefore produces a
different digest.

### 4. Plan the delta

Local and remote manifests are compared using these rules:

| Condition | Category | Action |
| --- | --- | --- |
| Article ID exists only locally | `added` | Upload and index the local file. |
| Same ID, but SHA-256 or filename differs | `updated` | Upload new version, then remove old version. |
| Same ID, SHA-256, and filename | `skipped` | No remote write. |
| Article ID exists only remotely | `removed` | Detach and delete the remote file. |

SHA-256 catches content and metadata changes, including a changed
`Article URL` or `Last Updated` line. Filename comparison also detects title
changes even if the body is otherwise identical.

Example comparison:

```text
ID 10: local only                         -> added
ID 20: local hash=new, remote hash=old    -> updated
ID 30: same hash and same filename        -> skipped
ID 40: remote only                        -> removed
```

Only IDs 10 and 20 are uploaded. ID 30 costs no upload/indexing work, while ID
40 is removed after all new indexing has succeeded.

### 5. Static chunking

The default configuration is:

```text
maximum chunk size = 1,200 tokens
chunk overlap      =   200 tokens
effective stride   = 1,000 tokens
tokenizer estimate = o200k_base
```

The overlap repeats context at chunk boundaries to reduce retrieval misses
when an answer spans two neighboring chunks. Configuration validation enforces:

- chunk size from 100 through 4,096 tokens;
- non-negative overlap;
- overlap no greater than half of the chunk size.

For a document larger than one chunk, the estimate is:

```text
1 + ceil((token_count - max_chunk_size) / (max_chunk_size - overlap))
```

For example, a 2,201-token article with size 1,200 and overlap 200 produces
three estimated windows:

```text
Chunk 1: tokens    1-1200
Chunk 2: tokens 1001-2200  (tokens 1001-1200 overlap Chunk 1)
Chunk 3: tokens 2001-2201  (tokens 2001-2200 overlap Chunk 2)
```

If an instruction begins near token 1,190 and finishes near token 1,230,
Chunk 2 retains the transition instead of containing only its second half.

Estimation is performed locally for transparency and reporting. The identical
static configuration is sent in each Vector Store batch entry, so OpenAI uses
the requested values for real indexing.

CLI overrides are available:

```powershell
python main.py --all --chunk-size 1200 --chunk-overlap 200
```

### 6. Apply changes safely

The mutation order is designed to preserve the existing knowledge base when a
replacement upload fails:

1. Upload every added/updated Markdown file with purpose `assistants`.
2. Attach files to the Vector Store in batches of at most 500.
3. Supply per-file attributes and static chunking settings.
4. Poll until each batch is fully completed.
5. Validate completed, failed, cancelled, and in-progress counts.
6. Only after successful indexing, detach old updated files, removed articles,
   and stale duplicate copies.
7. Delete obsolete OpenAI File objects to avoid unused storage.

If upload or indexing fails, newly created files are cleaned up on a best-effort
basis and the old indexed versions remain attached. A 404 during obsolete-file
cleanup is treated as already detached/deleted, which makes retries safe.

For example, when article 20 is updated, `file_new_20` is uploaded and polled
until indexing completes. Only then is `file_old_20` detached and deleted. If
the new batch fails, cleanup targets `file_new_20`, while `file_old_20` remains
available to answer Assistant questions.

### 7. Persist state and reports

After a real successful sync:

- Vector Store metadata is updated with source count, chunk settings, and last
  sync time.
- The staged corpus replaces `data/markdown`; stale local Markdown is removed.
- `data/state/vector_store.json` records the store ID and compact sync state.
- `artifacts/run_reports/daily_sync_<UTC timestamp>.json` records scrape,
  delta, duplicate, chunk estimate, batch, upload, deletion, and storage data.

The local mirror is updated only after remote synchronization succeeds.

A shortened report looks like this:

```json
{
  "mode": "daily_sync",
  "status": "completed",
  "delta": {
    "counts": {"added": 1, "updated": 1, "skipped": 400, "removed": 0}
  },
  "openai": {"uploaded_files": 2, "detached_files": 1}
}
```

This distinguishes a healthy no-change run from a run that actually uploaded
or removed knowledge.

### 8. Dry-run behavior

```powershell
python main.py --all --dry-run
```

Dry-run reads the remote manifest, performs a fresh scrape, calculates the
delta and chunk estimates, and writes a report. It does not apply the delta,
update Vector Store metadata, replace the local Markdown mirror, or write the
state file.

For a strictly read-only dry-run, provide an existing Vector Store ID. If no ID
is available anywhere, the current resolver creates a new empty Vector Store
before the dry-run branch is reached.

## Question-answering and retrieval pipeline

Once ingestion is complete, the OptiBot Assistant uses the same Vector Store
through the hosted File Search tool. This is the online RAG path executed for a
user question:

```text
User question
     |
     v
Assistant decides to call File Search
     |
     v
Semantic query representation + keyword query
     |
     v
Search Vector Store chunk index
     |
     v
Rank and select the most relevant chunks
     |
     v
Add selected chunk text to the model context
     |
     v
Generate a grounded answer under the system instructions
     |
     v
Attach file citation annotations to supported statements
```

### 1. Receive the question

The user sends natural language such as:

```text
How do I add a YouTube video?
```

The Assistant has File Search enabled and is associated with the OptiBot
Vector Store. The model can call that hosted tool when the question requires
knowledge from the uploaded support corpus.

### 2. Search by meaning and keywords

File Search supports both semantic and keyword search. Keyword matching helps
when the user and article share literal terms such as `YouTube`. Semantic
matching uses embeddings to find related meaning even when wording differs.

For example:

```text
Question: "How can I show a short YouTube clip on a screen?"
Article:  "How to use YouTube with OptiSigns"
```

The two strings are not identical, but their vector representations should be
close because both describe displaying YouTube content. A passage about
`YouTube Shorts`, `/shorts/`, and `/embed/` can therefore rank highly.

The Playground setting `Max num. results = 5` limits how many retrieval results
the tool may supply. It does not mean five source files and does not force five
citations. Several results can be chunks from the same Markdown file.

### 3. Rank candidate chunks

The index may contain hundreds of article files and many more chunks. Search
scores candidate chunks for relevance and sends only the highest-ranked subset
forward. This is why RAG is cheaper and more focused than placing the entire
support corpus into every model prompt.

Conceptual result set:

```text
0.92  how-to-use-youtube-with-optisigns.md  "Open Files/Assets..."
0.88  how-to-use-youtube-with-optisigns.md  "For Shorts replace /shorts/..."
0.41  youtube-live-app.md                    "Add the YouTube Live app..."
0.09  weather-wall.md                       "Display a weather widget..."
```

The numbers are illustrative. The hosted tool owns the real scoring and index;
the repository does not receive or calculate these values in normal Assistant
Playground usage.

### 4. Augment the model context

The selected chunk text is placed into the model's temporary context together
with the user question and system instructions. The model is not retrained and
the retrieved text does not permanently modify model weights. It is additional
evidence available only for this response.

Conceptually, the generation input becomes:

```text
System: Answer only using uploaded documents; be concise; cite sources.
User: How do I add a YouTube video?
Retrieved context:
  - Open Files/Assets and select the YouTube app...
  - Paste the full URL and click Save...
  - For Shorts, replace /shorts/ with /embed/...
```

This is the "Augmented" part of Retrieval-Augmented Generation.

### 5. Generate the grounded answer

The model synthesizes the retrieved passages rather than copying an entire
article. It can combine relevant instructions into a short ordered answer while
following the configured tone and bullet limit.

If the question is outside the corpus, such as `What is the weather in Hanoi?`,
the Vector Store should not provide authoritative real-time weather context.
The system instruction to answer only from uploaded documents then causes the
Assistant to refuse or explain that the information is unavailable.

### 6. Produce citations

File Search returns citation annotations containing the originating `file_id`
and `filename`. The Playground renders those annotations as markers such as
`[1]` and `[2]`. Two markers may point to the same `.md` file when two claims or
retrieved passages originate from that article; this is valid and does not mean
the file was uploaded twice.

The corpus also contains a literal `Article URL:` line. That line is ordinary
indexed text, while `[1]` is a platform-generated file citation. They serve
related but different purposes:

```text
[1]             -> identifies the uploaded source file used by File Search
Article URL: ... -> gives the original public OptiSigns support-page URL
```

For a long article, the URL may be present in an earlier chunk while the answer
passage is in a later chunk. Automatic `[n]` file citations can still identify
the source file even when the model does not print the literal URL line.

## Complete RAG example

The following example connects ingestion and answering end to end:

1. Zendesk returns article `360051014713` with YouTube setup instructions.
2. The scraper removes navigation and writes
   `how-to-use-youtube-with-optisigns.md` with its Article ID and URL.
3. SHA-256 differs from the remote version, so the delta planner marks it
   `updated`.
4. The file is uploaded and attached with static chunking `1,200 / 200`.
5. OpenAI parses the Markdown, creates overlapping chunks, embeds each chunk,
   and adds them to the Vector Store index.
6. The new file reaches `completed`; only then is the previous file removed.
7. The user asks `How do I add a YouTube video?`.
8. File Search matches the query against semantic vectors and keywords.
9. The highest-ranked YouTube chunks augment the model context.
10. The Assistant generates concise setup steps and attaches citations pointing
    to `how-to-use-youtube-with-optisigns.md`.

## Technical limitations and design implications

- Delta detection is file-level, not chunk-level. One changed byte causes the
  whole article to be re-indexed.
- Chunk estimates are local predictions; OpenAI owns the actual parsing and
  index contents.
- Raw embedding vectors and the internal index algorithm are intentionally not
  stored or inspected by this application.
- Larger chunks provide more context per result but may mix topics. Smaller
  chunks are more precise but may lose surrounding instructions and create more
  vectors. The 1,200/200 configuration favors complete support procedures.
- More retrieval results can improve recall but increase context size, latency,
  and the chance of including weak matches.
- Retrieval improves grounding but does not guarantee perfect answers. System
  instructions, source quality, chunk boundaries, ranking, and model synthesis
  all affect the final response.

## Official technical references

- [OpenAI Retrieval guide](https://developers.openai.com/api/docs/guides/retrieval)
  explains semantic search, vector stores, chunking, embeddings, indexing, and
  ranking.
- [OpenAI File Search guide](https://developers.openai.com/api/docs/guides/tools-file-search)
  explains the hosted tool, Vector Store connection, result limits, and file
  citation annotations.

## Tests

`tests/test_chunking.py` verifies overlap math, validation limits, UTF-8 input,
and non-empty file estimation.

`tests/test_delta_sync.py` uses OpenAI API doubles to verify:

- all four delta categories;
- metadata bootstrapping for legacy files;
- upload-only behavior for added/updated documents;
- upload-before-delete replacement order;
- static chunking payload propagation;
- newest-copy selection and stale duplicate cleanup;
- retry safety when a stale file is already detached.

## Related files

| File | Responsibility |
| --- | --- |
| [`main.py`](../main.py) | Resolves credentials/store ID, validates CLI chunk settings, and starts daily sync. |
| [`src/support_ingestion/pipeline/scrape_pipeline.py`](../src/support_ingestion/pipeline/scrape_pipeline.py) | Produces the fresh Markdown corpus before indexing. |
| [`src/support_ingestion/markdown/converter.py`](../src/support_ingestion/markdown/converter.py) | Performs the local HTML parsing, cleanup, Markdown conversion, and source metadata insertion. |
| [`src/support_ingestion/pipeline/daily_sync.py`](../src/support_ingestion/pipeline/daily_sync.py) | Orchestrates staging scrape, manifests, delta, upload, mirror, state, and report. |
| [`src/support_ingestion/vector_store/chunking.py`](../src/support_ingestion/vector_store/chunking.py) | Validates static chunking and estimates per-file/corpus chunks. |
| [`src/support_ingestion/vector_store/sync.py`](../src/support_ingestion/vector_store/sync.py) | Builds manifests, plans deltas, and performs safe OpenAI synchronization. |
| [`data/markdown/`](../data/markdown/) | Successful source corpus and legacy-file bootstrap baseline. |
| [`data/state/vector_store.json`](../data/state/vector_store.json) | Compact local state containing Vector Store and chunking information. |
| [`artifacts/run_reports/`](../artifacts/run_reports/) | Detailed JSON output from real and dry-run syncs. |
| [`.env.example`](../.env.example) | Safe template for API key and Vector Store ID configuration. |
| [`tests/test_chunking.py`](../tests/test_chunking.py) | Unit tests for chunk validation and estimation. |
| [`tests/test_delta_sync.py`](../tests/test_delta_sync.py) | Unit tests for manifest, delta, upload, replacement, and duplicate handling. |
| [`requirements.txt`](../requirements.txt) | Declares the OpenAI SDK, `tiktoken`, and environment loader. |
