# 2026-11-24 — Final audit fixes

- **Date:** 2026-11-24
- **Component:** TeX bundle delivery, reference checker and Project evaluation
- **Change type:** Fixed / Changed / Testing
- **Status:** Implemented locally
- **Related commit / PR:** Local Git could not create `.git/index.lock`. No commit was made.

## Motivation

The final audit found that an entry missing its opening delimiter, or a plain-text file, could produce an empty JSON result and exit successfully. It also found that a checked TeX/PDF bundle could be recompiled just to verify a copy, and that the Project evaluation treated opening a needed template as an extra fetch.

## Changes made

- The BibTeX checker reports malformed entry headers, non-BibTeX input and file read failures as `ERROR`. A blank or comment-only bibliography produces an explicit `SKIP` with zero entries checked. A valid entry after a malformed header is still checked.
- The TeX bundle checker adds `--verify-copy DIR`. It compares the checked local `.tex`, sibling PDF and supported static dependencies with the downloaded files at the same relative paths. It reports missing files or SHA-256 mismatches and performs no compilation. Delivery instructions use this mode for a checked baseline and use a clean rebuild when no baseline is available.
- The Project evaluation records the route and edition, necessary reads, avoidable reads and verified files. The homework case allows one matching TeX template when needed.

## Files affected

`skills/econ-research/scripts/verify_references.py` and its literature-search task, `shared/scripts/check_tex_bundle.py` and `shared/deliver-file.md`, their generated skill copies and link pages, the corresponding regression tests, `tests/link-route-evaluation.md`, `README.md` and `CHANGELOG.md`.

## Behavior and compatibility

`--compile` still checks an existing PDF against a fresh build. `--verify-copy` establishes byte identity against the local baseline. A failed read or parse uses the existing BibTeX `ERROR` status and exit code 2. A bibliography without entries uses `SKIP` and exit code 0.

## Verification and evidence

| Check | Result | Evidence |
| --- | --- | --- |
| BibTeX input and recovery | Pass | The CLI returned 2 for a malformed header and a plain-text file, and reported `SKIP` for a comment-only file. Regression coverage also includes unreadable encoding, a blank file and recovery to a later valid entry. |
| Download comparison | Pass | Built a real PDF with a nested TeX input, checked the copied bundle and rejected a changed input. Regression coverage also includes changed source, PDF and figure bytes, a missing file and comparison with the same directory. |
| Repository checks | Pass | `python3 tools/check_all.py` rebuilt the generated pages and passed structural validation, 99 unit tests and whitespace checks. The homework route is 47,834 bytes, within the 48,000-byte test limit. |
| Project evaluation | Checked locally | The homework route links the language templates and the rubric allows the needed read. |
| Live Project and GitHub Actions | Not run | The changes are in the local checkout. |

## Known limitations and risks

Byte comparison requires a previously checked baseline and copies that preserve the original bytes. The helper checks its supported static bundle dependencies. Other requested attachments must be verified as part of delivery.
