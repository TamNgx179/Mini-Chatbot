"""Plan and apply idempotent file-level deltas to an OpenAI Vector Store."""

from __future__ import annotations

import hashlib
import logging
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

from support_ingestion.vector_store.chunking import ChunkingConfig


LOGGER = logging.getLogger(__name__)

# Regex used to extract Article ID from generated Markdown files.
ARTICLE_ID_PATTERN = re.compile(r"^Article ID:\s*(\S+)\s*$", re.MULTILINE)

# Required metadata keys stored on each remote Vector Store file.
# These attributes allow later daily sync runs to compare local files with
# remote files without downloading and hashing remote content again.
REMOTE_ATTRIBUTE_KEYS = ("article_id", "sha256", "filename")


@dataclass(frozen=True)
class LocalDocument:
    """
    Represents one Markdown document in the local corpus.

    Local documents are built from files in data/markdown or a staging scrape
    directory before being compared with remote Vector Store files.
    """

    article_id: str
    filename: str
    sha256: str
    path: Path

    @property
    def attributes(self) -> dict[str, str]:
        """
        Metadata attached to the OpenAI Vector Store file.

        These attributes are later used to detect whether a document is new,
        updated, unchanged, or removed.
        """

        return {
            "article_id": self.article_id,
            "sha256": self.sha256,
            "filename": self.filename,
        }


@dataclass(frozen=True)
class RemoteDocument:
    """
    Represents one document currently stored in the OpenAI Vector Store.
    """

    article_id: str
    filename: str
    sha256: str
    file_id: str
    created_at: int = 0


@dataclass(frozen=True)
class DocumentUpdate:
    """
    Represents an updated document.

    local:
        New local version that should be uploaded.

    remote:
        Existing remote version that should be removed after the new version
        is uploaded successfully.
    """
     
    local: LocalDocument
    remote: RemoteDocument


@dataclass(frozen=True)
class DeltaPlan:
    """
    Plan describing differences between local corpus and remote Vector Store.
    """

    # Documents that exist locally but not remotely.
    added: tuple[LocalDocument, ...]

    # Documents that exist in both places but changed by content hash or filename.
    updated: tuple[DocumentUpdate, ...]

    # Documents that exist in both places but changed by content hash or filename.
    skipped: tuple[LocalDocument, ...]

    # Documents that are identical locally and remotely.
    removed: tuple[RemoteDocument, ...]

    @property
    def changed_documents(self) -> tuple[LocalDocument, ...]:
        """
        Return documents that need to be uploaded.

        Only added and updated local documents need uploading.
        Skipped documents are already up to date.
        Removed documents do not need uploading; they need deletion.
        """
        return self.added + tuple(item.local for item in self.updated)

    def to_dict(self) -> dict[str, object]:
        """
        Convert the delta plan into a report-friendly dictionary.
        """

        return {
            "counts": {
                "added": len(self.added),
                "updated": len(self.updated),
                "skipped": len(self.skipped),
                "removed": len(self.removed),
            },
            "added": [item.filename for item in self.added],
            "updated": [item.local.filename for item in self.updated],
            "skipped": [item.filename for item in self.skipped],
            "removed": [item.filename for item in self.removed],
        }


@dataclass(frozen=True)
class DeltaSyncResult:
    """
    Result returned after applying a delta sync to OpenAI Vector Store.
    """

    batch_ids: tuple[str, ...]
    uploaded_files: int
    detached_files: int
    deleted_file_objects: int
    vector_store_bytes: int

    def to_dict(self) -> dict[str, object]:
        """
        Convert the result into a JSON-serializable dictionary.
        """
        return asdict(self)


class VectorStoreDeltaSyncError(RuntimeError):
    """Raised when incremental Vector Store synchronization is incomplete."""


def sha256_bytes(content: bytes) -> str:
    """
    Return SHA256 hash for raw file content.

    This hash is used to detect whether a Markdown document changed.
    """

    return hashlib.sha256(content).hexdigest()


def article_id_from_markdown(content: str, *, source: str) -> str:
    """
    Extract Article ID from Markdown content.

    Args:
        content:
            Full Markdown content.

        source:
            File path or source label used in the error message.

    Returns:
        Article ID string.

    Raises:
        ValueError if the Markdown file does not contain an Article ID line.
    """
    match = ARTICLE_ID_PATTERN.search(content)
    if not match:
        raise ValueError(f"Markdown is missing an Article ID line: {source}")
    return match.group(1)


def build_local_documents(paths: Iterable[Path]) -> dict[str, LocalDocument]:
    """
    Build local document manifest from Markdown files.

    The returned dictionary is keyed by article_id so it can be compared
    directly against the remote document manifest.
    """

    documents: dict[str, LocalDocument] = {}

    # Process files in sorted order for deterministic behavior.
    for path in sorted(paths):
        # Read raw bytes so the SHA256 hash is based on exact file content.
        content = path.read_bytes()

        # Extract stable article ID from the Markdown content.
        article_id = article_id_from_markdown(
            content.decode("utf-8"),
            source=str(path),
        )

         # Extract stable article ID from the Markdown content.
        if article_id in documents:
            raise ValueError(f"Duplicate Article ID in local corpus: {article_id}")
        
        # Store local document metadata.
        documents[article_id] = LocalDocument(
            article_id=article_id,
            filename=path.name,
            sha256=sha256_bytes(content),
            path=path,
        )
    return documents


def plan_delta(
    local: dict[str, LocalDocument],
    remote: dict[str, RemoteDocument],
) -> DeltaPlan:
    """
    Compare local documents against remote documents and build a delta plan.

    Rules:
    - local only       => added
    - local + remote but hash/filename differs => updated
    - local + remote and hash/filename same    => skipped
    - remote only      => removed
    """

    added: list[LocalDocument] = []
    updated: list[DocumentUpdate] = []
    skipped: list[LocalDocument] = []

    # Compare every local document with its remote counterpart by article_id.
    for article_id, local_document in sorted(local.items()):
        remote_document = remote.get(article_id)

        # New local document that does not exist in Vector Store yet.
        if remote_document is None:
            added.append(local_document)

        # Existing document changed.
        # We consider it updated if content hash changed or filename changed.
        elif (
            local_document.sha256 != remote_document.sha256
            or local_document.filename != remote_document.filename
        ):
            updated.append(
                DocumentUpdate(local=local_document, remote=remote_document)
            )
        
        # Same article, same content hash, same filename.
        # No upload needed.
        else:
            skipped.append(local_document)

    # Documents that exist remotely but are no longer present locally.
    removed = [
        remote[article_id]
        for article_id in sorted(set(remote).difference(local))
    ]
    return DeltaPlan(
        added=tuple(added),
        updated=tuple(updated),
        skipped=tuple(skipped),
        removed=tuple(removed),
    )


class OpenAIVectorStoreDeltaSync:
    """
    Compare and synchronize article versions using remote file attributes.

    This class performs the OpenAI-specific operations:
    - load remote Vector Store file manifest
    - upload added/updated files
    - attach uploaded files to Vector Store
    - remove obsolete remote files
    - update Vector Store metadata
    """

    def __init__(
        self,
        client: Any,
        vector_store_id: str,
        chunking: ChunkingConfig,
        *,
        batch_size: int = 500,
    ) -> None:
        # OpenAI file batch API should be used with a bounded batch size.
        if not 1 <= batch_size <= 500:
            raise ValueError("batch_size must be between 1 and 500")
        
        # OpenAI file batch API should be used with a bounded batch size.
        self.client = client
        self.vector_store_id = vector_store_id
        self.chunking = chunking
        self.batch_size = batch_size
        self.duplicate_documents: list[RemoteDocument] = []

    def load_remote_documents(
        self,
        *,
        bootstrap_documents: dict[str, LocalDocument] | None = None,
        persist_bootstrap_attributes: bool = True,
    ) -> dict[str, RemoteDocument]:
        """
        Load the remote Vector Store document manifest.

        If remote files already have article_id/sha256/filename attributes,
        those attributes are used directly.

        If remote files are legacy files without attributes, this method can
        bootstrap attributes from local Markdown files by matching filenames.
        """

        # List files currently attached to the Vector Store.
        first_page = self.client.vector_stores.files.list(
            vector_store_id=self.vector_store_id,
            limit=100,
            order="asc",
        )


        pages = (
            first_page.iter_pages()
            if hasattr(first_page, "iter_pages")
            else (first_page,)
        )

        # Remote manifest keyed by article_id.
        documents: dict[str, RemoteDocument] = {}
        self.duplicate_documents = []

        # Build filename -> LocalDocument map for bootstrapping legacy files.
        bootstrap_by_filename = {
            item.filename: item
            for item in (bootstrap_documents or {}).values()
        }

        # Iterate through every page and every Vector Store file.
        for page in pages:
            for vector_file in page.data:
                # Remote file must be fully processed before we sync.
                status = getattr(vector_file, "status", "completed")
                if status != "completed":
                    raise VectorStoreDeltaSyncError(
                        f"Remote file {vector_file.id} has status {status}"
                    )

                # Read metadata attributes from the Vector Store file.
                attributes = dict(getattr(vector_file, "attributes", None) or {})

                # Normal path: Remote file already has article_id, filename, and sha256.
                if all(attributes.get(key) for key in REMOTE_ATTRIBUTE_KEYS):
                    article_id = str(attributes["article_id"])
                    filename = str(attributes["filename"])
                    digest = str(attributes["sha256"])

                # Legacy path: Remote file does not have attributes yet. Use local Markdown mirror to reconstruct attributes by filename.    
                else:
                    # Retrieve OpenAI File object to get its filename.
                    file_object = self.client.files.retrieve(vector_file.id)
                    filename = str(file_object.filename)

                    # Match remote filename to local baseline document.
                    baseline = bootstrap_by_filename.get(filename)

                    # If no local file exists for this remote file, sync is unsafe.
                    if baseline is None:
                        raise VectorStoreDeltaSyncError(
                            "Cannot bootstrap legacy Vector Store file "
                            f"{filename!r}: the original Markdown file is not "
                            "available in data/markdown"
                        )
                    
                    # Use local baseline metadata.
                    article_id = baseline.article_id
                    digest = baseline.sha256
                    attributes = {
                        "article_id": article_id,
                        "filename": filename,
                        "sha256": digest,
                    }

                    # Persist reconstructed attributes to remote file when allowed.
                    # This makes future syncs faster and more reliable.
                    if persist_bootstrap_attributes:
                        self.client.vector_stores.files.update(
                            vector_file.id,
                            vector_store_id=self.vector_store_id,
                            attributes=attributes,
                        )
                        LOGGER.info("Bootstrapped remote attributes for %s", filename)

                candidate = RemoteDocument(
                    article_id=article_id,
                    filename=filename,
                    sha256=digest,
                    file_id=vector_file.id,
                    created_at=int(getattr(vector_file, "created_at", 0) or 0),
                )

                # OpenAI file removal is eventually consistent. During that
                # window both the old and replacement copy may be listed.
                # Keep the newest completed copy and clean the stale one in
                # apply() instead of failing the entire daily job.
                existing = documents.get(article_id)
                if existing is None:
                    documents[article_id] = candidate
                    continue

                if (candidate.created_at, candidate.file_id) > (
                    existing.created_at,
                    existing.file_id,
                ):
                    documents[article_id] = candidate
                    stale = existing
                else:
                    stale = candidate
                self.duplicate_documents.append(stale)
                LOGGER.warning(
                    "Duplicate Article ID %s: keeping newest file and "
                    "queuing stale file %s for cleanup",
                    article_id,
                    stale.file_id,
                )
        return documents

    def apply(self, plan: DeltaPlan) -> DeltaSyncResult:
        """
        Apply a delta plan to the OpenAI Vector Store.

        Order is important:
        1. Upload added/updated files first.
        2. Attach and wait for indexing to complete.
        3. Only then remove old updated files and removed files.

        This prevents losing existing knowledge if the new upload fails.
        """

        uploaded_file_ids: list[str] = []
        batch_ids: list[str] = []
        changed = plan.changed_documents

        try:
            # Entries passed to vector_stores.file_batches.create_and_poll().
            entries: list[dict[str, object]] = []

            # Upload each changed local document as an OpenAI File object.
            for document in changed:
                with document.path.open("rb") as stream:
                    uploaded = self.client.files.create(
                        file=stream,
                        purpose="assistants",
                    )

                # Track uploaded ID for possible cleanup.
                uploaded_file_ids.append(uploaded.id)

                # Prepare Vector Store file batch entry.
                entries.append(
                    {
                        "file_id": uploaded.id,
                        "attributes": document.attributes,
                        "chunking_strategy": self.chunking.api_payload,
                    }
                )

            # Attach uploaded files to the Vector Store in batches.
            for start in range(0, len(entries), self.batch_size):
                batch_entries = entries[start : start + self.batch_size]
                batch = self.client.vector_stores.file_batches.create_and_poll(
                    vector_store_id=self.vector_store_id,
                    files=batch_entries,
                )

                # Validate batch ingestion status.
                counts = batch.file_counts
                if (
                    batch.status != "completed"
                    or counts.completed != len(batch_entries)
                    or counts.failed
                    or counts.cancelled
                    or counts.in_progress
                ):
                    raise VectorStoreDeltaSyncError(
                        "Delta batch ingestion was incomplete: "
                        f"status={batch.status}, completed={counts.completed}, "
                        f"expected={len(batch_entries)}, failed={counts.failed}, "
                        f"cancelled={counts.cancelled}, "
                        f"in_progress={counts.in_progress}"
                    )
                
                # Save batch ID for report.
                batch_ids.append(batch.id)
        
        # If any upload/indexing step fails, remove newly created OpenAI files.
        except Exception:
            self._cleanup_new_files(uploaded_file_ids)
            raise
        
        # Obsolete remote files are:
        # - old remote versions of updated documents
        # - documents removed from the source corpus
        obsolete_candidates = (
            [item.remote for item in plan.updated]
            + list(plan.removed)
            + self.duplicate_documents
        )
        obsolete = list(
            {item.file_id: item for item in obsolete_candidates}.values()
        )
        detached = 0
        deleted_objects = 0

        # Detach and delete obsolete files.
        for document in obsolete:
            try:
                self.client.vector_stores.files.delete(
                    document.file_id,
                    vector_store_id=self.vector_store_id,
                )
                detached += 1
            except Exception as error:
                # A previous run may already have detached the file while an
                # eventually-consistent list response still returns it.
                if getattr(error, "status_code", None) == 404:
                    LOGGER.info(
                        "Vector Store file %s was already detached",
                        document.file_id,
                    )
                else:
                    raise
            try:
                self.client.files.delete(document.file_id)
                deleted_objects += 1
            except Exception as error:  # pragma: no cover - remote cleanup warning
                if getattr(error, "status_code", None) == 404:
                    LOGGER.info(
                        "OpenAI File object %s was already deleted",
                        document.file_id,
                    )
                else:
                    LOGGER.warning(
                        "Detached %s but could not delete File object %s: %s",
                        document.filename,
                        document.file_id,
                        error,
                    )

        # Retrieve updated Vector Store usage.
        store = self.client.vector_stores.retrieve(self.vector_store_id)

        # Return sync result for report/logging.
        return DeltaSyncResult(
            batch_ids=tuple(batch_ids),
            uploaded_files=len(uploaded_file_ids),
            detached_files=detached,
            deleted_file_objects=deleted_objects,
            vector_store_bytes=store.usage_bytes,
        )

    def update_store_metadata(self, source_files: int, timestamp: str) -> None:
        """
        Update Vector Store metadata after a successful sync.
        """

        self.client.vector_stores.update(
            self.vector_store_id,
            metadata={
                "corpus": "optisigns_support",
                "source_files": str(source_files),
                "chunk_size": str(self.chunking.max_chunk_size_tokens),
                "chunk_overlap": str(self.chunking.chunk_overlap_tokens),
                "last_synced_utc": timestamp,
            },
        )

    def _cleanup_new_files(self, file_ids: Iterable[str]) -> None:
        """
        Best-effort cleanup for files uploaded during a failed sync.

        This function intentionally suppresses cleanup errors because the
        original upload/indexing exception is more important.
        """

        for file_id in file_ids:
            # Try to detach the file from the Vector Store if it was attached.
            try:
                self.client.vector_stores.files.delete(
                    file_id,
                    vector_store_id=self.vector_store_id,
                )
            except Exception:
                pass

            # Try to delete the OpenAI File object.
            try:
                self.client.files.delete(file_id)
            except Exception:
                pass
