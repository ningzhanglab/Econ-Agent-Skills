#!/usr/bin/env python3
"""Check references against Crossref by DOI.

Usage (from the skill's folder):
  python3 scripts/verify_references.py --doi 10.1257/aer.20190623
  python3 scripts/verify_references.py --bib references.bib [--json]

For each DOI, fetch the Crossref record and report:
  PASS  the record exists and the entry's title, year, first author, volume
        and pages (when given) agree with it; notes may still follow;
  WARN  the record exists but a field differs (the canonical value is shown);
  FAIL  no record for the DOI, or the title does not match the record;
  SKIP  an entry without a DOI, or a bibliography with no entries;
  ERROR the lookup failed after retries, or the entry could not be parsed:
        the entry is unchecked.

A rate limit, server error or network failure is retried up to three times
with a short wait. Each DOI is looked up once per run.

Notes under a PASS (a venue that differs, or a year one after a late-year print
date) must be reported to the user; they are not errors by themselves.

Standard library only. Read-only on the .bib file. Sends only the DOI to
Crossref, with a generic User-Agent and no personal details. It cannot prove
a paper says what a summary claims; it only confirms bibliographic metadata.
Exit status is 2 if any entry ERRORs (the check is incomplete), otherwise 1
if any entry FAILs, otherwise 0.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Callable, Optional

CROSSREF = "https://api.crossref.org/works/"
USER_AGENT = "econ-research-reference-checker/0.1"
Fetcher = Callable[[str], Optional[dict]]


ATTEMPTS = 3
MAX_WAIT = 10.0


def retry_wait(err: Exception, attempt: int) -> Optional[float]:
    """Seconds to wait before retrying after err, or None if it should not be retried."""
    if isinstance(err, urllib.error.HTTPError):
        if err.code != 429 and err.code < 500:
            return None
        header = (err.headers or {}).get("Retry-After", "")
        if header.strip().isdigit():
            return min(float(header), MAX_WAIT)
    return min(2.0 ** attempt, MAX_WAIT)


def fetch_crossref(doi: str, timeout: float = 20.0, opener=urllib.request.urlopen,
                   sleep=time.sleep) -> Optional[dict]:
    """Return the Crossref 'message' for a DOI, or None if Crossref has no record.

    A rate limit (429), a server error (5xx) or a network failure is retried with
    a short wait, up to ATTEMPTS tries; the last failure is raised.
    """
    url = CROSSREF + urllib.parse.quote(doi, safe="/")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(ATTEMPTS):
        try:
            with opener(req, timeout=timeout) as resp:
                return json.load(resp).get("message")
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            wait = retry_wait(err, attempt)
            if wait is None or attempt == ATTEMPTS - 1:
                raise
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            if attempt == ATTEMPTS - 1:
                raise
            wait = retry_wait(err, attempt)
        sleep(wait)
    return None


def clean_doi(raw: str) -> str:
    doi = raw.strip().strip("{}").strip()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi, flags=re.I)
    return doi.lower()


# LaTeX accents keep their base letter: {\'e}, \'{e}, \"o, \c{c}, \u{g}, {\'\i}.
LATEX_ACCENT = re.compile(r"\\[`'^\"~=.]\s*|\\[cuvHkdbrt](?![a-zA-Z])\s*")
LATEX_LETTER = re.compile(r"\\(ss|ae|AE|oe|OE|aa|AA|[ijoOlL])(?![a-zA-Z])")


def normalize(text: str) -> str:
    text = LATEX_ACCENT.sub("", text or "")
    text = LATEX_LETTER.sub(lambda m: m.group(1), text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[{}]", "", text)
    text = re.sub(r"[$\\]", " ", text)
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def normalize_title(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html.unescape(text or ""))
    return normalize(text.replace("&", " and "))


def title_forms(rec: dict) -> set[str]:
    """Normalized forms of the record's title that count as the same title."""
    title, subtitle = first(rec.get("title")), first(rec.get("subtitle"))
    forms = {normalize_title(title), normalize_title(title.split(":")[0])}
    if subtitle:
        forms.add(normalize_title(f"{title} {subtitle}"))
    return forms - {""}


def similarity(a: str, b: str) -> float:
    ta, tb = set(normalize(a).split()), set(normalize(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


ENTRY_START = re.compile(r"^[ \t]*%[^\n]*|^[ \t]*@(\w+)(?:\s*([({]))?|@(\w+)\s*([({])", re.M)
ENTRY_KEY = re.compile(r"\s*([^,\s{}()]+)\s*,")
FIELD = re.compile(r"([A-Za-z][\w-]*)\s*=\s*")
SPACE = re.compile(r"\s*")
BARE_VALUE = re.compile(r'[^\s,#{}()"]+')
RECOVERY = re.compile(r"^[ \t]*@\w+", re.M)
CHECKED_FIELDS = {"author", "booktitle", "doi", "journal", "pages", "title", "volume", "year"}


def group_end(text: str, start: int, closing: str) -> int:
    """Find a delimiter outside nested braces and escaped characters."""
    depth, i = 0, start + 1
    while i < len(text):
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if char == closing and depth == 0:
            return i
        if char == "{":
            depth += 1
        if char == "}":
            depth -= 1
        if depth < 0:
            break
        i += 1
    raise ValueError(f"missing closing {closing!r}")


def parse_fields(text: str, i: int, closing: str) -> tuple[dict, int]:
    fields = {}
    while True:
        i = SPACE.match(text, i).end()
        if text[i:i + 1] == closing:
            return fields, i + 1
        match = FIELD.match(text, i)
        if not match:
            raise ValueError(f"expected a field or {closing!r}")
        name, i = match[1].lower(), match.end()
        delimiter = text[i:i + 1]
        if delimiter in ('"', "{"):
            end = group_end(text, i, '"' if delimiter == '"' else "}")
            value, i = text[i + 1:end], end + 1
        else:
            bare = BARE_VALUE.match(text, i)
            if not bare:
                raise ValueError(f"missing value for {name}")
            value, i = bare[0], bare.end()
            if name in CHECKED_FIELDS and re.fullmatch(r"[A-Za-z][\w-]*", value):
                raise ValueError(f"unexpanded BibTeX macro in {name}")
        fields[name] = " ".join(value.split())
        i = SPACE.match(text, i).end()
        separator = text[i:i + 1]
        if separator == "#":
            raise ValueError(f"BibTeX concatenation in {name}; expand the field first")
        if separator == closing:
            return fields, i + 1
        if separator != ",":
            raise ValueError(f"expected ',' or {closing!r} after {name}")
        i += 1


def parse_bib(text: str) -> list[dict]:
    """Read literal fields and keep parse errors with their entry and source line."""
    entries, pos = [], 0
    saw_header = False
    while match := ENTRY_START.search(text, pos):
        start_type, start_delimiter, inline_type, inline_delimiter = match.groups()
        etype = start_type or inline_type
        pos = match.end()
        if etype is None:
            continue
        saw_header = True
        line = text.count("\n", 0, match.start()) + 1
        opening = start_delimiter or inline_delimiter
        if opening is None:
            entries.append({"key": f"line {line}", "error": f"line {line}: missing '{{' or '(' after @{etype}"})
            continue
        closing = "}" if opening == "{" else ")"
        key = ENTRY_KEY.match(text, pos)
        try:
            if etype.lower() in {"comment", "preamble", "string"}:
                pos = group_end(text, pos - 1, closing) + 1
                continue
            if not key:
                raise ValueError("missing entry key or comma after key")
            fields, pos = parse_fields(text, key.end(), closing)
            entries.append({"key": key[1], "fields": fields})
        except ValueError as err:
            entries.append({"key": key[1] if key else f"line {line}", "error": f"line {line}: {err}"})
            following = RECOVERY.search(text, match.end())
            pos = following.start() if following else len(text)
    if not saw_header:
        for line, content in enumerate(text.splitlines(), 1):
            if content.strip() and not content.lstrip().startswith("%"):
                entries.append({"key": f"line {line}", "error": f"line {line}: no BibTeX entry or directive found"})
                break
    return entries


DATE_KEYS = ("published-print", "published-online", "issued", "published")


def record_dates(rec: dict) -> list[tuple[int, Optional[int]]]:
    """All (year, month) pairs the record reports, including its journal issue's dates."""
    sources = [rec.get(key) for key in DATE_KEYS]
    issue = rec.get("journal-issue") or {}
    sources += [issue.get("published-print"), issue.get("published-online")]
    dates = []
    for src in sources:
        parts = (src or {}).get("date-parts") or [[None]]
        if parts and parts[0] and parts[0][0]:
            month = int(parts[0][1]) if len(parts[0]) > 1 and parts[0][1] else None
            dates.append((int(parts[0][0]), month))
    return dates


def record_year(rec: dict) -> Optional[int]:
    for key in DATE_KEYS:
        parts = (rec.get(key) or {}).get("date-parts") or [[None]]
        if parts and parts[0] and parts[0][0]:
            return int(parts[0][0])
    return None


def check_year(given: str, rec: dict) -> tuple[str, Optional[str]]:
    """Return (status, note) for the entry's year against every date in the record.

    A year matching any reported date passes. A year one after the latest date
    passes with a note when that date falls in November or December, because
    late-year print dates often belong to the next year's volume (for example
    a QJE issue 1 printed in late December). Anything else is a WARN.
    """
    dates = record_dates(rec)
    years = {y for y, _ in dates}
    given = given.strip()
    if not years or given in {str(year) for year in years}:
        return "PASS", None
    shown = ", ".join(str(y) for y in sorted(years))
    latest = max(dates, key=lambda date: (date[0], date[1] or 0))
    if given == str(latest[0] + 1) and (latest[1] or 0) >= 11:
        return "PASS", (f"year {given} vs record dates {shown}: the record's latest date is late "
                        f"{latest[0]}, so {given} may be the volume year; confirm with the issue")
    return "WARN", f"year {given} vs record {record_year(rec)} (record dates: {shown})"


def first(values) -> str:
    return html.unescape(values[0]) if values else ""


def compare(fields: dict, rec: dict) -> tuple[str, list[str]]:
    notes, status = [], "PASS"
    canon_title = first(rec.get("title"))
    if fields.get("title"):
        bib_title, forms = normalize_title(fields["title"]), title_forms(rec)
        if max((similarity(bib_title, form) for form in forms), default=0.0) < 0.5:
            return "FAIL", [f"title does not match record: {canon_title!r}"]
        if bib_title not in forms:
            status = "WARN"
            notes.append(f"title differs; record: {canon_title!r}")
    if fields.get("year"):
        year_status, note = check_year(fields["year"], rec)
        if year_status == "WARN":
            status = "WARN"
        if note:
            notes.append(note)
    authors = rec.get("author") or []
    if fields.get("author") and authors:
        bib_first = normalize(re.split(r"\s+and\s+", fields["author"], flags=re.I)[0]).split()
        rec_family = normalize(authors[0].get("family", "")).split()
        n = len(rec_family)
        if n and not any(bib_first[i:i + n] == rec_family for i in range(len(bib_first) - n + 1)):
            status = "WARN"
            notes.append(f"first author vs record {authors[0].get('family')!r}")
    journal = fields.get("journal") or fields.get("booktitle")
    venues = [html.unescape(v) for v in (rec.get("container-title") or []) + (rec.get("short-container-title") or [])]
    if journal and venues and max(similarity(journal, v) for v in venues) < 0.6:
        # The DOI and title already identify the paper, so a venue difference is a
        # note, not a WARN: journals get renamed (ILR Review was Industrial and Labor
        # Relations Review) and entries use abbreviations. Report it; do not "correct" it blindly.
        notes.append(f"venue differs from record {venues[0]!r}: renamed journal, abbreviation or wrong venue; check")
    for field, rkey in (("volume", "volume"), ("pages", "page")):
        mine, theirs = fields.get(field), rec.get(rkey)
        if mine and theirs and normalize(mine).replace(" ", "") != normalize(theirs).replace(" ", ""):
            status = "WARN"
            notes.append(f"{field} {mine} vs record {theirs}")
    return status, notes


def describe(rec: dict) -> str:
    authors = ", ".join(a.get("family", "") for a in (rec.get("author") or [])[:4])
    parts = [f"{authors} ({record_year(rec)})", first(rec.get("title")), first(rec.get("container-title"))]
    return " · ".join(part.strip() for part in parts if part.strip())


def check_doi(doi: str, fields: dict, fetch: Fetcher) -> dict:
    try:
        rec = fetch(doi)
    except (urllib.error.URLError, TimeoutError, OSError) as err:
        return {"doi": doi, "status": "ERROR", "notes": [f"lookup failed: {err}"]}
    if rec is None:
        return {"doi": doi, "status": "FAIL", "notes": ["no Crossref record for this DOI"]}
    status, notes = compare(fields, rec)
    return {"doi": doi, "status": status, "notes": notes, "record": describe(rec)}


def cached(fetch: Fetcher) -> Fetcher:
    """Look each DOI up once per run; a failed lookup is not cached."""
    seen: dict[str, Optional[dict]] = {}

    def lookup(doi: str) -> Optional[dict]:
        if doi not in seen:
            seen[doi] = fetch(doi)
        return seen[doi]
    return lookup


def run(dois: list[str], bib: Optional[Path], fetch: Fetcher) -> list[dict]:
    fetch = cached(fetch)
    results = []
    for doi in dois:
        results.append({"key": None, **check_doi(clean_doi(doi), {}, fetch)})
    if bib:
        try:
            entries = parse_bib(bib.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError) as err:
            results.append({"key": bib.name, "doi": None, "status": "ERROR",
                            "notes": [f"cannot read bibliography: {err}"]})
            return results
        if not entries:
            results.append({"key": bib.name, "doi": None, "status": "SKIP",
                            "notes": ["no bibliography entries; nothing checked"]})
        for entry in entries:
            if "error" in entry:
                results.append({"key": entry["key"], "doi": None, "status": "ERROR",
                                "notes": [entry["error"]]})
                continue
            doi = entry["fields"].get("doi")
            if not doi:
                results.append({"key": entry["key"], "doi": None, "status": "SKIP",
                                "notes": ["no DOI; check by hand"]})
                continue
            results.append({"key": entry["key"], **check_doi(clean_doi(doi), entry["fields"], fetch)})
    return results


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--doi", action="append", default=[], help="a DOI to check (repeatable)")
    parser.add_argument("--bib", type=Path, help="a .bib file to check")
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    args = parser.parse_args(argv)
    if not args.doi and not args.bib:
        parser.error("give --doi or --bib")
    results = run(args.doi, args.bib, fetch_crossref)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for r in results:
            label = r["key"] or r["doi"]
            print(f"{r['status']:5} {label}" + (f"  [{r['record']}]" if r.get("record") else ""))
            for note in r["notes"]:
                print(f"      - {note}")
        counts = {s: sum(r["status"] == s for r in results) for s in ("PASS", "WARN", "FAIL", "SKIP", "ERROR")}
        print("Summary: " + ", ".join(f"{k} {v}" for k, v in counts.items() if v))
    if any(r["status"] == "ERROR" for r in results):
        return 2
    return 1 if any(r["status"] == "FAIL" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
