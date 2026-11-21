# 2026-11-20 — Trim econ-learn's course-management pages; drop econ-write's "hiding" sentence

- **Date:** 2026-11-20
- **Component:** `econ-learn`, `econ-write`, README
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for two of the cuts proposed in a review of whether the skills had unnecessary restrictions.

- **A.** Four `econ-learn` pages held 3,900 words of procedure written for cloud-drive work: file-ID manifests, a Course State lifecycle, per-step provider updates, three-pass ingestion and a long version-selection procedure. That is 19% of the skill's text for a low-frequency request. Comparison runs showed the skill's value comes from source labels, notation and finding course material, and that it lost points for length. No run had shown these pages to help.
- **D.** `econ-write` ended with "It is not a tool for hiding AI assistance." Meanwhile `econ-learn`'s homework page sends "remove AI traces" requests to `econ-write`. That mixed message invites a lecture in reply to a legitimate editing request. The Defaults already remind the user once when a course or journal requires disclosure.

## Changes made

- `tasks/course.md`, `guides/sources-and-versions.md`, `guides/large-files.md` and `tasks/learning-log.md` were rewritten shorter: 3,900 words down to 1,446. They keep:
  - same-stem grouping, and the rule that a format read must be named;
  - version choice by user, then instructor, then content, never by date or size;
  - the four coverage states that the templates use;
  - "a map is navigation: reopen the original";
  - source precedence;
  - the untrusted-material boundary;
  - on-demand, private learning logs that are appended, never overwritten, and confirmed before claiming a save;
  - honest coverage reporting.
- Dropped: cloud file-ID and checksum fields as requirements, the per-step persistence lifecycle, provider-specific update instructions, repeated warnings about memory and background saving, and procedural detail that restated these rules.
- `econ-write/SKILL.md`: the sentence is removed. The README line now says what the skill does: it reminds once when disclosure is required and leaves the decision to the user.

## Files affected

- `skills/econ-learn/tasks/course.md`, `skills/econ-learn/guides/sources-and-versions.md`, `skills/econ-learn/guides/large-files.md`, `skills/econ-learn/tasks/learning-log.md`.
- `skills/econ-write/SKILL.md`, `README.md`, `CHANGELOG.md`, regenerated `link/` pages.

## Behavior and compatibility

- Course onboarding and resuming from saved maps follow the same principles with less procedure.
- The `course` route page fell from 43,345 to 24,855 bytes.
- Templates, the Course State example, the helper scripts and every pinned preference are unchanged.
- Agents may record less provider metadata (file IDs, checksums) in a Course State unless the template's fields prompt it.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Generators, validation, unit tests, whitespace | Pass | `python3 tools/check_all.py`: all PASS. The course contract tests still find their phrases ("Group same-basename", "filename stem", "one logical", "ask a brief clarification", "untrusted material", "reopen", "course-state.example.json"). The learning-log pin "Default is on demand, not continuous" holds. |
| Anchors | Pass | `whole-lecture.md` still links to `course.md#progressive-verification-states`, and no other anchor into these pages exists. |
| Real course onboarding | Not run | No course collection was run with the shorter pages. |

## Known limitations and risks

The shorter pages give less step-by-step guidance for a large cloud course. If an onboarding run on real material shows a missing step, restore that step alone.

## Follow-up

The next time a whole course is organized, check that versions and coverage are reported correctly.
