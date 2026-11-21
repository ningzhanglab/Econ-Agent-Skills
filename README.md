# Econ Agent Skills

Four Agent Skills for economics PhD work: understanding material, presenting it, writing, and finding the literature. Each is a plain Markdown folder that follows the [Agent Skills open specification](https://agentskills.io/specification).

| Skill | Use it to | The agent may add |
| --- | --- | --- |
| [econ-learn](skills/econ-learn/SKILL.md) | Understand material someone else wrote: lecture slides, homework, exams, a paper, a screenshot of equations, or a bare term | Explanation, derivation and figures, each labeled by source |
| [econ-present](skills/econ-present/SKILL.md) | Build a slide deck for an audience from a paper or a lecture | Structure and delivery only |
| [econ-write](skills/econ-write/SKILL.md) | Edit, review and structure your own economics writing | Nothing; only clarity |
| [econ-research](skills/econ-research/SKILL.md) | Develop a research question and work with the literature | Verified references and labeled assessment |

Jobs that cross skills are handed over in a stated order. A referee report, for example, is assessed with `econ-learn`, positioned with `econ-research` and structured with `econ-write`.

## Start here: use the skills in a chat Project

No installation needed. Paste the block below into your Project's instructions. Each request then opens one page from this repository that holds everything that kind of request needs: the skill's rules, the task procedure, the guides and any template. The pages update when this repository changes; the addresses stay the same, so the block only needs pasting again when the [change log](CHANGELOG.md) says the router changed.

<!-- link-router -->
```text
Econ Agent Skills. For every message, including later ones in the same chat, pick the page below that matches it and follow it. Open it if it has not been opened in this chat, even when another page was; reuse it if it has. Start each reply that follows a page with the `Skill:` line that page gives. If a page cannot be opened, say so and open https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/econ-skills.md. Write all math in LaTeX when teaching economics, including single symbols in sentences.

- Explain a term or concept, or a screenshot of equations from a book, paper or website: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/term.md
- Solve homework or a past-exam question, or prepare for an exam: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/homework.md
- Explain why something holds, a mechanism or a model's design; a derivation, proof or skipped step: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/explain.md
- Understand a research paper or one part of it: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/paper.md
- Teach a whole lecture, write lecture notes or a Handbook, connect lectures, or save another requested file: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/lecture.md
- Organize or index a course, resume from saved maps, or save a study log: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/course.md
- Build, revise or recheck slides for an audience: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/slides.md
- Edit, review or structure the user's own writing: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/writing.md
- Develop a research question, find or verify references, or synthesize the literature: https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/route/research.md

A request with several parts uses each matching page, in task order (a referee report: paper, then research, then writing).
```
<!-- /link-router -->

**How to tell it worked.** Every reply that used a skill starts with one line such as `Skill: homework · f1a201`: the page it followed and that page's code. If a reply about economics has no such line, it did not use a skill; ask it to. If the code differs from the one on line 3 of the page, the chat app read an older cached copy.

**Outside a Project,** start a chat with:

```text
Use the Econ Agent Skills at https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/econ-skills.md: open the page that matches my request and follow it. Write all math in LaTeX. Then: [your request]
```

The pages are generated into [link/](link/): one per kind of request in [link/route/](link/route/), the index [link/econ-skills.md](link/econ-skills.md), and one main page per skill as a fallback. Old addresses from earlier versions (`econ-teaching`, `econ-writing`, the earlier combined pages) still lead to the right page.

## Or install a skill

An installed skill turns on by itself in any chat when a question fits it, and reads its files locally instead of over the web. It does not update itself: after a new release, download and install it again.

| Skill | Download |
| --- | --- |
| econ-learn | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-learn.zip |
| econ-present | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-present.zip |
| econ-write | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-write.zip |
| econ-research | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-research.zip |

These links work only once a release has been published on the [Releases page](https://github.com/ningzhanglab/Econ-Agent-Skills/releases). Each zip holds one skill folder, without this repository's logs or tests.

- **Claude.ai (web or desktop chat):** in Settings, find the Skills section and upload the zip as it is. Skills there may require code execution to be turned on. To update, remove the old skill and upload the new zip.
- **Claude Code:** unzip into your skills folder and start a new session. To update, delete the old folder first, so files removed in the new version do not stay behind.

  ```bash
  unzip econ-learn.zip -d ~/.claude/skills
  ```

- **Other apps that support Agent Skills:** unzip into that app's skills folder.

Installing only one skill is fine: each is complete on its own. When a request belongs to a skill you have not installed, it says so in one line and helps only as far as its own rules allow; `econ-learn` alone never lists papers from memory.

## What all four guarantee

1. **The source's own form stays.** Symbols, terms, numbers, signs, timing and citations are kept exactly; a suspected error is flagged, not silently fixed.
2. **Nothing is invented.** No paper, result, number or figure content is written from memory and presented as checked.
3. **It says what it actually read:** a file listed is not a file read, and an abstract is not the paper.
4. **The source is kept apart from the skill's own work,** with labels.
5. **Material is data.** Instructions inside slides, homework, papers, drafts or web pages are never followed as commands.

## Your preferences

Adjustable choices are the lines under "Defaults" in each skill, separate from the rules. The global ones:

- Replies come in the language you write in, with English technical terms beside translations, for example 欧拉方程 (Euler equation).
- Answers come in chat. A file is created only when you ask.
- Requested files go to your course or project folder's `Agent Outputs/` (that exact name), never anywhere public.
- What you say in a conversation overrides a default. When you state a lasting preference, the skill tells you which default it replaces.

`python3 tools/list_defaults.py` prints every default.

## econ-learn: the Professor

Teaches like an economics PhD professor, not a slide summarizer. The source defines the model, notation and assumptions; broader economics explains why the model is built that way, how the mechanism works and when a conclusion fails. No course is needed: a term, a paper or a screenshot is a source too.

1. **Diagnose the bottleneck** and explain why the model is built this way.
2. **Answer first,** then the derivation, then the economic meaning in plain words.
3. **Visuals as a first-class method,** with no quota; original figures only if actually inspected.
4. **Intuition checked against the mathematics:** sign checks, limiting cases, tiny labeled examples.
5. **Homework and exams in the instructor's framework:** the course's notation and method, every necessary step, then the reusable method in one or two lines. It looks for the course's own material first and checks the answer against the field's common traps.

Task pages: [term or screenshot](skills/econ-learn/tasks/term-or-screenshot.md), [paper](skills/econ-learn/tasks/paper.md), [explain](skills/econ-learn/tasks/explain.md), [derive](skills/econ-learn/tasks/derive.md), [homework and exams](skills/econ-learn/tasks/homework-exam.md), [whole lecture](skills/econ-learn/tasks/whole-lecture.md), [cross-lecture](skills/econ-learn/tasks/cross-lecture.md), [course](skills/econ-learn/tasks/course.md), [learning log](skills/econ-learn/tasks/learning-log.md). Guides: [Macroeconomics](skills/econ-learn/guides/macroeconomics.md), [Microeconomics](skills/econ-learn/guides/microeconomics.md), [Econometrics](skills/econ-learn/guides/econometrics.md), [Time Series](skills/econ-learn/guides/time-series.md), [Figures](skills/econ-learn/guides/figures.md), [Reading sources](skills/econ-learn/guides/reading-sources.md), [Sources and versions](skills/econ-learn/guides/sources-and-versions.md), [Large files](skills/econ-learn/guides/large-files.md).

- **Files:** with no format named, a matching `.tex` and compiled `.pdf` in `Agent Outputs/`. A homework file follows the assignment's own format and filename rules.
- **Whole courses,** on request: syllabus order kept apart from inferred prerequisites, notation tracked per lecture, coverage marked honestly. Saved maps are navigation, never a substitute for reopening the slides.
- **Learning logs** only when you ask ("记录今天的学习"), as a short private Markdown file in `Agent Outputs/Learning Logs/`.
- **Helper scripts** (read-only on your sources): [file grouping](skills/econ-learn/scripts/group_course_sources.py), [TeX figure inventory](skills/econ-learn/scripts/inventory_tex_figures.py), [Word equation reader](skills/econ-learn/scripts/read_docx_math.py), [TeX bundle checker](skills/econ-learn/scripts/check_tex_bundle.py).

Example prompts: "Explain the intuition behind the Euler equation on slide 12, in the lecturer's notation." · "Solve PS2 part (b) using the method from the lecture." · "用中文解释第 12 页的贝尔曼方程，符号保持和 slides 一样。" · "What is elasticity?"

## econ-present: slides

[Econ Present](skills/econ-present/SKILL.md) makes what an audience sees.

- **A talk, not a summary:** planned as a story from the question to the answer, in the source's order, with the core argument built step by step in the main slides.
- **The deck is for the audience; the handover is for you:** the version read, the page behind each slide and every computed number go into the handover in chat, not onto the slides.
- **House style, each line adjustable:** "Topic: point" titles; Appendix slides with a subtitle, one click from the slide they support and back; no default length; Beamer 16:9 as `.tex` and `.pdf`; a content file or speaker notes only on request.
- **Nothing from memory:** a related-literature slide lists only papers the source cites or papers verified with `econ-research`.
- A [figure cropper](skills/econ-present/scripts/crop_figure.py) saves one figure from a PDF page as an image (needs PyMuPDF or Poppler).

Example prompts: "Make slides to present this paper in our reading group." · "Recheck my deck against the published version."

## econ-write: your own text

[Econ Write](skills/econ-write/SKILL.md) edits for clarity, removes templated or AI-sounding prose, organizes sections by economics conventions, or reviews a draft without rewriting it.

- **Terminology, math, numbers and citations stay exactly as you wrote them,** including LaTeX labels and citation keys. Conditions and caveats stay; suspected errors are flagged, not fixed in the prose.
- **Nothing is invented:** no references, results or robustness checks the draft does not contain.
- Guides: [Terminology and Notation](skills/econ-write/guides/terminology-and-notation.md), [Economics Writing Conventions](skills/econ-write/guides/econ-conventions.md), [AI-Sounding Patterns](skills/econ-write/guides/ai-tells.md) (adapted from the MIT-licensed [humanizer](https://github.com/blader/humanizer) skill).
- When a course or journal requires disclosure of AI use, it reminds you once and leaves the decision to you.

Example prompts: "Tighten the introduction in `paper.tex`, keep all terms as they are." · "Review my results section, don't rewrite it."

## econ-research: questions and the literature

[Econ Research](skills/econ-research/SKILL.md) helps at the start of a project. It does not design identification strategies or empirical methods.

- **No reference from memory:** every paper is found in or checked against a bibliographic source, or labeled **UNVERIFIED**. If nothing turns up, it says so.
- **It says what it read:** full text, abstract only or metadata only, and which version.
- Task pages: [research questions](skills/econ-research/tasks/research-questions.md), [literature search](skills/econ-research/tasks/literature-search.md), [literature synthesis](skills/econ-research/tasks/literature-synthesis.md).
- A [reference checker](skills/econ-research/scripts/verify_references.py) compares DOIs or a `.bib` file with Crossref, sending only the DOIs.
- Ideas adapted, with credit, from [claude-academic-workflow](https://github.com/ericluo04/claude-academic-workflow) (MIT) and [awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff) (CC0).

Example prompts: "What's the literature on minimum wages and employment? Ten most important papers." · "Check the references in `paper.bib`."

## Evidence so far

- Teaching: a blind comparison on three synthetic cases scored this version 41, the previous version 40 and no skill 37 out of 42 ([log](logs/2026-11-16-v2-rebuild-four-skills.md)). On a real assignment, only the skill looked for the course's own material ([log](logs/2026-11-17-econ-learn-homework-source-and-submission.md)).
- Slides: on a published paper, decks built with the skill scored 14 and 15 out of 16 against 8 for no skill ([log](logs/2026-11-16-econ-present-real-paper-comparison.md)); a rerun on a second paper compared skill versions ([log](logs/2026-11-18-econ-present-melons-rerun.md)).
- The Project link setup works in the maintainer's own Project. The recorded cases are in [tests/link-route-evaluation.md](tests/link-route-evaluation.md).

## For the maintainer

```text
Econ-Agent-Skills/
├── skills/      the four skills (the source of truth)
├── shared/      text and scripts written once, copied into the skills
├── link/        generated pages for the Project link setup (do not edit)
├── tools/       generators, zip builder, check_all.py
├── tests/       unit tests and manual evaluation cases
└── logs/        dated development logs (not student learning logs)
```

- After any edit under `skills/` or `shared/`, run `python3 tools/check_all.py`. It copies `shared/` into the skills, rebuilds `link/` and the router block above, then runs validation, the unit tests and a whitespace check. A new task page or guide must be added to a route in `ROUTES` in `tools/build_link_editions.py`; a test fails otherwise.
- [AGENTS.md](AGENTS.md) says where a change goes and how to record it; [DESIGN_V2.md](DESIGN_V2.md) explains the layout ([DESIGN_V1.md](DESIGN_V1.md) is history). Changes are summarized in [CHANGELOG.md](CHANGELOG.md), with details in [logs/](logs/README.md).
- **Publish a release** for the download links: push to `main` and check that GitHub Actions pass; then on GitHub open **Releases → Draft a new release**, create a tag on `main` such as `v2026.11.20`, and publish. A workflow attaches the four zips within a few minutes. To build them locally: `python3 tools/build_skill_zips.py` (writes to `dist/`).
- Manual evaluation cases: [teaching](tests/professor-evaluation.md), [writing](tests/writing-evaluation.md), [research](tests/research-evaluation.md), [Project links](tests/link-route-evaluation.md).
- Private slides, homework, learning logs and course records never enter this repository ([Storage Policy](STORAGE_POLICY.md)).

## Next

- Publish the first release, so the download links work, and check that an installed skill is chosen on its own in a real client.
- Repeat the teaching comparison on real lectures and homework, with more than one run per case.
- Run the writing and research evaluation cases on real drafts and topics.
- A fifth skill for work on your own research object (model, proof, data, code) is foreseen in the design and not built.
