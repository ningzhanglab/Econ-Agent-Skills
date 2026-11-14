# Change Log

A short, chronological summary of meaningful changes to the Econ Agent Skills repository. Newest changes appear first. Detailed records explain rationale and validation in [logs/](logs/README.md). Exact diffs and commit history are preserved by Git.

## Unreleased

_No uncommitted planned changes are represented as completed here._

## 2026-11-13

### Econ Teaching — Whole-class handout test on STAT 516

- Built one class handout from a real course folder with 46 source files (Word notes and supplements, scanned PDF handouts, SAS example files, data files, five assignments, a past midterm and the syllabus): a 19-page `.tex` and `.pdf` with five figures. Every Word equation in the eight class notes was read. Passed, self-graded, with no critical fail in the delivered file.
- **What worked:** exact notation kept; 17 suspected typos in the course files shown as written and flagged separately, each with a check; the course's own unit-root statistic and SAS forecasts reproduced from its data files; honest coverage table; assignments and the past midterm mapped to the method they use.
- **New rules exercised:** the near-miss output folder question (case 55) was asked once and answered. The unreadable-page rule (case 54) fired for one section whose equations are embedded images.
- **Not completed:** the files were handed to the user, not written to the course's cloud folder, because this session had read-only access to the drive.
- **Fixed** in Slide Fidelity: Word equations are read from the document XML, not from a text export; embedded equation images count as unread; a Word file is cited by section heading because it has no fixed pages.
- **Added** a standard-library [Word equation reader](skills/econ-teaching/scripts/read_docx_math.py): it prints a `.docx` as text with its typed equations kept, and marks pictures and embedded equation objects as not read. Eight offline unit tests in `tests/test_docx_math.py`.
- **Added** to Slide Fidelity and TeX/PDF Outputs: before delivering a document, re-read every displayed formula against the source, because the textbook form of a formula is what silently replaces the lecturer's. Evaluation case 56 covers it.
- Details: [2026-11-13 — STAT 516 class handout test](logs/2026-11-13-professor-stat516-class-handout-test.md).

### Econ Teaching — Consolidation and two fixes from real-course tests

- **Less repetition, same behavior.** `SKILL.md` stated the Homework rule three times and now states it once; its "Teaching quality in different requests" section is folded into the principles and the mode list. In Teaching Design, the intervention list is merged into the bottleneck table and the per-field depth list is removed in favor of the domain lenses. Expert Teaching now holds only the angles of explanation and points to Teaching Design for diagnosis, model motivation and answer length. The skill's teaching text is about 580 words shorter.
- **Unreadable slide page:** when an answer depends on a page that could not be read, the Professor names the page and asks for a screenshot of that one page, and teaches what is verified meanwhile.
- **Near-miss output folder:** when a course already has a folder such as `agent output` and no exact `Agent Outputs`, the Professor asks once which to use instead of silently creating a second folder. The default name `Agent Outputs` is unchanged.
- Regression cases 54 and 55 added to the Professor evaluation. Not yet run on a real course.
- Details: [2026-11-13 — Teaching consolidation and source fixes](logs/2026-11-13-teaching-consolidation-and-source-fixes.md).

## 2026-11-12

### Econ Research — Independent rerun and fixes

- An agent that did not write `econ-research` reran all seven evaluation cases on new topics (minimum wages, refugees and native workers, the 2022 Ukrainian refugee inflow, housing and inequality, the China shock and marriage, a HANK/trade/immigration `.bib`, Borjas 2003). All seven passed (self-graded by that agent). Its probes of the checker found two false WARNs on correct entries and a zero exit code on failed lookups.
- **Fixed** in the reference checker: a year is checked against every date in the Crossref record, and a year one after a late-November/December print date passes with a note (QJE 137(1) is the 2022 volume but has a 2021 print date). A venue that differs from the record is now a note, not a WARN, because journals get renamed. A failed lookup (ERROR) now exits with status 2. Five regression tests added.
- **Fixed** in Literature Search: cite the volume year, not the Crossref print date; take years from Crossref or the publisher, not aggregators; look for a missing published version in RePEc/JSTOR; check that an "abstract" is real and say where it came from; say when a PDF could not be read; rank "most important" papers by relevance then influence and sort by citations only with a title filter; ERROR and notes documented. Research Questions: stating assumptions and proceeding is fine for broad brainstorming requests. Case 6 of the evaluation now has optional harder entries.
- Details: [2026-11-12 — independent rerun](logs/2026-11-12-econ-research-independent-rerun.md) and [2026-11-12 — fixes from the independent rerun](logs/2026-11-12-econ-research-rerun-fixes.md).

### Econ Research — Cases 6 and 7; all seven cases run once

- Bibliography check: correct PASS/WARN/FAIL/SKIP results, follow-up searches for the failed and no-DOI entries, user file left unchanged. Paywalled paper: abstract-only summary, labeled. Both passed (self-graded); all seven research cases have now been run once.
- **Fixed** in Literature Search: search the title before calling a failed DOI fabricated, report which fields of a no-DOI entry were confirmed, and list corrections instead of editing the user's file.
- Details: [2026-11-12 — econ-research cases 6 and 7](logs/2026-11-12-econ-research-cases-6-7.md).

### Econ Research — Cases 2, 4 and 5; two checker fixes

- Fake-paper case: no such paper found, no summary given, closest real paper offered. Research-idea cases: three second-year-paper candidates near the Aiyagari literature tested; one recommended, one judged largely done by an existing paper; "is it done?" answered against verified closest papers. All passed (self-graded).
- **Fixed** in the reference checker: HTML entities in Crossref records are decoded, and records without a venue print cleanly. Added a unit test.
- Details: [2026-11-12 — econ-research cases 2, 4 and 5](logs/2026-11-12-econ-research-cases-2-4-5.md).

### Econ Research — First real-topic test, three fixes

- Ran `econ-research` on precautionary saving and wealth inequality in Aiyagari-type models: 17 papers found, all 17 DOIs verified against Crossref, abstracts read for 12 and the rest reported as metadata only. Case 1 passed and case 3 partly (self-graded).
- **Fixed** in Literature Search: known papers may be used only as verified search seeds; cite the print year when sources disagree; fill incomplete records from another version and name the source; older work without a DOI is checked in RePEc or a catalogue, otherwise cited only as UNVERIFIED.
- Details: [2026-11-12 — First econ-research topic test](logs/2026-11-12-econ-research-first-topic-test.md).

### New skill — Econ Research (v0.1: questions and literature)

- Added [`econ-research`](skills/econ-research/SKILL.md) for developing research questions and working with the literature: testing an idea for contribution, identification and feasibility; searching, screening and verifying papers; synthesizing agreement, splits and gaps; positioning a project.
- **No reference from memory:** every paper is checked against a bibliographic source or labeled UNVERIFIED, and answers say whether the full text, abstract or only metadata was read.
- New standard-library [reference checker](skills/econ-research/scripts/verify_references.py) compares DOIs or a `.bib` file with Crossref (PASS / WARN / FAIL / SKIP), with offline unit tests in `tests/test_research_contracts.py`, and seven manual [research evaluation cases](tests/research-evaluation.md).
- Ideas adapted with credit from claude-academic-workflow (MIT) and awesome-econ-ai-stuff (CC0). Identification design and empirical methods are not included yet.
- Details: [2026-11-12 — Econ Research skill](logs/2026-11-12-econ-research-skill.md).

### Rename — `econ-teaching` and `econ-research`

- `econ-phd-professor` is now **`econ-teaching`** (folder `skills/econ-teaching/` and skill `name`), so the three skills are named after what they do: `econ-teaching`, `econ-writing` and the planned `econ-research` (formerly `econ-research-agent`). Behavior is unchanged; the skill still presents itself as the Econ PhD Professor.
- Existing installs must be replaced with the folder under its new name, and prompts that used `$econ-phd-professor` should use `$econ-teaching`.
- Links in active docs, tests and script usage lines updated. Older entries below and dated logs keep the old name as written.
- Details: [2026-11-12 — Rename to econ-teaching](logs/2026-11-12-rename-econ-teaching.md).

### New skill — Econ Writing (v0.1)

- Added [`econ-writing`](skills/econ-writing/SKILL.md), a separate skill for editing, reviewing and structuring the user's own English economics writing: research papers, thesis chapters, referee and research reports, and homework write-ups.
- **Terminology stays unchanged.** The skill builds a term list from the draft first and uses each term exactly as written; it never swaps in synonyms and flags inconsistent use instead of choosing. Math, numbers, citation keys, LaTeX labels and stated conditions are also left as written.
- Three references: terminology and LaTeX safety, economics writing conventions (paper sections, thesis chapters, referee reports, homework), and AI-sounding patterns adapted for economics from the MIT-licensed [humanizer](https://github.com/blader/humanizer) skill.
- Added seven manual [writing evaluation cases](tests/writing-evaluation.md); README, AGENTS.md, DESIGN_V1.md and STORAGE_POLICY.md now describe the second skill. Not yet tested on real drafts.
- Details: [2026-11-12 — Econ Writing skill](logs/2026-11-12-econ-writing-skill.md).

## 2026-10-29

### Professor — Econometrics and time-series tests, two fixes

- Tested on ECONS 512 (IV lecture with matching homework) and STAT 516 (unit-root notes, an assignment and a real past midterm); ten prompts, all cases passed, no critical fails (self-graded). The notes' ADF statistics were reproduced exactly from the course's own data.
- **Fixed:** same-name files in different subfolders of one course are now compared before being treated as one document; a course's own rules against sharing materials are respected and mentioned once. Added regression cases 52 and 53.
- Details: [2026-10-29 — ECONS 512 and STAT 516 tests](logs/2026-10-29-professor-econs512-stat516-tests.md).

### Professor — First real-lecture test of v1.1, two fixes

- Ran the Professor on one ECONS 509 lecture (stationary equilibrium in the Aiyagari model) with six prompts covering cases 45, 47, 48, 49 and 2, plus a substitute for 46. All passed in final form; see the log for scores.
- **Found and fixed:** (1) a first draft cited three wrong page numbers by counting frames in the TeX source; Slide Fidelity now requires taking page numbers from the rendered PDF and checking them. (2) Exam preparation assumed an exam exists; the course has none, so the skill now says to check and prepare for the actual assessments. Added regression cases 50 and 51.
- Details: [2026-10-29 — ECONS 509 lecture test](logs/2026-10-29-professor-econs509-se-lecture-test.md).

### Professor — Common traps and portable helper scripts

- Each domain lens (macro with numerical methods, micro, econometrics, time series) now ends with **common PhD-level traps to anticipate**; Teaching Design says how to use them: tentatively, only when relevant, and in the Slide's notation.
- Helper scripts moved from `scripts/` to `skills/econ-phd-professor/scripts/`, so a standalone install of the skill keeps them; links, tests and README updated.
- Review fixes: removed the last link outside the skill folder, clarified *answer first* for proof questions, stated the LATE conditions in full. Added evaluation case 49.
- Details: [2026-10-29 — Common traps and portable scripts](logs/2026-10-29-professor-common-traps-and-portable-scripts.md).
- Merged in [PR #1](https://github.com/ningzhanglab/Econ-Agent-Skills/pull/1) (`526b477`) with CI passing; README updated afterwards to describe the trap lists and the self-contained skill folder.

### Professor v1.1 — Teaching revision

- Reorganised SKILL.md so the teaching argument leads: seven teaching principles first, source navigation and file output as supporting duties. All v1 guarantees are kept.
- New learning habits: **answer first**, close substantive derivations with their **economic meaning**, check intuition against the math, **name the reusable method** after Homework and exam solutions, an optional held-back practice item for exam preparation, and teaching in the student's language with unchanged symbols.
- Fixed rendering defects (escaped backticks, doubled backslashes) in six skill files; rewrote the README more compactly with an up-to-date repo tree; added evaluation cases 45–48 and two rubric dimensions; added `.gitignore`.
- Details: [2026-10-29 — Professor v1.1 teaching revision](logs/2026-10-29-professor-v1-1-teaching-revision.md).

## 2026-10-24

### Professor — Slide-aligned Homework and exam solutions

- Added a general rule for solving real Homework and preparing for exams: **keep the instructor's notation, assumptions and same/closest applicable Slide derivation**, retain the essential intermediate mathematical steps and check the conclusion.
- When notation or assumptions differ, map them explicitly; never claim an independently derived method is the professor's. Keep the response appropriately concise and follow documented course AI-use requirements.
- Applied the rule to the core Skill, Homework/reference guidance, adaptive teaching modes, README and v1 design record.
- Details: [2026-10-24 — Slide-aligned Homework and exam solutions](logs/2026-10-24-slide-aligned-homework-exam-solutions.md).


### Professor — Remove overfitting to legacy STAT 516 instructions

- Replaced the prior beginner-first Time Series lesson template with a concise, optional [Time Series reasoning lens](skills/econ-teaching/references/time-series.md). It preserves rigor about time dependence, lag conventions, model properties, inference and forecasting **without imposing a seven-stage teaching style, SAS requirement or default textbook length**.
- Refined Econometrics, LaTeX guidance and README; actual course and current user requests now determine depth and output.
- Historical course-specific instructions remain historical context, not global Skill requirements. Details: [design correction](logs/2026-10-24-remove-legacy-time-series-template-overfit.md).


### Professor — Beginner-first Time Series learning (same Skill)

- Added [Time Series teaching lens](skills/econ-teaching/references/time-series.md) inside the existing Professor Skill (not another Skill) with flexible beginner-to-rigorous teaching, justified derivations, original notation, relevant ACF/PACF visuals, SAS interpretation, concise Homework vs comprehensive guide modes.
- Connected the reference to core Skill routing, Econometrics, Teaching Design and LaTeX output guidance.
- Clarified that an explicitly user-selected **existing course output folder** overrides the generic `Agent Outputs` name; this avoids accidentally duplicating a course's already verified nonstandard `Agent output` folder.
- Reviewed the STAT 516 course folder and confirmed the specified teaching-style companion exists; **no private course files were committed to GitHub, and no Handbook or unnecessary cloud test was generated**.
- Details: [Time Series teaching lens development log](logs/2026-10-24-professor-time-series-learning-lens.md).


### Professor — Add optional course Learning Logs

- Added a concise editable Markdown [Learning Log template](skills/econ-teaching/templates/learning-log.md) and [opt-in workflow](skills/econ-teaching/references/learning-log.md) for study-session topics, questions, clarifications, verified Lecture/Homework links and open issues.
- Learning notes are **private course artifacts**, separate from public GitHub development logs. They are saved **on demand**, not automatically after every chat; existing dated notes are read before safe append, or a separate filename is used to avoid data loss.
- Integrated log routing into the Professor, Drive guidance, teaching architecture and README without changing the default TeX/PDF convention for other requested files.
- Initialized an ECONS 509 `Agent Outputs/Learning Logs/2026-10-24.md` setup-only file, with no fabricated learning/mastery claims.
- Details: [2026-10-24 optional private Learning Logs](logs/2026-10-24-optional-private-learning-logs.md).


### Professor v1 — Consolidated design and cross-lecture reasoning

- Integrated cross-lecture economic transfer: verified common objects, changes in primitives/closure versus numerical/empirical methods, notation mapping, limits and explicit/derived/provisional source evidence.
- Simplified on-demand course indexing, corrected the course-retrieval numbering error, and updated existing Course Map/Lecture Index instead of adding another required concept registry.
- Created [DESIGN_V1.md](DESIGN_V1.md) as the final architecture and **stop rule** for speculative design churn. README now labels a v1 design baseline without overstating independent teaching validation.
- No new Handbook, cloud upload or benchmark; existing CI retained for proportional regression checks.
- Details: [v1 consolidated design](logs/2026-10-24-professor-v1-consolidated-design.md).


### Professor — Diagnose misconceptions and explain why models are designed this way

- Added question-to-bottleneck teaching guidance covering notation, missing mathematical steps, incentives, modeling assumptions, identification and numerical approximation, without ungrounded claims about a student's understanding.
- Explicitly explained the **purpose, gain, excluded channels and controlled alternatives** of economic modeling choices; distinguished modeling primitives from statistical identifying assumptions and numerical approximation.
- Strengthened the use of decisive derivations and **checked** counterexamples; added short hypothetical Macro, Micro, Econometrics and numerical-economics examples.
- Preserved all source, visual, Homework and cloud file rules. Used existing CI only; no new Handbook or large end-to-end benchmark.
- Details: [2026-10-24-professor-diagnostic-model-design.md](logs/2026-10-24-professor-diagnostic-model-design.md).


### Design — Teach first, route workflows on demand

- Reorganized `econ-phd-professor` around learner intent and six adaptive explanation modes rather than a fixed multi-step file/indexing process.
- Added a focused [Teaching Design](skills/econ-teaching/references/teaching-design.md) reference integrating exact-notation mathematics, visual intuition, Homework and economics depth without mandatory headings or extra artifacts.
- Simplified core reference routing while keeping all source integrity, original-figure provenance, course mapping, and exact private `Agent Outputs/` + default TeX/PDF requirements.
- Added proportional evaluation guidance: preserve existing CI, but prioritize Skill design and limit new end-to-end or multi-file tests to significant changes.
- Details: [2026-10-24-professor-teaching-first-design.md](logs/2026-10-24-professor-teaching-first-design.md).


### Real-course visual-first test — ECONS 509 DSDP + PS1

- Produced a separately versioned **18-page** Visual-Enhanced Volume III, versus the prior 15-page text/math-only version, with five embedded vector diagrams explaining borrowing constraints, VFI bounds, policy transitions, Howard, and solution-accuracy layers.
- Retrieved and inspected the original 50-page DSDP handout; used **independent labeled teaching schematics** rather than claiming they appeared in the instructor deck or fabricating PS1 solver data.
- Verified both TeX/PDF files in private `Agent Outputs/`; cloud SHA-256 matched local files, and downloaded TeX compiled cleanly into an 18-page PDF with identical extracted text.
- Details: [2026-10-24-econs509-dsdp-ps1-visual-enhanced-e2e](logs/2026-10-24-econs509-dsdp-ps1-visual-enhanced-e2e.md).


### Professor — Visual-first teaching, Figure Index and test expansion

- Replaced new-image-as-last-resort wording with proactive visual teaching alongside exact mathematics; no arbitrary figure quotas.
- Added an original figure locator and [Figure Index template](skills/econ-teaching/templates/figure-index.md); when a TeX figure asset is missing, check the corresponding rendered handout PDF before declaring the figure unseen.
- Simplified the Professor's core rules from 12 to six priorities, while preserving exact notation, Homework and private TeX/PDF cloud delivery.
- Added teaching evaluation cases 38–44 and Python tests for provenance and nested TeX figure sources.
- Details: [2026-10-24-professor-visual-first-figure-index](logs/2026-10-24-professor-visual-first-figure-index.md).


### Test — ECONS 509 Volume III, source-grounded DSDP + PS1 teaching

- Added a 15-page Chinese DSDP teaching companion grounded in the original Lecture and PS1, including Bellman contraction, policy-induced Markov distribution, Howard=Newton, residual-gradient and Euler/KKT derivations, with explicit PS1(a)--(h) mapping.
- Uploaded and verified TeX/PDF in the exact private `Agent Outputs/`; SHA-256 of both downloaded formats matched local sources; clean-directory XeLaTeX rebuild matched PDF page count and text.
- Lecture rendered overlays, numerical solver runs and independent economics grading remain outside this test.
- Details: [2026-10-24-professor-dsdp-ps1-lecture-handbook.md](logs/2026-10-24-professor-dsdp-ps1-lecture-handbook.md).


### Test — ECONS 509 detailed quantitative methods (Volume II)

- Added a 20-page Chinese deep-dive companion to the existing 22-page course Handbook, with detailed DSDP/CSDP/DLDP/SE derivations and PS1–PS3 learning links.
- Saved TeX and PDF in the verified private `Agent Outputs/`; re-downloaded both; cloud TeX SHA matched local and compiled again to a 20-page PDF with identical extracted text to cloud PDF.
- Missing source visual assets and independent teaching review remain untested; no raw course materials or handbook contents committed to this public repository.
- Details: [2026-10-24-professor-econs509-deep-dive-volume-ii.md](logs/2026-10-24-professor-econs509-deep-dive-volume-ii.md).


### Test — ECONS 509 end-to-end whole-course handbook

- Built a 22-page Chinese course handbook from eight real Lecture TeX sources, the Syllabus and PS1--PS3; compiled XeLaTeX into PDF.
- Verified both TeX and PDF uploads into the correct course `Agent Outputs/`, round-trip SHA-256 equality and clean-directory TeX recompilation.
- Source figure inspection and independent pedagogical blind grading remain outside the test.
- Details: [2026-10-24-professor-econs509-handbook-e2e](logs/2026-10-24-professor-econs509-handbook-e2e.md).


### CI — Validate all active Markdown reference links

- Added standard-library CI tests for local links in README, active Skill references, templates, policies and manual test guidance.
- The check excludes immutable dated history logs and does not attempt to validate external websites.
- Details: [2026-10-24-active-link-validation](logs/2026-10-24-active-link-validation.md).


### Course-file metadata — Group matching TeX, PDF and Word safely

- Added read-only exact-parent, same-stem file grouping and tests for cross-course collisions and presenter variants.
- Updated Course State example to track available format representations as provisional, not confirmed identical.
- Details: [2026-10-24-group-course-file-formats](logs/2026-10-24-group-course-file-formats.md).


### Fix — TeX asset recursion and safe partial cloud delivery

- Fixed TeX/PDF validation so binary figure assets are copied without attempting UTF-8 decoding, and nested `\\input` dependencies are checked recursively.
- Added a real figure-bearing LaTeX scratch-compilation regression and fail-closed handling for dynamic `\\graphicspath` / bibliographies.
- Clarified that a generated file is not saved to Google Drive until a supported file-reference upload is verified; partial `.tex`/`.pdf` uploads are reported as incomplete.
- Details: [2026-10-24-tex-bundle-and-upload-validation](logs/2026-10-24-tex-bundle-and-upload-validation.md).


### econ-phd-professor — Treat same-basename TeX/PDF/Word as one logical source

- Files with matching stems in the same course folder are grouped as representations of a **single lecture** by default, avoiding inflated lecture counts and unnecessary confirmation.
- The Professor chooses the most reliable readable source (often TeX or Word), consulting PDF for diagrams and rendered notation as needed; material inconsistencies remain explicit.
- Added regression cases 35–37 and a Python contract test.
- Details: [2026-10-24-professor-multiformat-sources](logs/2026-10-24-professor-multiformat-sources.md).


### econ-phd-professor — Course recovery and reproducible-output hardening

- Distinguished lecture source roles (student handout PDF, presenter PDF and LaTeX), verified instructor revisions, and added private Course State JSON for source-version checks when resuming.
- Added Lecture ↔ Homework mapping, version annotations in course and lecture indexes, and explicit handling of untrusted operational instructions embedded in course files.
- Added a minimal Chinese `ctexart` template, a TeX asset/scratch-compile checker and Python contract tests to the GitHub Actions workflow.
- The first expanded CI run exposed a source-rule wording mismatch; fixed this and resource warnings. End-to-end Google Drive paired-file upload remains a separate acceptance test.
- Details: [2026-10-24-professor-recovery-hardening](logs/2026-10-24-professor-recovery-hardening.md).


### econ-phd-professor — Optional added charts, Homework integration and simple TeX/PDF default

- Relevant **original Slide figures can be used freely**; new illustrative charts are added **only when pedagogically needed**, with clear sourcing.
- Linked relevant Homework/Problem Sets to the lecture models and learning objectives, respecting the lecturer's notation and assignment AI-use rules.
- Added a minimal `article` LaTeX template and default **paired `.tex` + compiled `.pdf`** output for unspecified-format file requests; the verified cloud destination remains `Agent Outputs/`.
- Template compiled and rendered locally; course-specific paired cloud delivery remains untested.
- Details: [2026-10-24-professor-visuals-homework-texpdf](logs/2026-10-24-professor-visuals-homework-texpdf.md).


### Repository storage policy — Exact Agent Outputs folder

- Corrected the default cloud folder name from `outputs/` to **`Agent Outputs/`** for the Professor and future skills, with exact capitalization and spacing.
- Reused the existing Econs 509 `Agent Outputs` folder and moved the prior Course Map there; verified the Google Drive file parent.
- Introduced repository-wide [STORAGE_POLICY.md](STORAGE_POLICY.md), updated teaching/reference/templates, and added a regression case for coexistence with legacy `outputs`.
- Prior dated change logs remain historical records; this change supersedes their older output-folder convention.
- Details: [2026-10-24-agent-outputs-convention](logs/2026-10-24-agent-outputs-convention.md).


### econ-phd-professor — Cloud sources and mandatory cloud outputs

- Defined connected cloud drive (Google Drive when available) as the source of course Slides and supporting files.
- Required generated files to be saved to the **exact `outputs/` folder** of the verified active course workspace, with file metadata/read-back verification and a cloud link.
- Added safe destination resolution, naming/versioning and permission-failure behavior, with manual acceptance tests; kept private material out of the public GitHub repository.
- Details: [2026-10-24-professor-cloud-outputs](logs/2026-10-24-professor-cloud-outputs.md).


### econ-phd-professor — Add whole-course navigation and large-file handling

- Added syllabus-aware onboarding, separate instructor and prerequisite orders, lecture-level indexing, scoped notation registry and honest DISCOVERED / INDEXED / REVIEWED / BLOCKED coverage.
- Added bounded ingestion and source-reopening strategy for large courses, PDFs, TeX dependencies and missing graphics.
- Created private-workspace course map, lecture index and notation templates; expanded manual regression cases for course sequencing, revisions, scale and notation conflicts.
- No lecture/course data were committed to this public repository.
- Details: [2026-10-24-professor-course-navigation](logs/2026-10-24-professor-course-navigation.md).


### econ-phd-professor — Manual smoke test on a dynamic-programming lecture

- Tested expert economic interpretation, mathematical reasoning, notation fidelity, borrowing-limit constraints, and appropriate handling of unavailable visual assets.
- Sample explanations passed **self-review**, but this was not an independently evaluated or installed-host Skill run; six linked PDF figures were missing.
- No teaching instructions changed. Detailed limitations and future tests are recorded.
- Details: [2026-10-24-professor-dldp-smoke-test](logs/2026-10-24-professor-dldp-smoke-test.md).


### Repository maintenance — Add change logging

- Added repository-level agent instructions for documenting meaningful changes.
- Introduced dated detailed logs, a reusable log template and this summary file.
- Updated the README to direct future contributors to the logging workflow.
- Details: [2026-10-24-logging-system](logs/2026-10-24-logging-system.md).

### econ-phd-professor — Initial v0.1 implementation

- Introduced one adaptive Professor Skill for macroeconomics, microeconomics and econometrics.
- Required faithful preservation of lecture-slide notation and explicit separation of lecture claims from supplementary explanations.
- Added expert teaching, mathematical reasoning, domain references, a hypothetical Bellman teaching example, manual evaluation cases and structural validation.
- Initial commits: [catalog](https://github.com/ningzhanglab/Econ-Agent-Skills/commit/0fcce9cef2b955cf418f1b7704dce9b4ee27db62) and [Professor Skill](https://github.com/ningzhanglab/Econ-Agent-Skills/commit/30b089491cc552cf51844b8acabf1b4da5785f8c).
- Details: [2026-10-24-professor-v0.1](logs/2026-10-24-professor-v0.1.md).

## Logging policy

Add a dated record and update this document for meaningful edits to a Skill, its supporting materials or repository workflows. Use [the template](logs/TEMPLATE.md), and follow [AGENTS.md](AGENTS.md). Do not mistake automated structure checks for pedagogical validation.
