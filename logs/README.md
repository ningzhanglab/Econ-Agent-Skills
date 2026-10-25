# Detailed Change Logs

This directory records **why and how** the repository changed. Use it alongside:

- [CHANGELOG.md](../CHANGELOG.md): quick, newest-first change summary.
- Git history: authoritative diffs, authorship and commits.
- [AGENTS.md](../AGENTS.md): instructions requiring logs in future Agent changes.

## Naming

Write one record for each logical change:

```text
logs/YYYY-MM-DD-short-descriptive-slug.md
```

For example, `logs/2026-10-24-professor-v0.1.md` or `logs/2026-10-24-add-equilibrium-examples.md`.

Use a **new unique filename** when multiple changes occur on the same date. Never reuse a filename to describe an unrelated later modification.

## Procedure

1. Copy [TEMPLATE.md](TEMPLATE.md) into a new dated file.
2. Fill in all relevant fields: scope, motivation, changes, files, behavior, validation, limitations and next steps.
3. Add a short, linked entry at the **top of the relevant date section** in [CHANGELOG.md](../CHANGELOG.md).
4. Commit the log together with its corresponding changes. The Git commit is the authoritative source for exact file diffs.
5. If future evaluation finds a problem, add a **new** correction record and link back; do not erase historical evidence.

## What to capture

- **Changed:** what concrete files, workflows, or instructional rules changed?
- **Why:** which user requirement, bug, failure, or new use case motivated it?
- **Behavior:** what will the Agent now do differently?
- **Verification:** what did you execute or inspect? What passed, failed, or wasn't run?
- **Risk/next steps:** what remains unknown or unresolved?

Be economical. Logs are **decision and validation records**, not copies of every modified file.

## Current records

- [2026-10-24 — Professor: adaptive visuals, Homework connections and minimal TeX/PDF outputs](2026-10-24-professor-visuals-homework-texpdf.md).

- [2026-10-24 — Set exact cloud destination to Agent Outputs](2026-10-24-agent-outputs-convention.md).

- [2026-10-24 — Professor Cloud Drive input and `outputs/` delivery policy](2026-10-24-professor-cloud-outputs.md).

- [2026-10-24 — Professor course navigation and large-file strategy](2026-10-24-professor-course-navigation.md).

- [2026-10-24 — Professor v0.1 dynamic-programming lecture smoke test](2026-10-24-professor-dldp-smoke-test.md).

- [2026-10-24 — Add repository change logging](2026-10-24-logging-system.md).
- [2026-10-24 — Initial Professor v0.1](2026-10-24-professor-v0.1.md).
