"""Tests for hobgoblin.extract.

These require the spaCy model ``en_core_web_sm``. If it isn't installed the
whole module is skipped (with an instruction to install it).
"""

import pytest

from hobgoblin import extract

pytest.importorskip("spacy", reason="spaCy not installed")

try:
    import spacy

    spacy.load("en_core_web_sm")
except Exception:  # noqa: BLE001
    pytest.skip(
        "en_core_web_sm not installed: python -m spacy download en_core_web_sm",
        allow_module_level=True,
    )


SENT = "Last Tuesday, John bought three boxes of red apples."


def _by_head(entities, head):
    return next(e for e in entities if e["head"] == head)


def test_finds_adj_noun_entity():
    ents = extract(SENT)
    heads = {e["head"] for e in ents}
    assert "apples" in heads
    apples = _by_head(ents, "apples")
    # "red apples" should be an ADJ+NOUN pattern.
    assert apples["pattern"] == "ADJ+NOUN"
    assert "red" in [m["text"] for m in apples["modifiers"]]


def test_char_spans_reconstruct_source():
    ents = extract(SENT)
    apples = _by_head(ents, "apples")
    s, e = apples["span"]
    assert SENT[s:e] == apples["entity"]
    # every token span must round-trip too
    for tok in apples["tokens"]:
        ts, te = tok["span"]
        assert SENT[ts:te] == tok["text"]


def test_governing_verb_and_count_and_date():
    ents = extract(SENT)
    apples = _by_head(ents, "apples")
    ctx = apples["context"]
    assert ctx["verb"]["lemma"] == "buy"
    # "three boxes of red apples" -> measure construction
    count = ctx["count"]
    assert count is not None
    assert count["value"] == 3
    assert count["measure"]["text"] == "boxes"
    assert count["helper"]["text"] == "of"
    # date picked up by NER
    assert any(d["text"].lower().endswith("tuesday") for d in ctx["dates"])


def test_bare_numeric_count():
    ents = extract("She has three cats.")
    cats = _by_head(ents, "cats")
    assert cats["context"]["count"]["value"] == 3
    assert "measure" not in cats["context"]["count"]


def test_anchors_flag_mode_marks_all():
    ents = extract(SENT, anchors=["apple"])
    apples = _by_head(ents, "apples")
    assert apples["anchors_matched"] == ["apple"]
    # flag mode keeps non-matching entities too
    assert any(e["anchors_matched"] == [] for e in ents)


def test_anchors_filter_mode_drops_non_matches():
    ents = extract(SENT, anchors=["apple"], anchor_mode="filter")
    assert len(ents) >= 1
    assert all(e["anchors_matched"] for e in ents)
    assert all("apple" in e["anchors_matched"] for e in ents)


def test_overlap_linking():
    ents = extract("the old wooden table")
    # the head entity should exist; inner overlaps (if any) link via part_of
    spans = {tuple(e["span"]) for e in ents}
    for e in ents:
        if e["part_of"] is not None:
            assert tuple(e["part_of"]) in spans
