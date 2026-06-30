"""CLI entry point for one-shot scraping and OpenAI Vector Store syncing."""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Resolve the project root based on this main.py location.
PROJECT_ROOT = Path(__file__).resolve().parent

# Directory that contains the internal support_ingestion package.
SRC_DIR = PROJECT_ROOT / "src"

# Add src/ to Python import path so the script can import local modules.
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# Load environment variables from .env.
load_dotenv(PROJECT_ROOT / ".env")

# Import local modules after sys.path is configured.
from support_ingestion.pipeline.daily_sync import run_daily_sync  
from support_ingestion.pipeline.scrape_pipeline import run_scrape  
from support_ingestion.vector_store.chunking import ChunkingConfig  

# Default directory where scraped Markdown files are stored.
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "markdown"

# Default state file used to remember the current Vector Store ID and previous sync metadata.
DEFAULT_STATE = PROJECT_ROOT / "data" / "state" / "vector_store.json"

# Default directory where daily sync reports are written.
DEFAULT_REPORT_DIR = PROJECT_ROOT / "artifacts" / "run_reports"


def state_vector_store_id(path: Path) -> str | None:
    """
    Read the vector_store_id from a local state file.

    The state file is created after a successful vector store upload/sync.
    This allows future runs to reuse the same Vector Store without requiring
    the user to pass --vector-store-id every time.
    """
        
    # If the state file does not exist, there is no saved Vector Store ID.
    if not path.is_file():
        return None
    
    # Read and parse the state JSON file.
    payload = json.loads(path.read_text(encoding="utf-8"))

    # Extract vector_store_id from the JSON payload.
    value = payload.get("vector_store_id")

    return str(value) if value else None


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the one-shot daily job.

    Examples:
        python main.py
        python main.py --scrape-only
        python main.py --dry-run
        python main.py --limit 30
        python main.py --all
        python main.py --vector-store-id vs_xxx
    """
        
    parser = argparse.ArgumentParser(
        description=(
            "Run the one-shot OptiBot daily job: scrape all articles, detect "
            "added/updated/skipped documents, and sync only the delta."
        )
    )

    # --limit and --all cannot be used together.
    limit_group = parser.add_mutually_exclusive_group()

    limit_group.add_argument(
        "--limit",
        type=int,
        help="Fetch a limited corpus for local testing (minimum: 30).",
    )

    limit_group.add_argument(
        "--all",
        action="store_true",
        help="Fetch the full public corpus (the default daily-job behavior).",
    )

    # Run only the scraping step and skip OpenAI entirely.
    parser.add_argument(
        "--scrape-only",
        action="store_true",
        help="Scrape Markdown without calling OpenAI.",
    )

    # Dry-run mode reports what would change without updating remote state.
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Read remote state and report the delta without changing it.",
    )

    # Directory where Markdown files will be written.
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)

    # State file path used to persist vector store and sync metadata.
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)

    # Directory where sync reports will be written.
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)

    # Existing Vector Store ID.
    parser.add_argument(
        "--vector-store-id",
        default=os.getenv("OPENAI_VECTOR_STORE_ID"),
        help=(
            "Existing Vector Store ID. If omitted, local state is checked; "
            "if neither exists, a new store is created."
        ),
    )

    # Static chunking configuration used for Vector Store ingestion.
    parser.add_argument("--chunk-size", type=int, default=1_200)
    parser.add_argument("--chunk-overlap", type=int, default=200)

    return parser.parse_args()


def main() -> int:
    """
    Run the one-shot daily sync job.

    Modes:
    - --scrape-only:
        Scrape Markdown files only, no OpenAI API calls.

    - normal mode:
        Scrape articles, detect added/updated/skipped/removed files,
        and sync only the delta to OpenAI Vector Store.

    - --dry-run:
        Compute/report the delta but avoid making remote changes.
    """

    args = parse_args()

    # Every scrape must be at least 30 articles
    if args.limit is not None and args.limit < 30:
        raise SystemExit("--limit must be at least 30")

    # Configure readable logs for terminal, Docker, and cloud job logs.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    # Reduce noisy logs from HTTP/OpenAI internals.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)

     # If no --limit is provided, use None, limit=None means fetch all available public articles.
    limit = args.limit if args.limit is not None else None

    # Scrape-only mode: validating article ingestion and Markdown writing without calling OpenAI or spending API credits.
    if args.scrape_only:
        summary = run_scrape(args.output, limit=limit)
        logging.info(
            "Scrape complete: fetched=%d written=%d output=%s",
            summary.fetched,
            summary.written,
            summary.output_dir,
        )

        # Return success only if the minimum required article count is satisfied.
        return 0 if summary.written >= 30 else 1

    # In normal sync mode, OpenAI API key is required.
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set")

    # Build static chunking configuration.
    chunking = ChunkingConfig(
        max_chunk_size_tokens=args.chunk_size,
        chunk_overlap_tokens=args.chunk_overlap,
    )

    # Get the Vector Store ID 
    vector_store_id = args.vector_store_id or state_vector_store_id(args.state)

    # Create OpenAI client with retry and timeout settings.
    client = OpenAI(max_retries=4, timeout=90.0)

    # Run the full daily sync pipeline.
    summary = run_daily_sync(
        client=client,
        vector_store_id=vector_store_id,
        output_dir=args.output,
        state_path=args.state,
        report_dir=args.report_dir,
        limit=limit,
        chunking=chunking,
        dry_run=args.dry_run,
    )

    # Log final summary.
    logging.info(
        "Daily sync complete: store=%s fetched=%d files=%d chunks~=%d "
        "added=%d updated=%d skipped=%d removed=%d report=%s",
        summary.vector_store_id,
        summary.fetched,
        summary.source_files,
        summary.estimated_chunks,
        summary.added,
        summary.updated,
        summary.skipped,
        summary.removed,
        summary.report_path,
    )
    return 0


if __name__ == "__main__":
    # Convert main() return value into a real process exit code.
    raise SystemExit(main())
