"""Tests for the wizard (LLM-escalation) layer.

No real API calls — a fake ``llm`` callable stands in for the model, so these run
without ``anthropic`` installed or any API key.
"""

import pytest

from hobgoblin import wizard, ANCHORS
from hobgoblin.wizard import _extract_json, build_anchor_prompt, build_fix_prompt

pytest.importorskip("spacy", reason="spaCy not installed")

try:
    import spacy

    spacy.load("en_core_web_sm")
except Exception:  # noqa: BLE001
    pytest.skip(
        "en_core_web_sm not installed: python -m spacy download en_core_web_sm",
        allow_module_level=True,
    )

TEXT = "Colonel John Smith led the 3rd Brigade near Paris. It moved at dawn."


def test_extract_json_plain():
    assert _extract_json('{"a": 1}') == {"a": 1}


def test_extract_json_code_fence():
    fenced = "```json\n{\"corrections\": [{\"action\": \"drop\"}]}\n```"
    assert _extract_json(fenced) == {"corrections": [{"action": "drop"}]}


def test_extract_json_with_surrounding_prose():
    messy = 'Here you go:\n{"suggestions": {}, "notes": "x"}\nHope that helps!'
    assert _extract_json(messy)["notes"] == "x"


def test_extract_json_rejects_garbage():
    with pytest.raises(ValueError):
        _extract_json("no json here at all")


def test_anchor_prompt_lists_untyped_entities():
    prompt = build_anchor_prompt(TEXT, __import__("hobgoblin").extract(TEXT), ANCHORS)
    assert "Return ONLY JSON" in prompt
    assert "Current categories" in prompt
    assert TEXT in prompt  # the document is included


def test_fix_prompt_includes_draft():
    prompt = build_fix_prompt(TEXT, __import__("hobgoblin").extract(TEXT))
    assert "corrections" in prompt
    assert "Smith" in prompt  # an entity from the draft


def test_dry_run_calls_no_model():
    # a dry run must not invoke the llm — pass one that would blow up if called
    boom = lambda p: (_ for _ in ()).throw(AssertionError("llm should not be called"))
    out = wizard.suggest_anchors(TEXT, anchors=ANCHORS, llm=boom, dry_run=True)
    assert "prompt" in out and out["model"] == "claude-opus-4-8"


def test_suggest_anchors_with_fake_llm():
    fake = lambda p: '{"suggestions": {"military_unit": ["QRF"]}, "notes": "ok"}'
    res = wizard.suggest_anchors(TEXT, anchors=ANCHORS, llm=fake)
    assert res["suggestions"] == {"military_unit": ["QRF"]}
    assert res["notes"] == "ok"


def test_fix_with_fake_llm():
    fake = lambda p: '{"corrections": [{"action": "drop", "entity": "It"}]}'
    res = wizard.fix(TEXT, llm=fake)
    assert res["corrections"][0]["entity"] == "It"


def test_claude_code_llm_builds_headless_command(monkeypatch):
    import hobgoblin.wizard as w

    monkeypatch.setattr(w.shutil, "which", lambda c: "/usr/bin/claude")
    captured = {}

    class _Result:
        returncode = 0
        stdout = '{"corrections": []}'
        stderr = ""

    def fake_run(cmd, **kw):
        captured["cmd"] = cmd
        captured["input"] = kw.get("input")
        return _Result()

    monkeypatch.setattr(w.subprocess, "run", fake_run)
    llm = w.claude_code_llm(model="opus")
    assert llm("hello") == '{"corrections": []}'
    assert captured["cmd"][:2] == ["claude", "-p"]
    assert "--model" in captured["cmd"] and "opus" in captured["cmd"]
    assert "--no-session-persistence" in captured["cmd"]
    assert captured["input"] == "hello"


def test_claude_code_llm_missing_binary(monkeypatch):
    import hobgoblin.wizard as w

    monkeypatch.setattr(w.shutil, "which", lambda c: None)
    with pytest.raises(FileNotFoundError):
        w.claude_code_llm(command="definitely-not-a-real-cli")


def test_fix_reuses_passed_entities():
    # passing entities avoids re-running extract; a fake llm echoes empty corrections
    ents = __import__("hobgoblin").extract(TEXT)
    fake = lambda p: '{"corrections": []}'
    res = wizard.fix(TEXT, entities=ents, llm=fake)
    assert res["corrections"] == []
