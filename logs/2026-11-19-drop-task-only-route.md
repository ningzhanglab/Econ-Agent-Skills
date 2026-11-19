# 2026-11-19 — Drop the task-only route and relax the reference title match

- **Date:** 2026-11-19
- **Component:** Link editions, `econ-research`, README
- **Change type:** Changed / Fixed / Documentation
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

A review of the [follow-up audit](2026-11-19-follow-up-skill-audit.md) checked each change against the repository's rule that a new rule needs an observed failure, a user requirement or a missing capability.

- The task-only route ("if you already read the main `econ-learn` instructions in this chat, open only the task page") came from a byte-count review, not an observed failure. The [earlier log](2026-11-19-combined-link-and-review-fixes.md) had made further route changes depend on a fresh Project comparison, which has not been run. The route also asks the model to judge what it read earlier in the chat, which it may get wrong.
- The reference checker had changed from a similarity threshold to an exact normalized title match. That catches reordered titles, but it also warns when a correct title differs from Crossref's only by a subtitle in the separate `subtitle` field, by `&` written as "and", or by HTML markup in the record.
- The README status line said the skills share one link and then cited evaluations, which ran the skill files rather than the link. One README paragraph addressed the model's routing rule to the reader and restated a rule kept in the combined index.

## Changes made

- **Combined link.** The index keeps both links on the term and homework rows. It opens the combined page and names the main skill page and task page as the fallback. The task-only instruction is removed.
- **Reference checks.** A title passes when its normalized words equal the record's title, the record's title plus its `subtitle`, or the part before a colon. Markup is stripped and `&` is read as "and" before comparison. The FAIL threshold uses the closest of these forms. A reordered title still receives WARN.
- **README.** The status line says the comparisons ran the skill files and that the paste-a-link method has been checked only for whether pages open. The combined-entry paragraph no longer gives the routing rule.

## Files affected

- `tools/build_link_editions.py` and generated `link/` pages: index note.
- `skills/econ-research/scripts/verify_references.py` and `tests/test_research_contracts.py`: title forms and one regression test.
- `README.md`, `CHANGELOG.md`, and a marked correction appended to the follow-up audit log.

## Behavior and compatibility

All link addresses are unchanged. The index is 2,358 bytes, down from 2,486 and up from 2,060 before the follow-up audit. The term route reads 18,658 bytes and the time-series homework route 31,414 bytes, counted as in the earlier log. After `econ-learn` has been read, a second term or homework request again opens the combined page, as it did before the follow-up audit. Bibliography entries that previously received WARN for a subtitle, `&` or markup difference now receive PASS.

## Verification and evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Build and validation | Pass | `python3 tools/build_all.py`, `--check`, `python3 tests/validate_skills.py` (4 skills) and `git diff --check`. |
| Unit tests | Pass | `python3 -m unittest discover -s tests`: 79 tests, OK. The new test covers a Crossref `subtitle` field, a record title with a colon and `&amp;`, and HTML markup. The reordered-title test still gives WARN. |
| CI and published links | Not run | Not pushed when this log was written. |
| Fresh model comparison in the user's Project | Not run | Still the open follow-up from both earlier logs. |

## Known limitations and risks

A `.bib` title that leaves out the subtitle passes. A subtitle that is present but wrong still receives WARN. Second requests in a chat again read the full combined page.

## Follow-up

Run the fresh Project comparison (combined page versus separate pages, first and second request) before reintroducing a task-only route.
