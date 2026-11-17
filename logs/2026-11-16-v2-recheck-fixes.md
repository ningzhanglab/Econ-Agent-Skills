# 2026-11-16 — v2 recheck: duplicates, leftovers, script paths, Beamer in CI

- **Date:** 2026-11-16
- **Component:** `econ-research`, `econ-learn`, CI
- **Change type:** Fixed / Testing
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for a recheck of v2 after reading the logs. Three small issues were found and fixed. The user then asked to think the whole recheck over again; a second pass read the task pages, guides, templates and scripts the first pass had skipped and found the items under "Second pass".

## Changes made

- **`econ-research/SKILL.md`:** the scoping rule (a single-word topic or unclear field gets one focused question before searching) was stated both under Defaults and below the routing table. The second copy now points to Defaults. The "Task files" list, which repeated the routing table's links, is removed; the credits paragraph that followed it keeps its own heading.
- **`econ-learn/tasks/paper.md`:** when only fetched text of a linked source came back, the page asked for the file "not a screenshot of one page", while `SKILL.md` asks for a screenshot of a single unreadable page. The sentence now says why the cases differ: the whole source is unseen, so one page is not enough; the screenshot request is for a single unreadable page.
- **CI (`.github/workflows/validate-skills.yml`):** the TeX install had only `texlive-latex-base`, so `test_slides_template_compiles_cleanly` was always skipped on GitHub. It now also installs `texlive-latex-recommended` (Beamer) and `texlive-pictures` (pgf, which Beamer needs).
- **Second pass.**
  - The bundle checker's usage line said `python skills/econ-learn/scripts/check_tex_bundle.py`, and its copy in `econ-present` therefore named another skill's folder, which an `econ-present` installed alone does not have. Every script's usage line, and the reference-checker commands on the literature-search page, now read `python3 scripts/<name>.py`, run from the skill's folder.
  - `econ-research/tasks/literature-search.md` restated three Defaults from `SKILL.md` ("recent" as five years, scoping a single-word topic, ranking by relevance then influence). Each now points to the skill's Defaults, where the pinned phrase stays.
  - Five `econ-learn` templates said they were "a reusable template in GitHub" and told the agent to save to a "cloud" `Agent Outputs/` and return a cloud link, which is wrong for a local course folder and repeats the delivery page. Each now has one note: a filled copy is saved only on request, as Deliver a file describes, never in a public repository.
  - `tasks/learning-log.md` described the repository's own `logs/` folder (maintainer text, naming a folder outside the skill) and called itself a "behavior reference"; `guides/time-series.md` called itself a "domain reference". Both reworded.

## Files affected

`skills/econ-research/SKILL.md`, `skills/econ-research/tasks/literature-search.md`, `skills/econ-research/scripts/verify_references.py`; `skills/econ-learn/tasks/paper.md`, `tasks/learning-log.md`, `guides/time-series.md`, five files in `templates/`, three scripts in `scripts/`; `shared/scripts/check_tex_bundle.py` and its two copies; `.github/workflows/validate-skills.yml`; `link/econ-learn.md`, `link/econ-present.md`, `link/econ-research.md` (rebuilt); `CHANGELOG.md`, this log.

## Behavior and compatibility

No rule changed. Agents read each `econ-research` Default once, see no apparent conflict between the two screenshot instructions, and get a script command that works in an installed skill. Templates no longer imply that every course folder is in the cloud. CI now runs the slides-template compile test instead of skipping it.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read every changed file's diff. Second pass read all `econ-learn` task pages, the literature-search page and the templates' notes; `econ-write` guides and the remaining `econ-learn` guides were searched for v1 wording, not read in full |
| Automated structural validation | Pass | `python3 tools/build_all.py` (three link editions rewritten), `python3 tests/validate_skills.py` (4 skills), `python3 -m unittest discover -s tests` (66 tests, slides template compiled locally). `--help` ran for three changed scripts; the bundle checker ran from `skills/econ-present` with the new command form |
| Real slide / domain evaluation | Not run | Editorial change only |
| GitHub Actions or other CI | Not run | Not pushed; whether the Ubuntu packages are enough for Beamer is unconfirmed until the workflow runs |

## Known limitations and risks

If the CI image needs a further TeX package, the slides compile test will fail on GitHub rather than skip; the log of the first run will show which.

## Follow-up

Still open from the earlier v2 logs: run `econ-present`, `econ-write` and `econ-research` on real material; re-run the comparison cases and count the files read; try slides triggering in a real client; publish a v2 release so the README zip links resolve.
