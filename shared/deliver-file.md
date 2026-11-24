# Deliver a File

Use this only when the user asks to create, export or save a file. An ordinary question is answered in chat and creates nothing.

## Defaults

- **Format:** with no format named, a matching editable `.tex` and compiled `.pdf` with the same informative base name, for example `Macro_Lecture08_Notes.tex` and `Macro_Lecture08_Notes.pdf`. A format the user names replaces this: `.md`, `.docx`, a spreadsheet, an image or a Google Doc as asked; "PDF only" delivers the PDF; "LaTeX source only" delivers the `.tex`.
- **Destination:** the folder named exactly `Agent Outputs` (case and spacing matter) in the verified course or project workspace, unless the user gives another folder.
- **Never overwrite silently:** if the filename exists, use a versioned name or follow an explicit update instruction.

## Find the destination before writing

Source files stay in the user's own folders. Outputs never go to a public repository, and a temporary local path or chat attachment alone is not delivery when a cloud workspace is in use.

1. Follow an exact destination folder link or ID the user gave. If a specific course Project explicitly selects an existing output folder with another name, use that verified folder for that course; this is an explicit override, not a change to the convention.
2. Otherwise identify the active course or project workspace from source file metadata, parent folder and syllabus. Do not guess from filename similarity.
3. Select the child folder named exactly `Agent Outputs` in that workspace. If it is absent and the provider allows, create it, only when an output is requested.
4. If the source files are at the cloud root with no workspace, use or create the root `Agent Outputs` folder.
5. If several workspaces or destinations remain plausible, resolve by evidence or ask one targeted question. Never put files in an unrelated folder.
6. Folders named `outputs`, `output` or `generated` are not `Agent Outputs`. If a legacy `outputs` and the correct `Agent Outputs` both exist, use `Agent Outputs`. Do not rename or remove other folders without authorization.
7. **Near-miss folder.** If the workspace has no exact `Agent Outputs` but has a folder differing only in capitalization, spacing or singular/plural (for example `agent output`), do not silently use it and do not silently create a second folder beside it. Ask the user once, naming the existing folder: use it, or create `Agent Outputs`. Choosing the existing folder is the explicit override in step 1 for that course; note it in a saved Course State when one is kept, so the question is not repeated. If nobody can be asked, create the exact `Agent Outputs` and report that both folders now exist.

## Write the TeX

- Start from the skill's own template and keep it simple: conventional structure, normal margins, the needed math packages, and `graphicx`, TikZ or PGFPlots when a useful figure needs them. Avoid decoration, not genuine economic visuals.
- Keep the source's mathematical notation exactly, including primes, expectations, indices and sign conventions. Outside examples are labeled and mapped.
- A brief document stays brief. A substantial one gets a table of contents when it helps navigation; no length or chapter structure is imposed.
- **Chinese text** needs a Unicode setup: `ctexart` (or `ctexbeamer` for slides) with XeLaTeX. A plain Latin class with PDFLaTeX is not enough. If the fonts or packages are missing, report it; never drop the characters, show boxes, or present an uncompiled PDF.

## Keep the bundle reproducible

A `.tex` that compiled once can still be unusable if it points to figures or subfiles that lived only in a temporary build directory.

- Keep figures in a stable folder beside the `.tex` and cite them by relative path. No absolute temporary paths, unexplained network links or missing macro files.
- Deliver every file the `.tex` needs through `\input`, `\include` and `\includegraphics`.
- The [bundle checker](../scripts/check_tex_bundle.py) follows literal `\input`, `\include` and `\includegraphics`. Use `--build-pdf` for a fresh PDF, following the overwrite default above. Use `--compile` to compare an existing PDF's pages with a clean build. It needs Poppler when PDF bytes differ. Check PDF links separately. Unsupported dependencies such as bibliographies or `\graphicspath` need a clean manual build.
- Download the bundle to a separate directory with its relative paths intact. Run `check_tex_bundle.py LOCAL.tex --verify-copy DOWNLOAD_DIR` to compare the source, PDF and static dependencies with the checked local bundle by SHA-256. Check other attachments separately. Without a checked baseline, use `--compile` on the download or compare after a clean manual build.

## Compile and check

1. Compile with an engine that is actually available: `latexmk -pdf` or `pdflatex` for Latin text, `xelatex` when Unicode or Chinese needs it, with enough passes to resolve references.
2. Re-read each displayed formula against its source before treating the document as final.
3. Confirm that compilation succeeded and that math, figures, fonts and references render. Look at the rendered pages when possible, especially Greek symbols, subscripts, tables and Chinese text; a file that merely exists is not checked. Fix problems and recompile.
4. If compilation cannot run or fails, do not claim the PDF exists. Deliver the `.tex` if feasible and say why the PDF was not produced, what remains unverified and which dependency is missing.

## Upload and verify

1. If the file was created locally first, the local copy is intermediate, not the delivery.
2. Before promising cloud delivery, confirm the host has a real way to hand a generated file to the provider, not only local file generation. Upload with an actual supported tool; never fabricate a file reference, ID or URL.
3. Verify every resulting file by metadata or folder read-back: name, file ID, type and parent folder. For the default pair, confirm both `.tex` and `.pdf` are present and return both links, and state the folder. A source-only `.tex` is not a compiled PDF.
4. If access or upload fails, or the destination cannot be resolved, say exactly what was and was not saved. A local fallback may be offered but is not a cloud upload. If only one of the pair uploads, delivery is incomplete: report which file succeeded and which failed, and do not delete or overwrite the uploaded one without authorization.

## Permissions and privacy

Never make the user's files public, change sharing, or delete or move original source files without explicit permission. Respect a course's own sharing rules: when a syllabus restricts reposting course materials or uploading them to outside services, keep every output that reproduces course content private, and mention the rule to the user once when it bears on what they asked for; whether to use the materials with an assistant is their decision. A skill describes behavior; it cannot itself grant cloud access or upload rights.
