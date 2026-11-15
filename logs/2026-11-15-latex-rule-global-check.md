# 2026-11-15 — LaTeX rule checked across the repository

- **Date:** 2026-11-15
- **Component:** `econ-teaching`, `README.md`, `tests/professor-evaluation.md`
- **Change type:** Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for a check of whether the recent chat-LaTeX rule (commits 4a6a652 and e4ea9c8) fits the whole repository, not only the line that states it.

## Findings

1. **Contradicting example (real).** `examples/bellman-teaching-example.md`, the skill's only example of a good answer, wrote inline math as bare LaTeX without delimiters (`\beta E[V(k',z')\mid z]` inside a sentence) and displays as `\[...\]`. Agents imitate examples, so it taught the style the rule forbids.
2. **Dollar signs (real, economics-specific).** With `$...$` as the math delimiter, a price written as `$10 to $12` is paired as math by common renderers and garbles the sentence. Elasticity and transfer examples make this likely.
3. **Code (minor).** "Every equation and symbol in LaTeX" could push LaTeX into SAS, Python or Stata code and comments.
4. **Terminal (minor).** Claude Code in a terminal shows `$...$` as code on the first answer; an accepted trade-off, but undocumented.

Checked and fine: `econ-writing` must keep the writer's own form and correctly has no LaTeX rule; `econ-research` writes little math; principles 1 and 7, the `.tex`/`.pdf` file default and evaluation case 59 agree with the rule; the link edition test keeps `link/` current.

## Changes made

- `skills/econ-teaching/SKILL.md`, the "Math in chat is LaTeX" line: adds "Write money as `\$10` or USD 10 so a dollar sign is not read as math, and keep code (SAS, Python, Stata) as code."
- `skills/econ-teaching/examples/bellman-teaching-example.md`: all math in `$...$` and `$$...$$`; symbols, wording and structure unchanged; one sentence says the example follows the chat math style.
- `tests/professor-evaluation.md`, case 57: the formula is in LaTeX and any price in the example is written as `\$10` or USD 10.
- `README.md`: under the Claude Code install step, a terminal shows LaTeX as code; ask for plain text to switch.
- `link/econ-teaching.md` regenerated.

## Files affected

As listed above, plus `CHANGELOG.md`.

## Behavior and compatibility

Same rule; fewer ways for it to go wrong. No change to requested files or to the other skills.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Search for LaTeX mentions and math style in skills, examples and evaluation cases | Pass | `grep` over `skills/` and `tests/professor-evaluation.md`; only the Bellman example conflicted; no dollar amounts in skill files |
| Example symbols unchanged | Pass | Same symbols before and after; only delimiters added |
| Link edition regenerated | Pass | `tools/build_link_editions.py` |
| Structural validation and unit tests | Pass | Run before committing |
| Real chat with a price in the answer | Not run | Not tried |

## Known limitations and risks

Renderers differ in how they treat `\$`; USD 10 is the safe fallback.

## Follow-up

Ask the elasticity question in a real chat and check both the formula and the prices.
