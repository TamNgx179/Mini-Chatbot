"""Coordinate Zendesk fetching, HTML conversion, and Markdown writing."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from support_ingestion.markdown.converter import convert_article
from support_ingestion.markdown.writer import MarkdownWriter
from support_ingestion.scraper.zendesk_client import ZendeskClient


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class ScrapeSummary:
    """
    Summary result returned after the scrape pipeline finishes.
    """

    fetched: int
    written: int
    output_dir: Path


def run_scrape(output_dir: Path, limit: int | None = 30) -> ScrapeSummary:
    """
    Run the article scraping pipeline.

    This function coordinates the full scrape process:
    1. Fetch articles from Zendesk.
    2. Convert each article into clean Markdown.
    3. Write each Markdown file to the output directory.
    4. Return a summary for logging and exit-code handling.
    """

    client = ZendeskClient()
    writer = MarkdownWriter(output_dir)
    fetched = 0
    written = 0

    # Iterate through Zendesk articles one by one.
    for article in client.iter_articles(limit=limit):
        fetched += 1
        content = convert_article(article) # Convert the raw Zendesk article dictionary into clean Markdown content.
        destination = writer.write(article, content)  # Write the Markdown content to the output directory.
        written += 1
        LOGGER.debug("Wrote %s", destination) # Debug log for each written file.

    if written < 30:
        LOGGER.error("Only %d articles were written; at least 30 are required", written)

    # Return a structured summary so main.py can log it and decide exit code.
    return ScrapeSummary(
        fetched=fetched,
        written=written,
        output_dir=output_dir.resolve(),
    )
