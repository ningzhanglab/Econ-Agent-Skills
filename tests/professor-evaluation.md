# Professor v0.1: Manual Evaluation Cases

**Purpose:** assess real teaching quality. Passing file-format checks is not evidence of subject expertise, accuracy, slide-reading quality or adaptive teaching.

## Scoring rubric

Score each dimension 0 = failure, 1 = partial, 2 = strong. Record the **exact source slide** used in the run.

| Dimension | 2-point target |
| --- | --- |
| Slide faithfulness | No invented slide claims, equations, numbering or visible features |
| Notation fidelity | No silent changes to letters, primes, conditioning, timing or signs |
| Expert insight | Explains model purpose and mechanism beyond repeating text |
| Rigor | Correct assumptions, derivation and special cases |
| Complementary perspectives | Useful alternative view or example when appropriate, not forced |
| Adaptivity | Matches the question's scope and the student's confusion |
| Cross-field relevance | Connects fields only when grounded and informative |
| Source transparency | Separates slide, derivation, hypothetical example and external source |
| Course coverage honesty | Distinguishes discovery, indexing and page/figure review; never claims unseen content |
| Course structure | Instructor sequence and inferred prerequisites recorded separately; no cross-lecture notation conflation |

Critical fails: invented lecture content, unmarked notation substitutions, incorrect central claim, false citations, or pretending to inspect an unreadable graph. A critical fail means the case does not pass irrespective of numeric sum.

## Cases

### 1. Exact notation under a dynamic program

**Fixture:** any genuine lecture slide with an equation using a prime for a next-period choice and conditional expectations.

**Prompt:** "Explain this Bellman equation intuitively and derive the necessary optimality step. Keep the slide notation."

**Pass:** continues with the original prime and conditional operator; explains trade-offs; states needed assumptions; no invented definitions.

### 2. Narrow mathematics question

**Fixture:** slide with a minus sign after differentiation or a particular substitution.

**Prompt:** "Why does this negative sign appear?"

**Pass:** answers the exact algebra step briefly; does not produce an irrelevant mini-lecture.

### 3. Multiple economic interpretations

**Fixture:** slide with a consumption Euler equation.

**Prompt:** "I understand the formula but not the economics. Explain it from genuinely different angles."

**Pass:** offers different marginal trade-off, real-world and model-assumption perspectives; distinguishes constrained/interior cases; respects notations.

### 4. Visual analysis

**Fixture:** slide with graph, labeled axes, curves and one shift.

**Prompt:** "Explain everything this graph is telling us and what it cannot establish."

**Pass:** verifies actual visual content; identifies movement vs shift, axes and economic logic; does not fabricate numeric values.

### 5. Micro strategic mechanism

**Fixture:** lecture slide with information asymmetry or strategic game.

**Prompt:** "Why does the equilibrium change when information changes?"

**Pass:** states who observes what, why incentives/beliefs change, and a contrasting case.

### 6. Econometric identification

**Fixture:** IV or DID slide with explicit assumptions.

**Prompt:** "Why is this assumption needed? Give a counterexample."

**Pass:** separates identifying assumptions from estimator properties; counterexample changes a meaningful assumption; no causal overclaim.

### 7. Inconsistent lecture notation

**Fixture:** controlled test slide with a deliberate conflict between two equations.

**Prompt:** "Can you derive the result?"

**Pass:** flags the conflict, reproduces both versions, explains the possible interpretations, and does not quietly rewrite the slide.

### 8. Missing or unreadable slide

**Fixture:** reference to a slide number without uploading it, or an unreadable equation screenshot.

**Prompt:** "Explain equation (5) using my slide's notation."

**Pass:** does not hallucinate notation or claim the slide has been read; requests/reports the missing source while providing only clearly generic context if useful.

### 9. Whole-course syllabus order versus conceptual dependencies

**Fixture:** synthetic or authorized sample collection with four lectures; syllabus order L01 → L04 → L02 → L03, while L02 provides a prerequisite for L04.

**Prompt:** "Create the course map and tell me the best order to understand the material."

**Pass:** reports **syllabus order L01/L04/L02/L03** as source-backed and **conceptual L02 → L04** as a separately labeled inferred dependency. Does not falsely claim that inferred order is what the instructor taught.

### 10. No syllabus; filenames ambiguous

**Fixture:** lecture files named \`part_A.pdf\`, \`week_unknown.pdf\`, \`notes_final.pdf\` without syllabus, plus different title-page numbering.

**Prompt:** "Put the lectures in order."

**Pass:** produces a **provisional** ordering with evidence and unknowns, not a confidently invented schedule; tracks file coverage honestly.

### 11. Long multi-file TeX course and missing visuals

**Fixture:** one main TeX file references \`\\input\` chapters, shared macros, and external \`\\includegraphics\` PDF files; one dependency or figure is missing.

**Prompt:** "Understand all the lectures, including the graphs."

**Pass:** inventories reachable sources, records **BLOCKED** files/images, refuses to interpret unseen curves, and indexes by lecture chunks with source locators. It does not claim every graph was viewed.

### 12. Same symbol in different lectures

**Fixture:** two lectures use \`V\` for two different economic objects, and one external textbook uses a third symbol for one of them.

**Prompt:** "Connect these two lectures using their original notation."

**Pass:** preserves each lecture's \`V\` with scope/qualifiers, gives explicit mapping only for genuinely comparable objects and never globally rewrites both models into one symbol dictionary.

### 13. Focused question in a big course

**Fixture:** course map with 30 lecture files, only some INDEXED. Exact target slide is accessible.

**Prompt:** "Why does the sign flip on slide 9 in L13?"

**Pass:** opens slide 9 and nearby relevant equations, answers the narrow mathematical question, and does **not** scan all 30 lectures or claim broad understanding.

### 14. New lecture revision invalidates index

**Fixture:** L06 has an older indexed version and a newly uploaded revision with a changed definition.

**Prompt:** "Continue from my updated L06."

**Pass:** recognizes the revision, downgrades affected coverage, revisits source definitions and updates impacted notation/cross-links rather than silently relying on the old summary.

### 15. Cloud source and correct outputs destination

**Fixture:** connected course folder `ECONS509/` containing `slides.pdf`, `syllabus.pdf` and its own `outputs/`.

**Prompt:** "Read the course slides and create a PDF summary."

**Pass:** reads source slides through the authorized cloud connector; writes the final PDF into the course's exact `outputs/`; verifies file ID, name, format and parent folder; returns a real cloud link. Local-only output is not a pass.

### 16. Fuzzy folder name collision

**Fixture:** `agent outputs/` and `Agent output/` appear in cloud-wide search, while current course files are in a verified `Macro/` parent with no `outputs/` yet.

**Prompt:** "Save my course map in outputs."

**Pass:** never silently uses a similarly named folder. Creates `Macro/outputs/` when authorized or requests a target if the course workspace is ambiguous. Checks existing children before creating a folder.

### 17. Cloud-write failure

**Fixture:** lecture PDF is readable but provider denies folder creation/upload.

**Prompt:** "Write my lecture notes as LaTeX and save them to outputs."

**Pass:** reports the failure honestly and does not imply a temporary local artifact is in the cloud. Preserves requested .tex format and identifies a fallback if useful.

### 18. Safe updates and read-back

**Fixture:** output filename already exists and the course folder has more than one version of Lecture 8.

**Prompt:** "Generate an updated lecture-8 study guide."

**Pass:** uses the correct current lecture version, avoids unsafe overwrite without authorization, verifies the output name/type/parent, and reports the actual resulting cloud link.

## Run log template

- Date / Agent & model / Skill commit SHA:
- Slide title or file, page reference:
- Case:
- Prompt:
- Score per dimension:
- Critical fail? Why:
- What should change in the skill:
- New regression case needed?:
