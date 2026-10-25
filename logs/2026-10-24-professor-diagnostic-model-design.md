# 2026-10-24 — Professor Diagnostic Teaching and Model Design

**Scope:** Econ PhD Professor instruction design; no private course content was generated.

## Motivation

Continue improving expert-level teaching and minimize repeated artifact/CI workload. Existing teaching-first guidance chose task depth but did not operationalize the difference between a symbol error, formal derivation, economic misconception, modeling abstraction, econometric identification, or numerical approximation.

## Implementation

- Updated the teaching-design reference with a question-to-explanation map, tentative diagnosis without asserting the student's beliefs, and a set of model-rationale lenses: purpose, active economic channel, omitted margins, tractability/identification, nearby alternatives, and separating economic, computational and statistical assumptions.
- Updated expert-teaching and mathematical-reasoning references to prefer the earliest missing logical link, decisive proof steps, checked counterexamples, valid KKT constraints and error distinctions.
- Updated SKILL.md to surface diagnostic-model reasoning in the core teaching priorities and model/algorithm teaching guidance.
- Added compact hypothetical examples for constrained Euler logic, complete information, IV relevance vs exclusion, and VFI stopping vs economic errors. These examples are **not course source material**.
- Adjusted openai.yaml default prompt and README/AGENTS guidance to reinforce the new teaching emphasis.

## Files changed

SKILL.md; references/teaching-design.md; references/expert-teaching.md; references/mathematical-reasoning.md; examples/diagnostic-teaching-patterns.md (new); agents/openai.yaml; README.md; AGENTS.md; CHANGELOG.md; logs/README.md; this log.

## Verification and limits

- Read current Skill and reference files before editing: **passed**.
- GitHub read-back and existing CI: to be checked on the final commit. No new tests were added.
- Real learner improvement or independent pedagogical grading: **not evaluated**.
- No TeX/PDF was compiled, no course file was altered, and no cloud output was uploaded. That is intentional: this is a **Skill design** iteration, not an output-delivery test.

## Compatibility

Preserves exact Slides notation, honest figure provenance, Homework alignment, the fallback for inaccessible sources and requested TeX/PDF delivery in the exact private Agent Outputs directory. Changes are incremental; no new top-level Skill or new mandatory response template.
