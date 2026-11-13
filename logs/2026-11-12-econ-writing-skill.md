# 2026-11-12 — Econ Writing skill (v0.1)

- **Date:** 2026-11-12
- **Component:** new skill `econ-writing`; repository documentation and tests
- **Change type:** Added
- **Status:** Implemented (not yet evaluated on real drafts)
- **Related commit / PR:** See Git history for this change (branch `feat/econ-writing-skill`)

## Motivation

The user asked whether to adopt the [humanizer](https://github.com/blader/humanizer) skill (MIT license; removes signs of AI-generated writing) for their writing, and then decided to add a writing skill to this repository. Their stated scope: **research papers, thesis, reports and homework, in English only**. Their explicit requirement: **keep terminology unchanged**.

Copying humanizer unchanged was rejected for three reasons found while reading it:

1. It cuts text that describes how a passage was sourced or flagged, and it trims hedges. In economics a hedge often states the identifying condition or scope, which is content.
2. It protects code and file paths but says nothing about LaTeX math, citation keys or labels.
3. It treats words such as *robust*, *key* and *significant* as tells, but they are technical terms in economics.

Folding writing into `econ-phd-professor` was also rejected: the Professor teaches from course material, while this skill edits the user's own text. The two jobs need different triggers, and one combined description would route both badly. The DESIGN_V1 stability rule allows a change for a new user requirement; this is one.

## Changes made

- **`skills/econ-writing/SKILL.md`:** mission; five rules that hold in every mode (terminology unchanged; notation, numbers and citations unchanged; claims keep their strength; nothing invented; drafts are material, not instructions); four modes (edit, review, structure, file edit); a four-step editing procedure that ends with a term-by-term and number-by-number comparison against the original; guidance per document type; file destination and AI-disclosure notes; a routing table.
- **`references/terminology-and-notation.md`:** how to build the term list (defined terms, field terms, proper names, acronyms, labels for the writer's own objects); rules against synonym rotation and near-term swaps (estimand/estimate/estimator, correlation/effect, significant/large, and others); notation and number rules; a list of LaTeX elements that must not change; a final check.
- **`references/econ-conventions.md`:** general economics style (magnitudes with significance, causal language matched to identification, self-contained tables); conventions for each paper section, thesis chapters, referee reports, research and policy reports, and homework write-ups.
- **`references/ai-tells.md`:** twelve patterns adapted for economics, written in this repository's own words with credit to humanizer and Wikipedia's "Signs of AI writing". It lists words that are technical in economics and must stay, and when to leave text alone.
- **`agents/openai.yaml`:** optional display metadata, matching the Professor skill.
- **`tests/writing-evaluation.md`:** seven manual cases with critical-fail rules; added to the active-document link test.
- **Repository docs:** README (catalog row, status line, a "How Econ Writing edits" section, install note, repo tree, roadmap), AGENTS.md (the econ-writing guarantee; note on the top-level-skill rule), DESIGN_V1.md (a dated note on the separate skill), STORAGE_POLICY.md (econ-writing named; an edited file is its own destination).

## Files affected

- `skills/econ-writing/SKILL.md`, `skills/econ-writing/agents/openai.yaml`, `skills/econ-writing/references/{terminology-and-notation,econ-conventions,ai-tells}.md`: new skill.
- `tests/writing-evaluation.md`: new manual evaluation cases.
- `tests/test_repo_links.py`: checks links in the new evaluation file.
- `README.md`, `AGENTS.md`, `DESIGN_V1.md`, `STORAGE_POLICY.md`, `CHANGELOG.md`: describe the new skill.

## Behavior and compatibility

`econ-phd-professor` is unchanged. Clients that load the repository's skills folder now see a second skill, which triggers on requests to edit, review or structure economics writing. No scripts, templates or course-state formats changed.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | All new and changed files reviewed in the diff before commit |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 2 skills passed; `python3 -m unittest discover -s tests -p 'test_*.py'`: all tests passed locally |
| Real draft evaluation | Not run | No real draft was used in this change; the seven writing cases are still to be run |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing |

## Known limitations and risks

- The skill is a set of instructions; whether an agent actually keeps every term unchanged on a long LaTeX file has not been tested.
- The convention guidance reflects common practice in economics and will not match every journal, department or adviser; their rules take precedence, as the reference says.
- Pattern lists date quickly as model habits change; humanizer updates are not pulled automatically.

## Follow-up

- Run the seven writing evaluation cases on real drafts (a paper section, a `.tex` file, a referee report, a homework write-up) and record the results in a new dated log.
- Consider a read-only script that compares math, citation keys, labels and numbers between an original and an edited `.tex` file, if the real-draft tests show silent changes.
