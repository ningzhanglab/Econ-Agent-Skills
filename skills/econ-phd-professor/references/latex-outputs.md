# Default TeX + PDF Teaching Deliverables

## Trigger and destination

**Only when the user asks to create/export/save a file** (notes, chapter explanations, study guides, course maps, derivations, summaries, etc.), the Professor's default deliverable is a matched **editable \`.tex\` source and compiled \`.pdf\`**, with the same base filename. This is the default when **no format is specified**. An explicit user format or file preference overrides it.

Place the two final files in the verified active course's **\`Agent Outputs/\`** cloud folder, as required by [Cloud Drive workflow](cloud-drive-workflow.md). Verify both by name, type, ID and correct parent. Do not put the course-specific output in the public GitHub repository.

Regular chat explanations do **not** automatically create a file.

## Simple LaTeX first

Use the accompanying [minimal template](../templates/simple-notes.tex) as the default structure. The goal is readable economics notes, not a decorative publication design:

- \`article\` class, conventional title/section/subsection hierarchy, normal margins, clean paragraphs.
- Load only needed packages: \`amsmath\`, \`amssymb\` for economics math, optional \`graphicx\` when actually including figures. Avoid elaborate header/footer systems, color themes, slides/Beamer, complex custom macros and heavyweight template dependencies by default.
- Keep the **original lecture's mathematical notation** exactly, including primes, expectations, indices and sign conventions; outside examples must be explicitly labeled and mapped.
- A brief document should stay brief. Add sections for homework connections or assumptions only when relevant, not as mandatory boilerplate.
- When the user requests Chinese text, use a minimal Unicode-capable LaTeX setup appropriate to the available environment (e.g., \`ctexart\` with XeLaTeX if installed); if the needed TeX packages/fonts are missing, report the issue rather than silently dropping Chinese characters or presenting an uncompiled PDF.

## Compiling and checking

1. Compose valid, self-contained LaTeX from the chosen minimal template.
2. Save with descriptive matching names, for example \`ECONS509_Lecture08_Notes.tex\` and \`ECONS509_Lecture08_Notes.pdf\`.
3. Compile using a suitable **available** TeX engine, e.g., \`latexmk -pdf\` or \`pdflatex\` for standard Latin text, and \`xelatex\` when Unicode/Chinese setup requires it; compile the necessary passes to resolve references.
4. Check that compilation actually succeeded, relevant math/figures render correctly and there are no missing external images, fonts or broken references. Inspect/render PDF pages when possible. Fix problems and recompile.
5. Keep both source and PDF in \`Agent Outputs/\`; include any figure dependencies necessary to recompile the \`.tex\` (or use reproducible relative paths into permitted source assets).
6. Return **both verified cloud links**, and state the final folder.
7. If compilation cannot run or fails, do **not** claim the PDF exists. Deliver the \`.tex\` if feasible and report clearly why the PDF was not produced, what remains unverified, and which environment dependency is missing. If upload fails, disclose that separately.

A local generated PDF or a successful LaTeX syntax check alone does not prove the requested files were written to Google Drive. Confirm cloud metadata for both.

## Format overrides

- Explicit \`.md\`, \`.docx\`, spreadsheet, image or Google Doc request: follow the user's requested format, without imposing a PDF/TeX pair.
- Explicit "PDF only": deliver PDF; optional TeX only if requested or helpful and approved.
- Explicit "LaTeX source only": deliver TeX only.
- Default without a format: deliver **both** \`.tex\` and \`.pdf\`.

When using lesson visuals in the document, follow [Visual Teaching and Homework](visuals-and-homework.md): original source-slide figures may be freely incorporated as needed; *new* figures should only be added when they meaningfully clarify a topic.
