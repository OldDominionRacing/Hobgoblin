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


def test_year_is_not_counted():
    # "1903" in "the 1903 Nobel Prize" is a year (DATE), not a count.
    ents = extract("She won the 1903 Nobel Prize in Physics.", items=False)
    prize = _by_head(ents, "Prize")
    assert prize["context"]["count"] is None


def test_of_phrase_without_numeral_is_not_a_count():
    # "division of the United States Army" -> "Army" is pobj of "of" but there's
    # no numeral, so it must not be reported as a count.
    ents = extract("It is a division of the United States Army.", items=False)
    army = _by_head(ents, "Army")
    assert army["context"]["count"] is None


def test_ordinal_unit_name_is_not_counted():
    ents = extract("The 1st Infantry Division fought bravely.", items=False)
    div = _by_head(ents, "Division")
    assert div["context"]["count"] is None


def test_bare_numeric_count():
    ents = extract("She has three cats.")
    cats = _by_head(ents, "cats")
    assert cats["context"]["count"]["value"] == 3
    assert "measure" not in cats["context"]["count"]


@pytest.mark.parametrize("text", ["3x cars drove off.", "3X cars", "3× cars here."])
def test_multiplier_shorthand_counts(text):
    ents = extract(text, items=False, military=False)
    cars = _by_head(ents, "cars")
    count = cars["context"]["count"]
    assert count["value"] == 3
    assert count["form"] == "multiplier"


@pytest.mark.parametrize("text,lo,hi", [
    ("3-5 cars", 3, 5),
    ("3 to 5 cars", 3, 5),
    ("between 3 and 5 cars", 3, 5),
])
def test_range_counts(text, lo, hi):
    ents = extract(text, items=False, military=False)
    count = _by_head(ents, "cars")["context"]["count"]
    assert count["range"] == [lo, hi]


@pytest.mark.parametrize("text,qual", [
    ("about three cars", "about"),
    ("approximately 3 cars", "approximately"),
    ("~3 cars", "~"),
    ("more than 5 cars", "more than"),
    ("over 100 cars", "over"),
    ("at least 10 cars", "at least"),
])
def test_approximator_counts(text, qual):
    ents = extract(text, items=False, military=False)
    count = _by_head(ents, "cars")["context"]["count"]
    assert count["approx"] is True
    assert count["qualifier"] == qual


def test_all_caps_recovers_entities_and_preserves_casing():
    caps = "THE 3RD BRIGADE AND I CORPS MOVED 12 HMMWV TRUCKS."
    heads = {e["head"] for e in extract(caps, items=False)}
    # I CORPS / 12 HMMWV TRUCKS are lost without normalization; recovered with it
    assert "CORPS" in heads
    assert any("TRUCKS" in e["entity"] for e in extract(caps, items=False))
    # surface text keeps original casing, not the lowercased copy spaCy parsed
    assert any(e["entity"].isupper() for e in extract(caps, items=False))


def test_all_caps_annotates_units():
    ents = extract("I CORPS ADVANCED.", items=False)
    corps = _by_head(ents, "CORPS")
    assert corps["mil_unit"] and corps["mil_unit"]["echelon"] == "Corps"


def test_normalize_case_can_be_disabled():
    caps = "THE 3RD BRIGADE AND I CORPS MOVED."
    off = {e["head"] for e in extract(caps, items=False, normalize_case=False)}
    on = {e["head"] for e in extract(caps, items=False, normalize_case=True)}
    # normalization recovers at least as many heads as leaving it off
    assert len(on) >= len(off)


def test_drop_generic_precision_mode():
    text = "The film featured great actors. Microsoft and John Smith attended."
    default = {e["head"] for e in extract(text)}
    assert "film" in default and "actors" in default          # kept by default
    precise = {e["head"] for e in extract(text, drop_generic=True)}
    assert "film" not in precise and "actors" not in precise   # generic dropped
    assert "Microsoft" in precise and "Smith" in precise       # proper nouns kept


def test_drop_generic_keeps_anchored():
    # an anchored common noun is elevated even in precision mode
    ents = extract("The depot was secure.", anchors={"facility": ["depot"]},
                   drop_generic=True)
    assert any(e["head"] == "depot" for e in ents)


def test_drops_stopword_entities():
    heads = {e["head"] for e in extract("It moved. The brigade advanced.")}
    assert "It" not in heads          # bare pronoun dropped
    assert "brigade" in heads         # content entity kept
    # disabling the filter keeps them
    assert "It" in {e["head"] for e in extract("It moved.", drop_stops=False)}


def test_plain_count_has_no_range_or_approx():
    count = _by_head(extract("She has three cars.", items=False), "cars")["context"]["count"]
    assert "range" not in count
    assert "approx" not in count


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
