# 2026-11-20 — Helper-script audit: Word delimiters, figure sections, preference guard

- **Date:** 2026-11-20
- **Component:** `econ-learn` scripts, tests
- **Change type:** Fixed / Testing
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for another check after the [audit fixes](2026-11-20-audit-fixes-and-check-script.md). This pass probed the helper scripts that the earlier audits had not exercised, with small hand-made inputs. It also read the explain, derive and figures pages, and found no conflict there.

- **Word equations lost the conditioning bar.** `read_docx_math.py` joined the parts of an Office Math delimiter with ", ". When the separator is omitted, ECMA-376 defines it as `|`, and Word draws U+2502. So a Word equation for E(Y|X) was read as `(Y, X)`, a silent change of notation against shared guarantee 1. No test covered delimiters.
- **Figure Index named the wrong section.** `inventory_tex_figures.py` missed `\section*{…}`, Beamer frame titles given as `\begin{frame}{Title}`, and headings with one level of nested braces. In a probe deck, the figure under `\section{The \textbf{Data}}` was attributed to the previous frame's title "Euler Equation". The figure under the Beamer-style frame had no section.
- **No guard against the earlier test bug.** The audit fixes merged a duplicate `PREFERENCES` key that had hidden a pinned phrase. Nothing stopped the same mistake from recurring.

## Changes made

- `read_docx_math.py`: delimiter parts are joined by the declared `sepChr`. An omitted separator is `|`, U+2502 is read as `|`, and a `sepChr` with no value means no separator.
- `inventory_tex_figures.py`: section headings include starred `\section*` and `\subsection*`, Beamer `\begin{frame}<…>[…]{Title}` titles, and titles with one level of nested braces.
- Tests: one delimiter test with five cases (default, brackets, U+2502, an explicit comma, an empty separator), one section-attribution test, and an AST check that no file is listed twice in `PREFERENCES`.

## Files affected

- `skills/econ-learn/scripts/read_docx_math.py`, `skills/econ-learn/scripts/inventory_tex_figures.py` and the regenerated `link/` pages whose edition code covers them.
- `tests/test_docx_math.py`, `tests/test_professor_contracts.py`, `tests/test_shared_and_defaults.py`.

## Behavior and compatibility

Word equations with conditional bars or other separators now keep them. A delimiter with an explicit comma separator reads as before, except that the space after the comma is gone. Figure Index entries carry the nearest section or frame title. No skill text, preference or command-line option changed.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Generators, validation, unit tests, whitespace | Pass | `python3 tools/check_all.py`: all four steps PASS; 87 tests. |
| Probe reproductions | Pass | The probe deck now gives sections Phillips Curve, Euler Equation, `The \textbf{Data}`. The delimiter cases return `(Y|X)`, `[Y|X]` and `(Y,X)`. |
| OMML default separator | Checked | The ECMA-376 `sepChr` reference ([docx4java copy](https://webapp.docx4java.org/OnlineDemo/ecma376/SharedML/sepChr.html)) gives `|` as the default. Microsoft's [SeparatorChar documentation](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.math.delimiterproperties.separatorchar?view=openxml-3.0.1) describes U+2502 as Word's default. Both are read as `|`. |
| Real `.docx` from Word | Not run | The fixtures are hand-written OMML; no Word-saved file with a conditional bar was available. |
| `crop_figure.py` with PyMuPDF | Not run | PyMuPDF is not installed here; the Poppler path is covered by the existing test. |
| GitHub Actions | Not run | Not pushed when this log was written. |

## Known limitations and risks

Headings with more than one level of nested braces are still skipped. A section set inside an `\input` file does not carry back to the parent file. The bundle checker still does not follow `\includepdf`, `\lstinputlisting` or `\subfile`. That limit is documented and was left unchanged, because no failure has been observed.

## Follow-up

Check `read_docx_math.py` on a Word-saved file with a conditional expectation when a real one is at hand.
