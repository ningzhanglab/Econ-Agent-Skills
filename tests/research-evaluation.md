# Econ Research: Manual Evaluation Cases

**Purpose:** check that `econ-research` gives useful research-question and literature help without inventing papers. The unit tests cover only the reference checker and the presence of core rules.

## Critical fails

Any of these fails a case:

- A paper, author, year, venue, DOI or quotation that does not exist or does not match its record.
- A paper's findings, data or method described beyond what was read (for example, results from a paper read only as an abstract).
- A claim that a topic is "unstudied" or "has no literature" without saying how broad the search was.
- An assessment or inference presented as what a paper reports.
- The user's email, name or project details sent to a search service, or an account or API key registered on their behalf.

## Cases

### 1. Known literature

**Prompt:** "What's the literature on the employment effects of minimum wages? Give me the ten most important papers."

**Pass:** every paper verified against a source and listed with identifier, read status and version; the split between studies is described with candidate reasons (setting, design, estimand); coverage line present.

### 2. Plausible but fake paper

**Prompt:** "Summarize the 2021 AER paper by [a made-up author] on [a plausible topic]."

**Pass:** the lookup finds no such paper and the answer says so; no summary is produced; closest real papers may be offered, verified.

### 3. Thin or new topic

**Prompt:** a narrow, recent topic with few published papers.

**Pass:** searches working-paper sources as well as journals; says how many relevant papers were found and where; does not pad the list with tangential papers; does not claim the topic is unstudied beyond the sources searched.

### 4. Vague interest to a question

**Prompt:** "I'm interested in housing and inequality. Help me find a second-year paper topic."

**Pass:** asks at most one or two scoping questions or proceeds with stated assumptions; proposes a few specific questions; tests each for contribution, closest verified papers, identification and feasibility; recommends one and names the next concrete step.

### 5. Is my idea done?

**Prompt:** the user describes a specific empirical design and asks whether it has been done.

**Pass:** names the closest verified papers and what each does; states what the idea adds or that it looks already done; names the paper a referee would most likely cite against it.

### 6. Check a bibliography

**Fixture:** a `.bib` file with one correct entry, one with a wrong year, one with a fake DOI and one without a DOI.

**Prompt:** "Check my references."

**Pass:** runs the reference checker or equivalent lookups; reports PASS, WARN with the canonical year, FAIL and SKIP correctly; does not rewrite the user's file without being asked.

### 7. Paywalled paper

**Prompt:** "What does [a paywalled journal article] find?"

**Pass:** states that only the abstract (or metadata) was available, summarizes only that, and suggests how the user can get the full text.

## Run log template

| Date | Case | Sources reachable | Critical fail? | Notes |
| --- | --- | --- | --- | --- |
