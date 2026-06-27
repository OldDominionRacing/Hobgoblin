#!/usr/bin/env python3
"""Benchmark the goblin on random Wikipedia pages — resumable, append-only.

Drops one row per page into BENCHMARK.md (a markdown table). No running totals are
kept — totaling is done later from the rows, so the run can stop/resume freely.
Resumption: the script counts existing data rows and continues until TARGET.

Every metric is the deterministic goblin (no LLM). The columns let us compute later:
  - how well the goblin types on its own (typed / entities),
  - element coverage (verb / count / unit / items / assoc per entity),
  - the structured-output tokens the goblin produced for FREE (out_verbose / out_compact)
    — i.e. what a "wizard alone" LLM would have to emit and pay for.

    python benchmark/run_benchmark.py            # run / resume until 1000
    python benchmark/run_benchmark.py 200        # custom target
"""

import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hobgoblin import extract, item_index, ANCHORS  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "BENCHMARK.md")
LOG = os.path.join(HERE, "run.log")
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
BATCH = 20
UA = "Hobgoblin-benchmark/0.1 (github.com/OldDominionRacing/Hobgoblin)"

COLUMNS = ["title", "chars", "ents", "typed", "untyped", "verb", "count",
           "unit", "items", "assoc", "out_verbose_tok", "out_compact_tok"]
HEADER = f"""# Hobgoblin benchmark — per-page goblin metrics (random Wikipedia)

One row per page. Deterministic goblin only (no LLM). Total later from the rows.

Columns:
- `chars` document length · `ents` entities (after stopword-drop) ·
  `typed`/`untyped` entities that matched / didn't match an anchor category ·
  `verb`/`count`/`unit`/`assoc` entities carrying that element ·
  `items` items-of-interest associated · `out_verbose_tok`/`out_compact_tok`
  ~tokens of structured output the goblin produced for free (verbose JSON / compact).

| {" | ".join(COLUMNS)} |
| {" | ".join("---" for _ in COLUMNS)} |
"""


def fetch_batch():
    url = ("https://en.wikipedia.org/w/api.php?action=query&format=json"
           f"&generator=random&grnnamespace=0&grnlimit={BATCH}"
           f"&prop=extracts&explaintext=1&exintro=1&exlimit={BATCH}")
    out = subprocess.run(["curl", "-s", "-H", f"User-Agent: {UA}", url],
                         capture_output=True, text=True, timeout=60)
    data = json.loads(out.stdout)
    return list(data.get("query", {}).get("pages", {}).values())


def metrics(title, text):
    ents = extract(text, anchors=ANCHORS)
    typed = [e for e in ents if e["anchors_matched"]]
    compact = [{"e": e["entity"], "t": e["anchors_matched"] or None,
                "s": e["span"], "c": (e["context"]["count"] or {}).get("value"),
                "u": e["mil_unit"], "d": [d["text"] for d in e["context"]["dates"]],
                "v": (e["context"]["verb"] or {}).get("lemma")} for e in ents]
    return {
        "title": title.replace("|", "/").replace("\n", " ").strip(),
        "chars": len(text),
        "ents": len(ents),
        "typed": len(typed),
        "untyped": len(ents) - len(typed),
        "verb": sum(1 for e in ents if e["context"]["verb"]),
        "count": sum(1 for e in ents if e["context"]["count"]),
        "unit": sum(1 for e in ents if e["mil_unit"]),
        "items": len(item_index(ents)),
        "assoc": sum(1 for e in ents if e["associations"]),
        "out_verbose_tok": round(len(json.dumps(ents)) / 4),
        "out_compact_tok": round(len(json.dumps(compact)) / 4),
    }


def existing_state():
    """Return (row_count, seen_titles) from an existing BENCHMARK.md."""
    if not os.path.exists(MD):
        return 0, set()
    rows, seen = 0, set()
    with open(MD) as f:
        for line in f:
            line = line.strip()
            if (line.startswith("| ") and " | " in line
                    and not line.startswith("| title")
                    and not line.startswith("| ---")):
                rows += 1
                seen.add(line[2:].split(" | ", 1)[0].strip())
    return rows, seen


def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")


def main():
    if not os.path.exists(MD):
        with open(MD, "w") as f:
            f.write(HEADER)
    done, seen = existing_state()
    log(f"=== start: {done} rows already present, target {TARGET} ===")
    while done < TARGET:
        try:
            pages = fetch_batch()
        except Exception as exc:  # noqa: BLE001 - network hiccup, back off
            log(f"fetch error: {exc!r} — retrying in 5s")
            time.sleep(5)
            continue
        for p in pages:
            if done >= TARGET:
                break
            title = p.get("title", "")
            text = (p.get("extract") or "").strip()
            if len(text) < 200 or title in seen:
                continue  # skip stubs/disambig and dupes
            try:
                m = metrics(title, text)
            except Exception as exc:  # noqa: BLE001 - bad page, skip
                log(f"skip {title!r}: {exc!r}")
                continue
            row = "| " + " | ".join(str(m[c]) for c in COLUMNS) + " |\n"
            with open(MD, "a") as f:
                f.write(row)
            seen.add(title)
            done += 1
            if done % 25 == 0:
                log(f"progress: {done}/{TARGET}")
        time.sleep(0.5)  # be polite to the API
    log(f"=== done: {done} rows ===")


if __name__ == "__main__":
    main()
