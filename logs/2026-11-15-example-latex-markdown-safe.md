# 2026-11-15 — Example math rewritten so Markdown does not break it

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (examples)
- **Change type:** Fixed
- **Status:** Implemented; rendering not viewed by the agent
- **Related commit / PR:** See Git history for this change

## Motivation

The user read the new Slutsky example (commit 79ba00d) and reported that some of its notation did not render as LaTeX. The report did not say which lines or in which viewer.

## Cause found

Reading the source found two constructs that a Markdown parser can take before the math renderer sees them:

1. **A displayed equation line starting with `- ` or `+ `.** Both displayed derivative equations in the Slutsky example were broken across lines with the operator first. Markdown reads `- ` and `+ ` at the start of a line as a list item, which splits the `$$ ... $$` block.
2. **Backslash followed by punctuation** (`\,`, `\;`, `\{`, `\}`). Markdown treats these as escaped punctuation and can drop the backslash, so a thin space becomes a visible comma and braces disappear.

Whether these are the lines the user saw is an inference from the source, not a confirmed match.

## Changes made

No symbol or result changed; only how the same math is typed.

- `slutsky-teaching-example.md`: each displayed equation is on one line, with no line starting with an operator; `\,` removed; `\big( \big)` replaced by plain parentheses; the illustrative demand is written `w/(2p_1)` and its derivative `-w/(2p_1^2)` instead of `\tfrac{1}{2}\, w/p_1`; `\tfrac` replaced by `\frac`; an explicit `\cdot` between the two derivatives.
- `omitted-variable-homework-example.md`: `\xrightarrow{\;p\;}` became `\xrightarrow{p}`; `\,` and `\;` removed; the placeholder `\hat{\,\cdot\,}^{\,s}` is now the words "the superscript $s$".
- `bellman-teaching-example.md`: `\{ ... \}` became `\lbrace ... \rbrace` (same output); `E[\,\cdot \mid z]` became `E[\cdot \mid z]`.
- `link/econ-teaching.md` regenerated (new edition code).

## Files affected

The three example files above, `link/econ-teaching.md`, `CHANGELOG.md`.

## Behavior and compatibility

None for rules. The examples no longer show agents the two fragile constructs.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Scan for the two constructs | Pass | `grep` over the examples, references and `SKILL.md` for lines starting with `-`/`+`/`=` followed by a TeX command and for `\,` `\;` `\{` `\}` inside math: no hit left |
| Structural validation and unit tests | Pass | `python3 tests/validate_skills.py`; 57 tests |
| Rendered view | Not run | The files were not opened in GitHub or a Markdown viewer by the agent |

## Known limitations and risks

Other viewers have other limits (for example no support for `\operatorname` or `\xrightarrow`). If something still shows as code, the line and the viewer are needed to find it.

## Follow-up

The user reopens the Slutsky example and reports any line that still fails, with the viewer used.

## Update (2026-11-15, after the user's test; same uncommitted change)

The fixes above did not cover what the user saw. The user named the viewer (the Claude desktop app) and three spans that stayed as raw `$...$`, then opened a 15-line test file written for the purpose (kept outside the repository) and reported that lines 1, 4, 12 and 13 did not render.

What the test shows about that viewer's inline math:

| Case | Result |
| --- | --- |
| Letters and brackets only, such as `$v(p,w)$`, alone or two joined by "and" | Not rendered |
| The same with a subscript, such as `$v_0(p,w)$`; anything with `_`, `^` or a TeX command | Rendered |
| A single letter, such as `$w$` | Rendered |
| Closing `$` followed by a quotation mark | Not rendered |
| Closing `$` followed by a full stop or comma; formula ending in a number; formula starting with a minus sign | Rendered |
| `$-\frac{\partial x_1}{\partial w} x_1 = -\frac{1}{4} \times 25 = -6.25$` | Not rendered; the cause was not isolated (a shorter fraction-and-numbers formula rendered) |
| A displayed `$$ ... $$` equation on its own lines | Rendered |

The first, fourth and sixth rows are observations from one test in one app, not a documented rule.

Further changes, again with no symbol or result changed:

- `slutsky-teaching-example.md`: `$v(p,w)$` and `$e(p,u)$` in sentences became "$v$ for the indirect utility function" and "$e$ for the expenditure function"; "`$u = v(p,w)$`" in sentences became "the utility level $u$ the consumer actually reaches"; the numerical check moved into two displayed equations; the formula before a closing quotation mark was reworded.
- `bellman-teaching-example.md`: `$k'$` and `$z'$` became `$k^{\prime}$` and `$z^{\prime}$` (the same symbol); `$u(c)$` and `$V(k,z)$` in sentences were reworded around single letters; a formula before a closing quotation mark was reworded. Whether `$k'$` failed in the viewer was not tested; it was changed because it matches the first row.
- `omitted-variable-homework-example.md`: no further change; every inline formula there has a subscript or a TeX command.
- `link/econ-teaching.md` regenerated.

`SKILL.md` and the chat LaTeX rule were not changed. The finding bears on them: an agent that follows the rule and writes `$v(p,w)$` in the Claude desktop app would hit the same limit. No wording was added, because the limit is one app's and was seen in one test.

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Scan of the three examples for the failing patterns | Pass | A script listing inline formulas with no `_`, `^` or backslash and more than one character, or followed by a quotation mark, reports none |
| Structural validation and unit tests | Pass | `python3 tests/validate_skills.py`; 57 tests |
| Rendered view of the revised files | Not run by the agent | To be confirmed by the user in the Claude desktop app |
