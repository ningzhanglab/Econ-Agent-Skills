# 2026-11-15 — Link editions for the paste-a-link method

- **Date:** 2026-11-15
- **Component:** repository tooling and documentation (all three skills are read, none is changed)
- **Change type:** Fixed / Added
- **Status:** Implemented; not yet tried in a real chat app
- **Related commit / PR:** See Git history for this change

## Motivation

The user reported that agents given a skill by link were not reading all the files the skill requires. Which chat app showed this, and whether the agent failed to open the files or did not try, was not established.

Two likely causes, both from how the method worked:

1. `SKILL.md` links its references by relative path. An installed skill resolves these on disk. An agent reading from a URL must build each address itself, and many chat apps only open addresses that appear word for word in the conversation or in a page already read. A built address has appeared nowhere, so it is refused.
2. Nothing on the page told the agent that the reference files are required, so it answered from `SKILL.md` alone.

Options considered:

- **One bundle file per skill** (`SKILL.md` plus every reference). One fetch, but roughly 40k tokens for `econ-teaching` on every use, and fetch tools often cut long pages. Not chosen.
- **Stronger wording in the README prompt only.** Does nothing about refused addresses. Not chosen.
- **Put full addresses back into `SKILL.md`.** This is the note removed on 2026-11-14: it hard-codes the repository address into every portable skill and is read by every installed user. Not chosen.
- **A generated link edition outside the skill folders.** Chosen.

## Changes made

- `tools/build_link_editions.py`: for each skill writes `link/<skill>.md`, containing a note for the agent, the frontmatter as a code block, the `SKILL.md` body with every relative link rewritten to its full raw GitHub address (an anchor becomes `(section "...")` after the link, since a raw file has no anchors), and a file index listing every file of the skill with its full address. `--check` writes nothing and fails if a file is out of date. It refuses a link to a missing file.
- The note tells the agent to open each reference file the page names for the request, to resolve links inside a reference file through the file index, to say which file could not be opened and not guess its content, and to end the first answer with one line listing the skill files it read.
- `link/econ-teaching.md`, `link/econ-writing.md`, `link/econ-research.md`: generated and committed.
- `tests/test_link_editions.py`: five tests (committed files match the skills; no relative link left; every address points to a real file; every linked reference and every skill file is in the index; note and description present).
- `README.md`: the three paste-a-link prompts point to the link editions; the limits say what the closing line is for; maintainer note to rebuild `link/` after changing a skill; layout tree updated.

## Files affected

- `tools/build_link_editions.py`, `tests/test_link_editions.py`, `link/*.md` (new)
- `README.md`, `CHANGELOG.md`

## Behavior and compatibility

- Skill folders are untouched, so installed and zipped skills behave exactly as before and still contain no repository address.
- Pasting a raw `SKILL.md` link still works as badly as before; the README no longer suggests it.
- The link edition asks for one extra line at the end of the first answer (the files read). This applies only to the paste-a-link method.
- The addresses name `ningzhanglab/Econ-Agent-Skills` and the `main` branch; a fork must change `RAW_BASE` in the tool and rebuild.
- Sizes: `link/econ-teaching.md` 23,022 characters (its `SKILL.md` is about 13,400), `econ-writing` 9,871, `econ-research` 9,420. The extra is the full addresses and the file index.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills OK |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 56 tests OK (51 before, 5 new), Python 3.9.6, local |
| `--check` on the committed files | Pass | `python3 tools/build_link_editions.py --check` reports all three up to date |
| Raw addresses of the link editions on GitHub | Not run | The files do not exist on `main` until this change is pushed |
| Real chat app following a link edition | Not run | No chat app was driven; whether a given app now opens the reference files is untested |
| GitHub Actions | Not run | Not checked at the time of writing |

## Known limitations and risks

- The method stays best-effort. An agent can still skip a file; the closing line makes that visible instead of silent. Installing the zip is the reliable route.
- Links inside reference files are still relative. The agent has to look the target up in the file index; this is an instruction, not a guarantee.
- Some chat apps cannot open `raw.githubusercontent.com` at all; nothing here helps with that.
- The link editions must be rebuilt after any change to a `SKILL.md` or to the set of files in a skill. The test catches a stale file in CI, not before a push.

## Follow-up

Try one link edition in the chat app where the problem was seen and note which files the answer lists. If references are still skipped, consider naming two or three always-required files per skill in the note.
