# 2026-11-15 — Slides: shared block titles

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference, slides template)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

`references/slides.md` asked for a title that states each slide's point, with Propositions named in the title. On a one-hour seminar deck built that way, the user said the titles varied too much: questions, statements, topic labels and several ad hoc prefixes ("Preview:", "Literature:", "Historical Patterns:"). A first fix made all sixty titles point statements in one style. The user then said the real problem was different: with a new title on every slide the audience gets lost quickly, and slides on the same topic should share one title. Asked whether each slide should keep a subtitle with its point, the user chose no subtitles.

## Changes made

- "Plan the story first", **Titles:** consecutive slides on one topic share one block title, one line, in one consistent style. The specific point of each slide is said by the presenter and appears in the speaker notes when they are requested. A slide that states a Proposition, Definition or Assumption names it in a bold lead-in line in the body, in place of the earlier rule that named it in the title. Appendix slides keep their own titles starting "Appendix:", because the Appendix links name them.
- **Outline:** sections are marked with plain `\section{...}`, which creates no divider slide, and the section name is shown in the footer beside the page number, using the Outline's names. The existing ban on section-divider slides and `\AtBeginSection` is unchanged.
- "Format and checks", **Flow:** "the titles alone tell the story" became: the block titles follow the story's parts in order, the slides under one title build that part step by step, and each slide follows from the one before.
- `templates/simple-slides.tex`: a footer with section name and page number, `\section` markers, two slides under the block title "The Model", and a Proposition lead-in.

## Files affected

- `skills/econ-teaching/references/slides.md` — Titles, Outline and Flow items.
- `skills/econ-teaching/templates/simple-slides.tex` — the pattern in a compiled example.
- `link/econ-teaching.md` — regenerated with `tools/build_link_editions.py`.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

New decks have far fewer distinct titles. Titles that say a slide's point, which the guidance had preferred since the "talk, not a summary" change earlier today, are replaced by block titles. The point moves to what the presenter says. The content file is unaffected: its `## Slide N: Title` headings repeat the block title, and the bundle checker compares titles by position, so repeated titles pass. Plain `\section` is not in the checker's list of constructs that prevent counting frames, so decks with section markers are still checked.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the three edited items; searched `slides.md` and the template for other statements about titles |
| Template compile | Pass | latexmk/pdfLaTeX in a scratch folder: 6 pages, no overfull boxes; footer shows the section; the Appendix button and Back button point at each other (pages 3 and 6) |
| Automated structural validation | Pass | `python tests/validate_skills.py` |
| Unit tests | Pass | `python -m unittest discover -s tests -p 'test_*.py'` |
| Real slide / domain evaluation | Pass (one deck) | Applied to the user's one-hour seminar deck before the rule was written: 13 block titles for 60 main slides, lead-ins for Propositions 1 to 5 and Definition 1, all main slides viewed as images with no text reaching the footer, the bundle checker passing on the deck and its content file. Not yet tried on a deck built from the written rule |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing |

## Known limitations and risks

- Without per-slide titles, a reader of the PDF alone (not attending the talk) loses each slide's point unless the speaker notes are provided. The guidance accepts this for talks; a handout would need the points back.
- How large a block should be is left to judgment; the one-hour deck used blocks of three to seven slides.

## Follow-up

Build one new deck from the written rule alone and check that it groups slides into blocks without prompting.
