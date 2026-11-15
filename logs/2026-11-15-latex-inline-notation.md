# 2026-11-15 — LaTeX for notation in sentences too

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Fixed
- **Status:** Implemented; retest pending
- **Related commit / PR:** See Git history for this change

## Motivation

After commit 6f896c4 reduced the chat-LaTeX requirement to one phrase ("with math written in LaTeX from the first answer"), the user observed that agents now write equations in LaTeX but name symbols inside sentences in plain text. The word "math" was read as "equations".

## Root cause

The skill mentioned LaTeX only in the sentence about requested files ("only when the user requests a file, default to a matching `.tex` and compiled `.pdf`"), so agents took LaTeX to mean "making a PDF". The chat requirement is placed in that same sentence to undo the association where it forms. `references/latex-outputs.md` was considered and left unchanged: agents open it only when a file is requested, when they already use LaTeX.

## Changes made

- `skills/econ-teaching/SKILL.md`, Supporting duties: "Ordinary questions are answered in chat, with all math in LaTeX from the first answer, even a single symbol in a sentence; no file is created." Still one place, no rendering details. A longer draft listing examples (`$\beta$`, `$k_t$`) and "not only equations" was shortened at the user's suggestion; saying only "use TeX" was rejected because it leaves the scope open and can be read as writing the whole answer, or a file, in TeX.
- `tests/professor-evaluation.md`, case 59: every symbol named in a sentence is in LaTeX as well as the equations.
- `link/econ-teaching.md` regenerated.

## Files affected

`skills/econ-teaching/SKILL.md`, `tests/professor-evaluation.md`, `link/econ-teaching.md`, `CHANGELOG.md`.

## Behavior and compatibility

Inline symbols are now explicitly covered; no delimiter rule is added.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Link edition regenerated | Pass | `tools/build_link_editions.py` |
| Structural validation and unit tests | Pass | Run before committing |
| Real chat retest | Not run | The user will retest |

## Known limitations and risks

None new.

## Follow-up

Retest with a question whose answer names several symbols in prose.
