# Hobgoblin quality eval — goblin error rates judged by an LLM (the wizard)

One row per page. The judge is `wizard.fix()` (LLM); its corrections are the errors:
`drops` = false positives, `adds` = missed entities, `retypes` = wrong type.
Total later: precision ~= 1-drops/ents · recall ~= ents/(ents+adds) ·
typing-accuracy ~= 1-retypes/typed.

| title | ents | typed | drops | adds | retypes |
| --- | --- | --- | --- | --- | --- |
