# 2026-10-24 — Validate Active Markdown Links in CI

- **Date:** 2026-10-24
- **Component:** Repository tests and reference integrity
- **Status:** Implemented; verify CI run on final commit

## Motivation

The old structural test checked relative links in SKILL.md but not in all active references, templates, README, policies and test guidance. A typo could therefore point an Agent to a missing file without breaking CI.

## Change

Added tests/test_repo_links.py using Python standard library to scan active Markdown documents recursively, check that local file/directory links exist and are inside the repository, and ignore external HTTP links (no network access). Date-stamped historical logs remain append-only and excluded.

## Verification and limits

CI result for this commit must be read separately. This only checks target existence and path containment; it does not prove link semantics, external website availability, teaching correctness or Google Drive upload.

## Files

tests/test_repo_links.py; README.md; CHANGELOG.md; logs/README.md; this record.
