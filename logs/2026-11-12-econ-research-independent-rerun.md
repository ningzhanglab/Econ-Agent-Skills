# 2026-11-12 — Independent Rerun of the econ-research Evaluation Cases

- **Date:** 2026-11-12
- **Component:** `econ-research` (v0.1)
- **Change type:** Testing
- **Status:** Implemented (test record only; no skill, test, README or CHANGELOG file was changed)
- **Related commit / PR:** Not committed by the grading session; see Git history on branch `feat/econ-research-skill`

## Motivation

The agent that wrote `econ-research` also ran and graded its own seven manual cases. The user asked for an independent check by an agent that did not write the skill. This grader used only the skill files, the checker script and `tests/research-evaluation.md`. To stay independent it did **not** read the three earlier test logs (`2026-11-12-econ-research-first-topic-test.md`, `-cases-2-4-5.md`, `-cases-6-7.md`).

## Changes made

None to the skill. This log records a full rerun of the seven cases in `tests/research-evaluation.md` on topics different from the earlier precautionary-saving / wealth-inequality / Aiyagari runs, a grade for each, and findings about wording in the skill and behaviour of the checker.

## Files affected

- `logs/2026-11-12-econ-research-independent-rerun.md`: this record (the only repository file created).
- Scratch files (not in the repository): a helper for OpenAlex / Crossref / Semantic Scholar queries and the case-6 `.bib` fixture, both in the grading session's scratchpad.

## What was run

Files read first: `skills/econ-research/SKILL.md`, `references/research-questions.md`, `references/literature-search.md`, `references/literature-synthesis.md`, `scripts/verify_references.py`, `tests/research-evaluation.md`, `logs/TEMPLATE.md`.

Sources used, 2026-11-12, via `curl` / Python `urllib` with a generic User-Agent and no personal details, no API keys:

| Source | Reachable? | Notes |
| --- | --- | --- |
| Crossref REST API | Yes | Main verification source; also the checker's source |
| OpenAlex API | Yes | Main discovery source; abstracts via inverted index |
| Semantic Scholar API | Mostly no | HTTP 429 on every call after the first (no key); recorded as a failed source |
| RePEc / IDEAS | Yes | Used to confirm Card & Krueger (1994) AER, which Crossref and OpenAlex did not return as a journal record |
| NBER (site search API and chapter pages) | Yes | Working-paper pass (case 3) and the no-DOI chapter (case 6) |
| EconStor | Yes | Confirmed a GLO discussion paper (case 3) |
| Publisher page (MIT Press / QJE 2003) | No | HTTP 403 (case 7) |

Topics: case 1 used the fixed prompt (minimum wages); case 2 a fake paper on refugees and native occupational upgrading; case 3 the local labour-market effects of the 2022 Ukrainian refugee inflow; case 4 the fixed prompt (housing and inequality); case 5 a China-shock design applied to marriage and fertility; case 6 a HANK / trade / immigration `.bib`; case 7 Borjas (2003, QJE).

## Results

| Case | Sources reachable | Critical fail? | Grade | Notes |
| --- | --- | --- | --- | --- |
| 1 Known literature (minimum wages) | Crossref, OpenAlex, RePEc; S2 429 | No | **Pass** | 11 papers, all verified (see below); read status recorded per paper; split described with candidate reasons |
| 2 Fake paper | Crossref, OpenAlex (AER source filter), RePEc; S2 429 | No | **Pass** | No such paper found; no summary produced; one verified closest paper offered |
| 3 Thin topic (Ukrainian refugees) | Crossref, OpenAlex, NBER, EconStor; S2 429 | No | **Pass** | 3 directly relevant items (1 journal, 2 working papers); no padding; coverage stated |
| 4 Housing and inequality | Crossref, OpenAlex | No | **Pass** | Proceeded with stated assumptions; 3 candidates tested; one recommended with next step |
| 5 Is my idea done? | Crossref, OpenAlex | No | **Pass** | Verdict: largely done for the US; referee paper named |
| 6 Bibliography check | Crossref via checker; NBER for SKIP | No | **Pass** (case criteria) | PASS/WARN/FAIL/SKIP correct on the fixture; file unchanged. Extra probes found two false WARNs (Findings 1–2) |
| 7 Paywalled paper | Crossref, OpenAlex; publisher 403 | No | **Pass** | Abstract only, labelled; NBER working-paper route suggested |

All grades are **self-graded by this independent agent**: the grader also ran the cases, so the result is independent of the skill's author but not of the runner. Bibliographic facts listed below were checked against the named source during this session; the summaries are from abstracts only unless stated.

### Case 1 detail

Search: OpenAlex free text and a title filter sorted by citations; Crossref bibliographic queries for seed papers; RePEc for the 1994 AER article. Verified (Crossref unless noted); read status is **abstract only** except where marked:

1. Card & Krueger (1994), AER 84(4):772–793; RePEc handle `RePEc:aea:aecrev:v:84:y:1994:i:4:p:772-93` (no Crossref/OpenAlex journal record found; NBER WP `10.3386/w4509`). Abstract read on IDEAS.
2. Neumark & Wascher (1992), ILR Review 46(1):55–81, `10.1177/001979399204600105`.
3. Neumark & Wascher (2000), AER 90(5):1362–1396, `10.1257/aer.90.5.1362`: **metadata only** (the OpenAlex "abstract" is a boilerplate publication line).
4. Card & Krueger (2000), AER 90(5):1397–1420, `10.1257/aer.90.5.1397`: **metadata only**, same reason.
5. Dube, Lester & Reich (2010), REStat 92(4):945–964, `10.1162/rest_a_00039`.
6. Allegretto, Dube & Reich (2011), Industrial Relations 50(2):205–240, `10.1111/j.1468-232x.2011.00634.x`.
7. Neumark, Salas & Wascher (2014), ILR Review 67(3_suppl):608–648, `10.1177/00197939140670s307`.
8. Cengiz, Dube, Lindner & Zipperer (2019), QJE 134(3):1405–1454, `10.1093/qje/qjz014`.
9. Harasztosi & Lindner (2019), AER 109(8):2693–2727, `10.1257/aer.20171445`.
10. Jardim et al. (2022), AEJ: Economic Policy 14(2):263–314, `10.1257/pol.20180578`.
11. Manning (2021), JEP 35(1):3–26, `10.1257/jep.35.1.3` (review; listed as context).

Split (as an **assessment**, built from the abstracts): state-panel estimates with state and year fixed effects (2, 7) find teen disemployment; designs that restrict the control group to nearby or similar areas (5, 6) find effects near zero, and 7 disputes that restriction. Candidate reasons: control-group choice and spatial heterogeneity (design); teens versus all low-wage jobs (estimand, 8); size of the increase and setting (9: large Hungarian increase, small negative elasticities); headcount versus hours (10: Seattle hours fall). Coverage line given; Semantic Scholar unavailable; "ten most important" was read as relevance first, then influence by OpenAlex citation count.

### Case 2 detail

Invented paper: "Halvorsen and Okafor (2021), *Refugee Inflows and Native Occupational Upgrading: Evidence from Norwegian Municipalities*, AER". Crossref (author + title; title within AER ISSN 0002-8282, 2020–2022), OpenAlex (free text; AER source filter with author surname; AER source filter with "refugee", 2020–2022, which returned only Hussam et al. 2022) and RePEc returned nothing matching. Answer: no such paper found in these sources; no summary. Closest verified real paper: Foged & Peri (2016), AEJ: Applied 8(2):1–34, `10.1257/app.20150114` (Denmark, refugee dispersal; abstract only), noted as a different country and authors.

### Case 3 detail

Queries: four OpenAlex phrasings (title filter and free text), a working-paper pass (OpenAlex `type:preprint|report`), NBER site search (90 hits, none on the 2022 Ukrainian inflow's effect on natives), EconStor. Directly relevant:

- Postepska & Voloshyna (2025), *Journal of Population Economics* 38(1), `10.1007/s00148-025-01080-9`: abstract only (open-access PDF exists, not read). Czechia, LFS 2019–2022; no meaningful effect on locals' employment, more weekly hours.
- Nieuwenhuis, Postepska, Alessie & Voloshyna (2026), GLO Discussion Paper 1769, EconStor `hdl:10419/341158`: abstract only, working paper. Czechia, Germany, Poland; no population-wide displacement, heterogeneous subgroup effects.
- Dassel, Meshesha, Northcott & Rennert (2025), SSRN `10.2139/ssrn.5660262`: **metadata only** (no abstract in Crossref or OpenAlex), working paper on Poland.

Excluded as tangential: integration-of-refugees papers, an undergraduate journal article, OECD briefs. Coverage line: "three directly relevant items in these sources; IZA/CEPR not searched directly; SSRN only through OpenAlex/Crossref."

### Case 4 detail

Proceeded without a scoping question, stating assumptions (US, applied micro, public or purchasable data, one year). Candidates: (a) tenant-side mobility effects of St. Paul's 2021 rent control; (b) housing-price exposure and owner–renter wealth gaps; (c) housing regulation and regional convergence. Verified closest papers: Diamond, McQuade & Qian (2019), AER 109(9):3365–3394, `10.1257/aer.20181289`; Ahern & Giacoletti (2022), NBER WP 30083, `10.3386/w30083` (St. Paul property values and redistribution; WP abstract); Kholodilin (2024), JHE 63:101983 (review; abstract); Kuhn, Schularick & Steins (2020), JPE 128(9):3469–3519, `10.1086/708815`; Ganong & Shoag (2017), JUE 102:76–90, `10.1016/j.jue.2017.07.002` (summary from the NBER WP abstract, labelled as such). Recommended (a), with the gap labelled **inference** relative to these searches, the main identification threat (St. Paul versus Minneapolis trends; the 2022 exemption amendment) and the next step (check access to address-history data).

### Case 5 detail

Idea: "commuting-zone China-shock exposure, shift-share instrument, effect on marriage and fertility." Closest verified: Autor, Dorn & Hanson (2019), AER: Insights 1(2):161–178, `10.1257/aeri.20180010` (abstract: tests exactly this for 1990–2014); Autor, Dorn & Hanson (2013), AER 103(6):2121–2168; Giuntella, Rotunno & Stella (2022), NBER WP 30119 (Germany; abstract); Braga (2018), SSRN `10.2139/ssrn.3273714` (Brazil; metadata only); Borusyak, Hull & Jaravel (2022), REStud 89(1):181–213 (method). Verdict: already done for the US; referee would cite ADH (2019). Suggested ways to differ were labelled as assessment.

### Case 6 detail

Fixture (scratchpad only): ADH 2013 (correct); Kaplan, Moll & Violante with year 2016 (record 2018); a fake paper "Lindqvist & Mbeki (2020), JME" with DOI `10.1016/j.jmoneco.2020.99999`; Altonji & Card (1991) chapter without DOI. Extra probes: Dustmann et al. QJE 137(1) with year 2022; Card (1990) Mariel with a mistyped DOI.

Checker output: `PASS autor2013china`; `WARN kaplan2016hank — year 2016 vs record 2018`; `FAIL lindqvist2020ladders — no Crossref record`; `SKIP altonji1991effects`; `WARN dustmann2022reallocation — year 2022 vs record 2021`; `FAIL card1990mariel — no Crossref record`; exit 1; `.bib` byte-identical before and after.

Follow-up per `literature-search.md`: Lindqvist & Mbeki: no title/author match in Crossref or OpenAlex → "may be fabricated". Card (1990): exists as ILR Review 43(2):245–257, `10.1177/001979399004300205` (also JSTOR `10.2307/2523702`) → "the DOI is wrong; the paper exists as …". Altonji & Card: NBER chapter page confirms authors, title, book, editors (Abowd & Freeman), publisher (University of Chicago Press), 1991, "chap. 7"; **pages 201–234 not confirmed** by any source reached.

### Case 7 detail

Borjas (2003), QJE 118(4):1335–1374, `10.1162/003355303322552810` (Crossref). OpenAlex: `oa_status: closed`; publisher page 403. Answer summarised the abstract only (education–experience cells, imperfect substitution across experience, 10 % supply increase → wages 3–4 % lower) and labelled it. Suggested library access or the NBER WP 9755. A PDF was fetched from NBER into the scratchpad, but no text extractor was available, so it was **not read**; its 10-page length was not explained.

## Findings (ranked by severity)

1. **High — the year rule and the checker both reject a correct citation.** `literature-search.md` says "Cite the print year from the publisher's record", and `verify_references.py:117` takes `published-print` first. For Dustmann et al., QJE **137(1)** (the 2022 volume), Crossref has `published-print` 2021-12-24 and no 2022 date anywhere, so the checker reports `WARN year 2022 vs record 2021`. An agent following the rule would "correct" a right citation to 2021. *Fix:* in the reference, cite the year of the volume/issue and treat Crossref print/online dates as evidence; in the checker, accept any of print/online/issued years and the year after `published-print` for issue-1 records, or downgrade a one-year gap to a note.
2. **High — renamed journals cause false venue WARNs.** Card (1990) with the correct DOI and `journal = {Industrial and Labor Relations Review}` gives `WARN venue vs record 'ILR Review'` (token similarity 1/6 < 0.6, `verify_references.py:151`). The reference says WARN means "a field differs", inviting a wrong correction. *Fix:* also compare against Crossref `short-container-title` and treat a venue-only difference as a note, not WARN; say in the reference that journals get renamed.
3. **Medium — a failed lookup exits 0.** With the network blocked, the checker prints `ERROR … Summary: ERROR 1` and exits 0 (`verify_references.py:213` returns 1 only on FAIL). `literature-search.md` documents PASS/WARN/FAIL only, so ERROR is undocumented. An agent relying on exit status could treat unchecked entries as checked. *Fix:* non-zero exit (e.g. 2) on ERROR; document ERROR and SKIP in the reference.
4. **Medium — "abstract only" can be a false label.** OpenAlex returns an "abstract" for the AER 2000 comment and reply that is only a publication line ("Published in volume 90, issue 5 …"). Separately, an aggregator abstract attached to a published DOI may come from a working paper, and the skill's "name the version" rule gives no way to tell. *Fix:* one line in the Read section: check that an abstract is real text from the authors and say where it came from (publisher, Crossref, OpenAlex, WP page); if in doubt, label metadata only.
5. **Medium — "most important" is undefined, and citation-sorted free-text search returns noise.** The case 1 prompt asks for "the ten most important papers", but the skill ranks only by relevance (1–5). OpenAlex free-text search sorted by citations returned Callaway & Sant'Anna, an AI-alignment preprint and an Alzheimer's report for "minimum wage employment effects". *Fix:* a line in Query design: when the user asks for importance, rank by relevance then influence, name the citation source, and sort by citations only with a title/abstract filter.
6. **Medium — the seminal journal version can be missing from Crossref/OpenAlex.** Card & Krueger (1994, AER) appeared only as the NBER WP and as the 2000 comment/reply; RePEc confirmed the journal version. An agent using only the two APIs would cite the WP or drop the paper. *Fix:* in "Common cases", add: if the published version of a known paper is missing, check RePEc/JSTOR before citing the working paper.
7. **Low — aggregator years differ from the published year.** OpenAlex gives `publication_year 2018` for Borusyak, Hull & Jaravel (REStud 2022). The skill covers online versus print years, not "aggregator reports the first-version year". *Fix:* add to "Common cases": take the year from Crossref or the publisher, not OpenAlex.
8. **Low — scoping wording differs across files.** `SKILL.md` says to ask one question when the topic is a single word or the field is unclear; `research-questions.md` says "Ask only what is missing, one or two questions at a time". For "housing and inequality", both asking and proceeding are defensible; the test accepts both. *Fix:* in `research-questions.md`, say that stating assumptions and proceeding is fine when the request is clearly a brainstorming request.
9. **Low — reading full texts is not operationalised.** "Read as far as access allows" says nothing about fetching PDFs, the tools needed to extract text, or confirming with the user before downloads. In this run a PDF was reachable but unreadable. *Fix:* one sentence: if a PDF cannot be read, say so and keep the abstract-only label.
10. **Low — one article, two DOIs.** Card (1990) has SAGE and JSTOR DOIs; ILR comments in 1994 also appear twice. The duplicate rule ("merge by DOI, then by normalized title") handles this only if the agent applies the title step. No change needed; noted for test fixtures.

## Behavior and compatibility

No behaviour changed. Findings 1–3 are checker or reference issues that can lead an agent to give wrong advice on a correct `.bib`; the others are wording gaps.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read all skill files, the checker and the test file listed above |
| Automated structural validation | Not run | `tests/validate_skills.py` was not in scope; no skill file changed |
| Real domain evaluation (7 manual cases) | Pass (self-graded, 7/7) | Live Crossref, OpenAlex, RePEc, NBER, EconStor lookups on 2026-11-12; checker run on a scratch `.bib`; Semantic Scholar mostly unreachable (429) |
| Checker probes beyond the fixture | Fail (2 false WARNs, ERROR exits 0) | Findings 1–3; outputs quoted above |
| GitHub Actions or other CI | Not run | No commit made by this session |

Self-graded versus checked: every bibliographic field cited in this log was compared with the named source record in this session. The grades themselves are the grader's judgment and were not reviewed by a second agent or the user.

## Known limitations and risks

- One agent ran and graded the cases; grading is not blind.
- Most read statuses are abstract only; no full text was read, so no claim here goes beyond abstracts.
- Semantic Scholar was effectively unavailable, so citation chasing was not tested.
- Case 1's topic is fixed by the test prompt and may overlap with the author's earlier run, which this grader did not read.

## Follow-up

- Fix Findings 1–3 in `verify_references.py` and `literature-search.md`, with regression tests for an issue-1 OUP record, a renamed journal and a network error.
- Add short wording fixes for Findings 4–7.
- Consider adding the Dustmann et al. and ILR Review cases to the case-6 fixture in `tests/research-evaluation.md`.
