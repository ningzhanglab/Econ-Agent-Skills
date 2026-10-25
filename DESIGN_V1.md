# Econ PhD Professor — v1 Design Baseline

**Status:** Stable *design* baseline, not a claim of independent pedagogical certification or guaranteed host/plugin access.

## Goal

One graduate-level economics teacher that uses **actual lecture sources**, preserves local notation, explains model purpose and rigorous economics, employs purposeful graphs and actual Homework, and connects ideas across lectures **without equating different models**. File tooling serves teaching rather than governing every answer.

## Responsibility map

| Layer | Source of truth | Trigger |
| --- | --- | --- |
| Teaching entry and guarantees | [SKILL.md](skills/econ-phd-professor/SKILL.md) | Every invocation |
| Diagnose misunderstanding; select proof, intuition, visual or counterexample | [Teaching Design](skills/econ-phd-professor/references/teaching-design.md) and [Expert Teaching](skills/econ-phd-professor/references/expert-teaching.md) | Question requires explanation |
| Economic derivations and substantive lenses | [Mathematical Reasoning](skills/econ-phd-professor/references/mathematical-reasoning.md), Macro/Micro/Econometrics references | Relevant technical question |
| Course progression, cross-lecture mapping and sources | [Course Navigation](skills/econ-phd-professor/references/course-navigation.md), [Slide Fidelity](skills/econ-phd-professor/references/slide-fidelity.md) | Multi-lecture or source-specific question |
| Source graphics and Homework | [Visuals and Homework](skills/econ-phd-professor/references/visuals-and-homework.md) | Graph or task actually helps |
| Requested TeX/PDF and cloud persistence | [LaTeX](skills/econ-phd-professor/references/latex-outputs.md), [Cloud Workflow](skills/econ-phd-professor/references/cloud-drive-workflow.md), [Storage Policy](STORAGE_POLICY.md) | User requests a file |
| Optional private Learning Log | [Learning Logs](skills/econ-phd-professor/references/learning-log.md), [template](skills/econ-phd-professor/templates/learning-log.md) | Student explicitly requests a learning recap |

## Invariants

1. Preserve actual source assumptions, timing, expectations, notation and model version. Distinguish lecture text, justified derivation, outside perspective and independent illustration.
2. Identify the likely teaching bottleneck **tentatively**. Explain which assumption or modeling choice creates the mechanism; adapt length and medium to need rather than a rigid answer format.
3. Graphs are first-class teaching media, not decorations; original graphics require visual inspection and computed plots require real computation/data, no image quota.
4. Homework links use actual source problem statements and follow student-only/AI assistance requirements; they are not forced into every explanation.
5. For cross-lecture teaching, verify a common economic object, what assumptions/closure/solver/identification differ, qualified local notation mapping and source evidence. Keep instructor order separate from conceptual prerequisites.
6. Do not force a course index on a small question; same-stem TeX/PDF/Word is provisional grouping only, and previously saved maps must not substitute for original evidence.
7. Requested files default to a matched `.tex` and compiled `.pdf` in the verified private course folder named exactly `Agent Outputs/` unless user specifies another format/path. Never upload private course contents to this public repo.

## Done criteria and future-change policy

The above concepts have one authoritative home in existing references. There is no need for a parallel Professor/Research Agent, mandatory concept registry, universal chart generation or more code to satisfy v1. Existing structural CI and targeted source read-back are adequate for this **design-only** iteration. Independent teaching outcomes, arbitrary proof verification, automatic background course synchronization and external-cloud permissions are **not guaranteed**.

**Learning Log addition:** User-requested `.md` summaries are stored privately under the course `Agent Outputs/Learning Logs/`; never automatically archive chats or mistake a discussion for confirmed mastery. This explicit user requirement does not change default TeX/PDF for other requested teaching documents.

**Stop adding design features speculatively.** Only reopen the architecture when an actual teaching failure, user requirement or evidenced capability gap emerges. Fix the narrowest responsible document and use proportionate checks; do not launch a new full-course Handbook/cloud round-trip unless its behavior is the subject of the change.
