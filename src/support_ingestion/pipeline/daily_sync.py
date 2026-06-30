"""Orchestrate a full scrape, delta detection, remote sync, and run report."""

from __future__ import annotations

import json
import logging
import shutil
import tempfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from support_ingestion.pipeline.scrape_pipeline import run_scrape
from support_ingestion.vector_store.chunking import (
    ChunkingConfig,
    estimate_corpus_chunks,
)
from support_ingestion.vector_store.sync import (
    DeltaSyncResult,
    OpenAIVectorStoreDeltaSync,
    build_local_documents,
    plan_delta,
)


LOGGER = logging.getLogger(__name__)


def discover_markdown_files(directory: Path, minimum: int = 30) -> list[Path]:
    """Return sorted Markdown inputs and enforce the assignment minimum."""

    if not directory.is_dir():
        raise FileNotFoundError(f"Markdown directory does not exist: {directory}")
    paths = sorted(path for path in directory.glob("*.md") if path.is_file())
    if len(paths) < minimum:
        raise ValueError(
            f"Expected at least {minimum} Markdown files in {directory}; "
            f"found {len(paths)}"
        )
    return paths


@dataclass(frozen=True)
class DailySyncSummary:
    """
    Final summary returned by the daily sync pipeline.

    This object is used by main.py to print a concise job result
    to terminal/Docker/cloud logs.
    """

    timestamp_utc: str
    vector_store_id: str
    fetched: int
    source_files: int
    estimated_chunks: int
    added: int
    updated: int
    skipped: int
    removed: int
    report_path: Path


def create_vector_store(client: Any, chunking: ChunkingConfig) -> str:
    """
    Create a new OpenAI Vector Store.

    This is used when no existing vector_store_id is provided from:
    - command-line argument
    - environment variable
    - local state file

    Returns:
        The newly created vector_store_id.
    """

    store = client.vector_stores.create(
        name="OptiBot Support Knowledge Base",
        description=(
            "Public OptiSigns support articles normalized to Markdown for "
            "grounded customer-support retrieval."
        ),
        metadata={
            # Identify what corpus this Vector Store contains.
            "corpus": "optisigns_support",

            # At creation time no files have been synced yet.
            "source_files": "0",

            # Store chunking configuration for traceability.
            "chunk_size": str(chunking.max_chunk_size_tokens),
            "chunk_overlap": str(chunking.chunk_overlap_tokens),
        },
    )
    # Log the created Vector Store ID for debugging and setup.
    LOGGER.info("Created Vector Store %s", store.id)

    return str(store.id)


def write_json(path: Path, payload: dict[str, object]) -> None:
    """
    Write a dictionary payload to a formatted JSON file.

    Used for:
    - state file
    - daily sync report
    """

    # Ensure the parent folder exists.
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write pretty JSON with UTF-8 encoding and normalized newlines.
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def update_local_mirror(source_dir: Path, destination_dir: Path) -> None:
    """
    Copy the successful scrape into the local mirror and remove stale Markdown.

    source_dir:
        Temporary staging directory containing the latest scrape.

    destination_dir:
        Persistent Markdown directory, usually data/markdown.

    Why this exists:
        The daily job scrapes into a temporary folder first. Only after the
        remote Vector Store sync succeeds do we copy the new files into the
        persistent local mirror. This avoids corrupting the local mirror if
        scraping or syncing fails midway.
    """

    # Make sure the destination directory exists.
    destination_dir.mkdir(parents=True, exist_ok=True)

    # Collect file names from the latest successful scrape.
    source_names = {path.name for path in source_dir.glob("*.md")}

    # Copy every newly scraped Markdown file into the persistent mirror.
    for source in source_dir.glob("*.md"):
        shutil.copy2(source, destination_dir / source.name)

    # Remove stale Markdown files from the persistent mirror. If a file exists in destination but not in the latest scrape
    for existing in destination_dir.glob("*.md"):
        if existing.name not in source_names:
            existing.unlink()


def run_daily_sync(
    *,
    client: Any,
    vector_store_id: str | None,
    output_dir: Path,
    state_path: Path,
    report_dir: Path,
    limit: int | None,
    chunking: ChunkingConfig,
    dry_run: bool = False,
) -> DailySyncSummary:
    """
    Run the full daily sync workflow.

    Workflow:
    1. Resolve or create a Vector Store.
    2. Load current remote document state.
    3. Scrape latest Zendesk articles into a temporary directory.
    4. Build local document records from scraped Markdown.
    5. Compare local documents against remote documents.
    6. Apply only the delta to OpenAI Vector Store.
    7. Write state and report files.
    8. Return a concise summary.

    dry_run=True:
        Compute and report the delta without modifying OpenAI or local state.
    """

    # Create a UTC timestamp for state/report naming.
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    # Use existing Vector Store ID if provided. Otherwise, create a new Vector Store.
    resolved_store_id = vector_store_id or create_vector_store(client, chunking)

    # Create a synchronizer for delta operations against OpenAI Vector Store.
    synchronizer = OpenAIVectorStoreDeltaSync(
        client,
        resolved_store_id,
        chunking,
    )

    # Optional bootstrap from the existing local Markdown mirror.
    bootstrap_documents = {}

    if output_dir.is_dir():
        baseline_paths = sorted(
            path for path in output_dir.glob("*.md") if path.is_file()
        )
        if baseline_paths:
            bootstrap_documents = build_local_documents(baseline_paths)

    # Load document state from the remote Vector Store.
    remote_documents = synchronizer.load_remote_documents(
        bootstrap_documents=bootstrap_documents,
        persist_bootstrap_attributes=not dry_run,
    )

    # Scrape into a temporary directory first.
    # The temp folder is automatically deleted after the with-block.
    with tempfile.TemporaryDirectory(prefix="optibot-scrape-") as directory:
        staging_dir = Path(directory)

        # Scrape latest articles into the staging directory.
        scrape = run_scrape(staging_dir, limit=limit)

        # Find Markdown files and enforce minimum 30 documents.
        paths = discover_markdown_files(staging_dir, minimum=30)

        # Build local document records from the newly scraped Markdown files.
        local_documents = build_local_documents(paths)

        # Compare newly scraped local documents with current remote documents.
        # This produces added/updated/skipped/removed groups.
        delta = plan_delta(local_documents, remote_documents)

        # Estimate chunks for the full newly scraped corpus.
        corpus_estimate = estimate_corpus_chunks(paths, chunking)

        # Estimate chunks for the full newly scraped corpus.
        changed_paths = [item.path for item in delta.changed_documents]

        # Estimate chunks for only the changed/uploaded delta. If nothing changed, report zero uploaded chunks.
        changed_estimate = (
            estimate_corpus_chunks(changed_paths, chunking).to_dict()
            if changed_paths
            else {
                "source_files": 0,
                "total_tokens": 0,
                "estimated_chunks": 0,
                "files": [],
            }
        )

        # Log required delta counts.
        LOGGER.info(
            "Delta: added=%d updated=%d skipped=%d removed=%d duplicates=%d",
            len(delta.added),
            len(delta.updated),
            len(delta.skipped),
            len(delta.removed),
            len(synchronizer.duplicate_documents),
        )

        if dry_run:
            # Dry-run mode does not modify OpenAI or local mirror.
            # Return a zeroed sync result while still producing a report.
            sync_result = DeltaSyncResult(
                batch_ids=(),
                uploaded_files=0,
                detached_files=0,
                deleted_file_objects=0,
                vector_store_bytes=0,
            )
        else:
            # Apply only the delta:
            # - upload added documents
            # - replace updated documents
            # - detach/delete removed documents
            sync_result = synchronizer.apply(delta)

            # Update Vector Store metadata after a successful sync.
            synchronizer.update_store_metadata(len(paths), timestamp)

            # Persist the latest successful scrape into data/markdown.
            update_local_mirror(staging_dir, output_dir)

    # State is a compact record used by future runs.
    state: dict[str, object] = {
        "updated_at_utc": timestamp,
        "vector_store_id": resolved_store_id,
        "source_files": corpus_estimate.source_files,
        "estimated_chunks": corpus_estimate.estimated_chunks,
        "chunking_strategy": chunking.api_payload,
    }

    # Report is a detailed record for logs/deliverables.
    report: dict[str, object] = {
        "timestamp_utc": timestamp,
        "mode": "daily_sync_dry_run" if dry_run else "daily_sync",
        "status": "completed",
        "vector_store_id": resolved_store_id,
        "scrape": {
            "fetched": scrape.fetched,
            "source_files": corpus_estimate.source_files,
        },
        "delta": delta.to_dict(),
        "duplicate_remote_files": len(synchronizer.duplicate_documents),
        "chunk_estimate": {
            "corpus": corpus_estimate.to_dict(),
            "uploaded_delta": changed_estimate,
        },
        "openai": sync_result.to_dict(),
    }

    # Build report file path.
    report_path = report_dir / f"daily_sync_{timestamp}.json"

    # Only write persistent state for real syncs. Dry-run should not change local state.
    if not dry_run:
        write_json(state_path, state)

    # Always write a report, including dry-run reports.
    write_json(report_path, report)

    # Return concise summary to main.py.
    return DailySyncSummary(
        timestamp_utc=timestamp,
        vector_store_id=resolved_store_id,
        fetched=scrape.fetched,
        source_files=corpus_estimate.source_files,
        estimated_chunks=corpus_estimate.estimated_chunks,
        added=len(delta.added),
        updated=len(delta.updated),
        skipped=len(delta.skipped),
        removed=len(delta.removed),
        report_path=report_path,
    )
