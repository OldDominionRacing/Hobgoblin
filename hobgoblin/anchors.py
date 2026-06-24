"""Anchor matching.

Anchors are words the user cares about. They match entities by **lemma**,
**case-insensitively**, with **OR** logic across multiple anchors. Each matched
entity records *which* anchors hit it in ``anchors_matched``.

Two modes:
- ``"flag"``   (default) — return all entities, tagging matches.
- ``"filter"`` — return only entities that matched at least one anchor.
"""

from __future__ import annotations

from typing import Iterable

from ._model import DEFAULT_MODEL, load


def _lemmatize_anchors(anchors: Iterable[str], model: str = DEFAULT_MODEL) -> set[str]:
    """Reduce each anchor to its lowercased lemma(s)."""
    nlp = load(model)
    lemmas: set[str] = set()
    for anchor in anchors:
        for tok in nlp(anchor):
            if tok.is_space or tok.is_punct:
                continue
            lemmas.add(tok.lemma_.lower())
    return lemmas


def apply_anchors(
    entities: list[dict],
    anchors: Iterable[str],
    *,
    mode: str = "flag",
    model: str = DEFAULT_MODEL,
) -> list[dict]:
    """Tag (and optionally filter) ``entities`` by ``anchors``.

    Each entity dict must carry ``tokens`` with per-token ``lemma`` (as produced
    by :func:`hobgoblin.extract`). Mutates entities in place to set
    ``anchors_matched`` and returns the (possibly filtered) list.
    """
    if mode not in ("flag", "filter"):
        raise ValueError(f"mode must be 'flag' or 'filter', got {mode!r}")

    anchor_lemmas = _lemmatize_anchors(anchors, model=model)

    for ent in entities:
        ent_lemmas = {t.get("lemma", "").lower() for t in ent.get("tokens", [])}
        matched = sorted(anchor_lemmas & ent_lemmas)
        ent["anchors_matched"] = matched

    if mode == "filter":
        return [e for e in entities if e["anchors_matched"]]
    return entities
