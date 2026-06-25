"""The wizard — optional LLM escalation over the goblin's deterministic draft.

The goblin runs first and cheap; the wizard receives a *compact structured draft*
(not raw text), so the LLM does one narrow job and the call stays small. Two jobs:

- ``suggest_anchors(text, ...)`` — propose anchor terms/categories for this corpus,
  so the analyst's pack gets better over time (the goblin stays model-free at runtime).
- ``fix(text, ...)`` — review the goblin's draft and return a list of corrections
  (drop junk, merge split entities, retype, add a missed one).

Two ways to wire the LLM, both supported:

1. **Bring your own** — pass ``llm=callable(prompt: str) -> str`` (any model/SDK).
   This is also how an agent that already knows Hobgoblin (the way it knows
   pytesseract) would call it: run ``extract`` cheaply, then hand these prompts to
   whatever model it's already driving.
2. **Anthropic default** — install ``anthropic`` and set ``ANTHROPIC_API_KEY``; if
   no ``llm`` is given we call Claude (``claude-opus-4-8``) for you.

Every prompt is **inspectable before you spend a token**: call the ``build_*_prompt``
functions directly, or pass ``dry_run=True`` to get back the exact prompt instead of
calling the model.
"""

from __future__ import annotations

import json
import re
from typing import Callable, Optional

from .extract import extract

DEFAULT_MODEL = "claude-opus-4-8"


# --------------------------------------------------------------------------- #
# Compact the goblin draft for the prompt (keep tokens small)
# --------------------------------------------------------------------------- #
def _entity_type(ent: dict) -> str:
    return ",".join(ent.get("anchors_matched") or []) or "untyped"


def _compact(entities: list[dict]) -> list[dict]:
    out = []
    for e in entities:
        row = {"entity": e["entity"], "type": _entity_type(e)}
        if e.get("mil_unit"):
            m = e["mil_unit"]
            row["unit"] = f"{m['number']} {m.get('type') or ''} {m['echelon']}".strip()
        out.append(row)
    return out


# --------------------------------------------------------------------------- #
# Prompt builders (inspect these before running)
# --------------------------------------------------------------------------- #
def build_anchor_prompt(text: str, entities: list[dict], anchors=None) -> str:
    """The prompt for ``suggest_anchors`` — returns the exact string sent to the LLM."""
    if isinstance(anchors, dict):
        cats = {k: (len(v) if isinstance(v, list) else 1) for k, v in anchors.items()}
        cat_line = ", ".join(f"{k} ({n} terms)" for k, n in cats.items()) or "(none)"
    else:
        cat_line = ", ".join(anchors) if anchors else "(none)"
    untyped = sorted({e["entity"] for e in entities if _entity_type(e) == "untyped"})
    return f"""\
You are refining a deterministic entity extractor ("the goblin"). The goblin already
ran a cheap rule-based pass over the document below. Do NOT re-extract everything —
propose ADDITIONAL anchor terms the analyst should add so the goblin catches more of
what matters in documents like this one.

Anchors are keywords grouped by category; the goblin tags an entity with a category
when the entity contains one of that category's terms (it already handles typos and
upper-case abbreviations, so don't bother listing those variants).

Current categories: {cat_line}

Entities the goblin found but could NOT type (the gaps worth closing):
{json.dumps(untyped, ensure_ascii=False)}

Return ONLY JSON, no prose:
{{"suggestions": {{"<category>": ["term", ...]}}, "notes": "one short line"}}
- Reuse an existing category name when it fits; invent a new snake_case category only
  when clearly warranted.
- Only propose terms grounded in THIS document (or obvious base forms of them).
- Don't repeat terms an existing category would already match.

DOCUMENT:
\"\"\"{text}\"\"\""""


def build_fix_prompt(text: str, entities: list[dict]) -> str:
    """The prompt for ``fix`` — returns the exact string sent to the LLM."""
    draft = json.dumps(_compact(entities), ensure_ascii=False, indent=0)
    return f"""\
A cheap deterministic extractor ("the goblin") produced the draft below from the
document. Find its ERRORS only — do not re-extract from scratch. Typical errors:
- junk fragments (a mis-parsed pronoun or punctuation became an "entity"),
- an entity that should be merged (e.g. a multi-word name a parser split apart),
- a wrong category,
- a clearly-important entity the goblin missed entirely.

Return ONLY JSON, no prose:
{{"corrections": [
  {{"action": "drop",   "entity": "...", "reason": "..."}},
  {{"action": "merge",  "entities": ["...", "..."], "into": "...", "type": "...", "reason": "..."}},
  {{"action": "retype", "entity": "...", "type": "...", "reason": "..."}},
  {{"action": "add",    "entity": "...", "type": "...", "reason": "..."}}
]}}
Be conservative — only confident corrections. Return an empty list if the draft is fine.

DRAFT (entity -> type):
{draft}

DOCUMENT:
\"\"\"{text}\"\"\""""


# --------------------------------------------------------------------------- #
# LLM wiring
# --------------------------------------------------------------------------- #
def _anthropic_llm(model: str) -> Callable[[str], str]:
    try:
        import anthropic
    except ImportError as exc:  # pragma: no cover - depends on environment
        raise ImportError(
            "The wizard needs an LLM. Either pass llm=callable(prompt)->str, or:\n"
            "    pip install anthropic   (and set ANTHROPIC_API_KEY)"
        ) from exc

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

    def call(prompt: str) -> str:
        resp = client.messages.create(
            model=model,
            max_tokens=16000,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(b.text for b in resp.content if b.type == "text")

    return call


def _extract_json(text: str):
    """Parse a JSON object/array out of an LLM response, tolerating code fences."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    for open_c, close_c in (("{", "}"), ("[", "]")):
        i, j = text.find(open_c), text.rfind(close_c)
        if i != -1 and j > i:
            try:
                return json.loads(text[i:j + 1])
            except json.JSONDecodeError:
                continue
    raise ValueError(f"LLM did not return parseable JSON:\n{text[:400]}")


# --------------------------------------------------------------------------- #
# The two wizard jobs
# --------------------------------------------------------------------------- #
def suggest_anchors(text: str, anchors=None, *, entities=None,
                    llm: Optional[Callable[[str], str]] = None,
                    model: str = DEFAULT_MODEL, dry_run: bool = False, **extract_kw):
    """Ask the wizard for additional anchor terms/categories for ``text``.

    Returns ``{"suggestions": {...}, "notes": str, "prompt": str}``. With
    ``dry_run=True`` returns ``{"prompt": str, "model": str}`` and calls no model.
    """
    if entities is None:
        entities = extract(text, anchors=anchors, **extract_kw)
    prompt = build_anchor_prompt(text, entities, anchors)
    if dry_run:
        return {"prompt": prompt, "model": model}
    raw = (llm or _anthropic_llm(model))(prompt)
    data = _extract_json(raw)
    return {"suggestions": data.get("suggestions", {}),
            "notes": data.get("notes", ""), "prompt": prompt, "raw": raw}


def fix(text: str, *, entities=None, anchors=None,
        llm: Optional[Callable[[str], str]] = None,
        model: str = DEFAULT_MODEL, dry_run: bool = False, **extract_kw):
    """Ask the wizard to review the goblin's draft and return corrections.

    Returns ``{"corrections": [...], "prompt": str}``. With ``dry_run=True`` returns
    ``{"prompt": str, "model": str}`` and calls no model.
    """
    if entities is None:
        entities = extract(text, anchors=anchors, **extract_kw)
    prompt = build_fix_prompt(text, entities)
    if dry_run:
        return {"prompt": prompt, "model": model}
    raw = (llm or _anthropic_llm(model))(prompt)
    data = _extract_json(raw)
    return {"corrections": data.get("corrections", []), "prompt": prompt, "raw": raw}
