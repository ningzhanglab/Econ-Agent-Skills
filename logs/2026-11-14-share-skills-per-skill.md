# 2026-11-14 — Share one skill at a time

- **Date:** 2026-11-14
- **Component:** all three skills, repository tooling and documentation
- **Change type:** Added
- **Status:** Implemented; the first release has not been published yet
- **Related commit / PR:** See Git history for this change

## Motivation

The user wants to share the skills with other people, and often only one skill (for example only `econ-teaching`). Options discussed:

- **One link for all skills** (a root `USE-BY-LINK.md` telling a chat agent which skill to load). Drafted in this session and removed before commit: it is a second way to do the same thing, and sharing one skill is simpler with one link per skill.
- **Paste a `SKILL.md` link into a chat.** Works without installing and always reads the newest `main`, but must be repeated in every chat and depends on the agent fetching the reference files, where most detailed rules live. Kept as the "try it" option.
- **Plugin marketplace.** Updates automatically, but only for Claude Code users. Not chosen.
- **One zip per skill, attached to GitHub releases.** An installed skill triggers by itself and has all its files; one stable link per skill; works in Claude.ai and in skills folders. Chosen as the main method.

The user asked whether downloads update automatically. They do not: a zip is a copy, and people re-download from the same link to update. Zips are built only when the maintainer publishes a release, so unfinished work pushed to `main` never reaches people who download.

## Changes made

- `.github/workflows/release-skills.yml`: on a published release, validate the skills, build the three zips and attach them to the release with `gh release upload --clobber`. Needs `contents: write`; uses the built-in `GITHUB_TOKEN`.
- `tools/build_skill_zips.py`: standard-library builder. Each zip contains only `<skill>/…` at its top level; skips `.DS_Store`, `__pycache__`, `.pyc` and LaTeX by-products and symlinks; fixed timestamps make it reproducible; refuses a folder without `SKILL.md`.
- `tests/test_skill_zips.py`: five offline tests (real skills build with the folder at top and no junk or repo folders; junk skipped and sibling skills excluded; reproducible; no `SKILL.md` refused; unknown skill name fails).
- A one-paragraph note at the top of each `SKILL.md` with the raw GitHub folder URL for its linked files, for the paste-a-link method.
- `README.md`: "Share a skill" section (download links, installing in Claude.ai and Claude Code, paste prompt, updates, publishing a version, local build); repo-layout tree corrected and extended.
- `.gitignore`: `dist/`.

## Files affected

- `.github/workflows/release-skills.yml`, `tools/build_skill_zips.py`, `tests/test_skill_zips.py` (new)
- `skills/econ-teaching/SKILL.md`, `skills/econ-writing/SKILL.md`, `skills/econ-research/SKILL.md` (link note)
- `README.md`, `CHANGELOG.md`, `.gitignore`

## Behavior and compatibility

Installed skills behave as before; the `SKILL.md` note matters only when the file is read from a URL. The download links return 404 until the first release is published. The raw URLs and download links name `ningzhanglab/Econ-Agent-Skills`; a fork would need to change them.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Zip builder, local | Pass | `python tools/build_skill_zips.py` built econ-research (6 files), econ-teaching (32 files), econ-writing (5 files); `unzip -l` showed `econ-teaching/…` paths only |
| Unit tests | Pass | `python -m unittest discover -s tests -p 'test_*.py'`, including the five new zip tests, run before committing |
| Automated structural validation | Pass | `python tests/validate_skills.py` |
| Raw `SKILL.md` and reference URLs | Pass | `curl` returned HTTP 200 for the three `SKILL.md` raw URLs and two `econ-teaching` reference files |
| Release workflow on GitHub | Not run | Runs only when a release is published; none has been published yet |
| Uploading a zip to Claude.ai | Not run | Not tested in this session |

## Known limitations and risks

- The release workflow is untested until the first release; if it fails, the release has no zips and the download links return 404.
- Claude.ai's upload rules (size, required fields, whether code execution must be on) were not checked against a real upload.
- Downloaded copies go stale silently; the README tells users to re-download.

## Follow-up

Publish the first release, confirm the three zips appear on it, download `econ-teaching.zip` from the stable link and upload it to Claude.ai once.

## Correction (2026-11-14, later the same day)

The note at the top of each `SKILL.md` giving the raw GitHub folder was removed; the address now lives in each skill's paste-a-link prompt in the README. See [Self-contained skill folders](2026-11-14-self-contained-skills.md).
