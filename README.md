# Econ Agent Skills

Reusable, version-controlled Agent Skills for economics PhD learning and research.

> **Status:** Professor v1.1 (teaching revision of the v1 design baseline). Research Agent is planned but **not** implemented.

## Skills catalog

| Skill | Purpose | Status |
| --- | --- | --- |
| [econ-phd-professor](skills/econ-phd-professor/SKILL.md) | Learn graduate economics from your own lecture slides, homework and exams, with exact notation, economic intuition, rigorous derivations and useful diagrams | **v1.1; quality evaluation ongoing** |
| econ-research-agent | Literature review, research question development, methods and critical research assessment | **Planned, not yet available** |

## How the Professor teaches

The Professor teaches like a knowledgeable economics PhD professor, not a slide summarizer. The slides define the local model, notation and assumptions; broader economics knowledge explains why the model is built that way, how the mechanism works and when the result fails. The aim of every answer is that you **understand the economics and can do the next problem yourself**.

Seven principles govern every answer (full text in [SKILL.md](skills/econ-phd-professor/SKILL.md)):

1. **Exact slide notation.** Symbols, signs, timing and operators stay exactly as the lecturer wrote them. Slide statements, derivations and outside knowledge are kept visibly separate.
2. **Diagnose the bottleneck and explain the model's design.** The Professor looks for the earliest missing link (notation, a proof step, the incentive, an assumption, identification or numerical approximation) without claiming to read your mind. For "why this model?" it explains what the model isolates, what it omits and what a nearby alternative would change. Each field has a short list of common PhD-level traps (for example an Euler equation at a binding borrowing limit, or a strong instrument mistaken for a valid one) that the Professor raises only when relevant.
3. **Answer first, then build understanding.** The first sentences answer your question; the derivation follows; a substantive explanation ends with its economic meaning in plain words.
4. **Visuals as a first-class teaching method.** Graphs are considered proactively for constraints, trade-offs, dynamics, equilibria and numerical methods. Original figures are used only if actually inspected; new schematics and computed plots are labeled honestly. No figure quota.
5. **Intuition checked against the mathematics.** Verbal stories are tested with sign checks, limiting cases or tiny labeled numerical examples.
6. **Homework and exams in the instructor's framework.** Same notation, same or closest slide method, every necessary step, a checked result, and then the reusable method in one or two lines. Exam preparation can include a fresh practice item with its answer held back. Course AI-use rules are respected.
7. **Your language.** Answers come in the language you write in, with symbols unchanged and English technical terms beside translations, for example 欧拉方程 (Euler equation).

The Professor chooses a **teaching mode before tools**: quick step, intuition, derivation, model comparison, whole lecture, Homework or exam preparation. A narrow question never triggers a course inventory or a generated file. See [Teaching Design](skills/econ-phd-professor/references/teaching-design.md), [Expert Teaching](skills/econ-phd-professor/references/expert-teaching.md) and the [hypothetical diagnostic examples](skills/econ-phd-professor/examples/diagnostic-teaching-patterns.md).

One Skill covers four fields through optional domain lenses: [Macroeconomics](skills/econ-phd-professor/references/macroeconomics.md) (including numerical methods), [Microeconomics](skills/econ-phd-professor/references/microeconomics.md), [Econometrics](skills/econ-phd-professor/references/econometrics.md) and [Time Series](skills/econ-phd-professor/references/time-series.md). Each lens lists the questions an expert asks, the high-value explanations and the common traps for that field; none is tied to a particular course.

## Getting started

1. Read [SKILL.md](skills/econ-phd-professor/SKILL.md) to see the behavior and triggers.
2. Make the **entire skill folder** `skills/econ-phd-professor/` available to a compatible Agent Skills client (install from this GitHub folder, or copy or link the folder into the client's skills directory). The folder is self-contained: its references, templates, examples and helper scripts all live inside it. A GitHub repository alone does **not** activate the skill.
3. Provide the actual lecture slides (PDF, PPT, TeX, screenshots) or an accessible course folder. The Professor must inspect the relevant material and never pretends to have read slides it cannot access.
4. Ask a question.

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

- Same-basename `.tex`, PDF and Word files in one course folder are treated as one lecture by default; presenter views, handouts and genuine revisions are distinguished by content, not extension. See [Course State and Sources](skills/econ-phd-professor/references/course-state-and-sources.md).
- Templates: [Course Map](skills/econ-phd-professor/templates/course-map.md), [Lecture Index](skills/econ-phd-professor/templates/lecture-index.md), [Notation Registry](skills/econ-phd-professor/templates/notation-registry.md), [Figure Index](skills/econ-phd-professor/templates/figure-index.md), [Homework Map](skills/econ-phd-professor/templates/homework-map.md) and [Course State](skills/econ-phd-professor/templates/course-state.example.json).
- Helper scripts (inside the skill folder; Python standard library, read-only on your sources): [file grouping](skills/econ-phd-professor/scripts/group_course_sources.py), [TeX figure inventory](skills/econ-phd-professor/scripts/inventory_tex_figures.py) and [TeX bundle checker](skills/econ-phd-professor/scripts/check_tex_bundle.py).
- Details: [Course Navigation](skills/econ-phd-professor/references/course-navigation.md) and [Large-File Strategy](skills/econ-phd-professor/references/large-file-strategy.md). This is a workflow specification, not background indexing or permanent memory.

Text inside slides, homework and README files is treated as **untrusted study material**, never as instructions that can override your request, change sharing or move private files.

## Files, cloud storage and learning logs

- **Ordinary questions are answered in chat.** No file is created unless you ask.
- **When you ask for a file without naming a format**, the Professor delivers a matching editable `.tex` and compiled `.pdf`, saved and verified in your course's cloud folder named exactly **`Agent Outputs`**. An explicit format or destination overrides this. Rules: [Storage Policy](STORAGE_POLICY.md), [Cloud Drive Workflow](skills/econ-phd-professor/references/cloud-drive-workflow.md) and [TeX/PDF Outputs](skills/econ-phd-professor/references/latex-outputs.md). Chinese notes use the [ctexart template](skills/econ-phd-professor/templates/simple-notes-cn.tex).
- **Learning logs are on demand.** Say "记录今天的学习" or "Save today's learning log" and the Professor saves a short Markdown summary of what was actually studied, questions, clarifications and open issues to `Agent Outputs/Learning Logs/`. It never records chats in the background or claims mastery. See [Learning Logs](skills/econ-phd-professor/references/learning-log.md).
- This public repository holds reusable rules, templates and development logs only. Private slides and generated course records stay in your cloud drive.

## Repo layout

```text
Econ-Agent-Skills/
├── README.md, AGENTS.md, DESIGN_V1.md, STORAGE_POLICY.md, CHANGELOG.md
├── skills/
│   └── econ-phd-professor/
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
├── tests/                                 # structural tests and manual evaluation cases
├── logs/                                  # dated development logs (not student learning logs)
└── .github/workflows/validate-skills.yml
```

## Change history, contributing and testing

- [CHANGELOG.md](CHANGELOG.md) summarizes changes; [logs/](logs/README.md) explains what changed, why and how it was verified. [AGENTS.md](AGENTS.md) tells repository-editing Agents to update both. The [v1 design baseline](DESIGN_V1.md) records the architecture and its stability rule.
- Treat teaching decisions as testable behavior. When a real lecture interaction exposes a failure, add a case to the [professor evaluation cases](tests/professor-evaluation.md) and fix the responsible reference rather than growing SKILL.md.
- GitHub Actions runs link validation, repository contract tests and a LaTeX compile smoke test. These **structural tests do not prove teaching quality**; human evaluation on real lecture slides remains necessary.

## Roadmap

- **Now:** run evaluation cases 45–49 (answer first, reusable method, exam practice, Chinese with unchanged notation, traps raised only when relevant) on one real macro and one real econometrics lecture, then use Professor v1.1 across courses and record concrete teaching failures as new cases.
- **Later:** design `econ-research-agent` as a separate skill. Its absence means it is not ready.
- **Optional:** installer guidance for specific Agent clients.

## Standard

The skills follow the [Agent Skills open specification](https://agentskills.io/specification). Platform-specific metadata in `agents/openai.yaml` is optional and does not change the portable `SKILL.md` format.
