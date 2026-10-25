# Cloud Drive Workflow — Source Materials and Outputs

Apply when the user's lecture files reside in a connected cloud drive, or when the user requests a generated file.

## Storage contract

**Exact folder name: `Agent Outputs` (case and spacing matter)**. The repository [Storage Policy](../../../STORAGE_POLICY.md) overrides historical instructions naming `outputs/`.

- **Inputs:** use the user's authorized cloud workspace as the source of slides, syllabus, homework, readings, TeX dependencies and diagrams. Use connected Google Drive when available; respect another explicitly named accessible provider.
- **Outputs:** save **every requested final file** (notes, proof, PDF, DOCX, LaTeX, course map, lecture index, notation registry, spreadsheet, etc.) to the cloud **`Agent Outputs/` folder**, not only to a temporary local path, chat attachment or the public GitHub skills repository.
- Do **not** produce an unsolicited file for an ordinary chat explanation. Source files remain in the original course folder. Do not upload private source materials or generated course content to public GitHub.

## Identify the destination before writing

1. Follow an exact destination folder link or ID explicitly provided by the user.
2. Otherwise identify the active course workspace using accessible source file metadata, parent folder and syllabus; do not guess based on filename similarity.
3. Select a child folder named **exactly `Agent Outputs`** in that verified course workspace. If absent, and the connected provider allows it, create it **only when an output is requested**.
4. If the source course files are genuinely at cloud root with no course workspace, use or create the verified **root `Agent Outputs`** folder.
5. If multiple plausible course workspaces or exact destination folders remain, resolve by evidence or ask one targeted destination question. Never put files in an arbitrary unrelated folder.
6. Folder names `outputs`, `agent outputs`, `Agent output`, `output`, and `generated` do **not** qualify as the exact name `Agent Outputs`. If both legacy `outputs` and the correct `Agent Outputs` exist under the same verified course folder, **reuse `Agent Outputs`**. Do not rename or remove legacy folders without authorization.

## Source selection and saved-course recovery

When a cloud course has same-basename `lecture.tex`, `lecture.pdf`, `lecture.docx`/`lecture.doc`, **group them as one logical document by default**. Use the representation that reads most reliably (often TeX or readable Word), and consult PDF for figures and page/layout verification. Use [Course State and Sources](course-state-and-sources.md) when genuinely different handout/presenter variants or revisions appear; never assume the newest filename is authoritative. Ask whether formats are equivalent only if consequential differences remain unclear. A saved Course Map or Course State is an index, not source evidence. Recheck file IDs, revision markers and permissions and reopen the relevant original equations/figures in each new session.

## Read and teach from cloud sources

- Use cloud file/folder discovery and metadata to locate the course version and source. Read primary slide pages and relevant neighboring definitions; do not mistake search snippets or indexes for reading source.
- For cloud-native Docs, Sheets and Slides, use supported content workflows. For stored PDF, TeX, images and Office files, use supported file read/download tools as needed.
- Recheck mathematical notation and figure contents from the originals where available. A LaTeX source referring to missing graphics does not grant access to those images.
- Follow [Course Navigation](course-navigation.md) and [Large-File Strategy](large-file-strategy.md) for staged indexing and source fidelity.

## Create, upload and verify requested output

1. Respect explicitly requested file formats and names. **Professor default when the user requests an output file but does not specify its format: produce both a minimal `.tex` source and its compiled `.pdf`**, using matching informative base names (e.g., `ECONS509_L08_notes.tex` and `ECONS509_L08_notes.pdf`). A user-specified alternate format or single-format request overrides the pair. See [TeX/PDF Outputs](latex-outputs.md).
2. Generate the real output via available tools. If it is created locally first, treat the local file as **intermediate**, not as the final delivery.
3. Find or create the exact destination `Agent Outputs/` folder as above. Before asserting cloud delivery is possible, verify the host supports a **real generated-file → provider upload handoff** (for example a connector-supported file reference), not just local file generation. Upload the artifacts using an actual supported tool; never fabricate a file reference, ID or URL.
4. Check for an existing filename. Never silently overwrite another file; make a versioned name or follow an explicit, authorized update instruction.
5. **Verify every resulting file** using connector metadata or folder read-back: check name, file ID, type and the correct parent folder. For the default output, confirm **both** `.tex` and `.pdf` are present and return both cloud links. Do not claim that a source-only TeX file is a compiled PDF.
6. If cloud access or upload fails, or the destination cannot be resolved, clearly state what **was and was not saved**. A local fallback may be provided but must not be described as a cloud upload. If just one of the default `.tex`/`.pdf` pair uploads, treat delivery as **incomplete**, report the exact successful file and failed file, and do not delete or overwrite the uploaded item without authorization.

## Optional private Learning Logs

When the student explicitly asks to save a study-session recap, follow [Learning Logs](learning-log.md). Store a **brief Markdown `.md` summary** in the active verified course's `Agent Outputs/Learning Logs/` subfolder. This is a deliberate exception to the general TeX/PDF teaching-document default, because the user requested a log. Create the child folder only when needed and authorized; **never** store private Learning Logs under the public repository `logs/`.

Before appending to an existing dated file, read the current file and preserve earlier sessions. When the provider cannot safely append or replace the full file, create a collision-safe dated session file; do not overwrite silently. Verify cloud name, parent folder and file ID. A learning log is not background recording or a full transcript.

## Generated course indexes

When asked to persist a course map, lecture index or notation registry, store the completed course-specific artifact in the active cloud `Agent Outputs/`. Link it to the source file versions. When new lectures arrive, read and update relevant indexes carefully rather than assuming prior summaries remain current. Keep courses separated by actual folder ancestry and clear filenames.

## Permissions and privacy

Never make course files public, alter sharing or delete/move original source files without explicit permission. This skill defines behavior but cannot itself grant cloud tool access or upload rights.
