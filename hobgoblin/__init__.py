"""Hobgoblin — cheap-first, goblin-first primitives for agent subtasks.

The first primitive is :func:`extract`, a deterministic spaCy-based entity and
context extractor. See ``DESIGN.md`` for the full design.
"""

from .extract import extract
from .anchors import apply_anchors, NAME, PLACE
from .associate import item_index
from .items import detect as detect_items
from .military import detect_units
from .packs import ANCHORS

__all__ = [
    "extract", "apply_anchors", "item_index", "detect_items", "detect_units",
    "NAME", "PLACE", "ANCHORS",
]
__version__ = "0.1.0"
