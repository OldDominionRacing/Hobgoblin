"""Hobgoblin — cheap-first, goblin-first primitives for agent subtasks.

The first primitive is :func:`extract`, a deterministic spaCy-based entity and
context extractor. See ``DESIGN.md`` for the full design.
"""

from .extract import extract
from .anchors import apply_anchors

__all__ = ["extract", "apply_anchors"]
__version__ = "0.1.0"
