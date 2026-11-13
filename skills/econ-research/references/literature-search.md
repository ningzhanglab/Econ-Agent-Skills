# Literature Search

Turn a question into a ranked, verified reading list. The verification and honesty rules here are adapted from the MIT-licensed [claude-academic-workflow](https://github.com/ericluo04/claude-academic-workflow) `litreview` and `reading-papers` skills.

## Scope first

Before searching, fix:

- the question in one sentence, and the economic object it is about;
- the field and neighboring fields whose vocabulary may differ;
- a time window if the user implies one ("recent" means about the last five years; say that you read it that way);
- whether the user wants breadth (a map of the area) or depth (the five closest papers).

If the request is a single word or the field is ambiguous, ask one question before searching.

## Where to search

Use more than one source, because each covers a different slice:

| Source | Good for | Notes |
| --- | --- | --- |
| Crossref (`api.crossref.org`) | Verifying metadata by DOI; published journal articles | Free, no key. Little abstract coverage for some publishers |
| OpenAlex (`api.openalex.org`) | Broad search across journals and working papers, citation counts | Works without a key on a small shared daily budget; the user may supply their own key |
| Semantic Scholar | Search, citation links, related papers | Rate limited without a key; omits some abstracts by publisher request |
| RePEc / IDEAS, EconPapers | Economics working papers and journals, JEL codes | Best economics-specific coverage of working papers |
| NBER, SSRN, CEPR, IZA, central-bank and Fed working-paper series | Recent and unpublished work | Note the version; numbers often change before publication |
| Google Scholar | Wide recall, "cited by" chains | Results cannot be fetched reliably by an agent; use it through the user or for spot checks |
| Journal sites (AEA, Econometric Society, Oxford, Chicago, Elsevier) | Published versions, data and code appendices | Often paywalled; abstracts usually readable |
| The user's library (Zotero, a `.bib` file, a folder of PDFs) | What they have already read | Check it first when available |

Use whichever of these the environment can reach. If a source fails or is unreachable, continue with the others and report the gap.

## Query design

- Write two to four queries per topic, not one. Keep substantive nouns, drop filler, and spell out acronyms ("difference-in-differences", not only "DiD").
- Vary vocabulary across fields: labor economists, macroeconomists, finance and IO often name the same object differently.
- Add a JEL-code or venue pass when the topic has a clear home field, and a working-paper pass for recent work.
- From the two or three most relevant papers, follow citations backward (what they cite) and forward (who cites them).
- If results are dominated by one subfield, the query is inheriting its vocabulary; rewrite and merge.
- Papers you already know of may be used as **search seeds**: look each one up by title and keep it only if a source confirms it. Say in the coverage line that some entries came from seed lookups rather than open search.

## Screen

Merge duplicates across queries and sources by DOI, then by normalized title. Working-paper and published versions of one paper are one entry: cite the published version and note the working-paper version if it differs.

Score each paper once for relevance to the user's question:

- **5:** directly answers the question; would be cited in the introduction.
- **4:** closely related; would be cited in the paper.
- **3:** adjacent; worth knowing.
- **2:** tangential; include only if the user wants breadth.
- **1:** false positive; drop.

Return what clears the bar. A short honest list is better than a padded one.

## Verify every reference

Before any paper reaches the user:

1. Confirm it exists through an identifier (DOI, arXiv id, RePEc handle, NBER number) or a source record.
2. Check authors' surnames, year, title, venue, volume and pages against that record. Use the canonical values and note any correction.
3. Build BibTeX only from the record. Leave out a field rather than guess it.
4. If no source confirms it, keep it only if the user supplied it, and label it **UNVERIFIED** with the reason.

Common cases in economics:

- **Online and print years differ.** Sources disagree when a paper appeared online a year before its print issue. Cite the print year from the publisher's record and note the online year if a source reports it.
- **A record is incomplete.** Some records lack authors or pages (handbook chapters often do). Fill the gap from another record of the same work, such as its working-paper version, and say where each field came from.
- **Older work has no DOI.** Classic book chapters, conference volumes and pre-1990s working papers may have no DOI and weak database coverage. Check RePEc/IDEAS, the publisher's catalogue or a library catalogue; if none confirms the details, cite it only with the **UNVERIFIED** label, never with details filled in from memory.

The [reference checker](../scripts/verify_references.py) does steps 1–2 for DOIs and `.bib` files against Crossref:

```text
python skills/econ-research/scripts/verify_references.py --doi 10.1257/aer.20190623
python skills/econ-research/scripts/verify_references.py --bib references.bib
```

It reports PASS, WARN (a field differs) or FAIL (no record, or the title does not match). It cannot check entries without a DOI; check those by hand and say so.

Before calling a FAIL entry fabricated, search its title and authors: a mistyped DOI and a non-existent paper both fail. Report "the DOI is wrong; the paper exists as …" or "no paper with this title and authors was found in these sources; it may be fabricated". Check entries without a DOI field by field: a source may confirm the authors and title but not the edition or year, and the report should say exactly which fields were confirmed. Do not edit the user's file unless asked; list the corrections instead.

Citation counts differ across sources. Name the source of any count, and never mix sources in one column.

## Read

- Read the most relevant papers as far as access allows: the introduction, the identification or model section and the main results, at least.
- Record what was read: **full text**, **abstract only** or **metadata only**, and which version.
- A paywalled paper is summarized from its abstract and labeled so. Do not describe its body.

## Reading-list format

Order by relevance, then year (newest first). For each paper:

```text
[n] Relevance 5 · Authors (Year). Title. Venue. DOI or identifier.
    Verified: Crossref (or source) · Read: full text / abstract only / metadata only · Version: published / working paper
    Claim: what the paper finds, in your own words, with the key magnitude if read.
    Approach: data and identification, or model, in one line.
    Bears on the question: one or two sentences.
    Limits: the main caveat a referee would raise (your assessment).
```

Close with a coverage line: which sources were searched, which failed or were unreachable, the date of the search, and what the user could do to close any gap (for example, check a paywalled journal through their library).

## When nothing turns up

Relax the search in order: widen the time window, shorten the query to its two strongest terms, then drop venue filters. If there is still nothing, say what was tried and ask for a seed paper. Never offer a plausible-sounding paper to fill the space.
