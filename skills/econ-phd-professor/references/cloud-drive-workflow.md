# Cloud Drive Workflow — Source Materials and Outputs

Apply when the user's lecture files reside in a connected cloud drive, or when the user requests a generated file.

## Storage contract

- **Inputs:** use the user's authorized cloud workspace as the source of slides, syllabus, homework, readings, TeX dependencies and diagrams. Use connected Google Drive when available; respect another explicitly named accessible provider.
- **Outputs:** save **every requested final file** (notes, proof, PDF, DOCX, LaTeX, course map, lecture index, notation registry, spreadsheet, etc.) to the cloud **`outputs/` folder**, not only to a temporary local path, chat attachment or the public GitHub skills repository.
- Do **not** produce an unsolicited file for an ordinary chat explanation. Source files remain in the original course folder. Do not upload private source materials or generated course content to public GitHub.

## Identify the destination before writing

1. Follow an exact destination folder link or ID explicitly provided by the user.
2. Otherwise identify the active course workspace using accessible source file metadata, parent folder and syllabus; do not guess based on filename similarity.
3. Select a child folder named **exactly `outputs`** in that verified course workspace. If absent, and the connected provider allows it, create it **only when an output is requested**.
4. If the source course files are genuinely at cloud root with no course workspace, use or create the verified **root `outputs`** folder.
5. If multiple plausible course workspaces or exact destination folders remain, resolve by evidence or ask one targeted destination question. Never put files in an arbitrary unrelated folder.
6. Folder names `agent outputs`, `Agent output`, `output`, and `generated` do **not** qualify as the exact name `outputs`; fuzzy search is not enough. Check the parent and exact name before selecting or creating a folder.

## Read and teach from cloud sources

- Use cloud file/folder discovery and metadata to locate the course version and source. Read primary slide pages and relevant neighboring definitions; do not mistake search snippets or indexes for reading source.
- For cloud-native Docs, Sheets and Slides, use supported content workflows. For stored PDF, TeX, images and Office files, use supported file read/download tools as needed.
- Recheck mathematical notation and figure contents from the originals where available. A LaTeX source referring to missing graphics does not grant access to those images.
- Follow [Course Navigation](course-navigation.md) and [Large-File Strategy](large-file-strategy.md) for staged indexing and source fidelity.

## Create, upload and verify requested output

1. Respect the requested **file format and filename**. If no filename was specified, use an informative, course-scoped name such as `ECONS509_L08_notes_2026-10-24.pdf` or `ECONS509_course_map.md`.
2. Generate the real output via available tools. If it is created locally first, treat the local file as **intermediate**, not as the final delivery.
3. Find or create the exact destination `outputs/` folder as above, then upload the file or create/move the native cloud document into that folder using supported tools.
4. Check for an existing filename. Never silently overwrite another file; make a versioned name or follow an explicit, authorized update instruction.
5. **Verify the resulting file** using connector metadata or a folder read-back: check name, file ID, type and the correct parent folder. Return the verified cloud link and destination.
6. If cloud access or upload fails, or the destination cannot be resolved, clearly state that the file was **not saved to the cloud**. A local fallback may be provided but must not be described as a cloud upload.

## Generated course indexes

When asked to persist a course map, lecture index or notation registry, store the completed course-specific artifact in the active cloud `outputs/`. Link it to the source file versions. When new lectures arrive, read and update relevant indexes carefully rather than assuming prior summaries remain current. Keep courses separated by actual folder ancestry and clear filenames.

## Permissions and privacy

Never make course files public, alter sharing or delete/move original source files without explicit permission. This skill defines behavior but cannot itself grant cloud tool access or upload rights.
