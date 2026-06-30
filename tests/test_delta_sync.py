"""Tests for manifest bootstrap, delta planning, and remote replacement order."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from support_ingestion.vector_store.chunking import ChunkingConfig
from support_ingestion.vector_store.sync import (
    OpenAIVectorStoreDeltaSync,
    RemoteDocument,
    build_local_documents,
    plan_delta,
)


# Small OpenAI API doubles capture requests without making network calls.
class FakePage:
    def __init__(self, data: list[SimpleNamespace]) -> None:
        self.data = data

    def iter_pages(self):
        yield self


class FakeFilesAPI:
    def __init__(self) -> None:
        self.created: list[tuple[str, bytes, str]] = []
        self.deleted: list[str] = []

    def retrieve(self, file_id: str) -> SimpleNamespace:
        return SimpleNamespace(filename="old.md")

    def create(self, *, file, purpose: str) -> SimpleNamespace:
        file_id = f"file-new-{len(self.created) + 1}"
        self.created.append((file_id, file.read(), purpose))
        return SimpleNamespace(id=file_id)

    def delete(self, file_id: str) -> SimpleNamespace:
        self.deleted.append(file_id)
        return SimpleNamespace(id=file_id, deleted=True)


class FakeVectorStoreFilesAPI:
    def __init__(self) -> None:
        self.updated: list[tuple[str, dict[str, str]]] = []
        self.deleted: list[str] = []

    def list(self, **_: object) -> FakePage:
        return FakePage(
            [
                SimpleNamespace(
                    id="file-old",
                    status="completed",
                    attributes=None,
                )
            ]
        )

    def update(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        attributes: dict[str, str],
    ) -> SimpleNamespace:
        self.updated.append((file_id, attributes))
        return SimpleNamespace(id=file_id, attributes=attributes)

    def delete(self, file_id: str, **_: object) -> SimpleNamespace:
        self.deleted.append(file_id)
        return SimpleNamespace(id=file_id, deleted=True)


class FakeBatchesAPI:
    def __init__(self) -> None:
        self.calls: list[list[dict[str, object]]] = []

    def create_and_poll(self, **kwargs: object) -> SimpleNamespace:
        entries = list(kwargs["files"])
        self.calls.append(entries)
        return SimpleNamespace(
            id=f"batch-{len(self.calls)}",
            status="completed",
            file_counts=SimpleNamespace(
                completed=len(entries),
                failed=0,
                cancelled=0,
                in_progress=0,
            ),
        )


class FakeVectorStoresAPI:
    def __init__(self) -> None:
        self.files = FakeVectorStoreFilesAPI()
        self.file_batches = FakeBatchesAPI()
        self.metadata: dict[str, str] | None = None

    def retrieve(self, _: str) -> SimpleNamespace:
        return SimpleNamespace(usage_bytes=4321)

    def update(self, _: str, *, metadata: dict[str, str]) -> SimpleNamespace:
        self.metadata = metadata
        return SimpleNamespace(metadata=metadata)


class DeltaSyncTests(unittest.TestCase):
    def test_builds_manifest_and_plans_every_delta_category(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            added_path = root / "added.md"
            updated_path = root / "updated.md"
            skipped_path = root / "skipped.md"
            added_path.write_text("# Added\nArticle ID: 1\n", encoding="utf-8")
            updated_path.write_text("# Updated\nArticle ID: 2\n", encoding="utf-8")
            skipped_path.write_text("# Same\nArticle ID: 3\n", encoding="utf-8")

            local = build_local_documents([added_path, updated_path, skipped_path])
            remote = {
                "2": RemoteDocument("2", "updated.md", "old-hash", "file-2"),
                "3": RemoteDocument(
                    "3", "skipped.md", local["3"].sha256, "file-3"
                ),
                "4": RemoteDocument("4", "removed.md", "hash", "file-4"),
            }

            plan = plan_delta(local, remote)

            self.assertEqual(["1"], [item.article_id for item in plan.added])
            self.assertEqual(["2"], [item.local.article_id for item in plan.updated])
            self.assertEqual(["3"], [item.article_id for item in plan.skipped])
            self.assertEqual(["4"], [item.article_id for item in plan.removed])

    def test_bootstraps_attributes_for_legacy_vector_store_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "old.md"
            path.write_text("# Old\n\nArticle ID: 10\n", encoding="utf-8")
            baseline = build_local_documents([path])
            files = FakeFilesAPI()
            vector_stores = FakeVectorStoresAPI()
            client = SimpleNamespace(files=files, vector_stores=vector_stores)
            synchronizer = OpenAIVectorStoreDeltaSync(
                client,
                "vs-test",
                ChunkingConfig(),
            )

            manifest = synchronizer.load_remote_documents(
                bootstrap_documents=baseline
            )

            self.assertEqual("old.md", manifest["10"].filename)
            self.assertEqual("10", vector_stores.files.updated[0][1]["article_id"])
            self.assertEqual(64, len(vector_stores.files.updated[0][1]["sha256"]))

    def test_uploads_only_added_and_updated_then_removes_old_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            added_path = root / "added.md"
            updated_path = root / "updated.md"
            added_path.write_text("# Added\nArticle ID: 1\n", encoding="utf-8")
            updated_path.write_text("# Updated\nArticle ID: 2\n", encoding="utf-8")
            local = build_local_documents([added_path, updated_path])
            plan = plan_delta(
                local,
                {
                    "2": RemoteDocument("2", "updated.md", "old", "file-old-2"),
                    "3": RemoteDocument("3", "removed.md", "old", "file-old-3"),
                },
            )
            files = FakeFilesAPI()
            vector_stores = FakeVectorStoresAPI()
            client = SimpleNamespace(files=files, vector_stores=vector_stores)
            chunking = ChunkingConfig()

            result = OpenAIVectorStoreDeltaSync(
                client,
                "vs-test",
                chunking,
            ).apply(plan)

            self.assertEqual(2, result.uploaded_files)
            self.assertEqual(2, result.detached_files)
            self.assertEqual(["file-old-2", "file-old-3"], vector_stores.files.deleted)
            self.assertEqual(["file-old-2", "file-old-3"], files.deleted)
            entries = vector_stores.file_batches.calls[0]
            self.assertEqual(2, len(entries))
            self.assertEqual(chunking.api_payload, entries[0]["chunking_strategy"])
            self.assertEqual("1", entries[0]["attributes"]["article_id"])


if __name__ == "__main__":
    unittest.main()
