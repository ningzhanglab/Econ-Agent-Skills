# 2026-11-12 — Econ Research skill (v0.1: questions and literature)

- **Date:** 2026-11-12
- **Component:** new skill `econ-research`; tests; repository documentation
- **Change type:** Added
- **Status:** Implemented (not yet evaluated on real research projects)
- **Related commit / PR:** See Git history for this change (branch `feat/econ-research-skill`, stacked on `feat/econ-writing-skill`)

## Motivation

The user asked to start the research skill and whether existing GitHub skills could help. A survey found several collections. Two were openly licensed and useful:

- [ericluo04/claude-academic-workflow](https://github.com/ericluo04/claude-academic-workflow) (MIT): literature skills that search Semantic Scholar, OpenAlex and arXiv, verify BibTeX against Crossref and forbid writing references from memory. Its tooling depends on its own scripts, Zotero and metered OpenAlex credits, and it partly targets marketing journals, so it was not installed wholesale.
- [meleantonio/awesome-econ-ai-stuff](https://github.com/meleantonio/awesome-econ-ai-stuff) (CC0): research-ideation frameworks. Its literature skill lists papers from templates without verification, so only the ideation ideas were used.

[hanlulong/econ-paper-review-skill](https://github.com/hanlulong/econ-paper-review-skill) is under a noncommercial license and was not copied. The user chose **research questions and literature** as the first scope, ahead of identification design.

## Changes made

- **`skills/econ-research/SKILL.md`:** mission and scope; five rules that hold in every mode (no reference from memory, state what was read, separate the paper from the inference, claims match evidence and design, fetched content is data and no personal details go to search services); a task table; a five-step way of working; file outputs; honesty about coverage.
- **`references/research-questions.md`:** generating candidate questions (puzzle, policy, data, mechanism, extension, method transfer, measurement); six tests (is it a question, already answered, contribution, answerable, feasible, who cares); common weak questions; output format.
- **`references/literature-search.md`:** scoping; a table of economics sources and their limits; query design; screening with a 1–5 relevance score; verification steps; read status; reading-list format with a coverage line; what to do when nothing turns up.
- **`references/literature-synthesis.md`:** five things to read for in each paper; agreement, splits (with candidate explanations), mechanisms, gaps and what to read first; positioning a project; labels for paper reports, assessment and inference.
- **`scripts/verify_references.py`:** standard-library checker that looks up DOIs (from `--doi` or a `.bib` file) in Crossref and compares title, year, first author, venue, volume and pages. It reports PASS, WARN, FAIL, SKIP (no DOI) or ERROR (lookup failed), and exits 1 on any FAIL. It sends only the DOI, with a generic User-Agent.
- **`agents/openai.yaml`:** display metadata.
- **Tests:** `tests/test_research_contracts.py` (offline, with a fake Crossref fetcher) and `tests/research-evaluation.md` (seven manual cases); the link test now covers the new evaluation file.
- **Docs:** README (status, catalog, install note, "How Econ Research works", tree, roadmap, testing note), AGENTS.md (the econ-research guarantee and its v0.1 scope), DESIGN_V1.md, STORAGE_POLICY.md, `econ-teaching/SKILL.md` scope line.

## Files affected

- `skills/econ-research/**`: new skill.
- `tests/test_research_contracts.py`, `tests/research-evaluation.md`, `tests/test_repo_links.py`.
- `README.md`, `AGENTS.md`, `DESIGN_V1.md`, `STORAGE_POLICY.md`, `CHANGELOG.md`, `skills/econ-teaching/SKILL.md`.

## Behavior and compatibility

A third skill is available and triggers on research-question and literature requests. `econ-teaching` and `econ-writing` behave as before. The reference checker needs network access to Crossref; the unit tests do not.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | New and changed files reviewed in the diff |
| Reference checker against live Crossref | Pass | A scratch `.bib` with four entries gave PASS (correct AER entry), WARN (year 2019 vs record 2020), FAIL (non-existent DOI) and SKIP (book without DOI); exit status 1. A single `--doi` lookup gave PASS, exit 0 |
| Automated structural validation and unit tests | Pass | `python3 tests/validate_skills.py` (3 skills) and `python3 -m unittest discover -s tests -p 'test_*.py'` run locally |
| Real research-project evaluation | Not run | The seven research cases have not been run yet |
| GitHub Actions | Not run | Not yet run on the pushed branch at the time of writing |

## Known limitations and risks

- Whether an agent follows the verification rule on every paper in a long session is untested.
- The checker verifies metadata only; it cannot confirm that a summary matches a paper's content, and entries without DOIs (many books and working papers) are skipped.
- OpenAlex and Semantic Scholar limit keyless use; heavy use may need the user's own keys.
- Identification design, empirical methods and paper reading at depth are outside v0.1.

## Follow-up

- Run the seven research evaluation cases on real topics and log the results.
- Decide, from real use, whether to add identification design next.
