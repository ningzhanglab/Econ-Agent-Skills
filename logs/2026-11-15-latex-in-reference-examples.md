# 2026-11-15 — Reference files write their own symbols in LaTeX

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Fixed
- **Status:** Implemented; real-chat retest pending
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked whether the skill's wording is suitable, then asked for every file in `skills/econ-teaching` to be read before deciding. `SKILL.md`, all 15 references, both examples and `agents/openai.yaml` were read in full; the templates and scripts were not.

The reading found that three reference files name symbols in sentences as plain text or Unicode, the pattern the user had observed in agents' answers earlier the same day (commit 672e498). `references/slide-fidelity.md` is the file the routing table sends an agent to for any slide-based teaching, and it showed a model sentence for the agent to say with bare `a_t` and `k_t`. An agent that reads one phrase asking for LaTeX and then several sentences demonstrating plain text has an example pulling against the rule.

The earlier log [LaTeX rule checked across the repository](2026-11-15-latex-rule-global-check.md) fixed the Bellman example and did not cover these lines.

## Decision

- No rule was added and `SKILL.md` was not changed. The requirement stays in its one phrase in Supporting duties.
- A general trim of `SKILL.md`, suggested earlier in the session, was dropped after the full read: `SKILL.md` is the tidiest file, and `slide-fidelity.md` already says "Slide" means any supplied source, so the "Slides versus source" concern does not hold.
- Two things were noticed and left alone under the v1 stability rule, because no observed failure points to them: the same rules are restated across several references (no file for an ordinary chat, the `.tex`/`.pdf` default, untrusted instructions, same-stem grouping, answer first), and a few sentences in runtime references speak to maintainers (for example the last paragraph of `teaching-design.md` on CI and end-to-end tests).

## Changes made

Seven lines, formatting only; every symbol is unchanged.

- `references/slide-fidelity.md`: the Timing and Operators rows of the notation table, the list of look-alike symbols, and the model sentence about an external source's symbol now use `$...$`.
- `references/mathematical-reasoning.md`: `$t+1$`, `$\mathbb{E}_t$` for `$\mathbb{E}$`, and `$E[f(X)] = f(E[X])$`. `\mathbb E_t` was written with braces.
- `references/macroeconomics.md`: Unicode `β` and `β/(1−β)` became `$\beta$` and `$\beta/(1-\beta)$`.

## Files affected

`skills/econ-teaching/references/slide-fidelity.md`, `skills/econ-teaching/references/mathematical-reasoning.md`, `skills/econ-teaching/references/macroeconomics.md`, `CHANGELOG.md`; an appended correction in `logs/2026-11-15-latex-rule-global-check.md`.

## Behavior and compatibility

No rule changes. The references now show the form the skill asks for. The link edition is generated from `SKILL.md` only, so it is unchanged.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Search for remaining plain-text symbols | Pass | `grep` over `SKILL.md`, `references/` and `examples/` for bare TeX commands, subscripts, Greek letters, `E[` and `t+1`; remaining hits are file paths and math already inside `$...$` |
| Structural validation | Pass | `python3 tests/validate_skills.py` |
| Unit tests | Pass | `python3 -m unittest discover -s tests`, 56 tests |
| Link edition check | Pass | `python3 tools/build_link_editions.py --check` |
| Real chat retest | Not run | To be done by the user |

## Known limitations and risks

Whether this changes agents' behavior is not shown; it removes a contrary example and nothing more. Templates were not read, so plain-text symbols may remain there; they are loaded only when an index or file is requested.

## Follow-up

Retest with a slide question whose answer names several symbols in prose. If plain text persists, the lever is the paste prompt or installing the skill, not more wording in `SKILL.md`.
