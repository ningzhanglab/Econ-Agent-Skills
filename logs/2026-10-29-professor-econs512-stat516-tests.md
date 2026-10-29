# 2026-10-29 — ECONS 512 and STAT 516 tests of v1.1

- **Date:** 2026-10-29
- **Component:** `econ-phd-professor`
- **Change type:** Testing / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

After the [ECONS 509 test](2026-10-29-professor-econs509-se-lecture-test.md), the user asked to test the Professor on all courses in their Drive and to fix and merge any problems found. The remaining two courses cover the fields not yet tested: econometrics (ECONS 512) and time series (STAT 516).

## Test setup

- **Skill version:** `440e335`.
- **ECONS 512:** the instrumental-variables lecture (55 pages) with HW1 Questions 4–5, which match it, and the syllabus.
- **STAT 516:** the augmented Dickey–Fuller notes (two copies in different subfolders), the course's Fuller critical-value table, note 4 on identification, Assignment 4, the 2022 midterm and the syllabus. The notes' example data file was downloaded, and the notes' ADF statistics were reproduced exactly from it.
- **Access limits:** sources were read through the Drive connector's text extraction. Large PDFs could not be fetched as page images, so image-only slides, two diagrams and some Greek letters and equation objects were not viewed; every answer that depends on them says so.
- **Privacy:** no course content in this public log. The ECONS 512 syllabus asks students not to repost course materials; the full transcript went to the user privately.
- **Prompts:** ten (five per course), covering cases 45, 46 (twice, on real homework), 47 (with a real past exam), 48 (twice), 49, 51 and the time-series trap list.
- **Grader:** the same agent. Scores are a self-assessment.

## Results

| Case | Result |
| --- | --- |
| 45 Answer first | Pass (both courses) |
| 46 Homework names the method | Pass on an ECONS 512 homework part; partial on a STAT 516 assignment question whose coefficient was missing from the source (correctly not invented) |
| 47 Exam preparation, real past exam | Pass: past paper not treated as predicting the final; practice item labeled and held back |
| 48 Chinese, notation unchanged | Pass (both courses); declined to describe a diagram it had not seen |
| 49 Trap raised tentatively | Pass (strong vs valid instrument); time-series trap (non-rejection as proof) also passed |
| 50 Page numbers | Pass: PDF page markers used for ECONS 512; sections cited instead of page numbers for STAT 516, as the rule from the previous test requires |
| 51 No exam | Pass (ECONS 512 is graded by homework only) |

No critical fails. Six rubric scores of 1 across 10 answers, mostly honest partials where the source was unreadable, plus one answer that was longer than the question needed.

The time-series answer on choosing deterministic terms used a figure computed from the course's own data, with its provenance stated. The previous test's only observation about visuals was that this kind of figure had been missed, so this is the visual-first principle working.

## Changes made

1. **`references/course-state-and-sources.md`:** the same file name in *different subfolders of one course* is a candidate match, not a provisional one: compare a section first, then use each copy for what it reads best or treat them as versions. The rules previously covered only the same folder and different courses.
2. **`references/cloud-drive-workflow.md`:** respect a course's own rules on sharing materials. Keep any output that reproduces course content private and mention the rule to the student once when it bears on the request.
3. **`tests/professor-evaluation.md`:** regression cases 52 (same name, two subfolders) and 53 (course sharing rule).
4. **`README.md`** roadmap and **`CHANGELOG.md`** updated.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Real slide / domain evaluation | Pass (self-graded) | Ten prompts on two real courses, above. Every number in the answers was checked against the source output or recomputed; the ADF statistics were reproduced to five decimals from the course data. |
| Automated structural validation | Pass | `python tests/validate_skills.py`; `python -m unittest discover -s tests -p 'test_*.py'`: 19 tests OK. |
| Independent grader | Not run | Same agent answered and scored. |
| GitHub Actions | Pending at time of writing | Runs on push. |

## Known limitations and risks

- Micro theory is still untested; all three courses tested so far are macro, econometrics or time series.
- Text extraction limits what can be verified from large PDFs. The skill's honesty rules handled this, but the teaching is weaker where slides are image-only.
- Output-folder naming was not exercised: the ECONS 512 and STAT 516 folders use nonstandard names (`agent output`, `Agent output`), so a requested file would need the student to confirm the existing folder or accept a new `Agent Outputs`.

## Follow-up

- A microeconomics lecture, if one becomes available.
- An independent grader.
- A file-request run on a course with a nonstandard output folder.
