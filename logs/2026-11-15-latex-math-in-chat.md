# 2026-11-15 — LaTeX math in chat answers

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Added
- **Status:** Implemented; not yet tried in a real chat
- **Related commit / PR:** See Git history for this change

## Motivation

The user observed that the agent sometimes writes math in ordinary chat answers as plain text or Unicode (`β E_t[u'(c_{t+1})]`) instead of LaTeX, and switches only after being asked. A search of `econ-teaching` found that LaTeX is mentioned only for requested `.tex`/`.pdf` files; nothing says how to typeset math in chat, and "Keep output simple, portable" in Supporting duties can read as "avoid markup".

An earlier answer in the session judged the rule unnecessary: the exact-notation rule already covers symbols, rendering depends on the app, and no failure had been observed. A second review (pasted by the user) pointed out that the user's own observation is the failure, and that a fallback clause handles apps that cannot render math. The rule was added on that basis.

## How the wording was settled

1. First draft (same day, uncommitted): LaTeX from the first answer, plain text "only where the host cannot render math, such as a terminal". This asked the agent to judge whether its app renders math, which it often cannot know.
2. The user showed a screenshot from a web chat in which the agent wrote equations in plain text and, asked why, said LaTeX was only for requested TeX or PDF output, because the skill mentions LaTeX only there. The user also noted that other agents displayed LaTeX without trouble. The difference is the model's default habit, not the app: common web chats render LaTeX.
3. Final wording: LaTeX by default everywhere, with no judgment about the app; plain text only when the student asks or says the math shows as code. A clause on lecturer macros was kept because it is a notation-fidelity point, not formatting: a macro such as `\E` copied into chat does not render, and expanding it from habit can change the symbol (`\mathbb{E}` versus `\mathrm{E}`). Naming KaTeX was considered and rejected: it is a renderer, not a syntax, and apps differ.

## Changes made

- `skills/econ-teaching/SKILL.md`, principle 1: in chat, write math in LaTeX by default (`$...$` inline, `$$...$$` displayed), including in the first answer, and write a lecturer's own macros out as their source defines them; switch to plain text only if the student asks or says the math shows as code. It sits in `SKILL.md` because that file is always loaded, so it applies from the first answer.
- `tests/professor-evaluation.md`, case 59: the first answer writes equations in LaTeX; a variant checks that an author's own macro (such as `\E`) is written out as the source's `\newcommand` defines it.
- `link/econ-teaching.md`: regenerated with `python tools/build_link_editions.py`.

## Files affected

`skills/econ-teaching/SKILL.md`, `tests/professor-evaluation.md`, `link/econ-teaching.md`, `CHANGELOG.md`.

## Behavior and compatibility

Chat answers should use LaTeX math from the start in every app; a student who sees raw code can ask for plain text. Requested files are unchanged (still `.tex` and `.pdf`). In a terminal the plain-text fallback must still keep every symbol exact. About 40 extra words in `SKILL.md`.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Search for an existing chat-math rule | Pass | `grep` over `skills/econ-teaching`: LaTeX appears only for requested files |
| Link edition regenerated | Pass | `tools/build_link_editions.py` wrote `link/econ-teaching.md`; the other two were up to date |
| Structural validation and unit tests | Pass | Run before committing |
| Real chat answer | Not run | Not tried in Claude.ai, ChatGPT or a terminal |

## Known limitations and risks

In a terminal, the default produces raw `$...$` until the student asks for plain text; `$` can be confused with currency in some apps; other skills (`econ-writing`, `econ-research`) are unchanged.

## Follow-up

Ask one equation question in the app you use most and check the first answer.

## Correction (2026-11-15, later the same day)

A real test showed agents could miss the rule inside principle 1. It now stands on its own line at the top of "How to teach", and the Supporting duties line says chat answers use LaTeX. See [LaTeX rule made prominent](2026-11-15-latex-rule-prominent.md).

## Correction 2 (2026-11-15, later the same day)

The state described in the correction above did not last: the separate line was removed again. For the wording now in force see [LaTeX for inline notation](2026-11-15-latex-inline-notation.md). The macro clause added here is no longer in `SKILL.md`; evaluation case 59 still checks it.
