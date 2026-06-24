"""Lazy spaCy model loading.

The goblin ethos: a small, fast, CPU-only model by default. We cache loaded
pipelines so repeated ``extract`` calls don't reload the model.
"""

from __future__ import annotations

from functools import lru_cache

DEFAULT_MODEL = "en_core_web_sm"


@lru_cache(maxsize=None)
def load(model: str = DEFAULT_MODEL):
    """Load (and cache) a spaCy pipeline by name.

    Raises a friendly error if spaCy or the model isn't installed.
    """
    try:
        import spacy
    except ImportError as exc:  # pragma: no cover - depends on environment
        raise ImportError(
            "Hobgoblin needs spaCy. Install with:\n"
            "    pip install spacy\n"
            f"    python -m spacy download {model}"
        ) from exc

    try:
        return spacy.load(model)
    except OSError as exc:  # pragma: no cover - depends on environment
        raise OSError(
            f"spaCy model '{model}' isn't installed. Install it with:\n"
            f"    python -m spacy download {model}"
        ) from exc
