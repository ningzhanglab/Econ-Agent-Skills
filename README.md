# Econ Agent Skills

Reusable, version-controlled Agent Skills for economics PhD learning and research.

> **Status:** Professor Skill v0.1 implemented. Research Agent is planned but **not** implemented.

## Skills catalog

| Skill | Purpose | Status |
| --- | --- | --- |
| [econ-phd-professor](skills/econ-phd-professor/SKILL.md) | Learn graduate economics from lecture slides with domain expertise, economic intuition, derivations, and cross-field connections | **v0.1 — ready for evaluation** |
| econ-research-agent | Literature review, research question development, methods, and critical research assessment | **Planned — not yet available** |

## Change history and logs

Use [CHANGELOG.md](CHANGELOG.md) for a quick summary of changes and [logs/](logs/README.md) for dated explanations of **what changed, why, verification performed, and next steps**. [AGENTS.md](AGENTS.md) instructs future repository-editing Agents to update both when making meaningful changes. Git commits remain the source of truth for exact diffs.

## What makes Professor different?

The Professor treats slides as the **source of the local model**, not the limit of economics knowledge. It may add theoretical intuition, examples, counterexamples, comparisons, and research context, while carefully marking what comes from the lecture versus its own elaboration.

**Non-negotiable:** Preserve the lecturer's slide notation. Do not silently rename variables, parameters, indices, or operators. State mappings explicitly if discussing different notation from outside sources. See [notation and source fidelity](skills/econ-phd-professor/references/slide-fidelity.md).

The first release is a **single skill with adaptive domain references** (macro, micro, econometrics), not three competing professor personalities.

## Repo layout

```text
Econ-Agent-Skills/
├── README.md
├── skills/
│   └── econ-phd-professor/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       │   ├── slide-fidelity.md
│       │   ├── expert-teaching.md
│       │   ├── mathematical-reasoning.md
│       │   ├── macroeconomics.md
│       │   ├── microeconomics.md
│       │   └── econometrics.md
│       └── examples/
│           └── bellman-teaching-example.md
├── tests/
│   ├── professor-evaluation.md
│   └── validate_skills.py
└── .github/workflows/validate-skills.yml
```

## Getting started

1. Open [Professor SKILL.md](skills/econ-phd-professor/SKILL.md) to inspect behavior and triggers.
2. Make the **entire skill folder** available to a compatible Agent Skills client (install from this GitHub folder, or copy/link the folder into your client-supported skills directory). A GitHub repository alone does **not** activate the skill in ChatGPT or other agents.
3. Provide the actual lecture slides (PDF, PPT, screenshots) or an accessible course resource. The agent must inspect the relevant material; it should not pretend to have read slides it cannot access.
4. Ask a question, e.g. `Use $econ-phd-professor to explain the intuition behind the Euler equation on slide 12. Keep the lecturer's notation, and connect it to one other model.`
5. For iterative testing, use [professor evaluation cases](tests/professor-evaluation.md).

### Example prompts

- "Teach slides 10–16 as if you were my PhD macro professor. Use **exactly** the slides' symbols, and explain why this model is formulated this way."
- "I know the Bellman equation mechanically, but what are three **substantively different** ways to understand it?"
- "Explain this proof from the lecture. Show the missing steps **without changing notation**."
- "What does this graph imply? Distinguish what the graph directly shows from additional theory."
- "How does this result relate to a different economic model, and where does the analogy break down?"

## Learning philosophy

- **Expert first, not slide paraphraser:** connect assumptions, mechanisms, equilibrium, counterfactuals, empirical relevance and limitations.
- **Adapt rather than template:** one algebraic sign question deserves a focused answer; a conceptual question may deserve multiple perspectives.
- **Grounded extension:** label slide claims separately from external interpretation and speculative extensions. Do not invent page numbers or citations.
- **Visuals matter:** read diagrams, axes, curves, arrows, tables, and slide layout—not only paragraphs and equations.
- **Match course notation:** preserve all names, indexes, equation conventions and displayed timing; explain ambiguity rather than silently correcting.
- **Bilingual when useful:** reply in the user's requested language, retaining English technical terms where useful.

## Contributing and versioning

Treat teaching decisions as testable behavior. When a real lecture interaction exposes a failure, add a regression case to `tests/professor-evaluation.md` and revise the relevant reference rather than growing the main SKILL.md indiscriminately.

Automated checks verify file structure and metadata only; **they do not prove pedagogical quality**. Human evaluation using actual lecture slides remains necessary.

## Roadmap

- **Now:** evaluate Professor v0.1 against macro, micro, and econometrics slides and refine explanations and notation fidelity.
- **Later:** design `econ-research-agent` as a separate skill with research-specific workflows and standards. Do not infer that its absence means it is ready.
- **Optional:** distribution metadata or installer guidance for specific Agent clients as those environments are chosen.

## Standard

The skills use the [Agent Skills open specification](https://agentskills.io/specification). Platform-specific metadata in `agents/openai.yaml` is optional and does not change the portable `SKILL.md` format.
