# A Whole Course: Navigation and Onboarding

Use when the user provides a semester's collection of materials, asks for a course overview or wants saved maps reused. A question about how two lectures connect is [Cross-lecture](cross-lecture.md). Do not require course onboarding before a focused question about an available slide.

## Defaults

- **Indexes:** none is mandatory. A Course Map, Lecture Index, Notation Registry, Homework Map, Figure Index or Course State is made only when it helps the task or the user asks.
- **Depth during onboarding:** inventory and map, not deep commentary on every page.
- **Saved files:** only when requested, as [Deliver a file](deliver-file.md) describes.

## Two different orders

Maintain both rather than conflating them:

1. **Instructor sequence:** syllabus dates/order, explicit numbering and teaching progression. Highest-confidence evidence: syllabus, then slide title/front matter and numbering; filenames and upload order are weak evidence.
2. **Conceptual prerequisite order:** a reasoned dependency graph (e.g., optimization before a particular recursive model). Label inferred dependencies and distinguish them from the instructor's actual presentation order.

Do not silently reorder lectures as if the inferred conceptual order is what the lecturer taught. Multiple valid orders can coexist.

## Proportionate source and index work

A focused equation question needs the relevant original, not a Course Map. A syllabus overview may need one lightweight map. A persistent course project can use more indexes only when useful or requested; the Course Map, Lecture Index, Notation Registry, Homework Map, Figure Index and JSON state are options, not a required set.

## Onboarding procedure — inventory first

0. If previous course indexes exist, use [Sources and versions](../guides/sources-and-versions.md) to verify saved IDs and versions. Group same-basename `.tex`/PDF/Word within the verified course folder as one logical document by default, then distinguish truly different handout/presenter versions, revisions and homework/code by evidence rather than extension alone.
1. Enumerate only the files actually accessible in the workspace. Record file names, formats, accessible locations and relationships (lecture, syllabus, homework, solution, reading, image, appendix, code).
2. Inspect the syllabus/table of contents if present. Determine course identifier and dates only from sources; if absent, build a provisional sequence using lecture numbers and internal titles, without pretending the order is confirmed.
3. When a course overview or reusable index would help, draft a compact course map using [the course-map template](../templates/course-map.md). Each lecture entry gets a stable local ID, source locator, order evidence, central questions, models and coverage status.
4. For the lectures relevant to the user's scope, create a lightweight lecture index only when useful using [the lecture-index template](../templates/lecture-index.md): sections, slide/page locators, assumptions, definitions, model dependencies and figures. Do not perform deep commentary on every page during onboarding unless explicitly requested.
5. For relevant figure-bearing lectures, build a Figure Index if needed from [the template](../templates/figure-index.md) with actual asset/PDF locators and visual-review status. Discover LaTeX references using [the read-only inventory tool](../scripts/inventory_tex_figures.py) if useful; prefer visually checking source images or corresponding rendered handout PDF pages, never equate a TeX reference with having seen the image.
6. Create a course-scoped notation registry from [the notation template](../templates/notation-registry.md) only for symbols actually observed. Scope symbols to lecture and equation/model; same symbol in another lecture does not imply same meaning.
7. Add conceptual links across lectures, but label each as explicit (stated by lecturer), derived (logically follows from materials), or provisional (inferred teaching connection). Note conflicting assumptions or notation.
8. When relevant Homework is accessible and a reusable map helps, create a grounded Lecture ↔ Homework map using [the Homework Map template](../templates/homework-map.md). Record actual problem/part locators, linked lecture/model, skills tested and confidence; do not treat Homework as a replacement for Slides or claim to have seen inaccessible solutions.
9. When a persistent course-onboarding output is requested, store a compact [Course State JSON](../templates/course-state.example.json) alongside user-facing TeX/PDF summaries. The checkpoint assists future source/version checks but does not replace original slides.
10. Produce an overview of confirmed versus provisional sequencing, source coverage, missing figures, and next learning steps. Files requested at this stage follow [Storage & privacy](#storage--privacy).

## Cross-lecture economic transfer

Compare lectures as [Cross-lecture](cross-lecture.md) describes, from both verified lecture sources, and record each link as explicit, derived or provisional. The [Course Map](../templates/course-map.md) has an optional comparison table; no separate concept registry is needed.

## Progressive verification states

Use these values in the course map and lecture index:

- **DISCOVERED:** file exists or is listed; contents not examined.
- **INDEXED:** inspected enough to map topics/sections and relevant locators, but not checked carefully page by page.
- **REVIEWED:** relevant text, equations and figures have been inspected for the stated range; report range precisely.
- **BLOCKED:** inaccessible, corrupt, too large for current tooling, omitted TeX dependency, unreadable figure, or another reason prevents inspection.

A lecture can be INDEXED overall while particular pages are REVIEWED. Never mark a 100-page lecture REVIEWED based on a 5-page sample. When a source is revised, downgrade affected status until locators and notation are rechecked.

## On-demand teaching retrieval

For a specific question:

1. In a new session, first find and verify existing Course State/Map and source versions when available; otherwise begin with accessible course files. Identify relevant lecture and slide(s) using the map and index. If question is ambiguous, use the best grounded scope and state uncertainty; ask a targeted clarification only if essential.
2. **Reopen original source** at those slide/page locators and inspect neighboring assumptions, definitions and figures. An index or prior summary is a navigation aid, not authoritative proof of an equation.
3. Distinguish TeX source, current handout PDF, presenter PDF and revisions as described in [Sources and versions](../guides/sources-and-versions.md). Load notation scoped to the current lecture/model, check whether the intended symbol appears in another lecture with different meaning, and do not silently merge them.
4. Open related/prerequisite lectures only when the connection matters; explicitly distinguish their model assumptions, closure, numerical methods and notation.
5. Explain at the requested depth; update a persisted index only if relevant and authorized.
6. When source revisions change a model, invalidate affected links and recheck them, not the entire course.

## Mixed material and source precedence

- Slides and lecture notes define what was taught; syllabus defines the official order if available.
- Homework and solutions illustrate applications but are not proof the lecturer used that notation in the slides.
- Outside textbooks and papers can deepen interpretation, but must not overwrite the local course model or symbols.
- For LaTeX: inspect main files and accessible `\input`/`\include` dependencies; linked figures must be inspected separately where available. A .tex file does not make the linked image visible.
- Track absent components explicitly. Never invent diagram content or report all course materials as fully analyzed without coverage evidence.

## Storage & privacy

Course-specific maps and indexes are private to one course. When requested as files they follow [Deliver a file](deliver-file.md): the course's `Agent Outputs/` folder, verified after writing, never a public repository. Link each saved index to the source file versions it was built from; when new lectures arrive, update the affected entries rather than assuming earlier summaries are current, and keep courses separate by their actual folders.

Use [Large files](../guides/large-files.md) for bounded scanning, ingestion and refresh.
