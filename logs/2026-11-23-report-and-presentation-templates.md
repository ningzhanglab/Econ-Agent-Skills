# 2026-11-23 — Report, lecture and presentation templates

- **Date** 2026-11-23
- **Component** `econ-learn`, `econ-present`, `econ-write`, and the shared template build
- **Change type** Changed
- **Status** Implemented
- **Related commit** See Git history for this change.

## Motivation

The user approved a simple LaTeX layout with a left-aligned title, no running header and page numbers centered at the bottom. They asked to use it in the writing, presentation and learning skills.

## Changes made

- `shared/templates/simple-handout.tex` holds the approved English article starter and its generic report example. `tools/sync_shared.py` copies it into each skill under the name appropriate to its use.
- `econ-learn` uses the shared article for English notes. Its XeLaTeX template uses the same page layout and keeps Chinese headings and prose.
- `econ-write` uses the shared article for homework and report files.
- `econ-present` uses the shared article for requested prose handouts. Its Beamer template keeps the deck structure and places one frame number at the bottom center.
- The linked homework, lecture, slides and writing routes include the templates that their skill instructions reference.

## Files affected

- `skills/econ-learn/SKILL.md`, `tasks/whole-lecture.md` and both notes templates.
- `skills/econ-present/SKILL.md` and its slide and handout templates.
- `skills/econ-write/templates/simple-report.tex`, the shared article template, and the sync and link builders.
- The generated `link/` pages, `README.md`, `CHANGELOG.md` and the template preference checks.

## Behavior and compatibility

Each installed skill contains the template it uses. The English starter includes core math and graphics packages. Add other packages when the document needs them. The presentation skill uses 16:9 Beamer for decks and the article layout for requested prose handouts.

## Verification and evidence

| Check | Result | Evidence |
| --- | --- | --- |
| English and Chinese articles | Pass | Compiled with PDFLaTeX and XeLaTeX. Inspected the rendered pages and checked the footer position. Compared the English title position with the previous report. |
| Beamer deck | Pass | Compiled the previous and revised starters with PDFLaTeX. Verified that frame numbers on all six revised slides are centered at the bottom. |
| Repository checks | Pass | `python3 tools/check_all.py` rebuilt the link editions and passed structural validation, 91 unit tests and the whitespace check. |
| Skill packages | Pass | Built each affected skill archive locally. |
| Real-paper comparison | Not run | The change concerns template layout and discovery. |
| GitHub Actions | Not run | Verification used the local checkout. |

## Known limitations

The Beamer example emits the same Appendix bookmark translation warning as the previous template. Its PDF compiles and renders.
