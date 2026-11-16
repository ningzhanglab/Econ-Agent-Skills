# 2026-11-15 — Slides: complete-story check (coverage, framework, cold reader, flow)

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference)
- **Change type:** Added
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

A one-hour paper deck came out as a list of well-sourced slides without links between sections. Symbols used on slides were undefined and a key identification equation was missing. The user asked that the prompt check the whole framework and structure: whether the deck is a complete story from the paper and works for someone who has not read it.

## Changes made

- `slides.md`: item 5 now says every section appears somewhere or is named as omitted in the handover. A new first check under "Format and checks" has four parts: coverage map in the handover; framework (setup, decision rule or identification step, objects, observed versus inferred) complete before the first result; a cold-reader pass listing every undefined symbol, acronym, source, term and unexplained step; and a flow check of titles in which every slide after the first opens with a short connecting line (a slide whose bold first line is already its claim needs none), with bridges only from the paper's own transitions.
- `link/econ-teaching.md`: regenerated.

## Files affected

`skills/econ-teaching/references/slides.md`, `link/econ-teaching.md`, `CHANGELOG.md`.

## Behavior and compatibility

Decks get a coverage table in the handover, definitions for every symbol and term on first use, and linking first lines. Short decks are unaffected beyond the table. No new slide type is required.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the edited section. |
| Automated structural validation | Pass | `python3 -m unittest discover -s tests`: 60 tests OK. |
| Real slide / domain evaluation | Partial | Applied by hand to the one deck that prompted it: all sections 2 to 7 are mapped to slides; no new deck was generated from the revised prompt. |
| GitHub Actions or other CI | Not run | Not pushed. |

## Known limitations and risks

Nothing tests whether an agent follows the check; the rule relies on the handover table.

## Follow-up

None planned.
