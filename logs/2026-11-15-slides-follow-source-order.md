# 2026-11-15 — Correction: slides follow the source's order

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference)
- **Change type:** Fixed (correction to [2026-11-15 — Slides empirical order and tables](2026-11-15-slides-empirical-order-and-tables.md))
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

After commit `9fdfd30`, the user asked whether a deck should simply follow the paper's order. On review, the earlier change had imported advice meant for **presenting one's own paper** (Shapiro's applied-micro talk advice; the job-market and seminar structures in public Beamer skills) into a reference whose scope is **presenting someone else's paper or a lecture** (`slides.md`, line 3). That produced two errors:

- A theory-versus-empirical default order that reorders the authors' argument and is redundant: the paper already has its own structure, and an economics paper's introduction usually already states the question, the contribution and a preview of results.
- "Motivation from the economics, not from a gap in the literature" is advice to an author. When presenting someone else's paper, the motivation is the authors' own.

A smaller gap: the tables rule asked for each coefficient's meaning "in units", which could invite an interpretation the paper does not give.

## Changes made

- `slides.md` item 4 now reads **Order: follow the source**. The body follows the paper's (or lecture's) section order. Question, contribution and preview come from the paper's introduction, and a one-line preview that cites its section is added only if the introduction does not state the main result. Takeaways, Discussion and Backup are added at the end. Sections are not reordered; if the purpose needs another order, the handover says what moved and why.
- Item 5 (spend the time on the core; compress secondary sections or move them to Backup) is unchanged. It governs time, while item 4 governs order.
- The tables rule now says the meaning in units comes from the paper's own interpretation, or is computed from the table and traced in the handover, which is consistent with the existing numbers rule.
- Kept from `9fdfd30`: the rest of the tables rule, no overlays by default, and the short template titles. The short-title rule (item 3) is unchanged.

## Files affected

- `skills/econ-teaching/references/slides.md`: items 4 and Tables.
- `link/econ-teaching.md`: regenerated.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

Decks keep the paper's section order instead of a type-based template order, and the motivation is the authors'. Any reordering for a teaching purpose is disclosed in the handover. No script, interface or installation change.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Diff reviewed; no other file referenced the removed wording (`grep` over `skills/` and `tests/`) |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 60 tests OK after regenerating the link edition |
| Template compile | N/A | Template not changed in this commit |
| Real slide / domain evaluation | Not run | No deck built with the corrected rule yet |
| GitHub Actions or other CI | Not run | Not checked at the time of writing |

## Known limitations and risks

- Papers whose section order serves readers poorly (for example a long literature section before the model) are handled by compression under item 5, not reordering. This has not yet been tested on such a paper.

## Follow-up

Build one deck for a real paper and check that the slide order matches its sections and that the handover discloses any moves.
