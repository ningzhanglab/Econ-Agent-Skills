# Large-File and Long-Course Strategy

Goal: support many lectures and large PDFs/TeX/PPT files without false claims of complete reading, notation drift, excessive re-reading or lost visuals. **No context window can be assumed to hold an entire semester.**

## Start with access and manifest

- Identify the host's real file and page limits, supported formats and retrieval tools **without inventing numerical capacities**.
- Build a source manifest (verified cloud file path/ID and parent folder, type, lecture role, filename, version/date or hash if available, dependencies, parse status).
- Distinguish **file uploaded**, **text extracted**, **pages viewed**, **figures verified**, **equations checked** and **material understood well enough to teach**; these are not equivalent.
- Detect duplicated lectures, separate notes and appendices, revised versions, solution sets and copied filenames.
- Classify **lecture variants** (current handout PDF, presenter PDF, TeX source, dated revisions) and verify the selected source role rather than sorting solely by filename or modified timestamp. See [Course State and Sources](course-state-and-sources.md).
- After a user-requested course onboarding, consider saving a private machine-readable Course State in `Agent Outputs/` so a later session can check version changes before reusing a map.

## Progressive three-pass processing

**Pass A — Discovery:** list accessible files, syllabus, headings, lecture numbers, table of contents, dependencies and obvious missing assets. Produce a provisional map quickly. Do not force deep reading.

**Pass B — Index:** walk each accessible lecture in bounded chunks or page ranges, preserving headings, exact slide/page identifiers, formula anchors and the local notation definitions needed for later retrieval. Record partial coverage and gaps. For large courses, the Agent may need multiple user-approved sessions and persistent authorized storage; never promise autonomous completion after this conversation ends.

**Pass C — Deep reading:** only for the lecture/topic/page needed now, revisit primary material and surrounding assumptions. Inspect images or plots via suitable available tools. Run math/code checks when appropriate and supported. Update the scoped course index/registry afterward if authorized.

If a single file is too large or cannot be parsed accurately, use valid chapter/page-scoped extraction or split into reliable logical segments with overlap and stable locators. Avoid arbitrary truncation that drops assumptions; recover omitted boundaries before inferring a theorem.

## Retrieval budget and grounding

- Pick sources by topic, lecture IDs, syllabus order and dependency edges; ask which fact the answer depends on before loading more files.
- Retain a small working set: target pages, neighboring definitions, prerequisite theorem/model and an optional alternate interpretation. Expand only when the question needs it.
- Do not derive exact formula/figure details from summaries or embeddings; **check the original slide**.
- When only a compressed summary survives, mark its claims preliminary until verified against original material.
- Track ambiguous definitions, notation collisions and conflicting lecture revisions rather than silently choosing one.

## Math, figures and TeX caveats

- Text extraction can corrupt primes, fractions, indexing, equations, Greek letters and table layout. Cross-check exact equations against slide images or original LaTeX where possible.
- LaTeX source may reference external assets: inspect `\input`, `\include`, `\includegraphics`, bibliographies or custom macro files; record missing resources and whether they matter to the requested answer.
- Figure interpretation requires actually viewing the diagram, its axes, units, curves and legends. A caption alone is **not** verification of the plot.
- When slides use macro aliases for symbols, resolve definitions before asserting notation; leave unresolved aliases as such.

## Incremental updates

When course files change:

1. Check modified or added file identity/version.
2. Invalidate affected lecture entries, notation meanings and cross-links.
3. Re-index only changed content and its affected neighbors, preserving version references to avoid mixing old and new notes.
4. Reopen source pages for any high-stakes mathematical or assessment answer.

## Reporting honest coverage

At the end of onboarding, report:

- If the user requested generated files, the verified cloud `Agent Outputs/` path and links or a clear cloud-write failure (see [Cloud Drive workflow](cloud-drive-workflow.md)).

- Files discovered versus successfully indexed/reviewed; only count accessible files.
- Confirmed instructor sequence and any unresolved order.
- Whether figures, equations and `\input` dependencies were actually checked.
- Missing sources and blocked portions.
- Current map location and the next best study step.

**Never** claim "I understand the entire course" when only filenames, section titles or sampled pages were inspected. Do not assume upload = permanent availability across conversations or hosts.
