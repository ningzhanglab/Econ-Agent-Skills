# 2026-11-13 — Teaching consolidation and source fixes

- **Date:** 2026-11-13
- **Component:** `econ-teaching`, repository documentation
- **Change type:** Changed / Fixed / Documentation
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked to revise and improve `econ-teaching` and to be shown what needed doing. A review of the skill and of the October real-course test logs found three things, and the user approved all three:

1. **Repetition.** `DESIGN_V1.md` says each concept has one authoritative home, but the Homework rule was stated three times inside `SKILL.md` and again in two references; the bottleneck and "why this model" guidance appeared in `SKILL.md`, twice in Teaching Design and twice in Expert Teaching; answer length was specified in three files. The v1.1 log had already noted that `SKILL.md` should not grow further.
2. **Unreadable pages.** In the [ECONS 512 / STAT 516 test](2026-10-29-professor-econs512-stat516-tests.md), image-only slides, two diagrams and some symbols could not be viewed. Slide Fidelity told the Professor to state the limitation but not to ask for the page.
3. **Near-miss output folders.** The same test found both courses already had `agent output` / `Agent output`. The workflow said these are not `Agent Outputs`, so a file request would have created a second folder beside the user's own.

## Changes made

- **`SKILL.md`:** the "Teaching quality in different requests" section is removed. Its unique content moved into principle 2 (economic assumption versus identification versus computation; convergence is not accuracy), the quick-question mode, and a new "Complete lecture or Handbook" mode line. The Homework/exam mode line now points to principle 6 and keeps only what is specific to the mode (locate the actual problem and coverage; the no-exam check). The routing table sends "choosing how to explain" to Teaching Design, with Expert Teaching for the choice of angle. The seven principles are otherwise unchanged.
- **`references/teaching-design.md`:** "Select the teaching intervention" is merged into "Diagnose the learning bottleneck" (one new table row for over-generalized claims, plus a short paragraph on choosing one intervention, supplying a missing prerequisite and stopping). "Economics PhD depth without rigid answer templates" is removed: its per-field lists repeated the domain lenses, and its lecture thread moved into the Teaching arc. Section anchors used by other files are unchanged.
- **`references/expert-teaching.md`:** now only the internal lenses, the angles of explanation and intellectual honesty. The sections on model motivation, the student's misconception and adaptive length repeated Teaching Design and are removed; the visual and Homework paragraphs are replaced by a pointer to Visuals and Homework.
- **`references/slide-fidelity.md`:** when the answer depends on a page that could not be read, name the page and ask for a screenshot of that one page, and teach what is verified meanwhile.
- **`references/cloud-drive-workflow.md`** (new step 7) and **`STORAGE_POLICY.md`:** a near-miss folder in the verified course with no exact `Agent Outputs` triggers one question, naming the folder. Choosing it counts as the existing explicit override. If nobody can be asked, the exact `Agent Outputs` is created and both folders are reported.
- **`tests/professor-evaluation.md`:** regression cases 54 and 55.
- **`DESIGN_V1.md`**, **`README.md`**, **`CHANGELOG.md`** updated.

## Files affected

`skills/econ-teaching/SKILL.md`; `skills/econ-teaching/references/{teaching-design,expert-teaching,slide-fidelity,cloud-drive-workflow}.md`; `STORAGE_POLICY.md`; `tests/professor-evaluation.md`; `DESIGN_V1.md`; `README.md`; `CHANGELOG.md`; this log.

## Behavior and compatibility

- The consolidation is intended to change no behavior. Every v1 and v1.1 guarantee keeps its statement in `SKILL.md`: exact notation, tentative diagnosis, answer first and meaning last, visual-first teaching, intuition checked against the math, slide-matched Homework with the reusable method, and the student's language.
- `SKILL.md`, Teaching Design and Expert Teaching together went from 5,119 to 4,536 words.
- New visible behavior: a request for a screenshot of one named page when the answer depends on it; one question about the output folder when a course has a near-miss folder.
- The default folder name `Agent Outputs`, the TeX+PDF default, scripts, templates and the Course State schema are unchanged. No file was renamed or removed, so existing links and installs keep working.
- Deviation from the proposal shown to the user: Expert Teaching was slimmed in place instead of being folded into Teaching Design, so that links in older logs and the design document still resolve.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Re-read each edited section; checked that every sentence removed from `SKILL.md` and Expert Teaching is either stated in its remaining home or was moved. |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed. `python3 -m unittest discover -s tests -p 'test_*.py'`: 30 tests OK, including the link test and the wording contracts on `SKILL.md` and Expert Teaching. |
| Real slide / domain evaluation | Not run | No course material was used. Cases 54 and 55 have not been run. |
| GitHub Actions or other CI | Not run at time of writing | Runs on the pull request. |

## Known limitations and risks

- Whether an installed agent behaves the same after the consolidation is unverified; the claim rests on reading the text, not on a rerun of the October cases.
- The screenshot request could be over-used. The rule limits it to answers that depend on the unreadable part.
- The near-miss rule covers names that differ in capitalization, spacing or singular/plural. A differently named folder such as `outputs` is still treated as legacy.

## Follow-up

- Run cases 54 and 55, with case 55 as a real file request in a course that has a near-miss folder.
- Still owed from October: a microeconomics lecture and an independent grader for the teaching cases.
