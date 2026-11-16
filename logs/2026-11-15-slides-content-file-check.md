# 2026-11-15 — Slides: checker compares the content file with the frames

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (bundle checker, slides reference, tests)
- **Change type:** Added
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The content Markdown added earlier today is applied back to the `.tex` by slide number. If a slide is added or removed and the Markdown is not regenerated, every later edit lands on the wrong slide without any error. Nothing checked the two files against each other. The user asked whether a script should, and agreed to a light check.

## Changes made

- `check_tex_bundle.py`: new `content_file_problems(tex)`, called from `validate`. For a Beamer (or `ctexbeamer`) deck with `<stem>_content.md` beside it, it checks that the `## Slide N` sections are numbered 1..n in order, that their number equals the number of `\begin{frame}` in the source (comments ignored), and that each titled frame's title agrees with its section title after dropping math, TeX commands, punctuation and case. A frame without a title (the title page) is not compared.
- Not checked, by decision: the body text. Comparing it would need a LaTeX-to-Markdown conversion that depends on each deck's macros and layout, and would be complicated or noisy.
- No content file: nothing is checked and nothing fails, so decks made before the rule and non-slide documents are unaffected. A deck that uses `\pause`, `\only<`, `\onslide`, `\uncover<`, `\AtBeginSection`, `\input` or `\include` is skipped with a printed note, because its pages cannot be counted from the source.
- `slides.md`: the content-file item now says the deck's own macros are written out in standard LaTeX so a Markdown editor can render the math, and names the check and its limit.
- `tests/test_professor_contracts.py`: `test_slides_content_file_matches_frames`.

## Files affected

- `skills/econ-teaching/scripts/check_tex_bundle.py`
- `skills/econ-teaching/references/slides.md`
- `tests/test_professor_contracts.py`
- `link/econ-teaching.md` (regenerated), `CHANGELOG.md`, this log.

## Behavior and compatibility

The checker's command line is unchanged. It can now fail with one of three messages about the content file. It does not require the content file to exist.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the new function. |
| Automated structural validation | Pass | `python3 -m unittest discover -s tests`: 61 tests, OK, including the new one (aligned file, wrong numbering, extra section, wrong title, overlay skip, no file). `python3 tests/validate_skills.py`: 3 skills passed. |
| Real slide / domain evaluation | Pass | Copied a real 56-frame deck and the user's hand-kept content file into a scratch folder. The check reported that the sections were not numbered 1..57 in order (the user's copy had a duplicated Slide 2 section). With the duplicate removed it returned no problems: 56 sections, 55 titles compared, several containing math. |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing. |

## Known limitations and risks

- Body text can still drift between the Markdown and the `.tex`.
- The frame parser is simple: it reads the title from `\begin{frame}{...}` or `\frametitle{...}` and does not understand frames produced by macros.
- Whether macros are written out in the Markdown is not checked.
- The content-file rule itself has not yet been used to build a deck.

## Follow-up

Generate the content file for the trial one-hour deck and try the round trip.
