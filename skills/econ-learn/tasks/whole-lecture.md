# A Whole Lecture, Lecture Notes or a Handbook

## Defaults

- **Order:** the instructor's order.
- **Each block opens with its main result,** then derives it.
- **Included:** only relevant Homework, extensions and self-checks. No fixed length, chapter structure or section list.
- **As a file:** only when asked ([Deliver a file](deliver-file.md)), from the [notes template](../templates/simple-notes.tex), or the [Chinese template](../templates/simple-notes-cn.tex) with XeLaTeX when the text is Chinese.

## Build the lesson

Organize by coherent model blocks, not by slide. A lecture is a narrative: model motivation, prerequisites, mechanisms, sound derivations, figures integrated with equations, applications and recap. Do not replace a course with a file inventory, and do not pad with formula repetition.

One possible thread: economic question → primitives and notation → key mechanism → diagram or equation → derivation or algorithm → what can go wrong → a verified Homework connection. Reorder or omit for the learner's actual need.

Design check, not headings:

1. **Anchor.** What is actually on the slides? Verify notation, timing, assumptions and source version ([Reading sources](../guides/reading-sources.md)).
2. **Core idea.** What is being optimized or identified, what changes and why, and which misconception is most likely.
3. **Representations together.** Equations, verbal intuition and figures are complementary ([Figures](../guides/figures.md)); the most instructive order can begin with a visual. Connect them instead of writing "intuition", "derivation" and "figure" as three disconnected sections.
4. **Transfer.** If it genuinely helps, connect a verified Homework task or a second lecture ([Cross-lecture](cross-lecture.md)).
5. **Trim and check.** Remove duplicate paragraphs, unnecessary background, boilerplate captions and status chatter. Confirm the central claim is correct under the stated assumptions, and surface the one limitation that matters rather than every caveat.

## Homework in a lecture

When a course has Homework, read the relevant problem alongside its lecture when that helps, especially for conceptual review and exam preparation. Bring it into a focused explanation only when it sharpens the answer; in generated notes, include Homework connections where relevant, but do not reproduce a whole solution set unless that is the explicitly authorized task.

1. Connect the problem to its lecture: task number or part, source locator, linked model or equation, the skills tested and the economic question behind it. Homework date and scope are evidence about the course, not the whole syllabus. Only when a reusable record helps (course onboarding, exam preparation), save this as a [Homework Map](../templates/homework-map.md).
2. Use the Homework to show why a lecture concept matters: what students must compute, compare, derive, explain or verify, and how several lectures may build toward the same problem set. For a student's difficulty, an actual corresponding exercise is a good concrete example: explain its prerequisites and why it tests the lecture's mechanism.
3. Slides define the model and the local notation. Homework may use another parameterization: map it explicitly, and where the two genuinely differ, say so and what it changes.
4. Label whether a question actually appears in the Homework, is inferred from its structure, or is an extra exercise; do not claim to have read solutions that were not accessible. If no relevant Homework is accessible, teach from the verified Slides without pretending to have reviewed assignments.

## Teaching from zero

Spend the effort on definitions, transparent examples and justified intermediate steps before the general PhD-level claims. Rebuild missing prerequisites in the lecture's notation instead of giving a compressed technical summary.

## Coverage

Say which pages were actually reviewed. A lecture read in part is reported as read in part; the states DISCOVERED, INDEXED, REVIEWED and BLOCKED are defined in [Course](course.md#progressive-verification-states).

For a substantial document, plan the diagrams together with the equations and Homework connections, record source figures in a [Figure Index](../templates/figure-index.md), and keep figure paths reproducible.
