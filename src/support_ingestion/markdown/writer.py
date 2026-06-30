"""Write normalized articles to stable and collision-safe Markdown paths."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from slugify import slugify


class MarkdownWriter:
    """
    Write converted Markdown content to .md files.

    This class is responsible for:
    - creating the output directory if it does not exist
    - generating safe filenames from article titles
    - avoiding filename conflicts when articles have the same title
    - writing Markdown content using UTF-8 encoding
    """
        
    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir # Store the directory where Markdown files will be written.
        self.output_dir.mkdir(parents=True, exist_ok=True) # Create the output directory if it does not already exist.
        
        #Track which article owns each slug. This helps prevent filename collisions when two articles have the same or very similar titles.
        self._slug_owners: dict[str, str] = {}

    def write(self, article: dict[str, Any], content: str) -> Path:
        """
        Write one article's Markdown content to a .md file.
        """

        # Get the Zendesk article ID. If the article does not have an ID, use "unknown" as a fallback.
        article_id = str(article.get("id") or "unknown")

        # Convert article title into a safe filename slug.
        base_slug = slugify(str(article.get("title") or ""))

        # If the title is empty or cannot be converted into a slug, fall back to article-{id}.
        if not base_slug:
            base_slug = f"article-{article_id}"

        # Check if this slug has already been used by another article.
        owner = self._slug_owners.get(base_slug)

        # Mark this slug as owned by the current article ID.
        self._slug_owners[base_slug] = article_id

        # Build the final filename.
        filename = (
            f"{base_slug}.md"
            if owner in (None, article_id)
            else f"{base_slug}-{article_id}.md"
        )

        # Build the full destination path.
        destination = self.output_dir / filename
        destination.write_text(content, encoding="utf-8", newline="\n")
        return destination
