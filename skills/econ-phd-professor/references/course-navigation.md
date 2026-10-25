# Whole-Course Navigation and Course Onboarding

Use when the user provides a semester's collection of materials, asks for a course overview, or wants to connect ideas across lectures. Do **not** require full-course onboarding before a focused question about an available slide.

## Two different orders

Maintain **both** rather than conflating them:

1. **Instructor sequence:** syllabus dates/order, explicit numbering and teaching progression. Highest-confidence evidence: syllabus, then slide title/front matter and numbering; filenames and upload order are weak evidence.
2. **Conceptual prerequisite order:** a reasoned dependency graph (e.g., optimization before a particular recursive model). Label inferred dependencies and distinguish them from the instructor's actual presentation order.

Do not silently reorder lectures as if the inferred conceptual order is what the lecturer taught. Multiple valid orders can coexist.

## Onboarding procedure — inventory first

1. Enumerate only the files **actually accessible** in the workspace. Record file names, formats, accessible locations and relationships (lecture, syllabus, homework, solution, reading, image, appendix, code).
2. Inspect the syllabus/table of contents if present. Determine course identifier and dates only from sources; if absent, build a **provisional** sequence using lecture numbers and internal titles, without pretending the order is confirmed.
3. Draft a compact **course map** using [the course-map template](../templates/course-map.md). Each lecture entry gets a stable local ID, source locator, order evidence, central questions, models and coverage status.
4. For each lecture that you can access, create a **lightweight lecture index** using [the lecture-index template](../templates/lecture-index.md): sections, slide/page locators, assumptions, definitions, model dependencies and figures. **Do not perform deep commentary on every page during onboarding** unless explicitly requested.
5. Create a course-scoped **notation registry** from [the notation template](../templates/notation-registry.md) only for symbols actually observed. Scope symbols to lecture and equation/model; same symbol in another lecture does **not** imply same meaning.
6. Add conceptual links across lectures, but label each as **explicit** (stated by lecturer), **derived** (logically follows from materials), or **provisional** (inferred teaching connection). Note conflicting assumptions or notation.
7. Produce a user-facing overview with what is confirmed, what remains provisional, missing files/figures, and where to begin studying. When requested as files, save completed course maps, lecture indexes and notation registries in the **verified private course workspace's exact `Agent Outputs/` folder** via [Cloud Drive workflow](cloud-drive-workflow.md). Do not save them in this public Skill repository.

## Progressive verification states

Use these values in the course map and lecture index:

- **DISCOVERED:** file exists or is listed; contents not examined.
- **INDEXED:** inspected enough to map topics/sections and relevant locators, but not checked carefully page by page.
- **REVIEWED:** relevant text, equations and figures have been inspected for the stated range; report range precisely.
- **BLOCKED:** inaccessible, corrupt, too large for current tooling, omitted TeX dependency, unreadable figure, or another reason prevents inspection.

A lecture can be INDEXED overall while particular pages are REVIEWED. Never mark a 100-page lecture REVIEWED based on a 5-page sample. When a source is revised, downgrade affected status until locators and notation are rechecked.

## On-demand teaching retrieval

For a specific question:

1. Identify relevant lecture and slide(s) using the map and index. If question is ambiguous, use the best grounded scope and state uncertainty; ask a targeted clarification only if essential.
2. **Reopen original source** at those slide/page locators and inspect neighboring assumptions, definitions and figures. An index or prior summary is a navigation aid, not authoritative proof of an equation.
3. Load notation scoped to the **current lecture/model**, check whether the intended symbol appears in another lecture with different meaning, and do not silently merge them.
4. Open one or two prerequisite lectures or related models only when necessary; distinguish their notation and assumptions explicitly.
5. Explain at the requested depth; optionally refine indexes as new verified details become available, if workspace write access exists. Otherwise return a short update the user can save.
6. When new files are added or corrected, revise the map/index for affected material and document invalidated cross-links; do not regenerate everything by default.

## Mixed material and source precedence

- Slides and lecture notes define what was taught; syllabus defines the official order if available.
- Homework and solutions illustrate applications but are not proof the lecturer used that notation in the slides.
- Outside textbooks and papers can deepen interpretation, but must not overwrite the local course model or symbols.
- For LaTeX: inspect main files and accessible \`\\input\`/\`\\include\` dependencies; linked figures must be inspected separately where available. A .tex file does not make the linked image visible.
- Track absent components explicitly. Never invent diagram content or report all course materials as fully analyzed without coverage evidence.

## Storage & privacy

The skill is reusable; course-specific maps and indexes are artifacts of a particular private course. Use the user's connected cloud workspace and put requested persistent course artifacts in its **`Agent Outputs/` folder**, separate from source Slides. Verify successful cloud upload and the output parent folder. If the cloud connector lacks write access, disclose this rather than falsely reporting success. See [Cloud Drive workflow](cloud-drive-workflow.md). Do not send copyrighted/private course materials, answer keys, or identifiable learner notes to the public \`Econ-Agent-Skills\` repo by default.

Use [the large-file strategy](large-file-strategy.md) for bounded scanning, ingestion and refresh.
