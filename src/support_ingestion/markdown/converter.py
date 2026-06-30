"""Convert Zendesk article HTML into clean, source-attributed Markdown."""

from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup, Comment, Tag
from markdownify import STRIP, STRIP_ONE, markdownify

# Selectors that should be removed before converting HTML to Markdown.
UNWANTED_SELECTORS = (
    "script",
    "style",
    "noscript",
    "nav",
    "aside",
    "form",
    "[role='navigation']",
    ".advertisement",
    ".advertisements",
    ".ad",
    ".ads",
    ".ad-container",
    ".breadcrumbs",
    ".article-votes",
    ".article-return-to-top",
    ".related-articles",
)

# Regex used to detect programming language classes in code blocks.
LANGUAGE_CLASS = re.compile(r"^(?:language-|lang-)([A-Za-z0-9_+.-]+)$")


def _code_language(element: Tag) -> str | None:
    """
    Detect the programming language of a code block. 
    markdownify can call this function when converting <pre>/<code> blocks.
    If we return a language name, the generated Markdown code block can include it.
    """

    # Start by checking the element passed by markdownify.
    candidates = [element]

    code = element.find("code")
    if isinstance(code, Tag):
        candidates.append(code)

    # Check all possible elements for a class like language-python or lang-js.
    for candidate in candidates:
        for class_name in candidate.get("class", []):
            match = LANGUAGE_CLASS.match(str(class_name))
            if match:
                return match.group(1)
    return None


def clean_html(html: str) -> str:
    """
    Remove noisy/unwanted HTML before converting the article to Markdown.
    """

    # Parse the raw HTML string into a BeautifulSoup document tree.
    soup = BeautifulSoup(html, "html.parser")

    # Remove all unwanted elements that match the selectors above.
    for selector in UNWANTED_SELECTORS:
        for element in soup.select(selector):
            # decompose() removes the tag and all of its children from the tree.
            element.decompose()

    # Remove HTML comments such as <!-- comment -->.
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    return str(soup)


def convert_article(article: dict[str, Any]) -> str:
    """
    Convert one Zendesk article dictionary into clean Markdown.
    """

    # If a field is missing or None, fallback values prevent runtime errors.
    title = str(article.get("title") or "Untitled article").strip()
    article_url = str(article.get("html_url") or "").strip()
    article_id = str(article.get("id") or "").strip()
    updated_at = str(article.get("updated_at") or "").strip()
    body_html = str(article.get("body") or "")

    # Clean the raw Zendesk article HTML, then convert it to Markdown.
    body_markdown = markdownify(
        clean_html(body_html),
        heading_style="ATX", # Use ATX-style headings: #, ##, ###.
        bullets="-",  # Use "-" as the bullet character for unordered lists.
        code_language_callback=_code_language, # Preserve code block language when the HTML contains language classes.
        strip_document=STRIP,  # Strip unnecessary document-level wrappers.
        strip_pre=STRIP_ONE, # Strip only one wrapper level around <pre> blocks.
    ).strip()

    # Add metadata that helps the Assistant cite sources.
    metadata = [f"Article URL: {article_url}"]
    if article_id:
        metadata.append(f"Article ID: {article_id}")
    if updated_at:
        metadata.append(f"Last Updated: {updated_at}")

    # Build the final Markdown sections.
    # Section 1: title as H1
    # Section 2: source metadata
    sections = [f"# {title}", "\n".join(metadata)]

    # Section 3: article body
    if body_markdown:
        sections.append(body_markdown)

    # Join sections with blank lines, remove trailing whitespace and ensure the file ends with exactly one newline.    
    return "\n\n".join(sections).rstrip() + "\n"
