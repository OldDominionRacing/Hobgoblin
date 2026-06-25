"""Detect "items of interest" in text.

Everything here is deterministic: regex (with optional validators), spaCy token
alignment, a spaCy-NER pass for dates/times/percentages, and ``usaddress`` for
street addresses. Each item carries char span, token span, and a representative
root token index so the relatedness scorer can measure distance to entities.

Supported types:
    email, url, uuid, mac, ipv6, ipv4, coordinate, credit_card, ssn, phone,
    address, money, percent, time, handle, hashtag, file_path, zip, date
"""

from __future__ import annotations

import re

try:  # optional, declared dependency; degrade gracefully if absent
    import usaddress
except Exception:  # noqa: BLE001  # pragma: no cover
    usaddress = None


# --------------------------------------------------------------------------- #
# Validators (deterministic)
# --------------------------------------------------------------------------- #
def _luhn_ok(text: str) -> bool:
    digits = [int(c) for c in text if c.isdigit()]
    if not (13 <= len(digits) <= 19):
        return False
    total, parity = 0, len(digits) % 2
    for i, d in enumerate(digits):
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def _ipv4_ok(text: str) -> bool:
    parts = text.split(".")
    return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)


# --------------------------------------------------------------------------- #
# Patterns, in priority order (earlier wins on overlap). Each entry is
# (label, compiled_regex, validator_or_None).
# --------------------------------------------------------------------------- #
_STREET_SUFFIX = (
    r"Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|"
    r"Way|Place|Pl|Terrace|Ter|Circle|Cir|Highway|Hwy|Parkway|Pkwy"
)

_PATTERNS = [
    ("email", re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"), None),
    ("url", re.compile(r"\b(?:https?://|www\.)[^\s,;]+", re.I), None),
    ("uuid", re.compile(
        r"\b[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\b"), None),
    ("mac", re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b"), None),
    ("ipv6", re.compile(r"\b(?:[0-9A-Fa-f]{1,4}:){2,7}[0-9A-Fa-f]{1,4}\b"), None),
    ("ipv4", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), _ipv4_ok),
    ("coordinate", re.compile(
        r"[-+]?\d{1,3}\.\d+\s*,\s*[-+]?\d{1,3}\.\d+"), None),
    ("date", re.compile(
        r"\b\d{1,2}/\d{1,2}/\d{2,4}\b|\b\d{4}-\d{2}-\d{2}\b"), None),
    ("credit_card", re.compile(r"\b\d(?:[ -]?\d){12,18}\b"), _luhn_ok),
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), None),
    ("phone", re.compile(
        r"(?<!\d)(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}(?!\d)"),
        None),
    ("address", re.compile(
        r"\b\d{1,6}\s+(?:[A-Z][A-Za-z]*\.?\s+){1,4}(?:" + _STREET_SUFFIX + r")\b\.?"
        r"(?:,?\s+[A-Z][A-Za-z]+)*(?:,?\s+[A-Z]{2})?(?:\s+\d{5}(?:-\d{4})?)?"), None),
    ("money", re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?"), None),
    ("percent", re.compile(r"\b\d+(?:\.\d+)?\s?%"), None),
    ("time", re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\s?(?:[AaPp]\.?[Mm]\.?)?\b"), None),
    ("handle", re.compile(r"(?<!\w)@\w{2,}"), None),
    ("hashtag", re.compile(r"(?<!\w)#\w{2,}"), None),
    ("file_path", re.compile(
        r"[A-Za-z]:\\[\w\\.\- ]+|(?:/[\w.\-]+){2,}/?"), None),
    ("zip", re.compile(r"\b\d{5}(?:-\d{4})?\b"), None),
]

# spaCy NER labels mapped to item types (filled in after the regex pass so
# precise regex wins on overlap).
_NER_LABELS = {"DATE": "date", "TIME": "time", "PERCENT": "percent"}


def _ner_temporal_ok(text: str) -> bool:
    """Reject NER date/time spans that are just bare digit-runs (likely noise)."""
    text = text.strip()
    if re.search(r"[A-Za-z]", text):  # has a month/day word
        return True
    if re.search(r"[/\-.:]", text):  # has a date/time separator
        return True
    return bool(re.fullmatch(r"\d{4}", text))  # a lone 4-digit year is fine


def _parse_address(text: str):
    """Return usaddress components dict, or None if it doesn't look like one."""
    if usaddress is None:
        return None
    try:
        tagged, _kind = usaddress.tag(text)
    except Exception:  # noqa: BLE001 - RepeatedLabelError etc.
        return None
    if "AddressNumber" in tagged and any(k.startswith("StreetName") for k in tagged):
        return dict(tagged)
    return None


def _make_item(doc, label, cs, ce):
    span = doc.char_span(cs, ce, alignment_mode="expand")
    if span is None:
        return None
    item = {
        "type": label,
        "text": doc.text[cs:ce],
        "span": [cs, ce],
        "tok_start": span.start,
        "tok_end": span.end,
        "root_i": span.root.i,
    }
    if label == "address":
        comps = _parse_address(doc.text[cs:ce])
        if comps is None and usaddress is not None:
            return None  # usaddress available and rejected it
        if comps is not None:
            item["components"] = comps
    return item


def detect(doc) -> list[dict]:
    """Find items of interest in a spaCy ``doc`` (see module docstring)."""
    text = doc.text
    items: list[dict] = []
    claimed: list[tuple[int, int]] = []

    def _overlaps(cs, ce):
        return any(cs < oe and os < ce for os, oe in claimed)

    # 1. Regex patterns, priority order.
    for label, pattern, validator in _PATTERNS:
        for m in pattern.finditer(text):
            cs, ce = m.start(), m.end()
            if _overlaps(cs, ce):
                continue
            if validator and not validator(text[cs:ce]):
                continue
            item = _make_item(doc, label, cs, ce)
            if item is None:
                continue
            items.append(item)
            claimed.append((cs, ce))

    # 2. spaCy NER pass for dates/times/percentages not already claimed.
    for ent in doc.ents:
        label = _NER_LABELS.get(ent.label_)
        if not label or _overlaps(ent.start_char, ent.end_char):
            continue
        if label in ("date", "time") and not _ner_temporal_ok(ent.text):
            continue  # reject bare digit-runs NER sometimes mislabels as dates
        item = _make_item(doc, label, ent.start_char, ent.end_char)
        if item is None:
            continue
        items.append(item)
        claimed.append((ent.start_char, ent.end_char))

    items.sort(key=lambda it: it["span"][0])
    return items
