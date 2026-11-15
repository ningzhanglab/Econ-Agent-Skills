# 2026-11-14 — Questions outside a course

- **Date:** 2026-11-14
- **Component:** `econ-teaching` (with a one-line pointer in `econ-research`)
- **Change type:** Added
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for help with things that have no course behind them: a single term such as elasticity, a research paper they want explained (what it is about, its framework, or one part of it), equations in a screenshot taken from a book, paper or website, and small points they could not follow. The Professor's modes and source rules were written for lectures: a paper appeared only as outside material that must not override the lecture, and no mode said what to do when there is no source at all. The risk was that the skill would not trigger, or would look for a course folder or slides the user does not have.

Options considered with the user: a new "interpreter" skill, a prompt only, or a mode inside `econ-teaching`. A new skill would repeat the notation and answer-first rules and compete with `econ-teaching` for the same requests, against the stability rule in `DESIGN_V1.md`. Renaming the skill (`econ-learning`, `econ-training`) was discussed and not done: the description, not the folder name, drives triggering, and the skill was renamed two days earlier.

## Changes made

- One rule for all four cases: **whatever the student sends is the source**; no course folder search, index or request for slides unless the student points to a course.
- **Bare term:** short answer (definition, idea, example, usual formula) labeled as general economics knowledge; notation presented as a convention; differing definitions named briefly; no papers cited from memory.
- **Paper, overview:** question and claimed contribution in the authors' terms, framework (model or empirical design with its key or identifying assumption), main result with magnitude, mechanism, then a labeled link to a standard model; what was read and which version.
- **Paper, reading strategy: orient, then unblock.** The first answer is a short map plus a reading path, not a full walkthrough; depth follows where the student is stuck, diagnosed with the existing bottleneck table, and a missing prerequisite (a method, model family or term the paper assumes) is treated as the most common block. Close with the contribution in one plain sentence and, if useful, one reusable lesson for reading the next paper of this kind. Critique only when the purpose calls for it. An earlier draft with a fixed eight-step walkthrough (ask the purpose first, full notation table, critique and an understanding check every time) was rejected in discussion with the user: it replaced the student's own reading, ignored missing prerequisites, and imposed a template and a quiz that the Teaching Design rules already reject.
- **Paper, one part:** Slide Fidelity applies with the paper as the lecture; cite section, equation number and page; read the definitions the part relies on, including an appendix.
- **Screenshot:** exact symbols kept; source not guessed; assumed readings of off-screen symbols labeled, or the neighboring part requested when it matters; unreadable parts named.
- **Small confusion:** one or two sentences, then stop.
- Scope line: explaining a paper belongs to `econ-teaching`; literature positioning, evidence assessment and reference checks belong to `econ-research`.

## Files affected

- `skills/econ-teaching/SKILL.md`: description broadened to trigger on terms, papers and screenshots with no course; one Mission paragraph; one mode line; one routing row; scope sentence.
- `skills/econ-teaching/references/teaching-design.md`: new section "Questions outside a course" with the five-row table.
- `skills/econ-teaching/references/slide-fidelity.md`: opening line now covers papers and screenshots; new section "Papers and screenshots".
- `skills/econ-teaching/agents/openai.yaml`: short description mentions papers, equations and terms.
- `skills/econ-research/SKILL.md`: scope line points close reading of one paper to `econ-teaching`.
- `tests/professor-evaluation.md`: cases 57–60.
- `README.md`, `DESIGN_V1.md`, `CHANGELOG.md`: user-facing description, design note, change summary.

## Behavior and compatibility

Course-based behavior is unchanged: lectures, Homework, exams, Course Maps and file outputs work as before. New: the skill should trigger and answer directly for a term, a paper or a screenshot with no course connected. The skill folder name and `$econ-teaching` are unchanged, so no reinstall is needed beyond pulling the updated folder.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Edited sections reviewed; new anchors `#questions-outside-a-course` and `#papers-and-screenshots` match their headings |
| Automated structural validation | Pass | Run locally after the edits: `python tests/validate_skills.py` (3 skills OK) and `python -m unittest discover -s tests -p 'test_*.py'` (OK, including the LaTeX compile smoke test). `econ-teaching` description is 928 characters, under the 1024 limit |
| Real slide / domain evaluation | Not run | Cases 57–60 are new and have not been run on a real term, paper or screenshot |
| GitHub Actions or other CI | Not run | Not checked at the time of writing |

## Known limitations and risks

- Whether the broader description actually makes hosts pick `econ-teaching` for a bare term is untested.
- A short answer for a bare term from general knowledge cannot be source-checked; the label is the safeguard.
- Screenshot handling depends on the host's image reading.

## Follow-up

Run cases 57–60 on a real term, a real paper and a real screenshot, and fix the narrowest responsible text if a case fails.
