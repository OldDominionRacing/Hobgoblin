#!/usr/bin/env python3
"""Quality eval: how OFF is the goblin? Uses an LLM judge (the wizard) as ground truth.

Coverage (run_benchmark.py) counts what the goblin produced. This measures whether
it's *correct*, by running `wizard.fix()` per page and tallying its corrections:

    drop   -> goblin false positive   (identification precision)
    add    -> goblin missed it         (identification recall)
    retype -> goblin labeled it wrong  (typing accuracy)

Each page costs one LLM call. By default the judge is the Claude Code CLI
(`claude -p`), so it runs under your Claude Code / Max auth — NO API key. Run this
in a terminal where Claude Code is logged in.

Resumable + append-only, same as run_benchmark.py: one row per page in QUALITY.md,
no running totals (total later from the rows).

    python benchmark/eval_quality.py            # judge 50 pages (default)
    python benchmark/eval_quality.py 100        # custom sample size
"""

import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hobgoblin import extract, ANCHORS, wizard  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "QUALITY.md")
LOG = os.path.join(HERE, "quality.log")
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 50
BATCH = 20
UA = "Hobgoblin-benchmark/0.1 (github.com/OldDominionRacing/Hobgoblin)"
JUDGE = wizard.claude_code_llm(model="opus")  # runs under Claude Code / Max auth

COLUMNS = ["title", "ents", "typed", "drops", "adds", "retypes"]
HEADER = f"""# Hobgoblin quality eval — goblin error rates judged by an LLM (the wizard)

One row per page. The judge is `wizard.fix()` (LLM); its corrections are the errors:
`drops` = false positives, `adds` = missed entities, `retypes` = wrong type.
Total later: precision ~= 1-drops/ents · recall ~= ents/(ents+adds) ·
typing-accuracy ~= 1-retypes/typed.

| {" | ".join(COLUMNS)} |
| {" | ".join("---" for _ in COLUMNS)} |
"""


def fetch_batch():
    url = ("https://en.wikipedia.org/w/api.php?action=query&format=json"
           f"&generator=random&grnnamespace=0&grnlimit={BATCH}"
           f"&prop=extracts&explaintext=1&exintro=1&exlimit={BATCH}")
    out = subprocess.run(["curl", "-s", "-H", f"User-Agent: {UA}", url],
                         capture_output=True, text=True, timeout=60)
    return list(json.loads(out.stdout).get("query", {}).get("pages", {}).values())


def existing_state():
    if not os.path.exists(MD):
        return 0, set()
    rows, seen = 0, set()
    for line in open(MD):
        line = line.strip()
        if (line.startswith("| ") and " | " in line
                and not line.startswith("| title") and not line.startswith("| ---")):
            rows += 1
            seen.add(line[2:].split(" | ", 1)[0].strip())
    return rows, seen


def log(msg):
    open(LOG, "a").write(msg + "\n")


def main():
    if not os.path.exists(MD):
        open(MD, "w").write(HEADER)
    done, seen = existing_state()
    log(f"=== start: {done} rows, target {TARGET} ===")
    while done < TARGET:
        try:
            pages = fetch_batch()
        except Exception as exc:  # noqa: BLE001
            log(f"fetch error: {exc!r}")
            time.sleep(5)
            continue
        for p in pages:
            if done >= TARGET:
                break
            title = p.get("title", "")
            text = (p.get("extract") or "").strip()
            if len(text) < 200 or title in seen:
                continue
            try:
                ents = extract(text, anchors=ANCHORS)
                corr = wizard.fix(text, entities=ents, llm=JUDGE)["corrections"]
            except Exception as exc:  # noqa: BLE001
                log(f"skip {title!r}: {exc!r}")
                time.sleep(2)
                continue
            acts = [c.get("action") for c in corr]
            m = {
                "title": title.replace("|", "/").replace("\n", " ").strip(),
                "ents": len(ents),
                "typed": sum(1 for e in ents if e["anchors_matched"]),
                "drops": acts.count("drop"),
                "adds": acts.count("add"),
                "retypes": acts.count("retype"),
            }
            open(MD, "a").write("| " + " | ".join(str(m[c]) for c in COLUMNS) + " |\n")
            seen.add(title)
            done += 1
            log(f"{done}/{TARGET}: {title!r} drops={m['drops']} adds={m['adds']} retypes={m['retypes']}")
        time.sleep(0.5)
    log(f"=== done: {done} rows ===")


if __name__ == "__main__":
    main()
