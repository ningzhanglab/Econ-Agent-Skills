# 2026-11-15 — Slides: no fixed bullet count

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

`references/slides.md` limited each slide to "at most 3–4 bullets, each a complete thought of about one line." On a one-hour seminar deck, asked whether a slide may have more than four bullets, the user said it may have more, or sub-bullets, when needed, with little limitation.

## Changes made

- "Each slide", **Text:** no fixed bullet count. A slide uses as many bullets as its point needs; sub-bullets (a nested `itemize`) may group details under the point they support. A slide is split when it carries two ideas or no longer fits at a readable size. Bullets are still complete thoughts, and still no paragraphs.
- Removed: the "about one line" length for each bullet, which went with the count cap.
- "Format and checks", **Content file:** sub-bullets are written as indented list items.

## Files affected

- `skills/econ-teaching/references/slides.md` — the two items above.
- `link/econ-teaching.md` — regenerated with `tools/build_link_editions.py`.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

New decks may have more bullets per slide and nested lists. The "one idea per slide" rule in the story plan is unchanged, so density is still limited by what the slide is about and by readability, which the existing check of every rendered page for overflow and small type enforces. The bundle checker does not count bullets and is unaffected.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the edited items; searched the skill, README and tests for other statements of the 3–4 limit and found none |
| Automated structural validation | Pass | `python tests/validate_skills.py` |
| Unit tests | Pass | `python -m unittest discover -s tests -p 'test_*.py'` |
| Real slide / domain evaluation | N/A | Wording change requested by the user; no deck rebuilt for it |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing |

## Known limitations and risks

Without a count, a deck can drift back toward dense, summary-like slides. The guards are the existing one-idea-per-slide rule and the rendered-page check for small type.

## Follow-up

None planned.
