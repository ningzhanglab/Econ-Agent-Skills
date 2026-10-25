# Cloud Storage and Agent Output Requirements

Applies to all present and future skills in this repository, including `econ-phd-professor` and the planned `econ-research-agent`. The **default** folder name for user-requested cloud deliverables is **`Agent Outputs`**, with exact capitalization and spacing.

## Inputs and outputs

- Read lecture Slides, PDF/TeX files, syllabus, assignments, figures, data and readings from the user's **authorized connected cloud workspace**. Do not put private course material in this public GitHub skills repository.
- Unless the user explicitly requests another destination for a task, save **every requested generated file** in the verified active course folder's direct child **`Agent Outputs/`**, retaining its requested name and format. **An explicitly selected existing course folder (even with a different literal name) overrides the default for that course**; verify its ID and do not create a second output folder solely to enforce the default name.
- If sources are genuinely at cloud drive root with no course folder, use the verified root `Agent Outputs/`.
- An ordinary chat explanation is not a request to create a file.

## Professor's default file formats

For `econ-phd-professor`, if the user requests a generated teaching/study file but **does not specify a format**, deliver **both a matched `.tex` source and a compiled `.pdf`**, using a minimal LaTeX article template. Save and independently verify **both** files in the same `Agent Outputs/` folder. An explicit single or alternative format overrides this default. Chat explanations do not create files. See [TeX/PDF Outputs](skills/econ-phd-professor/references/latex-outputs.md).

## Exact destination workflow

1. Use an exact user-provided folder link/ID when supplied. Otherwise determine course folder through source file parents, syllabus and metadata; do not guess from filenames.
2. **Reuse** the current course folder's exact `Agent Outputs` child if present. Create it only if absent, needed for an actual output, and authorized by connector permissions.
3. Lowercase `outputs`, `agent outputs`, singular `Agent output`, and other similar names are **not equivalent**. When legacy `outputs` coexists with `Agent Outputs`, use `Agent Outputs`; do not create a duplicate or automatically delete legacy folders.
4. Generate the requested format; avoid silent overwrites, preserving earlier versions unless an update is explicitly authorized.
5. Verify cloud upload/create/move with file metadata or folder read-back, including file ID, name/type and **correct parent ID**. Return the verified cloud link.
6. If access, destination resolution or write fails, state that cloud saving was **not completed**. A local file is not equivalent.

## Repository and historical logs

- GitHub stores reusable Skills, templates, tests and non-sensitive change logs. Completed course maps, lecture indexes, notation registries, documents and research outputs stay in the course's `Agent Outputs/`.
- [AGENTS.md](AGENTS.md) governs development changes; update [CHANGELOG.md](CHANGELOG.md) and add a new dated log for material policy changes.
- Past dated logs mention an older `outputs/` convention. Those are historical records, **superseded by this policy**; preserve them unchanged.
- Professor implementation details: [Cloud Drive Workflow](skills/econ-phd-professor/references/cloud-drive-workflow.md).

## Example

```text
Econs 509/
├── lecture/
├── assignments/
├── syllabus/
└── Agent Outputs/
    └── ECONS509_Course_Map_Multifile_Test_2026-10-24
```
