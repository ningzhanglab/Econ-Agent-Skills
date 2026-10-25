# Figure Index — [Course] [Lecture]

This is a reusable template. A populated course-specific Figure Index belongs in the private cloud Agent Outputs folder when requested, not in this public repository.

## Original source and access

- Main lecture file ID, version, title:
- Student handout PDF file ID, version:
- Presenter PDF (if different):
- External assets and included TeX source files:
- Source pages/frames actually reviewed:

## Figure discovery and provenance

| Figure reference | TeX line / frame title | Source asset or rendered PDF page | Inspection status | Visible axes, labels, content (only after viewing) | Teaching purpose |
| --- | --- | --- | --- | --- | --- |
| policyplot.pdf | [source reference] | [asset ID or exact handout page] | REFERENCED_ONLY | Not inspected | Policy function near borrowing constraint |

Statuses must be precise:

- REFERENCED_ONLY: a reference exists but no image viewed.
- ASSET_LOCATED_NOT_VISUALLY_REVIEWED: a matching local/cloud asset was found, not visually inspected.
- SOURCE_IMAGE_VISUALLY_REVIEWED: actual original image inspected.
- RENDERED_PDF_VISUALLY_REVIEWED: matching rendered slide PDF page inspected.
- BLOCKED: missing, inaccessible or unreadable source figure.
- INDEPENDENT_SCHEMATIC: independently drawn illustration, not a recreated original figure.
- COMPUTED_PLOT: produced from actual model/data computation; record method, parameters, data and errors.

## Source recovery workflow

1. Find references in original slides, source TeX, included chapters and figure folders. The helper at [TeX figure inventory](../../../scripts/inventory_tex_figures.py) locates simple TeX references, but cannot visually inspect them.
2. If an image is absent, inspect the corresponding *rendered handout PDF* for an embedded original figure; a TeX frame number is not automatically a PDF page number.
3. Record the true image asset ID or PDF page locator and only then describe axes, curves and values.
4. If unavailable in all checked sources, explicitly mark BLOCKED. You may teach the mechanism with a separately labeled new analytical schematic; do not impersonate the unseen original.
5. Link figures to equations and economic intuition and preserve the original lecture's notation.

No quota or minimum figure count. Original reviewed figures can be used whenever relevant; new visuals are encouraged when pedagogically valuable, not as decoration. When generating TeX/PDF, keep required image dependencies with the delivered files and test clean-room compilation.
