# 2026-11-15 — Slides: empirical order, tables, no overlays, template titles

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference and template)
- **Change type:** Changed / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked whether public GitHub resources on economics slide making could improve the slides reference. The agent compared `references/slides.md` with a few public agent skills for Beamer decks (Noi1r/beamer-skill, meleantonio/awesome-econ-ai-stuff `beamer-presentation`) and with well-known advice for economics talks (for example Shapiro, "How to Give an Applied Micro Talk"; that PDF returned HTTP 403, so only quoted summaries were read). Only the agent skill pages and READMEs were read, not their full source.

Gaps found:

- The default deck order fit theory papers only (setup, then one equation); empirical papers need data, identification, results and robustness.
- There was no rule for regression tables, where decks often end up with small type or wrong numbers copied from a trimmed table.
- Overlays were unspecified; `\pause` produces repeated PDF pages in decks sent to others.
- The template's example titles ("State the question as a claim") still followed the assertion-title rule replaced earlier the same day by short one-line titles.

The user approved all four changes and asked to keep the short-title setting unchanged.

Not adopted, because it conflicts with the v1 stability rule or the default-without-asking rule: numeric scoring loops, multi-agent review, and a mandatory needs interview before drafting.

## Changes made

- `slides.md` item 4: a shared opening (motivation from the economics, not from a literature gap), then a theory/quantitative order and an empirical order (data; identification in the paper's words; results with magnitudes; robustness, briefly), then the shared ending.
- `slides.md` Each slide: a **Tables** rule. Keep only the rows and columns the argument needs, copy the numbers exactly, `\alert{}` the main coefficient and say what it means in units. Prefer the paper's figure when there is one, name the table and columns kept in the source line, and put the full table in Backup.
- `slides.md` Format: no `\pause` or overlays by default; use them only on request.
- `templates/simple-slides.tex`: example titles changed to "Research Question" and "Core Mechanism".
- `link/econ-teaching.md`: regenerated with `tools/build_link_editions.py`.

## Files affected

- `skills/econ-teaching/references/slides.md`: order, tables, overlays.
- `skills/econ-teaching/templates/simple-slides.tex`: short example titles.
- `link/econ-teaching.md`: regenerated link edition.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

Decks for empirical papers now follow a data → identification → results → robustness order by default. Tables on slides are trimmed and sourced by table and column. Decks have no overlays unless the user asks. The short-title rule (item 3) is unchanged. No interface, script or installation change.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Edited sections re-read in the diff |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 60 tests OK, after the link edition was regenerated. Before regeneration, `test_committed_link_editions_match_the_skills` failed for `econ-teaching`, both with and without this change (verified with `git stash`), so the committed link edition was already stale at `a712004` |
| Template compile | Pass | `latexmk -pdf` in a scratch copy: 0 overfull boxes; `check_tex_bundle.py --compile`: PASS |
| Real slide / domain evaluation | Not run | No deck regenerated with the new rules yet |
| GitHub Actions or other CI | Not run | Not checked at the time of writing |

## Known limitations and risks

- The empirical order is a default. Papers that mix a model with estimation still need judgment, and "Adjust to the purpose" still applies.
- The tables rule has not yet been exercised on a real deck.

## Follow-up

Build a deck for a real empirical paper and check the order, the trimmed table and its source line.
