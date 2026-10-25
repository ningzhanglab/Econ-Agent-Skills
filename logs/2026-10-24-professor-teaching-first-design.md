# 2026-10-24 — Professor Teaching-First Architecture

- **Date:** 2026-10-24
- **Component:** `econ-phd-professor`
- **Type:** Skill design / pedagogical workflow simplification
- **Status:** Implemented; this is **not** a new real-course content test

## Why change

The user asked to continue improvements while **reducing repetitive tests and focusing on Skill design**. Previous iterations built three ECONS 509 Handbooks, a visual edition, source indexes and extensive delivery tests. They established infrastructure but left the core Professor instruction long enough that the Agent could over-focus on indexing, upload or document-generation logistics for small student questions.

## Decisions and modifications

1. Added `references/teaching-design.md` as the pedagogical decision layer: quick clarification, intuition, rigorous derivation, model/algorithm comparison, whole lecture/Handbook, Homework tutoring, and research context. Choose depth and media by learning objective; these are response modes, **not additional Skills**.
2. Refactored `SKILL.md`: preserved the six strict source/teaching/privacy requirements; replaced overlapping course-intake, teaching workflow, reference routing and scenario boilerplate with a concise adaptive teaching and on-demand tool path. Whole-course navigation and Cloud/TeX remain in existing dedicated references.
3. Added misconception-oriented guidance to `expert-teaching.md`: target the missing economic/math link, and integrate figures with derivations rather than repeating a fixed formulaic format.
4. Updated `README.md` and `AGENTS.md`: pedagogical design before document production; existing CI is a lightweight safety net, while substantial real-course output or upload tests belong to specific milestones.

## Preserved requirements

- Maintain exact local source notation/assumptions, including source-versus-supplement distinctions.
- Inspect actual source images when claiming original graph details; allow useful independent diagrams and actual computed plots with honest provenance.
- Use actual Homework where relevant, observing the class's AI-use/manual-work protocol.
- Keep same-basename multi-format source handling, syllabus order vs prerequisite graph, scoped Notation Registry and index coverage reporting.
- Generate files only on request; default to paired TeX and compiled PDF in the verified course's exact `Agent Outputs/` directory, unless user specifies otherwise.
- The planned Research Agent is **not** represented as implemented.

## Verification and limitations

| Check | Result | Scope |
| --- | --- | --- |
| Read current repository source rules and references | Pass | Current Skill, expert teaching, domain guides and repository governance inspected. |
| Repository Markdown link/readback | Planned lightweight verification | Check new reference path and written files after commit. |
| Existing GitHub CI | Verify completed workflow after commit | Structural/LaTeX checks are automated by the existing workflow; no new benchmark added. |
| ECONS 509 Handbook or cloud round-trip | **Not run** | User requested design focus rather than additional real-course tests. |
| Independent pedagogical quality benchmark | **Not run** | The design describes intended behavior; an installed Agent's quality requires separate assessment. |

## Why this is simpler

The top-level Skill now decides the pedagogical goal and routes to only relevant references. Narrow questions can receive short direct answers. Course indexes, figure inventory and document building are tools the Professor may invoke as a consequence of a real task, not required stages of every conversation.

## Follow-up

Use the revised Professor for normal lectures and questions. Collect concrete cases where explanations are too long, too mechanical, omit relevant visuals, or incorrectly conflate Homework notation; revise the **teaching guidance** first. Do not repeatedly generate multi-volume PDFs unless the user needs the content.
