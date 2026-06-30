"""Tests for static chunk validation and transparent chunk estimation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from support_ingestion.vector_store.chunking import (
    ChunkingConfig,
    estimate_corpus_chunks,
)


class ChunkingConfigTests(unittest.TestCase):
    def test_estimates_overlapping_chunks(self) -> None:
        config = ChunkingConfig(
            max_chunk_size_tokens=1_200,
            chunk_overlap_tokens=200,
        )

        self.assertEqual(0, config.estimate_chunk_count(0))
        self.assertEqual(1, config.estimate_chunk_count(1_200))
        self.assertEqual(2, config.estimate_chunk_count(1_201))
        self.assertEqual(3, config.estimate_chunk_count(2_201))

    def test_rejects_overlap_greater_than_half(self) -> None:
        with self.assertRaises(ValueError):
            ChunkingConfig(
                max_chunk_size_tokens=1_000,
                chunk_overlap_tokens=501,
            )

    def test_estimates_nonempty_utf8_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "xin-chao.md"
            path.write_text("# Xin chào\n\nNội dung hỗ trợ.\n", encoding="utf-8")

            result = estimate_corpus_chunks([path], ChunkingConfig())

            self.assertEqual(1, result.source_files)
            self.assertGreater(result.total_tokens, 0)
            self.assertEqual(1, result.estimated_chunks)


if __name__ == "__main__":
    unittest.main()
