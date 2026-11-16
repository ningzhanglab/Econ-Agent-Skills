# Econ Agent Skills

Reusable, version-controlled Agent Skills for economics PhD learning and research.

> **Status:** v2 layout (2026-11-16), rebuilt from the v1 skills and not yet re-run on real lectures, drafts or decks. `econ-learn` (the Professor) carries the v1.1 teaching rules; `econ-present` holds the slide rules that used to sit inside it; `econ-write` and `econ-research` are v0.1 with the same rules as before. `econ-research` covers research questions and the literature; identification design and empirical methods are not included.
>
> **Renamed 2026-11-16:** `econ-teaching` is now `econ-learn`, `econ-writing` is now `econ-write`, and slides moved to the new `econ-present`. Reinstall each skill folder under its new name and use the new names in prompts. Old paste-a-link addresses lead to a page that points to the new one.

## Skills catalog

| Skill | Purpose | Status |
| --- | --- | --- |
| [econ-learn](skills/econ-learn/SKILL.md) | Understand material someone else wrote: your lecture slides, homework and exams, with exact notation, economic intuition, rigorous derivations and useful diagrams; or, with no course at all, a term, a paper or a screenshot of equations | **Rebuilt in v2 from v1.1; evaluation on real lectures to be re-run** |
| [econ-present](skills/econ-present/SKILL.md) | Build a slide deck for an audience from a paper (someone else's or your own) or a lecture: a talk planned as a story, the source's notation and numbers kept exactly, Appendix slides linked to the main slides | **New skill in v2, from the v1 slide rules; not yet re-run on a real deck** |
| [econ-write](skills/econ-write/SKILL.md) | Edit, review and structure your own economics writing (research papers, thesis chapters, referee and research reports, homework write-ups) while keeping every term, symbol, number and citation unchanged | **v0.1; not yet evaluated on real drafts** |
| [econ-research](skills/econ-research/SKILL.md) | Develop research questions and work with the literature: find, screen and verify papers, synthesize what is known, and position a project. No reference is written from memory | **v0.1 (questions and literature); not yet evaluated on real projects** |

The four skills differ in whose material it is and what the agent may add: explanation labeled by source (`econ-learn`), structure only (`econ-present`), nothing but clarity (`econ-write`), verified references and labeled assessment (`econ-research`). All four share the same five guarantees and the same global defaults, written once in [shared/](shared/) and copied into each skill.

## Share a skill

Each skill can be shared on its own. Send people only the skill they need.

| Skill | Download link (to install) |
| --- | --- |
| econ-learn | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-learn.zip |
| econ-present | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-present.zip |
| econ-write | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-write.zip |
| econ-research | https://github.com/ningzhanglab/Econ-Agent-Skills/releases/latest/download/econ-research.zip |

Each zip holds only that skill's folder: its `SKILL.md`, task and guide files, templates and scripts, without this repository's logs or tests. The links work once a release has been published (see [Publish a new version](#publish-a-new-version)).

### Install a downloaded skill

- **Claude.ai (web or desktop chat):** in Settings, find the Skills section and upload the zip as it is. Skills there may require code execution to be turned on.
- **Claude Code (terminal or the desktop app's Code tab):** unzip it into your skills folder, then start a new session:

  ```bash
  unzip econ-learn.zip -d ~/.claude/skills
  ```

  `econ-learn` writes math in LaTeX. A terminal shows it as code (`$\beta$`); if you prefer, ask it to write math as plain text.

- **Other apps that support Agent Skills:** unzip it into that app's skills folder.

Once installed, the skill turns on by itself when a question fits it, and it can read all its task and guide files. This is the most reliable way to use a skill.

**Installing only one skill is fine.** Each skill is complete on its own and never needs files from the others. When a request belongs to a skill you have not installed (for example, a literature search while only `econ-learn` is installed), it says so in one line, points to this README for installing the other skill, and helps only as far as its own rules allow; `econ-learn` on its own never lists papers, years or findings from memory.

### Try a skill without installing

In a chat that can open web pages, paste the line for the skill you want and replace `[your request]` with your question. Each line points to the skill's **link edition**: the same `SKILL.md`, with every reference file given as a full address the chat can open, an edition code, and an instruction to read the files the request needs and to list the ones it read.

econ-learn:

```text
Follow https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/econ-learn.md and open the files it names for my request. Start your answer with the edition code shown at the top of that page. If you cannot open the page or a file it names, say so and stop; do not answer from memory. Write all math in LaTeX, including single symbols in sentences. Then: [your request]
```

econ-present:

```text
Follow https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/econ-present.md and open the files it names for my request. Start your answer with the edition code shown at the top of that page. If you cannot open the page or a file it names, say so and stop; do not answer from memory. Then: [your request]
```

econ-write:

```text
Follow https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/econ-write.md and open the files it names for my request. Start your answer with the edition code shown at the top of that page. If you cannot open the page or a file it names, say so and stop; do not answer from memory. Then: [your request]
```

econ-research:

```text
Follow https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/econ-research.md and open the files it names for my request. Start your answer with the edition code shown at the top of that page. If you cannot open the page or a file it names, say so and stop; do not answer from memory. Then: [your request]
```

All four from one link: use this when you want one line for every request, for example in a chat project's instructions. The [index page](link/econ-skills.md) lists the four skills, and the agent opens the one or ones the request needs: to explain a paper and then place it in its literature, it opens both `econ-learn` and `econ-research`. This takes one more page to open than a single-skill line, so the separate lines above stay the most direct choice when you already know which skill you want.

```text
Follow https://raw.githubusercontent.com/ningzhanglab/Econ-Agent-Skills/main/link/econ-skills.md, open the skill page or pages it says my request needs, and open the files those pages name. Start your answer with the edition code of each skill page you opened. If you cannot open a page or a file it names, say so and stop; do not answer from memory. When teaching economics, write all math in LaTeX, including single symbols in sentences. Then: [your request]
```

Limits: it must be pasted again in every new chat, the chat app must be able to open GitHub links, and the agent may still skip a task or guide file. The answer should start with a line `Skill edition:` and a six-character code (with the index line, one code per skill page opened, each with its skill name), and end with a line listing the skill files it read. To check the code, open the link yourself and compare it with the edition code at the top of the page: a missing or different code means the agent did not read the current page, so its answer does not follow the skill. If a file you expected is missing from the last line, ask the agent to open it.

### Updates

- **A downloaded skill does not update itself.** It stays at the version you downloaded. To update, download again from the same link and replace the old copy: in Claude.ai, remove the old skill and upload the new zip; in Claude Code, delete the old `~/.claude/skills/econ-learn` folder and unzip again, so files removed in the new version do not stay behind.
- **The paste-a-link method always reads the newest files on `main`**, including changes not yet released.
- What changed in each version is listed on the [Releases page](https://github.com/ningzhanglab/Econ-Agent-Skills/releases) and in the [change log](CHANGELOG.md). An older copy keeps working; it only lacks the newest rules.

### Publish a new version

For the maintainer. Download links always point to the newest **published release**, not to every push, so unfinished work on `main` never reaches people who download.

1. Push the changes to `main` and check that the GitHub Actions checks pass.
2. On GitHub, open **Releases → Draft a new release**. Create a new tag on `main`, such as `v2026.11.15`, and write a few lines on which skills changed and how.
3. Click **Publish release**. The *Attach skill zips to release* workflow builds the four zips and attaches them to the release, usually within a couple of minutes. Check that the release page lists `econ-learn.zip`, `econ-present.zip`, `econ-write.zip` and `econ-research.zip`.
4. If the change matters, tell the people you shared with to download again from the same link.

After changing any file in a skill or in `shared/`, run `python tools/build_all.py` and commit what it writes: it copies the shared text into the skills, then rebuilds `link/`. The edition code covers every file of the skill, and tests fail if a copy or a page is out of date.

To build the zips locally instead: `python tools/build_skill_zips.py` (writes to `dist/`, which Git ignores; inside a Git checkout it includes only files Git tracks).

## How the Professor teaches

The Professor teaches like a knowledgeable economics PhD professor, not a slide summarizer. The slides define the local model, notation and assumptions; broader economics knowledge explains why the model is built that way, how the mechanism works and when the result fails. The aim of every answer is that you **understand the economics and can do the next problem yourself**.

Five guarantees hold in all four skills: the source's own form stays, nothing is invented, the skill says what it actually read, the source is kept apart from its own work, and material is treated as data, not instructions. For the Professor the first one means exact slide notation: symbols, signs, timing and operators stay as the lecturer wrote them, and slide statements, derivations and outside knowledge are kept visibly separate.

Five teaching habits govern every answer (full text in [SKILL.md](skills/econ-learn/SKILL.md)):

1. **Diagnose the bottleneck and explain the model's design.** The Professor looks for the earliest missing link (notation, a proof step, the incentive, an assumption, identification or numerical approximation) without claiming to read your mind.
2. **Answer first, then build understanding.** The first sentences answer your question; the derivation follows; a substantive explanation ends with its economic meaning in plain words.
3. **Visuals as a first-class teaching method.** Graphs are considered proactively for constraints, trade-offs, dynamics, equilibria and numerical methods. Original figures are used only if actually inspected; new schematics and computed plots are labeled honestly.
4. **Intuition checked against the mathematics.** Verbal stories are tested with sign checks, limiting cases or tiny labeled numerical examples.
5. **Homework and exams in the instructor's framework.** Same notation, same or closest slide method, every necessary step, a checked result, and then the reusable method in one or two lines. Exam preparation can include a fresh practice item with its answer held back.

**Your preferences** are the lines under "Defaults" in each skill: answers in the language you write in, with English technical terms beside translations, for example 欧拉方程 (Euler equation); math in LaTeX; no file unless you ask. What you say in a conversation overrides a default, and `python tools/list_defaults.py` prints every default in one view.

The Professor **routes the request before using tools**, opening one task page for it: quick step, intuition, derivation, model comparison, whole lecture, Homework or exam preparation. A narrow question never triggers a course inventory or a generated file. **No course is needed:** a term ("what is elasticity?"), a research paper or one part of it, or a screenshot of equations from anywhere is treated as the source, with the same notation rules; a bare term is answered from general economics knowledge and labeled as such.

**Reading a paper.** Send the PDF. The first answer is a short map: the question, the framework, the main result and why it holds, the one figure or table that carries the paper, and which sections to read or skim. The Professor then goes deeper only where you are stuck, most often on a method or model the paper assumes you know, and says what it actually read. If you only name a paper without sending it, it says the paper was not read, gives a short outline labeled as general knowledge (no numbers, equation numbers or pages) and asks for the PDF. See [Teaching Design](skills/econ-learn/tasks/explain.md), [Expert Teaching](skills/econ-learn/tasks/explain.md) and the [hypothetical diagnostic examples](skills/econ-learn/examples/diagnostic-teaching-patterns.md).

One Skill covers four fields through optional domain lenses: [Macroeconomics](skills/econ-learn/guides/macroeconomics.md) (including numerical methods), [Microeconomics](skills/econ-learn/guides/microeconomics.md), [Econometrics](skills/econ-learn/guides/econometrics.md) and [Time Series](skills/econ-learn/guides/time-series.md). Each lens lists the questions an expert asks, the high-value explanations and the common traps for that field; none is tied to a particular course.

## Getting started

1. Read [SKILL.md](skills/econ-learn/SKILL.md) to see the behavior and triggers.
2. Make the **entire skill folder** `skills/econ-learn/` available to a compatible Agent Skills client: download its zip (see [Share a skill](#share-a-skill)), or copy or link the folder from a clone of this repository into the client's skills directory. The folder is self-contained: its references, templates, examples and helper scripts all live inside it. A GitHub repository alone does **not** activate the skill.
3. For course questions, provide the actual lecture slides (PDF, PPT, TeX, screenshots) or an accessible course folder. The Professor must inspect the relevant material and never pretends to have read slides it cannot access. For a term, a paper or a screenshot from elsewhere, just send it.
4. Ask a question.

To use Econ Write, make `skills/econ-write/` available the same way; it needs no course folder, only the text or file you want edited. Econ Present installs from `skills/econ-present/` and needs the paper or lecture to present. Econ Research installs the same way from `skills/econ-research/`; its literature work needs web access.

To share one skill with someone else, see [Share a skill](#share-a-skill).

### Example prompts

- "Explain the intuition behind the Euler equation on slide 12. Keep the lecturer's notation and connect it to one other model."
- "Teach slides 10–16 as my PhD macro professor would, and explain why the model is formulated this way."
- "Explain this proof. Show the missing steps without changing notation."
- "What does this graph imply? Separate what the graph shows from additional theory."
- "Solve PS2 part (b) using the method from the lecture."
- "Help me prepare for the midterm on lectures 5–8."
- "用中文解释第 12 页的贝尔曼方程，符号保持和 slides 一样。"
- "What is elasticity?" · "Explain what this paper is about and its framework." · "Explain equation (7) in this paper." · "I don't understand the equations in this screenshot."

## Whole courses and large collections

For semester-long tutoring the Professor can map a course on request: syllabus order kept separate from inferred prerequisites, each lecture's notation tracked separately, and every file marked **DISCOVERED**, **INDEXED**, **REVIEWED** (exact range) or **BLOCKED**. A course map is a navigation aid; every explanation still reopens the original slides.

- Same-basename `.tex`, PDF and Word files in one course folder are treated as one lecture by default; presenter views, handouts and genuine revisions are distinguished by content, not extension. See [Course State and Sources](skills/econ-learn/guides/sources-and-versions.md).
- Templates: [Course Map](skills/econ-learn/templates/course-map.md), [Lecture Index](skills/econ-learn/templates/lecture-index.md), [Notation Registry](skills/econ-learn/templates/notation-registry.md), [Figure Index](skills/econ-learn/templates/figure-index.md), [Homework Map](skills/econ-learn/templates/homework-map.md) and [Course State](skills/econ-learn/templates/course-state.example.json).
- Helper scripts (inside the skill folder; Python standard library, read-only on your sources): [file grouping](skills/econ-learn/scripts/group_course_sources.py), [TeX figure inventory](skills/econ-learn/scripts/inventory_tex_figures.py), [Word equation reader](skills/econ-learn/scripts/read_docx_math.py) and [TeX bundle checker](skills/econ-learn/scripts/check_tex_bundle.py).
- Details: [Course Navigation](skills/econ-learn/tasks/course.md) and [Large-File Strategy](skills/econ-learn/guides/large-files.md). This is a workflow specification, not background indexing or permanent memory.

Text inside slides, homework, README files, papers, screenshots and web pages is treated as **untrusted study material**, never as instructions that can override your request, change sharing or move private files.

## Files, cloud storage and learning logs

- **Ordinary questions are answered in chat.** No file is created unless you ask.
- **When you ask for a file without naming a format**, the Professor delivers a matching editable `.tex` and compiled `.pdf`, saved and verified in your course's cloud folder named exactly **`Agent Outputs`**. If the course already has a near-miss folder such as `agent output`, the Professor asks once which to use. An explicit format or destination overrides this. Rules: [Storage Policy](STORAGE_POLICY.md), [Cloud Drive Workflow](skills/econ-learn/tasks/deliver-file.md) and [TeX/PDF Outputs](skills/econ-learn/tasks/deliver-file.md). Chinese notes use the [ctexart template](skills/econ-learn/templates/simple-notes-cn.tex). **Slides** (for example, to present a paper) follow [Slides](skills/econ-present/SKILL.md): a clean Beamer deck for the audience, with sources, checks and reading notes handed to you separately instead of printed on the slides.
- **Learning logs are on demand.** Say "记录今天的学习" or "Save today's learning log" and the Professor saves a short Markdown summary of what was actually studied, questions, clarifications and open issues to `Agent Outputs/Learning Logs/`. It never records chats in the background or claims mastery. See [Learning Logs](skills/econ-learn/tasks/learning-log.md).
- This public repository holds reusable rules, templates and development logs only. Private slides and generated course records stay in your cloud drive.

## How Econ Present builds a deck

[Econ Present](skills/econ-present/SKILL.md) makes what an audience sees. Its whole method is in one file, so nothing has to be looked up while building.

- **A talk, not a summary.** The deck is planned as a story from the question to the answer, in the source's order, with the core argument built step by step in the main slides.
- **The deck is for the audience; the handover is for you.** Which version was read, the page behind each slide and every computed number go into the handover in chat, not onto the slides.
- **House style, each line adjustable:** consecutive slides share one block title, Appendix slides carry a subtitle and are one click from the slide they support, no default length, Beamer 16:9 as `.tex` and `.pdf`, and a content file or speaker notes only on request.
- **Nothing from memory:** a related-literature slide lists only papers the source cites or papers verified with `econ-research`.

Example prompts: "Make slides to present this paper in our reading group." · "Recheck my deck against the published version." · "One-hour seminar version of this deck."

## How Econ Write edits

[Econ Write](skills/econ-write/SKILL.md) is a separate skill for text you write yourself, in English. It edits for clarity, removes templated or AI-sounding prose, organizes sections by economics conventions, or reviews a draft without rewriting it.

- **Terminology is fixed.** It first collects your defined terms, field terms, model and estimator names and acronyms, then uses each exactly as you do. It never swaps in synonyms, and it flags a term used two ways instead of choosing for you. See [Terminology and Notation](skills/econ-write/guides/terminology-and-notation.md).
- **Math, numbers and citations are untouched**, including LaTeX labels and citation keys. Conditions and caveats stay, and causal language is flagged, not silently changed.
- **Nothing is invented:** no references, results or robustness checks the draft does not contain.
- Conventions for papers, theses, referee reports and homework write-ups are in [Economics Writing Conventions](skills/econ-write/guides/econ-conventions.md); the prose patterns, adapted from the MIT-licensed [humanizer](https://github.com/blader/humanizer) skill, are in [AI-Sounding Patterns](skills/econ-write/guides/ai-tells.md).
- Course and journal rules on AI assistance still apply; the skill is for clarity, not for hiding assistance.

Example prompts: "Tighten the introduction in `paper.tex`, keep all terms as they are." · "Review my results section, don't rewrite it." · "Help me structure a referee report from these notes."

## How Econ Research works

[Econ Research](skills/econ-research/SKILL.md) helps at the start of a project: turning an interest into an answerable question, and finding out what is already known.

- **No reference from memory.** Every paper is found in or checked against a bibliographic source (Crossref, OpenAlex, Semantic Scholar, RePEc, NBER, SSRN, a journal page or your library), or labeled **UNVERIFIED**. If nothing turns up, it says so.
- **It says what it read:** full text, abstract only or metadata only, and which version. What a paper reports is kept separate from its own assessment and from proposed gaps.
- **Research questions** are tested for contribution, closest papers, identification, feasibility and audience. See [Research Questions](skills/econ-research/tasks/research-questions.md).
- **Literature** work covers search across sources, screening, verification and a reading-list format ([Literature Search](skills/econ-research/tasks/literature-search.md)), then agreement, splits, gaps and positioning ([Literature Synthesis](skills/econ-research/tasks/literature-synthesis.md)).
- A standard-library [reference checker](skills/econ-research/scripts/verify_references.py) compares DOIs or a `.bib` file with Crossref and reports PASS, WARN, FAIL, SKIP or ERROR (lookup failed, entry unchecked). It sends only DOIs, with no personal details.
- Ideas are adapted, with credit, from [claude-academic-workflow](https://github.com/ericluo04/claude-academic-workflow) (MIT) and [awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff) (CC0).

Example prompts: "What's the literature on minimum wages and employment? Ten most important papers." · "I'm interested in housing and inequality; help me find a second-year paper topic." · "Has anyone used this design before?" · "Check the references in `paper.bib`."

## Repo layout

```text
Econ-Agent-Skills/
├── README.md, AGENTS.md, DESIGN_V2.md, STORAGE_POLICY.md, CHANGELOG.md
├── shared/                                # written once, copied into the skills by tools/sync_shared.py
│   ├── guarantees.md                      # the five guarantees every skill opens with
│   ├── defaults.md                        # the global defaults (language, chat first, where files go)
│   ├── deliver-file.md                    # TeX/PDF, `Agent Outputs/`, compile and upload checks
│   └── scripts/check_tex_bundle.py
├── skills/
│   ├── econ-learn/
│   │   ├── SKILL.md                       # guarantees, teaching habits, defaults, routing table
│   │   ├── tasks/                         # one page per kind of request
│   │   │   ├── term-or-screenshot.md, paper.md, explain.md, derive.md
│   │   │   ├── homework-exam.md, whole-lecture.md, cross-lecture.md
│   │   │   ├── course.md, learning-log.md
│   │   │   └── deliver-file.md            # copy of shared/deliver-file.md
│   │   ├── guides/                        # opened when they apply
│   │   │   ├── macroeconomics.md, microeconomics.md, econometrics.md, time-series.md
│   │   │   ├── figures.md, reading-sources.md
│   │   │   └── sources-and-versions.md, large-files.md
│   │   ├── examples/                      # four worked answers
│   │   ├── scripts/                       # read-only helpers for TeX, Word and course files
│   │   └── templates/                     # course map, indexes, learning log, notes templates
│   ├── econ-present/
│   │   ├── SKILL.md                       # the whole deck method in one file
│   │   ├── tasks/deliver-file.md          # copy of shared/deliver-file.md
│   │   ├── scripts/check_tex_bundle.py    # copy of the shared checker
│   │   └── templates/simple-slides.tex
│   ├── econ-research/
│   │   ├── SKILL.md
│   │   ├── tasks/                         # research-questions.md, literature-search.md, literature-synthesis.md
│   │   └── scripts/verify_references.py
│   └── econ-write/
│       ├── SKILL.md
│       └── guides/                        # terminology-and-notation.md, econ-conventions.md, ai-tells.md
├── tests/                                 # structural tests and manual evaluation cases
├── logs/                                  # dated development logs (not student learning logs)
├── link/                                  # generated link editions, the index, and redirects for old names (do not edit)
├── tools/
│   ├── build_all.py                       # runs the two generators below, in order
│   ├── sync_shared.py                     # copies shared/ into the skills
│   ├── build_link_editions.py             # rebuilds link/ from the skills
│   ├── build_skill_zips.py                # builds one installable zip per skill
│   └── list_defaults.py                   # prints every Defaults section
└── .github/workflows/
    ├── validate-skills.yml               # checks on every push
    └── release-skills.yml                # attaches skill zips to each published release
```

## Change history, contributing and testing

- [CHANGELOG.md](CHANGELOG.md) summarizes changes; [logs/](logs/README.md) explains what changed, why and how it was verified. [AGENTS.md](AGENTS.md) tells repository-editing Agents to update both. The [v2 design](DESIGN_V2.md) records the current architecture, and the [v1 design baseline](DESIGN_V1.md) is kept as history.
- Treat teaching decisions as testable behavior. When a real lecture interaction exposes a failure, add a case to the [professor evaluation cases](tests/professor-evaluation.md), the [writing evaluation cases](tests/writing-evaluation.md) or the [research evaluation cases](tests/research-evaluation.md) and fix the responsible reference rather than growing SKILL.md.
- GitHub Actions runs link validation, repository contract tests and a LaTeX compile smoke test. It also checks that every skill is self-contained (no link or plain-text pointer to a file outside its folder, such as `STORAGE_POLICY.md`) and tests the zip builder. These **structural tests do not prove teaching quality**; human evaluation on real lecture slides remains necessary.

## Roadmap

- **First, after the v2 rebuild:** run a fixed set of cases (a term, a derivation, a Homework problem, a paper, a deck) with v2, with the last v1 commit and with no skill at all, and compare. Until then v2 is untested on real material.
- **v1.1 evidence (before the rebuild):** cases 45–51 passed on real lectures in three courses: macro ([ECONS 509](logs/2026-10-29-professor-econs509-se-lecture-test.md)), econometrics and time series ([ECONS 512, STAT 516](logs/2026-10-29-professor-econs512-stat516-tests.md)), including homework solved in the lecture's method and a real past exam. Still to do: a microeconomics lecture and an independent grader.
- **Econ Learn outside a course:** run evaluation cases 57–60 (a bare term, a paper overview, one equation in a paper, a screenshot from an unknown source) on real material.
- **Sharing:** publish the first release so the download links work, then upload one zip to Claude.ai to confirm the install steps.
- **Econ Write:** run the [writing evaluation cases](tests/writing-evaluation.md) on real drafts (a paper section, a LaTeX file, a referee report and a homework write-up) before calling it stable.
- **Econ Research:** run the [research evaluation cases](tests/research-evaluation.md) on real topics. A later version may add identification design and empirical methods, if real use shows the need.
- **Optional:** installer guidance for specific Agent clients.

## Standard

The skills follow the [Agent Skills open specification](https://agentskills.io/specification). Platform-specific metadata in `agents/openai.yaml` is optional and does not change the portable `SKILL.md` format.
