"""Validate static chunking settings and estimate corpus chunk counts."""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from pathlib import Path

import tiktoken


@dataclass(frozen=True)
class ChunkingConfig:
    """
    Configuration for static chunking.

    This config controls how Markdown documents are split before being indexed
    in the OpenAI Vector Store.

    Example:
        max_chunk_size_tokens = 1200
        chunk_overlap_tokens = 200

    Meaning:
        Each chunk can contain up to 1200 tokens.
        Neighboring chunks share 200 overlapping tokens.
    """

    # Maximum number of tokens in one chunk.
    max_chunk_size_tokens: int = 1_200

    # Number of tokens repeated between neighboring chunks.
    chunk_overlap_tokens: int = 200

    # Tokenizer encoding used to estimate token counts.
    encoding_name: str = "o200k_base"

    def __post_init__(self) -> None:
        """
        Validate chunking values after the dataclass is initialized.
        This prevents invalid chunking configuration 
        """

        # Keep chunk size in a reasonable range.
        if not 100 <= self.max_chunk_size_tokens <= 4_096:
            raise ValueError("max_chunk_size_tokens must be between 100 and 4096")
        
        # Overlap cannot be negative.
        if self.chunk_overlap_tokens < 0:
            raise ValueError("chunk_overlap_tokens must be non-negative")
        
        # Overlap should not be too large. If overlap is more than half of chunk size, chunks become too repetitive.
        if self.chunk_overlap_tokens > self.max_chunk_size_tokens // 2:
            raise ValueError("chunk overlap cannot exceed half the chunk size")

    @property
    def api_payload(self) -> dict[str, object]:
        """
        Convert this config into the payload format expected by OpenAI API.

        This allows the sync pipeline to pass the same settings to OpenAI.
        """

        return {
            "type": "static",
            "static": {
                "max_chunk_size_tokens": self.max_chunk_size_tokens,
                "chunk_overlap_tokens": self.chunk_overlap_tokens,
            },
        }

    def estimate_chunk_count(self, token_count: int) -> int:
        """
        Estimate how many chunks a document will produce.

        Args:
            token_count:
                Number of tokens in one Markdown file.

        Returns:
            Estimated number of chunks for that file.
        """
        
        # Empty content produces no chunks.
        if token_count <= 0:
            return 0
        
        # If the document fits within one chunk, only one chunk is needed.
        if token_count <= self.max_chunk_size_tokens:
            return 1
        
        # Stride is how far the chunk window moves each time.
        stride = self.max_chunk_size_tokens - self.chunk_overlap_tokens

        # First chunk is counted as 1.
        # The remaining tokens after the first chunk are split by stride.
        # math.ceil is used because any leftover tokens still need a chunk.
        return 1 + math.ceil((token_count - self.max_chunk_size_tokens) / stride)


@dataclass(frozen=True)
class FileChunkEstimate:
    """
    Chunk estimate for a single Markdown file.
    """
        
    filename: str
    token_count: int
    estimated_chunks: int


@dataclass(frozen=True)
class CorpusChunkEstimate:
    """
    Chunk estimate for the whole Markdown corpus.

    A corpus means all Markdown files that will be uploaded to the Vector Store.
    """

    source_files: int
    total_tokens: int
    estimated_chunks: int
    files: tuple[FileChunkEstimate, ...]

    def to_dict(self) -> dict[str, object]:
        """
        Convert the corpus estimate into a JSON-serializable dictionary.

        This is used when writing dry-run/upload reports.
        """
                
        return {
            "source_files": self.source_files,
            "total_tokens": self.total_tokens,
            "estimated_chunks": self.estimated_chunks,
            "files": [asdict(item) for item in self.files],
        }


def estimate_corpus_chunks(
    paths: list[Path],
    config: ChunkingConfig,
) -> CorpusChunkEstimate:
    """
    Estimate token and chunk counts for a list of Markdown files.

    Args:
        paths:
            List of Markdown file paths.

        config:
            Chunking configuration used for estimation.

    Returns:
        CorpusChunkEstimate containing:
        - total source files
        - total tokens
        - estimated total chunks
        - per-file estimates
    """
    
    # Load the tokenizer based on the configured encoding name.
    encoding = tiktoken.get_encoding(config.encoding_name)

    # Store per-file estimates here.
    estimates: list[FileChunkEstimate] = []

    # Process each Markdown file one by one.
    for path in paths:
        text = path.read_text(encoding="utf-8")

        # Empty Markdown files should not be uploaded
        if not text.strip():
            raise ValueError(f"Markdown file is empty: {path}")
        
        # Count tokens in this Markdown file.
        token_count = len(encoding.encode(text))

        # Estimate chunk count using the configured chunk size and overlap
        estimates.append(
            FileChunkEstimate(
                filename=path.name,
                token_count=token_count,
                estimated_chunks=config.estimate_chunk_count(token_count),
            )
        )

    # Return aggregated corpus-level statistics.
    return CorpusChunkEstimate(
        source_files=len(estimates),
        total_tokens=sum(item.token_count for item in estimates),
        estimated_chunks=sum(item.estimated_chunks for item in estimates),
        files=tuple(estimates),
    )
