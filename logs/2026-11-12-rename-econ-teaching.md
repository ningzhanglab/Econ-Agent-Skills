# 2026-11-12 — Rename `econ-phd-professor` to `econ-teaching`

- **Date:** 2026-11-12
- **Component:** `econ-teaching` (formerly `econ-phd-professor`), planned `econ-research` (formerly `econ-research-agent`), repository documentation and tests
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change (branch `feat/econ-writing-skill`, after the commit that added `econ-writing`)

## Motivation

With [`econ-writing`](2026-11-12-econ-writing-skill.md) added, the repository's skill names followed three patterns: a role with a level (`econ-phd-professor`), an activity (`econ-writing`) and a role with "agent" (`econ-research-agent`). The user chose to rename them so that each skill is named after what it does, and to do it now, before more installs depend on the old name.

## Changes made

- `git mv skills/econ-phd-professor skills/econ-teaching`; SKILL.md `name: econ-teaching`.
- The skill's heading, mission and persona are unchanged ("Econ PhD Professor"). Its description, which decides when it triggers, is unchanged.
- `agents/openai.yaml` default prompt now uses `$econ-teaching`; the display name stays "Econ PhD Professor".
- Usage lines in the three helper scripts, the self-reference in `references/time-series.md` and the cross-reference in `econ-writing/SKILL.md` updated.
- The planned research skill is now called `econ-research` in README, AGENTS.md, STORAGE_POLICY.md, DESIGN_V1.md and the teaching skill's scope note.
- README: catalog, status line with a rename notice, install steps and repo tree. AGENTS.md, DESIGN_V1.md and STORAGE_POLICY.md: name and link updates.
- `tests/test_professor_contracts.py`: skill path updated.
- CHANGELOG: link targets in older entries now point to `skills/econ-teaching/` so the active-link test passes; their prose and headings keep the old name. Dated logs are unchanged, so their links to `skills/econ-phd-professor/` no longer resolve; the link test excludes logs by design.

## Files affected

- `skills/econ-teaching/**` (moved from `skills/econ-phd-professor/**`): rename plus the edits listed above.
- `skills/econ-writing/SKILL.md`: cross-reference.
- `README.md`, `AGENTS.md`, `DESIGN_V1.md`, `STORAGE_POLICY.md`, `CHANGELOG.md`: names and links.
- `tests/test_professor_contracts.py`: path.

## Behavior and compatibility

Breaking for existing installs: a client that installed `skills/econ-phd-professor/` keeps the old copy until the user installs `skills/econ-teaching/`, and prompts that call `$econ-phd-professor` need the new name. The skill's instructions and behavior are unchanged. GitHub serves the repository at the same URL; old links to the folder path on GitHub will not resolve.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | `grep` finds no `econ-phd-professor` or `econ-research-agent` outside dated logs and historical CHANGELOG prose |
| Automated structural validation | Pass | `python3 tests/validate_skills.py` and `python3 -m unittest discover -s tests -p 'test_*.py'` run locally after the rename |
| Real slide / domain evaluation | N/A | No behavior change |
| GitHub Actions or other CI | Not run | Not yet run on the pushed branch at the time of writing |

## Known limitations and risks

- Links inside dated logs point to the old folder and are left as historical records.
- Anyone who copied the old folder has two copies until they remove it.

## Follow-up

- After merge, remove the old installed folder from any local client and reinstall `skills/econ-teaching/`.
