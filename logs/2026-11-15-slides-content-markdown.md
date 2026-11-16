# 2026-11-15 — Slides: matching content Markdown

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference)
- **Change type:** Added
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user revises the wording of a deck in a Markdown editor and had been keeping a hand-made `content.md` next to an earlier deck for that purpose. They asked that a deck always come with a matching content Markdown file for adjusting the text.

## Changes made

- `slides.md`, "Format and checks": a new **Content file** item. Every deck is delivered with a Markdown file beside it, named after the deck with `_content.md`: one `## Slide N: Title` section per slide, in order, N matching the page of the compiled PDF, text matching the `.tex` exactly, math in LaTeX (`$...$` and `$$` blocks), bold for `\textbf` or `\alert`, tables as Markdown tables, figures as relative image links.
- When the user returns the file edited, the agent applies the text to the matching slides in the `.tex`, recompiles and regenerates the file, so `.tex`, `.pdf` and `.md` stay in step.

## Files affected

- `skills/econ-teaching/references/slides.md`: the new item.
- `link/econ-teaching.md`: regenerated.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

A slides request now produces three files (`.tex`, `.pdf`, `_content.md`) plus the handover, instead of two. The format follows the file the user was already using. Slide content rules are unchanged. The bundle checker does not check the content file.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the new item in `slides.md`. |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed. `python3 -m unittest discover -s tests`: 60 tests, OK. |
| Real slide / domain evaluation | Not run | No deck has been generated with this item yet. |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing. |

## Known limitations and risks

- Nothing checks that the Markdown matches the `.tex`; it is written by the agent and can drift.
- Layout (columns, figure widths) is not represented in the Markdown, so only wording can be revised there.

## Follow-up

Generate the content file for the trial one-hour deck and check the round trip: edit the Markdown, apply to the `.tex`, recompile.
