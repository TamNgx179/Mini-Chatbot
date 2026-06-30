"""Focused tests for fetching, cleaning, and writing support articles."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from support_ingestion.markdown.converter import convert_article
from support_ingestion.markdown.writer import MarkdownWriter
from support_ingestion.scraper.zendesk_client import ZendeskClient


# Minimal HTTP doubles keep pagination tests offline and deterministic.
class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return self.payload


class FakeSession:
    def __init__(self, payloads: list[dict]) -> None:
        self.payloads = iter(payloads)
        self.calls: list[str] = []

    def get(self, url: str, **_: object) -> FakeResponse:
        self.calls.append(url)
        return FakeResponse(next(self.payloads))


class ScrapingTests(unittest.TestCase):
    def test_zendesk_client_follows_pagination_and_limit(self) -> None:
        next_url = (
            "https://support.optisigns.com/api/v2/help_center/"
            "en-us/articles?page%5Bafter%5D=cursor"
        )
        session = FakeSession(
            [
                {
                    "articles": [{"id": 1}, {"id": 2}],
                    "meta": {"has_more": True},
                    "links": {"next": next_url},
                },
                {
                    "articles": [{"id": 3}],
                    "meta": {"has_more": False},
                    "links": {},
                },
            ]
        )
        client = ZendeskClient(session=session)

        articles = list(client.iter_articles(limit=3, page_size=2))

        self.assertEqual([1, 2, 3], [item["id"] for item in articles])
        self.assertEqual([client.articles_url, next_url], session.calls)

    def test_converter_keeps_content_and_removes_page_chrome(self) -> None:
        result = convert_article(
            {
                "id": 123,
                "title": "Install player",
                "html_url": "https://support.optisigns.com/hc/en-us/articles/123",
                "body": """
                    <nav>Navigation</nav><!-- tracking -->
                    <div class="advertisement">Ad</div>
                    <h2>Setup</h2>
                    <p>Read the <a href="/hc/next">next guide</a>.</p>
                    <pre><code class="language-python">print("ok")</code></pre>
                """,
            }
        )

        self.assertIn("## Setup", result)
        self.assertIn("[next guide](/hc/next)", result)
        self.assertIn('```python\nprint("ok")\n```', result)
        self.assertIn("Article ID: 123", result)
        self.assertNotIn("Navigation", result)
        self.assertNotIn("Ad", result)
        self.assertNotIn("tracking", result)

    def test_writer_uses_slug_and_handles_title_collisions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            writer = MarkdownWriter(Path(directory))
            first = writer.write({"id": 1, "title": "Same title"}, "first")
            second = writer.write({"id": 2, "title": "Same title"}, "second")

            self.assertEqual("same-title.md", first.name)
            self.assertEqual("same-title-2.md", second.name)


if __name__ == "__main__":
    unittest.main()
