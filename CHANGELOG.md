# Change Log

A short, chronological summary of meaningful changes to the Econ Agent Skills repository. Newest changes appear first. Detailed records explain rationale and validation in [logs/](logs/README.md). Exact diffs and commit history are preserved by Git.

## Unreleased

_No uncommitted planned changes are represented as completed here._

## 2026-11-15

_Chat LaTeX rule, wording now in force after the entries below: "Ordinary questions are answered in chat, with all math in LaTeX from the first answer, even a single symbol in a sentence; no file is created." (`SKILL.md`, Supporting duties). The entries on the separate rule line, delimiters, money and code describe wording that was later removed._

### Econ Teaching — Worked examples for microeconomics and econometrics

- **Added** two model answers beside the Bellman (macro) example: a quick micro question about one sign in the Slutsky equation, and an econometrics Homework on omitted variable bias solved by the slide's method, with the reusable method named at the end. Both are hypothetical and write all math in LaTeX. `SKILL.md` lists the three examples by field and mode.
- Not reviewed by a second economist and not tried in a real chat.
- Details: [2026-11-15 — Micro and econometrics examples](logs/2026-11-15-micro-and-econometrics-examples.md).

### All skills — Edition code and stronger paste prompts

- **Added** an edition code at the top of each link edition, a six-character hash of every file in the skill. The paste prompts now ask the agent to start its answer with that code, and to say so and stop if it cannot open the page or a file, instead of answering from memory. The `econ-teaching` prompt also asks for all math in LaTeX. A missing or wrong code shows the page was not read.
- For maintainers: the link editions must now be rebuilt after a change to any file of a skill, not only `SKILL.md`; a test fails otherwise. One new test covers the code.
- Not yet tried in a real chat.
- Details: [2026-11-15 — Edition code and paste prompts](logs/2026-11-15-edition-code-and-paste-prompts.md).

### Econ Teaching and README — Cleanup after the LaTeX-rule iterations

- **Fixed** four places that still described removed wording: the README install note, line 3 of the Bellman example, and two logs that now carry appended corrections; a line at the top of this date's section quotes the wording in force.
- **Removed** four sentences addressed to maintainers from run-time references (`cloud-drive-workflow.md`, `course-state-and-sources.md`, `time-series.md`, `latex-outputs.md`). No rule changed.
- Details: [2026-11-15 — Cleanup after the LaTeX-rule iterations](logs/2026-11-15-cleanup-after-latex-iterations.md).

### Econ Teaching — Duplicated rules merged to one home each

- **Changed:** rules that were restated in three to five files now have one full statement and short pointers elsewhere: the language rule, answer-first and the other learning habits, when to use a figure, instructions inside course files, no file for an ordinary chat, the `.tex`/`.pdf` default, the `Agent Outputs/` destination, same-stem grouping and Learning Log saving. No rule was added or removed.
- `teaching-design.md` loses its third checklist ("Lightweight editorial quality check"); its two questions not covered elsewhere moved into the Teaching arc. `SKILL.md` and the references are about 4% shorter (17,469 to 16,783 words). Link edition rebuilt.
- Not tested in a real chat; no behavior change is intended.
- Details: [2026-11-15 — Duplicated rules merged](logs/2026-11-15-teaching-duplicate-rules-merged.md).

### Econ Teaching — Reference files write their own symbols in LaTeX

- **Fixed:** after a full read of the skill's references, three of them were found to name symbols in sentences as plain text or Unicode (`a_t`, `\beta versus \delta`, `β/(1−β)`), the same pattern seen in agents' answers (whether they copied it is not shown). `slide-fidelity.md`, `mathematical-reasoning.md` and `macroeconomics.md` now use `$...$` on those seven lines; every symbol is unchanged. No rule was added and `SKILL.md` is untouched.
- The earlier repository-wide check had fixed only the Bellman example. A general trim of `SKILL.md` was considered and dropped.
- Details: [2026-11-15 — LaTeX in reference examples](logs/2026-11-15-latex-in-reference-examples.md).

### Econ Teaching — LaTeX for notation in sentences too

- **Fixed:** agents wrote displayed equations in LaTeX but named symbols inside sentences in plain text ("the discount factor beta", "k_t"), reading "math" as equations only. The Supporting duties phrase now reads "with all math in LaTeX from the first answer, even a single symbol in a sentence; no file is created." Evaluation case 59 checks it. Link edition rebuilt.
- Root cause noted: the skill mentioned LaTeX only next to the `.tex`/`.pdf` file default, so agents took LaTeX to mean "making a PDF". The chat requirement sits in that same sentence to undo the link where it formed; `references/latex-outputs.md` is unchanged because agents open it only when a file is requested.
- Details: [2026-11-15 — LaTeX for inline notation](logs/2026-11-15-latex-inline-notation.md).

### Econ Teaching — Chat LaTeX rule reduced to one phrase

- **Removed** the separate "Math in chat is LaTeX" line (about 70 words: delimiters, money, code, when to switch to plain text). The requirement now lives only in the Supporting duties line the agent actually quoted when it skipped LaTeX: "Ordinary questions are answered in chat, with math written in LaTeX from the first answer; no file is created." Delimiters, dollar signs and rendering are left to the agent and app, which handle them well; the student can ask for another format.
- The failure was caused by the skill itself (LaTeX was mentioned only for files), so the fix is to remove that bias, not to add a formatting regime. The Bellman example keeps LaTeX, evaluation case 59 still checks LaTeX in the first answer and lecturer macros, and case 57 drops its price condition. Link edition rebuilt. If a retest still shows plain text, a separate line can come back.
- Details: [2026-11-15 — Chat LaTeX rule reduced](logs/2026-11-15-latex-rule-reduced.md).

### Econ Teaching — LaTeX rule checked across the repository

- **Fixed:** the Bellman style example, the one "good Professor response" the skill shows, wrote inline math as bare `\beta E[...]` and displays as `\[...\]`, the opposite of the new rule. It now uses `$...$` and `$$...$$`; every symbol is unchanged.
- **Added** to the LaTeX rule: write money as `\$10` or USD 10, because a bare dollar sign in an economics answer (`from $10 to $12`) is read as a math delimiter and garbles the line; keep code (SAS, Python, Stata) as code. Evaluation case 57 checks prices in the elasticity example.
- README: a line under the Claude Code install step saying a terminal shows LaTeX as code and how to switch to plain text.
- Checked and left alone: `econ-writing` (keeps the writer's own form, so no LaTeX rule) and `econ-research` (little math). Link edition rebuilt.
- Details: [2026-11-15 — LaTeX rule checked across the repository](logs/2026-11-15-latex-rule-global-check.md).

### Econ Teaching — Make the LaTeX rule hard to miss

- **Fixed:** in a real test, an agent read the skill page and still wrote chat math as plain text, saying the page only asks for LaTeX in requested `.tex`/`.pdf` files and that "ordinary questions are answered in chat". The rule was buried in the middle of principle 1, and the line the agent quoted pointed the other way.
- The rule now stands on its own line at the top of "How to teach" (**Math in chat is LaTeX**), and the Supporting duties line reads "Ordinary questions are answered in chat, with math in LaTeX; no file is created." Same rule, same plain-text exception; principle 1 no longer carries it. Link edition rebuilt. The README paste prompts are unchanged.
- Details: [2026-11-15 — LaTeX rule made prominent](logs/2026-11-15-latex-rule-prominent.md).

### Econ Teaching — LaTeX math in chat answers

- **Added** to principle 1 in `SKILL.md`: in chat, write math in LaTeX by default (`$...$` inline, `$$...$$` displayed), including in the first answer, and write a lecturer's own macros out as their source defines them; switch to plain text only if the student asks or says the math shows as code. Before this, LaTeX was mentioned only for requested files, and one agent explained its plain-text equations by that. The agent no longer tries to judge whether the app renders math.
- Evaluation case 59 gains a pass condition (LaTeX in the first answer) and a variant (an author's own macro written out as defined). Link edition `link/econ-teaching.md` rebuilt. Not yet run in a real chat.
- Details: [2026-11-15 — LaTeX math in chat](logs/2026-11-15-latex-math-in-chat.md).

### All skills — Link editions for the paste-a-link method

- **Fixed:** agents that were given a `SKILL.md` link often did not read the reference files, where most rules live. `SKILL.md` links them by relative path, and many chat apps only open addresses that appear word for word in a page already read, so the agent could not open them or did not try.
- **Added** a generated link edition per skill, `link/<skill>.md`: the same `SKILL.md` with every reference written as a full address, a short note telling the agent to open the files the request needs, to say which file could not be opened and to end with a line listing the files it read, and an index of every file in the skill.
- **Added** [tools/build_link_editions.py](tools/build_link_editions.py) (with `--check`) and five tests in `tests/test_link_editions.py`; one fails when `link/` is out of date with the skills.
- README: the paste-a-link prompts now point to the link editions. Skill folders are unchanged and still contain no repository address; installed and zipped skills are not affected.
- Not yet tried in a real chat app.
- Details: [2026-11-15 — Link editions](logs/2026-11-15-link-editions-for-paste-a-link.md).

## 2026-11-14

### Documentation — README brought up to date

- README now describes the paper-reading behavior (a short map first, then depth where the student is stuck; a paper only named, not sent, gets a labeled outline and a request for the PDF), that installing a single skill is fine and what happens when a request needs one that is not installed, the wider untrusted-content list (papers, screenshots, web pages), the self-containment checks in CI, and two roadmap items (run cases 57–60; publish the first release). Getting started points to the zip download. The paste-a-link prompts are shorter. No skill behavior changed.
- Details: [2026-11-14 — README update](logs/2026-11-14-readme-sync.md).

### All skills — Fixes from a review of today's changes

- **Fixed (teaching):** a paper the student only names, with no file to open, is no longer summarized in detail from memory. The Professor says it was not read, gives a short outline labeled as general knowledge with no magnitudes, equation numbers or page references, and asks for the PDF.
- **Changed (teaching):** in the paper overview, the link to a standard model is optional, the magnitude is given where there is one, and "why it holds" is included; two duplicated rules were removed; when a lecture and a paper are both in use, the one being asked about sets the notation. The description now says "a published research paper the student is reading". Evaluation case 58 was aligned and gains a variant. Not yet run.
- **Changed (all skills):** when a request belongs to a skill that is not installed, the skill now says so in one line and helps only as far as its own rules allow, instead of declining. `econ-teaching` adds: without `econ-research`, never list papers, years or findings from memory.
- **Fixed (tooling):** `tests/validate_skills.py` now fails when any file in a skill names a repository-only file such as `STORAGE_POLICY.md`, in a link or in plain text (the earlier link check could not catch the original bug), and checks more link forms. `tools/build_skill_zips.py` zips only Git-tracked files inside a checkout, so an untracked private file cannot reach a local build. Six tests added.
- README: update instruction for Claude Code corrected (delete the old folder, then unzip); two notes added.
- Details: [2026-11-14 — Review fixes](logs/2026-11-14-review-fixes-papers-and-tooling.md).

### All skills — Self-contained skill folders

- **Fixed** the one place a skill pointed outside its own folder: `econ-writing` told the agent to follow the repository's root `STORAGE_POLICY.md`, which a zipped or installed skill does not contain; the rule it needs is now stated inline. `econ-teaching`'s cloud workflow no longer mentions the root policy file.
- **Added** to each skill's existing scope line: if the skill a request needs is not installed, say so and do not do its job without its rules (for example, a literature question asked of `econ-teaching` alone).
- **Removed** the link note added to the top of each `SKILL.md` earlier today. It hard-coded this repository's GitHub address into every skill and was read on every use, although only people pasting a link need it. The folder address now sits in each skill's paste-a-link prompt in the README instead.
- **Considered and dropped:** a rule telling agents not to read the repository's logs, tests or other skills, to save tokens. An installed or zipped skill does not contain those files, so the rule saved little and cost tokens on every use; the routing tables already say to load only the references a task needs.
- `tests/validate_skills.py` now fails if any link in a skill's Markdown leaves its folder, which keeps the zips self-contained; two regression tests added.
- Details: [2026-11-14 — Self-contained skill folders](logs/2026-11-14-self-contained-skills.md).

### All skills — Share one skill at a time

- **Added** one download link per skill: publishing a GitHub release now runs a workflow that builds `econ-teaching.zip`, `econ-writing.zip` and `econ-research.zip` and attaches them to the release, so `releases/latest/download/<skill>.zip` always gives the newest released version. Each zip holds only that skill's folder, ready to upload to Claude.ai or unzip into a skills folder. Downloads do not update themselves; people re-download from the same link.
- **Added** [tools/build_skill_zips.py](tools/build_skill_zips.py), the standard-library zip builder the workflow uses (skips `.DS_Store`, `__pycache__` and LaTeX build files; reproducible output), with five unit tests in `tests/test_skill_zips.py`.
- **Added** a short note at the top of each `SKILL.md` giving the raw GitHub folder for its linked files, so a skill can also be tried by pasting its `SKILL.md` link into a chat. (Removed later the same day; see Self-contained skill folders above.)
- README: new "Share a skill" section near the top with the download links, how to install a zip in Claude.ai and Claude Code, the paste-a-link prompt, how updates work, and how to publish a new version. The repo-layout tree is corrected (`econ-teaching` was drawn as the last folder under `skills/`) and lists the new tool and workflow.
- Details: [2026-11-14 — Share one skill at a time](logs/2026-11-14-share-skills-per-skill.md).

### Econ Teaching — Questions outside a course

- **Added** a mode for questions with no course behind them: a bare term ("what is elasticity?"), a research paper (what it is about and its framework, or one section or equation), a screenshot of equations from a book, paper or website, or a small step the student could not follow. Whatever the student sends is the source; the Professor does not search for a course folder or ask for slides unless the student points to a course.
- A bare term is answered briefly from general economics knowledge and labeled so, with notation presented as a convention and no papers cited from memory. A paper keeps its own notation and is cited by section, equation number and page, with the version read stated. A screenshot keeps its exact symbols; the Professor does not guess its source, labels any assumed reading of an off-screen symbol, and names unreadable parts.
- **Reading a paper: orient, then unblock.** The first answer about a paper is a short map (question, claimed contribution, framework, main result, the one exhibit that carries the paper, and which sections to read or skim), not a full walkthrough. Depth follows where the student is stuck, diagnosed with the existing bottleneck table; the most common block is a method, model family or term the paper assumes the reader knows. It closes with the contribution in one plain sentence and, if useful, a reusable reading lesson. Critique only when the purpose calls for it.
- Where it lives: a new "Questions outside a course" section in Teaching Design, a "Papers and screenshots" section in Slide Fidelity, and a mode line, a routing row and a broader description in `SKILL.md`. `econ-research` now points close reading of one paper to `econ-teaching`. The skill name is unchanged.
- Evaluation cases 57–60 added. Not yet run.
- **Corrections after review (same day):** a term asked while a lecture, paper or screenshot is in use is answered in that source's definition and notation first, not from general knowledge; papers, screenshots and web pages are now listed as untrusted content; standard concept names (the Lucas critique) are allowed while exact papers, years and findings still need checking; a small confusion gets one justified step instead of a fixed one-or-two-sentence limit; the mode list in `SKILL.md` gains (h). Case 57 gets a mid-course variant.
- Details: [2026-11-14 — Questions outside a course](logs/2026-11-14-teaching-questions-outside-a-course.md).

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
