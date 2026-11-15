# 2026-11-14 — Review fixes: unsupplied papers, not-installed rule, validator and zip builder

- **Date:** 2026-11-14
- **Component:** all three skills, `tests/validate_skills.py`, `tools/build_skill_zips.py`, `README.md`
- **Change type:** Fixed / Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

A read-only review of commits `898730a..c1c6c28` (the outside-course mode, per-skill zips and self-contained skill folders) found no reason to revert anything but listed several small problems. The user asked for all of them to be fixed on `main`, except publishing the first release, which only the maintainer can do. The user also agreed to replace the "not installed" sentence after discussing whether skills should be barred from one another.

## Changes made

Teaching (`econ-teaching`):

- **A paper that is named but not supplied.** The paper rows asked for the main result "with its magnitude", and `SKILL.md` says to explain from general knowledge when there is no source. Together these invited numbers and equations written from memory. Now: say the paper was not read, give only a short outline labeled as general knowledge, with no magnitudes, equation numbers or page references, and ask for the PDF.
- **Paper overview row.** The link to a standard model is now "if it helps" instead of always; the magnitude is given "where there is one" (a theory paper may have none); "why it holds" is added, which evaluation case 58 already required; the closing one-sentence contribution applies after going deeper, so a short first answer does not state the contribution twice.
- **Duplicates removed.** The "small thing they could not follow" row repeated the Quick clarification row of the first table and is now one pointing sentence. The "one part of a paper" row no longer repeats the citation rule that Slide Fidelity owns.
- **Lecture and paper together.** Slide Fidelity now says the source the student is asking about sets the notation and the other is additional perspective.
- **Description.** "a research paper" became "a published research paper the student is reading", to lower the chance of triggering on the user's own draft (`econ-writing`).
- **Evaluation case 58** matches the rule (exhibit, optional standard-model link, magnitude where there is one) and gains a variant for a named but unsupplied paper.

Not-installed rule (all three skills):

- Was: "If that skill is not installed, say so and do not do its job without its rules." This could make a skill refuse a simple question that it can answer safely, and it was never tried in real use.
- Now: "say so in one line, then help only as far as this skill's own rules allow." `econ-teaching` adds the one protection that matters when `econ-research` is missing: never list papers, years or findings from memory; name the topic and say the references are unverified. Each skill's safety no longer depends on another skill being installed.

Tooling:

- `tests/validate_skills.py`: new `repo_file_mentions` fails if any text file in a skill names `STORAGE_POLICY.md`, `AGENTS.md`, `CHANGELOG.md` or `DESIGN_V1.md`. The earlier outside-link check could not have caught the bug it was written for, because that pointer was plain text, not a link. The link check now also covers angle-bracket links, images with an empty label, reference-style definitions, HTML `href`/`src` and `file:` URLs.
- `tools/build_skill_zips.py`: inside a Git checkout only tracked files are zipped, so an untracked private file left in a skill folder cannot reach a local build. A skill folder with nothing tracked is refused. Outside Git the builder behaves as before.
- `tests/test_skill_zips.py`: six new tests (untracked file left out; nothing tracked refused; other link forms reported; inside links with a title or anchor not reported; plain-text pointer reported; real skills name no repository file).

README: the update instruction for Claude Code now says to delete the old folder before unzipping (`unzip -o` left removed files behind); the paste-a-link limits name why some reference files may not be fetched; the local build line notes the tracked-files rule.

## Files affected

- `skills/econ-teaching/SKILL.md`, `skills/econ-teaching/references/teaching-design.md`, `skills/econ-teaching/references/slide-fidelity.md`
- `skills/econ-writing/SKILL.md`, `skills/econ-research/SKILL.md`
- `tests/validate_skills.py`, `tests/test_skill_zips.py`, `tests/professor-evaluation.md`
- `tools/build_skill_zips.py`
- `README.md`, `CHANGELOG.md`, `logs/2026-11-14-self-contained-skills.md` (correction appended)

## Behavior and compatibility

- Course-based teaching is unchanged. Outside a course, a named paper with no file now gets an honest outline and a request for the PDF instead of a detailed summary.
- A skill used alone now helps within its own rules instead of declining when a request belongs to a skill that is not installed.
- `econ-teaching` description: 915 → 948 characters (limit 1024). `econ-teaching/SKILL.md`: 13,224 → 13,388 characters. `teaching-design.md` is slightly shorter than before.
- A local zip build now needs the skill's files to be tracked by Git when run inside a checkout. The release workflow builds from a clean checkout and produces the same file lists as before.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills OK (Python 3.9.6, local) |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 51 tests OK (45 before, 6 new), including the LaTeX compile smoke test |
| New check against the original bug | Pass | Run on the `ee67b5a` copy of `skills/`: `repo_file_mentions` reports the `STORAGE_POLICY.md` mentions in `econ-writing/SKILL.md` and `econ-teaching/references/cloud-drive-workflow.md`; the old link check reported nothing there |
| Zip builder, local | Pass | Built econ-research (6 files), econ-teaching (32 files), econ-writing (5 files), the same counts as before the change |
| GitHub Actions on the four reviewed commits | Pass | "Validate Agent Skills" completed with success for `4720edf`, `ee67b5a`, `9f3fde6` and `c1c6c28`, read from the public GitHub API during the review |
| GitHub Actions on this change | Not run | Not checked at the time of writing |
| Release workflow on GitHub | Not run | No release has been published; the download links in the README still return 404 |
| Real evaluation of cases 57–60 and the new variant | Not run | No real paper or screenshot fixture was used |
| Not-installed rule with a single installed skill | Not run | Not tried in a host with only one skill installed |
| Uploading a zip to Claude.ai | Not run | Not tested |

## Known limitations and risks

- The link check still treats links inside fenced code blocks as real links, and it reads Markdown files only. The repository-file check reads every text file but knows only the four listed names.
- In `SKILL.md`, a link with a `"title"` or math such as `f[0,1](x)` is reported by the older broken-reference check. No skill has either today.
- The zip builder skips files ending in `.log` or `.out` and stores every file as mode 0644, so an executable bit would be lost. No skill has such files today.
- The release workflow runs the structural validator but not the unit tests, and it also runs for a pre-release, which `releases/latest/download` does not point to.
- Whether the narrower description changes which skill a host picks is untested.

## Follow-up

For the maintainer: publish the first release, confirm the three zips are attached, and upload one zip to Claude.ai once. Run cases 57–60 on a real term, paper and screenshot, and try one skill installed alone.
