# 2026-11-15 — Slides: no source lines on the paper's own figures and tables

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

On a real deck for one paper, the agent put a "Source: Author (Year), Section, Table" line on nearly every slide, including text-only ones. The user asked why and said agents over-apply source notation. In a talk about a single paper the title slide already names it, so such lines add clutter. A text-only-slide ban had already been added to `slides.md` in an earlier edit (it was swept into commit `bbb28f7`); this entry covers the remaining figure and table lines.

## Changes made

- Title slide carries the one full citation; the paper's own figures and tables carry no source line.
- A one-line source remains for a recomputed figure, another paper or dataset, or mixed sources; one line may cover a pair of figures.
- Section, table and equation references stay in the handover. The tables rule now says the full table goes to the Appendix when only some rows are kept.

## Files affected

`skills/econ-teaching/references/slides.md`, `link/econ-teaching.md` (regenerated), `CHANGELOG.md`.

## Behavior and compatibility

Decks of a single paper look cleaner. Users who want a credit line under each figure can ask for it.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Re-read the figures, tables and never-on-a-slide wording. |
| Automated structural validation | Pass | `python -m unittest discover -s tests`: 60 tests OK; link edition up to date. |
| Real slide / domain evaluation | Partial | The deck that prompted this was regenerated without source lines and compiled with no overfull boxes; pages were not re-viewed. |
| GitHub Actions or other CI | Not run | Not checked. |

## Known limitations and risks

Nothing tests deck contents; the rule depends on the agent following the wording.

## Follow-up

None planned.
