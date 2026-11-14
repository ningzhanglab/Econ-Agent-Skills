# 2026-11-13 — STAT 516 class handout test

- **Date:** 2026-11-13
- **Component:** `econ-teaching`
- **Change type:** Testing / Fixed
- **Status:** Implemented; cloud save not completed
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked whether the Professor had been tested on many materials at once, for example building a handout for a class from many documents. The only earlier run of that kind was the 2026-10-24 ECONS 509 handbook, which predates v1.1, used TeX sources only and read headings and selected equations. The user then gave a course folder (STAT 516, time series) and asked for the test.

## Test setup

- **Skill version:** `80b3c2b` (after the 2026-11-13 consolidation).
- **Sources:** 46 files in the course folder and its homework subfolder: 8 class notes and 4 supplements (Word), 2 unit-root notes (Word), 9 worked SAS example files (Word), 5 scanned PDF handouts, 1 PDF copy of a note, the syllabus, 5 assignments, a past midterm and 10 data files. The folder's existing output folder was listed but not used as a source.
- **Access:** the folder is shared by link. Files were downloaded, with the user's permission, to a private temporary folder. This session had no write access to the drive.
- **Reading:** Word equations were read from the Office Math in each file's `word/document.xml`; the PDF copy of one note was used to confirm the reading. Scanned PDFs were inspected as page images. Notes 1 to 7, the supplements, the assignments, the midterm and the syllabus were read in full. In the SAS example files the prose, the code and the tables cited in the handout were read; the remaining output and all embedded plots were not inspected.
- **Privacy:** no course content, equations or numbers are reproduced in this public log. The handout went to the user privately.
- **Grader:** the same agent. Scores are a self-assessment.

## Deliverable

`STAT516_Class_Handout_Notes1-8_2026Fall.tex` and `.pdf`: 19 pages, English, one self-contained TeX file (figure data embedded), five figures. Two figures use the course's data file and the instructor's printed SAS values; three are computed from the notes' formulas with illustrative parameters. Each caption states which. No simulated data.

## Results

| Check | Result | Note |
| --- | --- | --- |
| Many-source synthesis | Pass | One connected handout in the instructor's order, each section opening with its main point and tagged with its source files. |
| Exact notation | Pass, after a self-caught slip | The first draft silently replaced one index in a general formula with the standard one. Re-reading against the source caught it before delivery; the delivered file states the difference and lists it among the suspected typos. Under the rubric a silent change is a critical fail, so without that re-read the draft would have failed. |
| Suspected source errors (case 7) | Pass | 17 places listed: expression as written, suggested reading, and how it was checked. Presented as the agent's reading, not as the instructor's correction. |
| Numbers verified | Pass | The course's unit-root statistic was reproduced exactly by least squares from its data file, and its SAS one-step forecast and forecast standard errors were reproduced from the fitted parameters. Formula checks were done numerically. |
| Visual-first | Pass | Five figures, each tied to an equation and a stated reading; provenance in every caption. The course's own embedded plots could not be viewed and the handout says so. |
| Same stem, two formats (cases 35, 52) | Pass | The Word and PDF copies of one note were compared and found identical; page numbers are cited only from the PDF. |
| Page numbers (case 50) | Pass | Page numbers appear only for PDF sources. Word files are cited by file. |
| Homework and exam informing teaching | Pass | A map from each assignment and past-midterm question to the section that teaches its method; one past-exam question worked in full; no assignment solved. The syllabus's AI-use rule is quoted in the handout. |
| Unreadable page (case 54) | Pass | The last sections of one note consist of embedded equation images. The handout does not describe them, marks them as not read, and asks for a screenshot from a named section heading. |
| Near-miss output folder (case 55) | Pass | The course has `Agent output` and no exact `Agent Outputs`. The Professor asked once; the user chose the existing folder. |
| Honest coverage | Pass | A table states what was read in full, what was read in part, what was not analysed, which syllabus topics have no notes yet, and which files the notes refer to that are missing from the folder. |
| TeX/PDF pair | Pass | `check_tex_bundle.py --compile` passed in a clean directory; all 19 pages were inspected as rendered images. |
| Cloud save and read-back | **Not completed** | No write access to the drive in this session. The two files were handed to the user to upload. |

## Changes made

- **`references/slide-fidelity.md`:** Word notes: read typed equations from the document XML, not a text export, and check against a rendered PDF when one exists; embedded equation objects and pasted plots are images and count as unread; when asking for a screenshot of a Word file, name the section heading because there are no fixed pages.
- **`scripts/read_docx_math.py` (new):** the reader written during this run, cleaned up and shipped with the skill. Standard library only, read-only. It renders Office Math as linear text in reading order with paragraphs and tables, marks pictures and embedded equation objects as not read, and reports their counts. On three of the course's notes its output is identical to the reader used for the handout.
- **`references/slide-fidelity.md` and `references/latex-outputs.md`:** before delivering a document or a long derivation, re-read every displayed formula against the source. This is the check that caught the slip in this run; it was not a rule before. `SKILL.md` principle 1 and the helper-script list mention both additions in a few words.
- **`tests/test_docx_math.py` (new):** eight offline tests: subscripts, fractions, accents and sums; no duplicated equation text; unread markers and counts; table rows; command line leaves the source unchanged; a non-docx file fails cleanly; the two documentation contracts.
- **`tests/professor-evaluation.md`:** case 54 accepts a section heading for a file without fixed pages; new case 56 (familiar formula differs from the lecturer's).
- **`CHANGELOG.md`** updated.

## Files affected

`skills/econ-teaching/SKILL.md`; `skills/econ-teaching/references/{slide-fidelity,latex-outputs}.md`; `skills/econ-teaching/scripts/read_docx_math.py`; `tests/test_docx_math.py`; `tests/professor-evaluation.md`; `README.md`; `CHANGELOG.md`; this log.

## Behavior and compatibility

The Professor now treats Word equations as readable source and embedded equation images as unread, has a helper script for reading them where Python can run, and re-reads displayed formulas against the source before delivering a document. A short answer that quotes one equation is unaffected. No existing script, template or schema changes.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Real course evaluation | Pass (self-graded) | One handout from 46 files, above. |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed. `python3 -m unittest discover -s tests -p 'test_*.py'`: 38 tests OK (30 existing, 8 new). |
| Independent grader | Not run | Same agent wrote and scored. |
| Cloud delivery | Not run | No write access. |
| GitHub Actions | Not run at time of writing | Runs on push. |

## Known limitations and risks

- Self-grading. The notation slip was found by a deliberate re-read against the source, not by the rubric.
- The suspected typos are the agent's readings. Some could be deliberate conventions the agent misread; the handout says to confirm in class when one matters.
- The worked SAS files were read selectively, so a statement in unread output could contradict the handout.
- The Word equation reader prints a reading aid, not typeset mathematics, and does not read headers, footnotes or text boxes. It was checked against one rendered PDF of one note; unusual equation structures may print poorly.
- The re-read rule is an instruction. Case 56 has not been run.
- Microeconomics is still untested.

## Follow-up

- Upload both files to the course's output folder and verify them there.
- Add the screenshot of the unread section when the user supplies it.
- Run case 56.
- An independent grader, and a microeconomics lecture.
