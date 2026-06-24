"""``hobgoblin.extract`` — deterministic entity & context extraction via spaCy.

Finds candidate entities by their POS / dependency shape, then gathers the
surrounding context (governing verb, count, dates, modifiers) with exact
character offsets so the source document can be reconstructed and highlighted.

See ``DESIGN.md`` for the full specification.
"""

from __future__ import annotations

from typing import Iterable, Optional

from ._model import DEFAULT_MODEL, load
from .anchors import apply_anchors

# Lightweight word -> number map for count values. Unknown words keep value=None.
_NUM_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
    "thousand": 1000, "million": 1000000,
    "couple": 2, "pair": 2, "dozen": 12,
}

# Quantity words that imply a count without a precise numeric value.
_QUANTITY_WORDS = {
    "several", "many", "few", "numerous", "various", "multiple",
    "some", "lot", "lots", "plenty", "handful",
}


def _span(token) -> list[int]:
    """Character offsets ``[start, end]`` for a single token."""
    return [token.idx, token.idx + len(token.text)]


def _to_value(text: str) -> Optional[float]:
    """Best-effort numeric value for a count token."""
    cleaned = text.replace(",", "").strip()
    try:
        f = float(cleaned)
        return int(f) if f.is_integer() else f
    except ValueError:
        return _NUM_WORDS.get(cleaned.lower())


def _governing_verb(head) -> Optional[dict]:
    """The verb that grammatically governs ``head`` (nearest VERB, else AUX)."""
    fallback = None
    for anc in head.ancestors:
        if anc.pos_ == "VERB":
            return {"text": anc.text, "lemma": anc.lemma_, "span": _span(anc)}
        if anc.pos_ == "AUX" and fallback is None:
            fallback = {"text": anc.text, "lemma": anc.lemma_, "span": _span(anc)}
    return fallback


def _subject_of(verb_span: Optional[dict], doc) -> Optional[dict]:
    """nsubj of the verb token at ``verb_span`` (if any)."""
    if not verb_span:
        return None
    start = verb_span["span"][0]
    for tok in doc:
        if tok.idx == start:
            for child in tok.children:
                if child.dep_ in ("nsubj", "nsubjpass"):
                    return {"text": child.text, "span": _span(child)}
    return None


def _find_count(head) -> Optional[dict]:
    """Detect a count attached to ``head``.

    Handles three shapes, in priority order:
      1. measure + helper:  "three **boxes of** apples"  (head is pobj of "of")
      2. bare numeric:      "three apples"               (nummod on head)
      3. quantity word:     "several apples"             (value left as None)
    """
    # 1. measure-of construction: head is the object of an "of" preposition.
    if head.dep_ == "pobj" and head.head.lemma_ == "of" and head.head.pos_ == "ADP":
        helper = head.head
        measure = helper.head
        count = {
            "measure": {"text": measure.text, "span": _span(measure)},
            "helper": {"text": helper.text, "span": _span(helper)},
        }
        for child in measure.children:
            if child.dep_ == "nummod":
                count.update(
                    text=child.text, value=_to_value(child.text), span=_span(child)
                )
                break
        return count

    # 2. bare numeric modifier on the head.
    for child in head.children:
        if child.dep_ == "nummod":
            return {
                "text": child.text,
                "value": _to_value(child.text),
                "span": _span(child),
            }

    # 3. quantity word.
    for child in head.children:
        if child.lemma_.lower() in _QUANTITY_WORDS:
            return {
                "text": child.text,
                "value": _to_value(child.text),
                "span": _span(child),
            }

    return None


def _modifiers(head) -> list[dict]:
    """Adjectives / compounds decorating ``head``, in surface order."""
    mods = [
        {"text": c.text, "span": _span(c)}
        for c in head.children
        if c.dep_ in ("amod", "compound") and c.pos_ in ("ADJ", "NOUN", "PROPN")
    ]
    return sorted(mods, key=lambda m: m["span"][0])


def _pattern_label(chunk) -> str:
    """POS-shape label for a chunk, e.g. ``ADJ+NOUN`` (determiners dropped)."""
    poss = [t.pos_ for t in chunk if t.pos_ != "DET"]
    return "+".join(poss) if poss else chunk.root.pos_


def extract(
    text: str,
    anchors: Optional[Iterable[str]] = None,
    *,
    anchor_mode: str = "flag",
    model: str = DEFAULT_MODEL,
) -> list[dict]:
    """Extract entities and their context from ``text``.

    Returns a list of entity dicts (see ``DESIGN.md`` for the schema). If
    ``anchors`` is given, each entity is tagged with ``anchors_matched`` and,
    when ``anchor_mode="filter"``, only matched entities are returned.
    """
    nlp = load(model)
    doc = nlp(text)

    # Per-sentence date cache (spaCy NER DATE / TIME).
    sent_dates: dict[int, list[dict]] = {}
    for sent in doc.sents:
        sent_dates[sent.start] = [
            {"text": e.text, "label": e.label_, "span": [e.start_char, e.end_char]}
            for e in sent.ents
            if e.label_ in ("DATE", "TIME")
        ]

    entities: list[dict] = []
    for chunk in doc.noun_chunks:
        head = chunk.root
        sent = chunk.sent
        verb = _governing_verb(head)

        context = {
            "sentence": sent.text,
            "sentence_span": [sent.start_char, sent.end_char],
            "verb": verb,
            "count": _find_count(head),
            "dates": sent_dates.get(sent.start, []),
            "subject": _subject_of(verb, doc),
        }

        entities.append(
            {
                "entity": chunk.text,
                "head": head.text,
                "span": [chunk.start_char, chunk.end_char],
                "pattern": _pattern_label(chunk),
                "tokens": [
                    {
                        "text": t.text,
                        "pos": t.pos_,
                        "dep": t.dep_,
                        "lemma": t.lemma_,
                        "span": _span(t),
                    }
                    for t in chunk
                ],
                "modifiers": _modifiers(head),
                "context": context,
                "anchors_matched": [],
                "part_of": None,
            }
        )

    _link_overlaps(entities)

    if anchors is not None:
        entities = apply_anchors(entities, anchors, mode=anchor_mode, model=model)

    return entities


def _link_overlaps(entities: list[dict]) -> None:
    """Set ``part_of`` to the span of the smallest entity strictly containing each."""
    for ent in entities:
        s, e = ent["span"]
        smallest = None
        for other in entities:
            if other is ent:
                continue
            os, oe = other["span"]
            if os <= s and e <= oe and (os, oe) != (s, e):
                size = oe - os
                if smallest is None or size < smallest[0]:
                    smallest = (size, [os, oe])
        ent["part_of"] = smallest[1] if smallest else None
