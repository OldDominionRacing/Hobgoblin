#!/usr/bin/env python3
"""Run the wizard under your Claude Code auth (e.g. a Max plan) — no API key.

Run this in a terminal where Claude Code is logged in (you've run `claude` and
signed in, or set `claude setup-token`):

    python examples/wizard_claude_code.py

It runs the cheap goblin pass, then routes ONLY the residue to the wizard via the
`claude -p` CLI, so the LLM call is billed to your Claude Code subscription instead
of pay-as-you-go API credits.
"""

import json

from hobgoblin import extract, wizard, ANCHORS

TEXT = (
    "On 14 March 2025, Colonel John Smith reported that the 3rd Brigade and I Corps "
    "moved roughly 12 HMMWV trucks to Fort Bragg, North Carolina. The Quick Reaction "
    "Force and an EOD team secured the perimeter. World War II veterans attended the "
    "ceremony. Contact the TOC at 555-867-5309."
)

# Route the wizard through the Claude Code CLI instead of the Anthropic API.
llm = wizard.claude_code_llm(model="opus")

ents = extract(TEXT, anchors=ANCHORS)
print("GOBLIN typed:", [f"{e['entity']} [{','.join(e['anchors_matched'])}]"
                        for e in ents if e["anchors_matched"]])
print("GOBLIN untyped:", [e["entity"] for e in ents if not e["anchors_matched"]])

print("\n=== wizard.fix (via Claude Code) ===")
fx = wizard.fix(TEXT, entities=ents, llm=llm)
print(json.dumps(fx["corrections"], indent=2))

print("\n=== wizard.suggest_anchors (via Claude Code) ===")
sa = wizard.suggest_anchors(TEXT, anchors=ANCHORS, entities=ents, llm=llm)
print(json.dumps(sa["suggestions"], indent=2))
print("notes:", sa["notes"])
