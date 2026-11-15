# 2026-11-15 — LaTeX rule made prominent

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

After commit 4a6a652 added "write chat math in LaTeX by default" to principle 1, the user tested the paste-a-link method in an incognito chat. The agent read `link/econ-teaching.md` and four reference files, wrote the math as plain text, and when asked said nothing in the skill page asked for LaTeX in chat; it cited "Ordinary questions are answered in chat" and the `.tex`/`.pdf` file default. The live file did contain the rule (checked with `curl` against the raw URL). Likely causes: the rule sat in the middle of a 97-word paragraph about notation, and the Supporting duties line the agent quoted read as "no markup". A cached copy or a summarizing fetch tool may also have played a part. The user later reported that the current version displays LaTeX, and asked not to change the README prompts.

## Changes made

- `skills/econ-teaching/SKILL.md`: the rule moved out of principle 1 to its own bold line at the top of "How to teach": "Math in chat is LaTeX. Write every equation and symbol in LaTeX (`$...$` inline, `$$...$$` displayed) from the first answer, with a lecturer's own macros written out as their source defines them. Use plain text only if the student asks or says the math shows as code."
- Same file, Supporting duties: "Ordinary questions are answered in chat, with math in LaTeX; no file is created."
- `link/econ-teaching.md` regenerated.

Not changed, at the user's request: the README paste-a-link prompts.

## Files affected

`skills/econ-teaching/SKILL.md`, `link/econ-teaching.md`, `CHANGELOG.md`, and an appended note in `logs/2026-11-15-latex-math-in-chat.md`.

## Behavior and compatibility

Same rule as before, stated where an agent reads first and no longer contradicted by the line it quoted. No change to requested files.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Live rule present before this change | Pass | `curl` of the raw `link/econ-teaching.md` and `SKILL.md` found the 4a6a652 sentence |
| Link edition regenerated | Pass | `tools/build_link_editions.py` |
| Structural validation and unit tests | Pass | Run before committing |
| Real chat after this change | Not run | To be retested by the user in a new chat several minutes after the push |

## Known limitations and risks

A skill instruction cannot override an app's own formatting rules, and a fetch tool that summarizes pages may still drop it.

## Follow-up

Retest in a new chat; if plain text persists with this wording, the remaining lever is the user's own message or app preferences.
