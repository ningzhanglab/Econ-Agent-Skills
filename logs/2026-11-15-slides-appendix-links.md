# 2026-11-15 — Slides: clickable links to and from the Appendix

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference, slides template)
- **Change type:** Added
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

A one-hour deck built with the skill put full tables, derivation steps and numerical checks in the Appendix, as the slides guidance asks. During a talk none of it could be reached quickly: the presenter would have to page forward through the deck and then find the way back. The user asked that Appendix material be linked from the main slides, and then asked that this become part of the skill's instructions.

## Changes made

- `references/slides.md`, "Each slide": new **Appendix links** item. Every Appendix slide is one click from the main slide it supports and has a Back button to that slide. It names the Beamer mechanism (frame `label=`, `\hyperlink` with `\beamergotobutton` and `\beamerreturnbutton`, placed bottom right with `\vfill\hfill`). Several Appendix slides may return to one main slide. An Appendix slide that no main slide points to is linked or cut.
- `references/slides.md`, content file: each button is written as its own line, `*Button: Appendix: steps → Slide 61*`, so the Markdown still matches the slides.
- `references/slides.md`, delivery checks: every button must go to its intended page and back, read from the PDF's link targets when a PDF library is available, otherwise clicked through.
- `templates/simple-slides.tex`: the Core Mechanism slide links to the Appendix derivation slide, which links back.

## Files affected

- `skills/econ-teaching/references/slides.md` — the rule, the content-file form and the check.
- `skills/econ-teaching/templates/simple-slides.tex` — a working example of one linked pair.
- `link/econ-teaching.md` — regenerated with `tools/build_link_editions.py`.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

New decks get labelled frames and buttons; the PDF still has one page per slide, because buttons are not overlays. The bundle checker already reads frame titles when a frame carries options such as `[label=...]`: on the real 73-frame deck it compared the content file with the frames and passed. Decks made before this change are unaffected until they are revised.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the edited items in `slides.md`; template compiled with latexmk/pdfLaTeX in a scratch folder |
| Template links | Pass | PyMuPDF read the compiled template's link targets: page 3 → 5 and 5 → 3 |
| Automated structural validation | Pass | `python tests/validate_skills.py`: 3 skills passed |
| Unit tests | Pass | `python -m unittest discover -s tests -p 'test_*.py'`: 61 tests, run after this log was written (the first run failed only because the changelog linked to this log before it existed) |
| Real slide / domain evaluation | Pass (one deck) | Applied by hand to the user's one-hour seminar deck before the rule was written: 8 main slides with buttons, 13 Appendix slides with Back buttons, 22 links read back to the intended pages, and the linked pages viewed as images with no overflow. Not yet tried on a deck built from the written rule |
| GitHub Actions or other CI | Not run | Not pushed |

## Known limitations and risks

- Links work only in viewers that follow internal PDF links (Acrobat, Preview, Skim and most others); a presentation tool that imports the PDF as images loses them.
- The bundle checker does not check that buttons exist or point to the right frames; that is a manual or library check at delivery.
- A `.pptx` deck needs its own linking mechanism; the rule names only the Beamer one.

## Follow-up

Build one new deck from the written rule alone and see whether every Appendix slide gets a button and a Back button without prompting.
