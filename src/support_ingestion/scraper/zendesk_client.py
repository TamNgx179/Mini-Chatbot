"""Read public OptiSigns Help Center articles with pagination and retries."""

from __future__ import annotations

import logging
from collections.abc import Iterator
from typing import Any
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


LOGGER = logging.getLogger(__name__)

# Default Zendesk Help Center domain for OptiSigns.
DEFAULT_HELP_CENTER_URL = "https://support.optisigns.com"

# Default Help Center locale. OptiSigns articles usually live under /hc/en-us/...
DEFAULT_LOCALE = "en-us"


def build_retrying_session() -> requests.Session:
    """
    Create a requests Session with retry behavior.

    Due to rate limits, server errors, or connection issues network requests can fail temporarily so we need 
    retry mechanism
    """

    retry = Retry(
        total=4,
        connect=4,
        read=4,
        status=4,
        backoff_factor=0.5, # Wait time between retries. The delay increases after each failed attempt.
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}), # Only retry safe GET requests.
        respect_retry_after_header=True, # Respect the Retry-After header if the server provides it.
    )

    # Attach the retry strategy to an HTTP adapter.
    adapter = HTTPAdapter(max_retries=retry)

    session = requests.Session()
    session.mount("https://", adapter)
    
    # Set default headers for every request made by this session.
    session.headers.update(
        {
            "Accept": "application/json",
            "User-Agent": "mini-chatbot-take-home/1.0",
        }
    )
    return session


class ZendeskClient:
    """
    Small client for reading public Zendesk Help Center articles.

    This client is responsible for:
    - building the correct Zendesk article API URL
    - requesting paginated article data
    - yielding articles one by one
    - preventing pagination from jumping to an unexpected domain
    """

    def __init__(
        self,
        help_center_url: str = DEFAULT_HELP_CENTER_URL,
        locale: str = DEFAULT_LOCALE,
        session: requests.Session | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.help_center_url = help_center_url.rstrip("/") # Remove trailing slash 
        self.locale = locale
        self.session = session or build_retrying_session()  # Use the provided session if passed in. Otherwise, create a default retrying session.
        self.timeout = timeout
        self._expected_host = urlparse(self.help_center_url).netloc # Store the expected domain.

    @property
    def articles_url(self) -> str:
        """
        Build the Zendesk API endpoint for public Help Center articles.
        """
        return (
            f"{self.help_center_url}/api/v2/help_center/"
            f"{self.locale}/articles.json"
        )

    def iter_articles(
        self,
        limit: int | None = None,
        page_size: int = 100,
    ) -> Iterator[dict[str, Any]]:
        """
        Iterate through public Zendesk articles.

        Args:
            limit:
                Maximum number of articles to yield. If None, fetch all available articles.

            page_size:
                Number of articles to request per page.

        Yields:
            One article dictionary at a time.
        """

        # Validate limit.
        if limit is not None and limit <= 0:
            raise ValueError("limit must be positive or None")
        
        # Validate page size.
        if not 1 <= page_size <= 100:
            raise ValueError("page_size must be between 1 and 100")

        url: str | None = self.articles_url
        # Initial query params, page[size] is used by Zendesk cursor pagination style.
        params: dict[str, int] | None = {"page[size]": page_size}
        yielded = 0 # Count how many articles have been yielded so far.
        page_number = 0 # Count fetched pages for logging/debugging.

        # Keep fetching while there is a current page URL.
        while url:
            self._ensure_expected_host(url)
            
            # Send GET request to Zendesk API.
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            payload = response.json()
            page_number += 1

            articles = payload.get("articles")
            if not isinstance(articles, list):
                raise ValueError("Zendesk response does not contain an articles list")

             # Log the current page result.
            LOGGER.info(
                "Fetched Zendesk page %d containing %d articles",
                page_number,
                len(articles),
            )

            # Yield each valid article dictionary.
            for article in articles:
                # Skip invalid items just in case the API returns unexpected data.
                if not isinstance(article, dict):
                    continue

                yield article
                yielded += 1

                # Stop once the requested limit is reached.
                if limit is not None and yielded >= limit:
                    return

            # Read pagination information from Zendesk response.
            meta = payload.get("meta") or {}
            links = payload.get("links") or {}
            
            # If there are more pages, use the next page URL. Otherwise, set url to None to stop the loop.
            url = links.get("next") if meta.get("has_more") else None

            params = None

    def _ensure_expected_host(self, url: str) -> None:
        if urlparse(url).netloc != self._expected_host:
            raise ValueError("Zendesk pagination returned an unexpected host")
