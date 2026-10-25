# Course Map — [Course Title]

> **Cloud outputs:** This is a reusable template in GitHub. When the user requests a completed file, save that filled artifact to the verified current course's cloud `Agent Outputs/` folder and return the cloud link. Follow [Cloud Drive workflow](../references/cloud-drive-workflow.md).

> **Generated course-specific artifact:** copy this template into a **private** course workspace. Do not fill it with proprietary lectures and commit it to the public Skill repo.
>
> **Coverage labels:** DISCOVERED, INDEXED, REVIEWED (state actual range), BLOCKED. Follow [course-navigation](../references/course-navigation.md).

## Metadata & provenance

- Course / term / instructor (only if verified):
- Workspace or collection ID:
- Map updated (date and source revision):
- Syllabus locator and inspection status:
- Source inventory count: discovered __ / indexed __ / reviewed fully __ / blocked __
- Important absences or unresolved file versions:

## Instructor's actual course order

Use syllabus order when available. If no syllabus exists, mark inferred order **provisional**. Never infer a taught chronology solely from uploaded sort order.

| Course order | Lecture ID | Lecture title | Evidence for order | Source locator | Coverage | Missing pieces |
| --- | --- | --- | --- | --- | --- | --- |
| 1 (confirmed/provisional) | L01 | [Title] | [syllabus entry or filename heuristic] | [filename, link, ID] | DISCOVERED | [none / figure PDFs / etc.] |

## Conceptual dependency map (different from instructor order)

| From concept / lecture | Needed for | Relationship | Evidence | Confidence |
| --- | --- | --- | --- | --- |
| [topic A / L01] | [topic B / L04] | prerequisite / comparison / extension | exact lecture locator or labeled inference | explicit / derived / provisional |

If the lecturer intentionally introduces a result before its mathematical tools, retain that instructor order above and show conceptual prerequisites separately here.

## Course-wide model map

| Model or topic | Primary lecture(s) | Core economic question | Key assumptions | Useful related lectures |
| --- | --- | --- | --- | --- |
| [Name] | [Lxx] | [Why this model?] | [Source-linked] | [Related topic] |

## Visual learning map and source coverage

For a source-backed visual index, use [the Figure Index template](figure-index.md) rather than treating a TeX figure filename as a viewed graph.

| Lecture/model | Reviewed original figure (source and page) | New useful teaching schematic (if appropriate) | Actual computed plot (data/method) | Unseen or blocked figures |
| --- | --- | --- | --- | --- |
| [Lecture] | [image or rendered PDF, REVIEWED range] | [clearly labeled independent schematic] | [computed results only] | [TeX reference with no visually inspected image] |

Use **no image quota**. Plan visuals proactively when they clarify mechanics, constraints, dynamics, equilibria, or algorithms. Source data and independently illustrated concepts must never be conflated.

## Lecture ↔ Homework alignment

This section is based on **verified assignment files**, not merely schedule guesses. Use a separate [Homework Map template](homework-map.md) when the course has many exercises.

| Homework & part | Source locator | Related lecture / slide locator | Model and economic question | Method or conceptual skill | Confidence |
| --- | --- | --- | --- | --- | --- |
| [PS1(a)] | [verified file ID/page] | [L05, original frame/page] | [household problem] | [Bellman / VFI] | explicit / derived / provisional |

Record which assignments were only discovered, indexed, actually reviewed or unavailable; don't invent tasks, part numbers or a solution key.

## Source role/version decisions

- Current handout PDFs and presenter PDFs:
- Corresponding original TeX source IDs / revisions:
- Explicit instructor revision notices:
- Unresolved equation, chart or pagination differences:
- Last source check and saved [Course State](course-state.example.json):

## Notation and conflicts

- Course-specific registry: [path to private notation-registry.md]
- Known notation conflicts across lectures: [L02 x versus L08 x; do not assume identical meaning]
- Alias mappings from alternative texts: [external symbol ↔ local symbol, explicitly qualified]

## Coverage and uncertainty

- **Verified pages/images:** [lecture ID, specific page ranges, status]
- **Indexed only:** [lecture IDs and reasons]
- **Blocked:** [file/figure and why]
- **Unknown instructor order:** [list]
- **Unverified conceptual connections:** [list]

## Study entry points

- Suggested starting lecture given current question:
- Material to read next and why:
- What must be rechecked against original slides before a proof, diagram or homework answer:
