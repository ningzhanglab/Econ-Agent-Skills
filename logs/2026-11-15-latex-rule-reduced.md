# 2026-11-15 — Chat LaTeX rule reduced to one phrase

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Changed
- **Status:** Implemented; retest pending
- **Related commit / PR:** See Git history for this change

## Motivation

After commit 4524595 the chat-LaTeX rule had grown to about 70 words: delimiters, dollar signs, code, and when to switch to plain text. A further suggestion (allow `\(...\)` before plain text) would have added more. The user judged this too much detail, since current agents handle LaTeX rendering well, and asked for a rethink.

## Reasoning

The observed failure was not a missing formatting rule but a bias created by the skill: LaTeX was mentioned only for requested `.tex`/`.pdf` files, and the agent cited "Ordinary questions are answered in chat" as its reason for plain text. The screenshot shows the agent reads that exact line. Stating the requirement there removes the bias at the point of misreading, and keeps one home for the rule as `DESIGN_V1.md` asks. Delimiter choice, currency and code are things agents and apps already handle; the student can ask for another format.

## Changes made

- `skills/econ-teaching/SKILL.md`: removed the bold "Math in chat is LaTeX" line at the top of "How to teach". Supporting duties now reads "Ordinary questions are answered in chat, with math written in LaTeX from the first answer; no file is created."
- `tests/professor-evaluation.md`, case 57: removed the price/`\$10` condition. Case 59 unchanged (LaTeX in the first answer; lecturer macros as defined, which is a notation-fidelity point under principle 1).
- `link/econ-teaching.md` regenerated.
- Kept: the Bellman example in LaTeX (commit 4524595), and the README terminal note for users.

## Files affected

`skills/econ-teaching/SKILL.md`, `tests/professor-evaluation.md`, `link/econ-teaching.md`, `CHANGELOG.md`; an appended note in `logs/2026-11-15-latex-rule-global-check.md`.

## Behavior and compatibility

The requirement is the same (LaTeX in chat from the first answer); the details are no longer prescribed. About 60 fewer words in `SKILL.md`.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Link edition regenerated | Pass | `tools/build_link_editions.py` |
| Structural validation and unit tests | Pass | Run before committing |
| Real chat retest | Not run | The user will retest in a new incognito chat |

## Known limitations and risks

One phrase may be too weak; if the retest shows plain text, restore a short separate line.

## Follow-up

Retest in a new chat 5 to 10 minutes after the push.
