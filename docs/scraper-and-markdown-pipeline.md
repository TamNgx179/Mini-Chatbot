# Scraping and Markdown Normalization

## Purpose

This pipeline builds a reproducible local knowledge corpus from the public OptiSigns
Help Center. It reads articles through the Zendesk Help Center API, removes
page noise, converts the useful HTML body to Markdown, and writes one stable
UTF-8 `.md` file per article.

The generated Markdown corpus becomes the input for chunking and Vector Store
synchronization. Scraping does not call OpenAI and can therefore be run
independently with `--scrape-only`.

## Architecture

```text
OptiSigns Zendesk API
        |
        v
ZendeskClient: pagination, retries, host validation
        |
        v
convert_article: HTML cleanup and Markdown conversion
        |
        v
MarkdownWriter: stable, collision-safe filenames
        |
        v
data/markdown/*.md
```

Responsibilities are intentionally separated:

- The API client only retrieves and validates remote data.
- The converter only normalizes article content.
- The writer only owns paths and filesystem output.
- The scrape pipeline coordinates those components and returns a summary.

## Pipeline

### 1. CLI dispatch

`main.py` parses the command-line arguments and resolves the output directory.
With `--scrape-only`, it calls `run_scrape()` without constructing an OpenAI
client.

```powershell
# Scrape the complete public corpus without contacting OpenAI.
python main.py --all --scrape-only

# Fetch a smaller test corpus; the assignment minimum is 30 articles.
python main.py --limit 30 --scrape-only
```

The process exits unsuccessfully if fewer than 30 Markdown documents are
written.

### 2. Zendesk article retrieval

`ZendeskClient` starts from:

```text
https://support.optisigns.com/api/v2/help_center/en-us/articles.json
```

It requests up to 100 articles per page and follows the cursor URL returned in
`links.next` while `meta.has_more` is true. Articles are yielded one at a time,
so the pipeline does not need to hold the complete corpus in memory.

For example, if the first response contains articles and returns the cursor
below, the client processes those items and then requests `links.next`. It
stops when `has_more` becomes `false`.

```json
{
  "articles": [{"id": 101}, {"id": 102}],
  "meta": {"has_more": true},
  "links": {
    "next": "https://support.optisigns.com/api/v2/help_center/en-us/articles?page%5Bafter%5D=cursor"
  }
}
```

Network behavior:

- Request timeout: 30 seconds.
- Maximum retry count: 4.
- Retried conditions: connection/read failures and HTTP 429, 500, 502, 503,
  and 504.
- Backoff factor: 0.5 seconds with increasing retry delay.
- `Retry-After` is respected when supplied by Zendesk.
- Only idempotent `GET` requests are retried.
- Every pagination URL must remain on `support.optisigns.com`; an unexpected
  host raises an error instead of following an untrusted URL.

### 3. HTML cleanup and Markdown conversion

For each Zendesk article, `convert_article()`:

1. Reads `title`, `html_url`, `id`, `updated_at`, and `body`.
2. Parses the HTML using BeautifulSoup.
3. Removes scripts, styles, navigation, forms, advertisements, breadcrumbs,
   voting widgets, related-article blocks, and HTML comments.
4. Converts the remaining body with `markdownify`.
5. Preserves headings, links, lists, and fenced code block language when the
   source has a `language-*` or `lang-*` class.
6. Prepends source metadata needed by delta sync and Assistant citations.

Every generated document follows this shape:

```markdown
# Article title

Article URL: https://support.optisigns.com/...
Article ID: 123456789
Last Updated: 2026-01-01T00:00:00Z

Normalized article body...
```

For a concrete conversion, this source HTML:

```html
<nav>Help Center navigation</nav>
<h2>Add a video</h2>
<p>Open the <a href="https://app.optisigns.com">portal</a>.</p>
<div class="related-articles">Unrelated recommendations</div>
```

becomes:

```markdown
## Add a video

Open the [portal](https://app.optisigns.com).
```

The navigation and related-article block disappear, while the useful heading
and link remain. `Article ID` becomes the stable synchronization identity.
`Article URL` stays in the indexed content so the Assistant can cite the
original support page.

### 4. Stable file writing

`MarkdownWriter` turns the title into a lowercase slug. For example,
`How to use YouTube with OptiSigns` becomes
`how-to-use-youtube-with-optisigns.md`.

If two different articles produce the same slug, the later filename receives
the article ID suffix. Empty titles fall back to `article-{id}.md`. Files are
written as UTF-8 with normalized LF newlines.

Example collision handling:

```text
Article 100, title "Install Player" -> install-player.md
Article 205, title "Install Player" -> install-player-205.md
Article 300, empty title            -> article-300.md
```

### 5. Result validation

`run_scrape()` records `fetched`, `written`, and the resolved output directory.
The daily pipeline additionally calls `discover_markdown_files()` and refuses
to proceed when the staging corpus contains fewer than 30 files. This protects
the Vector Store synchronizer from treating a partial scrape as mass deletion.

For example, a successful scrape with 402 files is accepted. If a transient API
problem produces only 12 files, the run stops before comparing that incomplete
set with the remote corpus; it does not incorrectly plan the other 390 files as
removed.

## Failure behavior

- HTTP errors are raised after retry exhaustion.
- A malformed Zendesk response without an `articles` list fails immediately.
- Invalid `limit` or `page_size` values are rejected before any request.
- Cross-host pagination is rejected.
- Conversion or filesystem errors stop the run; the deployment workflow then
  exposes the non-zero exit code in the GitHub Actions log.
- During the full daily sync, scraping occurs in a temporary staging directory,
  so a failed run cannot overwrite the last successful local corpus.

## Tests

`tests/test_scraping.py` uses local HTTP doubles and does not require network
access. It verifies:

- cursor pagination and limit handling;
- removal of navigation, advertising, and comments;
- preservation of headings, links, and language-tagged code blocks;
- source `Article ID` metadata;
- slug generation and duplicate-title collision handling.

Run it as part of the complete suite:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
```

## Related files

| File | Responsibility |
| --- | --- |
| [`main.py`](../main.py) | CLI entry point and `--scrape-only` execution mode. |
| [`src/support_ingestion/pipeline/scrape_pipeline.py`](../src/support_ingestion/pipeline/scrape_pipeline.py) | Coordinates fetching, conversion, writing, and scrape summary. |
| [`src/support_ingestion/scraper/zendesk_client.py`](../src/support_ingestion/scraper/zendesk_client.py) | Zendesk endpoint, pagination, retries, timeout, and host validation. |
| [`src/support_ingestion/markdown/converter.py`](../src/support_ingestion/markdown/converter.py) | Cleans HTML, converts Markdown, and adds article metadata. |
| [`src/support_ingestion/markdown/writer.py`](../src/support_ingestion/markdown/writer.py) | Creates deterministic filenames and writes UTF-8 Markdown. |
| [`data/markdown/`](../data/markdown/) | Persistent mirror of the latest successful Markdown corpus. |
| [`tests/test_scraping.py`](../tests/test_scraping.py) | Offline tests for retrieval, cleanup, conversion, and filenames. |
| [`requirements.txt`](../requirements.txt) | Declares `requests`, `beautifulsoup4`, `markdownify`, and `python-slugify`. |
