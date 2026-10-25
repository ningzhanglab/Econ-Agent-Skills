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

## Reproducible output bundle

A pair of files that uploads successfully may still be **unreproducible** if its TeX refers to figures, tables, bibliography or subfiles that live only in the temporary build directory.

- Keep figures under a stable relative directory such as `Agent Outputs/figures/` or include self-contained TeX plotting code only when justified. Do **not** rely on absolute temporary paths, unexplained network links or missing TeX macro files.
- Check the `\input`, `\include` and `\includegraphics` references used in the actual generated TeX. When the user requests downloadable standalone reproducibility, include all required assets in the delivered bundle and use stable relative paths.
- After uploading, a strong reproducibility check is: re-download the `.tex`, `.pdf` and declared dependencies into a **clean directory**, then compile again there and inspect the rendered PDF.
- [The bundle checker](../../../scripts/check_tex_bundle.py) provides a **small conservative** local test for literal relative dependencies, a matching PDF and optional scratch compilation. It is **not** a full TeX dependency solver, does not understand all macro expansion or graphicspath rules, and is not evidence that a Google Drive upload succeeded.
- Verify the resulting PDF visually where possible, especially Greek symbols, subscripts, tables and CJK text; a syntactically valid PDF header is not sufficient.

### Chinese text smoke test

A plain Latin `article` + PDFLaTeX template is **not sufficient for Chinese characters**. Use the [ctexart example](../templates/simple-notes-cn.tex) with XeLaTeX when Chinese is present. Do not silently strip Chinese, replace characters with boxes, or report success without opening the actual rendered PDF. The standard CI job tests the **Latin** template; Chinese compilation depends on the host's installed CJK engine/fonts and must be checked separately.

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
