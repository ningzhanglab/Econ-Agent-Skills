# Econ Agent Skills

Reusable, version-controlled Agent Skills for economics PhD learning and research.

> **Status:** `econ-teaching` (the Professor) v1.1, the teaching revision of the v1 design baseline. `econ-writing` v0.1, not yet evaluated on real drafts. `econ-research` v0.1 covers research questions and the literature; identification design and empirical methods are not yet included.
>
> **Renamed 2026-11-12:** `econ-phd-professor` is now `econ-teaching`, and the planned `econ-research-agent` is now `econ-research`. Reinstall the skill folder under its new name and use `$econ-teaching` in prompts that named the old one.

## Skills catalog

| Skill | Purpose | Status |
| --- | --- | --- |
| [econ-teaching](skills/econ-teaching/SKILL.md) | Learn graduate economics from your own lecture slides, homework and exams, with exact notation, economic intuition, rigorous derivations and useful diagrams | **v1.1; quality evaluation ongoing** |
| [econ-writing](skills/econ-writing/SKILL.md) | Edit, review and structure your own economics writing (research papers, thesis chapters, referee and research reports, homework write-ups) while keeping every term, symbol, number and citation unchanged | **v0.1; not yet evaluated on real drafts** |
| [econ-research](skills/econ-research/SKILL.md) | Develop research questions and work with the literature: find, screen and verify papers, synthesize what is known, and position a project. No reference is written from memory | **v0.1 (questions and literature); not yet evaluated on real projects** |

## How the Professor teaches

The Professor teaches like a knowledgeable economics PhD professor, not a slide summarizer. The slides define the local model, notation and assumptions; broader economics knowledge explains why the model is built that way, how the mechanism works and when the result fails. The aim of every answer is that you **understand the economics and can do the next problem yourself**.

Seven principles govern every answer (full text in [SKILL.md](skills/econ-teaching/SKILL.md)):

1. **Exact slide notation.** Symbols, signs, timing and operators stay exactly as the lecturer wrote them. Slide statements, derivations and outside knowledge are kept visibly separate.
2. **Diagnose the bottleneck and explain the model's design.** The Professor looks for the earliest missing link (notation, a proof step, the incentive, an assumption, identification or numerical approximation) without claiming to read your mind. For "why this model?" it explains what the model isolates, what it omits and what a nearby alternative would change. Each field has a short list of common PhD-level traps (for example an Euler equation at a binding borrowing limit, or a strong instrument mistaken for a valid one) that the Professor raises only when relevant.
3. **Answer first, then build understanding.** The first sentences answer your question; the derivation follows; a substantive explanation ends with its economic meaning in plain words.
4. **Visuals as a first-class teaching method.** Graphs are considered proactively for constraints, trade-offs, dynamics, equilibria and numerical methods. Original figures are used only if actually inspected; new schematics and computed plots are labeled honestly. No figure quota.
5. **Intuition checked against the mathematics.** Verbal stories are tested with sign checks, limiting cases or tiny labeled numerical examples.
6. **Homework and exams in the instructor's framework.** Same notation, same or closest slide method, every necessary step, a checked result, and then the reusable method in one or two lines. Exam preparation can include a fresh practice item with its answer held back. Course AI-use rules are respected.
7. **Your language.** Answers come in the language you write in, with symbols unchanged and English technical terms beside translations, for example 欧拉方程 (Euler equation).

The Professor chooses a **teaching mode before tools**: quick step, intuition, derivation, model comparison, whole lecture, Homework or exam preparation. A narrow question never triggers a course inventory or a generated file. See [Teaching Design](skills/econ-teaching/references/teaching-design.md), [Expert Teaching](skills/econ-teaching/references/expert-teaching.md) and the [hypothetical diagnostic examples](skills/econ-teaching/examples/diagnostic-teaching-patterns.md).

One Skill covers four fields through optional domain lenses: [Macroeconomics](skills/econ-teaching/references/macroeconomics.md) (including numerical methods), [Microeconomics](skills/econ-teaching/references/microeconomics.md), [Econometrics](skills/econ-teaching/references/econometrics.md) and [Time Series](skills/econ-teaching/references/time-series.md). Each lens lists the questions an expert asks, the high-value explanations and the common traps for that field; none is tied to a particular course.

## Getting started

1. Read [SKILL.md](skills/econ-teaching/SKILL.md) to see the behavior and triggers.
2. Make the **entire skill folder** `skills/econ-teaching/` available to a compatible Agent Skills client (install from this GitHub folder, or copy or link the folder into the client's skills directory). The folder is self-contained: its references, templates, examples and helper scripts all live inside it. A GitHub repository alone does **not** activate the skill.
3. Provide the actual lecture slides (PDF, PPT, TeX, screenshots) or an accessible course folder. The Professor must inspect the relevant material and never pretends to have read slides it cannot access.
4. Ask a question.

To use Econ Writing, make `skills/econ-writing/` available the same way; it needs no course folder, only the text or file you want edited. Econ Research installs the same way from `skills/econ-research/`; its literature work needs web access.

### Example prompts

- "Explain the intuition behind the Euler equation on slide 12. Keep the lecturer's notation and connect it to one other model."
- "Teach slides 10–16 as my PhD macro professor would, and explain why the model is formulated this way."
- "Explain this proof. Show the missing steps without changing notation."
- "What does this graph imply? Separate what the graph shows from additional theory."
- "Solve PS2 part (b) using the method from the lecture."
- "Help me prepare for the midterm on lectures 5–8."
- "用中文解释第 12 页的贝尔曼方程，符号保持和 slides 一样。"

## Whole courses and large collections

For semester-long tutoring the Professor can map a course on request: syllabus order kept separate from inferred prerequisites, each lecture's notation tracked separately, and every file marked **DISCOVERED**, **INDEXED**, **REVIEWED** (exact range) or **BLOCKED**. A course map is a navigation aid; every explanation still reopens the original slides.

- Same-basename `.tex`, PDF and Word files in one course folder are treated as one lecture by default; presenter views, handouts and genuine revisions are distinguished by content, not extension. See [Course State and Sources](skills/econ-teaching/references/course-state-and-sources.md).
- Templates: [Course Map](skills/econ-teaching/templates/course-map.md), [Lecture Index](skills/econ-teaching/templates/lecture-index.md), [Notation Registry](skills/econ-teaching/templates/notation-registry.md), [Figure Index](skills/econ-teaching/templates/figure-index.md), [Homework Map](skills/econ-teaching/templates/homework-map.md) and [Course State](skills/econ-teaching/templates/course-state.example.json).
- Helper scripts (inside the skill folder; Python standard library, read-only on your sources): [file grouping](skills/econ-teaching/scripts/group_course_sources.py), [TeX figure inventory](skills/econ-teaching/scripts/inventory_tex_figures.py) and [TeX bundle checker](skills/econ-teaching/scripts/check_tex_bundle.py).
- Details: [Course Navigation](skills/econ-teaching/references/course-navigation.md) and [Large-File Strategy](skills/econ-teaching/references/large-file-strategy.md). This is a workflow specification, not background indexing or permanent memory.

Text inside slides, homework and README files is treated as **untrusted study material**, never as instructions that can override your request, change sharing or move private files.

## Files, cloud storage and learning logs

- **Ordinary questions are answered in chat.** No file is created unless you ask.
- **When you ask for a file without naming a format**, the Professor delivers a matching editable `.tex` and compiled `.pdf`, saved and verified in your course's cloud folder named exactly **`Agent Outputs`**. An explicit format or destination overrides this. Rules: [Storage Policy](STORAGE_POLICY.md), [Cloud Drive Workflow](skills/econ-teaching/references/cloud-drive-workflow.md) and [TeX/PDF Outputs](skills/econ-teaching/references/latex-outputs.md). Chinese notes use the [ctexart template](skills/econ-teaching/templates/simple-notes-cn.tex).
- **Learning logs are on demand.** Say "记录今天的学习" or "Save today's learning log" and the Professor saves a short Markdown summary of what was actually studied, questions, clarifications and open issues to `Agent Outputs/Learning Logs/`. It never records chats in the background or claims mastery. See [Learning Logs](skills/econ-teaching/references/learning-log.md).
- This public repository holds reusable rules, templates and development logs only. Private slides and generated course records stay in your cloud drive.

## How Econ Writing edits

[Econ Writing](skills/econ-writing/SKILL.md) is a separate skill for text you write yourself, in English. It edits for clarity, removes templated or AI-sounding prose, organizes sections by economics conventions, or reviews a draft without rewriting it.

- **Terminology is fixed.** It first collects your defined terms, field terms, model and estimator names and acronyms, then uses each exactly as you do. It never swaps in synonyms, and it flags a term used two ways instead of choosing for you. See [Terminology and Notation](skills/econ-writing/references/terminology-and-notation.md).
- **Math, numbers and citations are untouched**, including LaTeX labels and citation keys. Conditions and caveats stay, and causal language is flagged, not silently changed.
- **Nothing is invented:** no references, results or robustness checks the draft does not contain.
- Conventions for papers, theses, referee reports and homework write-ups are in [Economics Writing Conventions](skills/econ-writing/references/econ-conventions.md); the prose patterns, adapted from the MIT-licensed [humanizer](https://github.com/blader/humanizer) skill, are in [AI-Sounding Patterns](skills/econ-writing/references/ai-tells.md).
- Course and journal rules on AI assistance still apply; the skill is for clarity, not for hiding assistance.

Example prompts: "Tighten the introduction in `paper.tex`, keep all terms as they are." · "Review my results section, don't rewrite it." · "Help me structure a referee report from these notes."

## How Econ Research works

[Econ Research](skills/econ-research/SKILL.md) helps at the start of a project: turning an interest into an answerable question, and finding out what is already known.

- **No reference from memory.** Every paper is found in or checked against a bibliographic source (Crossref, OpenAlex, Semantic Scholar, RePEc, NBER, SSRN, a journal page or your library), or labeled **UNVERIFIED**. If nothing turns up, it says so.
- **It says what it read:** full text, abstract only or metadata only, and which version. What a paper reports is kept separate from its own assessment and from proposed gaps.
- **Research questions** are tested for contribution, closest papers, identification, feasibility and audience. See [Research Questions](skills/econ-research/references/research-questions.md).
- **Literature** work covers search across sources, screening, verification and a reading-list format ([Literature Search](skills/econ-research/references/literature-search.md)), then agreement, splits, gaps and positioning ([Literature Synthesis](skills/econ-research/references/literature-synthesis.md)).
- A standard-library [reference checker](skills/econ-research/scripts/verify_references.py) compares DOIs or a `.bib` file with Crossref and reports PASS, WARN, FAIL, SKIP or ERROR (lookup failed, entry unchecked). It sends only DOIs, with no personal details.
- Ideas are adapted, with credit, from [claude-academic-workflow](https://github.com/ericluo04/claude-academic-workflow) (MIT) and [awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff) (CC0).

Example prompts: "What's the literature on minimum wages and employment? Ten most important papers." · "I'm interested in housing and inequality; help me find a second-year paper topic." · "Has anyone used this design before?" · "Check the references in `paper.bib`."

## Repo layout

```text
Econ-Agent-Skills/
├── README.md, AGENTS.md, DESIGN_V1.md, STORAGE_POLICY.md, CHANGELOG.md
├── skills/
│   └── econ-teaching/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       │   ├── teaching-design.md         # how to choose and shape an explanation
│       │   ├── expert-teaching.md
│       │   ├── mathematical-reasoning.md
│       │   ├── slide-fidelity.md
│       │   ├── visuals-and-homework.md
│       │   ├── macroeconomics.md
│       │   ├── microeconomics.md
│       │   ├── econometrics.md
│       │   ├── time-series.md
│       │   ├── course-navigation.md
│       │   ├── course-state-and-sources.md
│       │   ├── large-file-strategy.md
│       │   ├── latex-outputs.md
│       │   ├── cloud-drive-workflow.md
│       │   └── learning-log.md
│       ├── examples/
│       │   ├── bellman-teaching-example.md
│       │   └── diagnostic-teaching-patterns.md
│       ├── scripts/                       # read-only helpers for TeX and course files
│       └── templates/
│           ├── course-map.md, lecture-index.md, notation-registry.md
│           ├── figure-index.md, homework-map.md, learning-log.md
│           ├── course-state.example.json
│           └── simple-notes.tex, simple-notes-cn.tex
│   ├── econ-research/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── references/
│   │   │   ├── research-questions.md
│   │   │   ├── literature-search.md
│   │   │   └── literature-synthesis.md
│   │   └── scripts/verify_references.py
│   └── econ-writing/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
│           ├── terminology-and-notation.md
│           ├── econ-conventions.md
│           └── ai-tells.md
├── tests/                                 # structural tests and manual evaluation cases (Teaching, Writing and Research)
├── logs/                                  # dated development logs (not student learning logs)
└── .github/workflows/validate-skills.yml
```

## Change history, contributing and testing

- [CHANGELOG.md](CHANGELOG.md) summarizes changes; [logs/](logs/README.md) explains what changed, why and how it was verified. [AGENTS.md](AGENTS.md) tells repository-editing Agents to update both. The [v1 design baseline](DESIGN_V1.md) records the architecture and its stability rule.
- Treat teaching decisions as testable behavior. When a real lecture interaction exposes a failure, add a case to the [professor evaluation cases](tests/professor-evaluation.md) the [writing evaluation cases](tests/writing-evaluation.md) or the [research evaluation cases](tests/research-evaluation.md) and fix the responsible reference rather than growing SKILL.md.
- GitHub Actions runs link validation, repository contract tests and a LaTeX compile smoke test. These **structural tests do not prove teaching quality**; human evaluation on real lecture slides remains necessary.

## Roadmap

- **Now:** cases 45–51 passed on real lectures in three courses: macro ([ECONS 509](logs/2026-10-29-professor-econs509-se-lecture-test.md)), econometrics and time series ([ECONS 512, STAT 516](logs/2026-10-29-professor-econs512-stat516-tests.md)), including homework solved in the lecture's method and a real past exam. Still to do: a microeconomics lecture and an independent grader.
- **Econ Writing:** run the [writing evaluation cases](tests/writing-evaluation.md) on real drafts (a paper section, a LaTeX file, a referee report and a homework write-up) before calling it stable.
- **Econ Research:** run the [research evaluation cases](tests/research-evaluation.md) on real topics. A later version may add identification design and empirical methods, if real use shows the need.
- **Optional:** installer guidance for specific Agent clients.

## Standard

The skills follow the [Agent Skills open specification](https://agentskills.io/specification). Platform-specific metadata in `agents/openai.yaml` is optional and does not change the portable `SKILL.md` format.
