# 2026-11-15 — Slides: Appendix title with subtitles

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference, slides template)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

[2026-11-15 — Slides: shared block titles](2026-11-15-slides-block-titles.md) kept separate titles on Appendix slides, each starting "Appendix:", while main slides moved to shared block titles. The user said the Appendix can have subtitles.

## Changes made

- `references/slides.md`, **Titles:** Appendix slides share the title "Appendix" and carry a subtitle (`\framesubtitle{...}`) saying what each one holds, so a presenter who jumps there from a link sees at once where they are. This replaces "Appendix slides keep their own titles, starting 'Appendix:', because the links name them."
- `templates/simple-slides.tex`: the Appendix slide is titled "Appendix" with the subtitle "Derivation of Proposition 1".

## Files affected

- `skills/econ-teaching/references/slides.md`
- `skills/econ-teaching/templates/simple-slides.tex`
- `link/econ-teaching.md` — regenerated with `tools/build_link_editions.py`.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

Appendix slides of new decks repeat one title and differ in their subtitle. Links still work: they target frame labels, not titles, and the button text on the main slide still names the Appendix content. In the content file each Appendix section heading is `## Slide N: Appendix`; the bundle checker compares titles by position, so repeated titles pass. A subtitle adds one short line at the top of the slide, so dense Appendix tables need checking for overflow at delivery, as every page already is.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the edited Titles item and the template's Appendix slide |
| Template compile | Pass | latexmk/pdfLaTeX in a scratch folder, no overfull boxes; Appendix button and Back button point at each other |
| Automated structural validation | Pass | `python tests/validate_skills.py` |
| Unit tests | Pass | `python -m unittest discover -s tests -p 'test_*.py'` |
| Real slide / domain evaluation | Pass (one deck) | Applied to the user's one-hour deck: 13 Appendix slides retitled "Appendix" with subtitles, all viewed as images with no text reaching the footer, the 22 links unchanged, the bundle checker passing |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing |

## Known limitations and risks

The subtitle line takes vertical space on Appendix slides that hold full tables or figures; on the one-hour deck nothing overflowed.

## Follow-up

None planned.
