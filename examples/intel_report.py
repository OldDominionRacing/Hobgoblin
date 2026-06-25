#!/usr/bin/env python3
"""End-to-end Hobgoblin example: typed extraction over a short report.

Run it:
    pip install -e .
    python -m spacy download en_core_web_sm
    python examples/intel_report.py

It shows the full deterministic ("goblin-first") pipeline on one paragraph:
  1. entity finding (POS / dependency) with categorized anchors  -> typed entities
  2. count parsing (ranges, approximators, multipliers)
  3. military unit recognition (number / type / echelon)
  4. items of interest (phone, coordinate, date, ...) associated to entities
  5. the inverted item -> best-entity view
"""

from hobgoblin import extract, item_index, detect_units, ANCHORS, NAME

REPORT = (
    "On 14 March 2025, Colonel John Smith reported that the 3rd Brigdae and "
    "I Corps moved roughly 12 HMMWV trucks to Fort Bragg. "
    "B Battery held the depot at 35.139, -79.006 with about 3 vehicles. "
    "Contact the TOC at 555-867-5309 between 2 and 4 patrols per day."
)

# You can use the built-in military pack as-is, or extend it. Here we add a couple
# of corpus-specific aliases/misspellings on top of the defaults.
anchors = {
    "name": NAME,                                            # rule-based
    "military_unit": ANCHORS["military_unit"] + ["bgd"],     # extend with your alias
    "facility": ANCHORS["facility"],
    "equipment": ANCHORS["equipment"],
}


def fmt_count(c):
    if not c:
        return ""
    bits = [f"value={c['value']}"]
    if "range" in c:
        bits.append(f"range={c['range']}")
    if c.get("approx"):
        bits.append(f"approx~{c['qualifier']!r}")
    if c.get("form") == "multiplier":
        bits.append("(multiplier)")
    return "  count[" + ", ".join(bits) + "]"


def main():
    print(REPORT)
    print("=" * 78)

    ents = extract(REPORT, anchors=anchors)

    print("\nTYPED ENTITIES (only those that matched an anchor):")
    for e in ents:
        if not e["anchors_matched"]:
            continue
        tags = ",".join(e["anchors_matched"])
        line = f"  [{tags:<9}] {e['entity']!r}"
        if e["mil_unit"]:
            m = e["mil_unit"]
            typ = f" {m['type']}" if m["type"] else ""
            line += f"   unit<#{m['number']}{typ} {m['echelon']} ({m['number_form']})>"
        line += fmt_count(e["context"]["count"])
        print(line)

    print("\nPARSED COUNTS (any entity with a numeric count):")
    for e in ents:
        c = e["context"]["count"]
        if c:
            print(f"  {e['entity']!r:28}{fmt_count(c)}")

    print("\nALL MILITARY UNITS (standalone recognizer):")
    for u in detect_units(REPORT):
        typ = f" · type {u['type']}" if u["type"] else ""
        print(f"  {u['text']!r:24} -> #{u['number']} · {u['echelon']}{typ}")

    print("\nITEMS OF INTEREST -> best-related entity:")
    for it in item_index(ents):
        be = it["best_entity"]
        target = f"{be['head']!r} (w={be['weight']})" if be else "(none)"
        print(f"  {it['type']:11} {it['text']!r:22} -> {target}")


if __name__ == "__main__":
    main()
