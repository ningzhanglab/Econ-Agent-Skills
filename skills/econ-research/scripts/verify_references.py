#!/usr/bin/env python3
"""Check references against Crossref by DOI.

Usage:
  python skills/econ-research/scripts/verify_references.py --doi 10.1257/aer.20190623
  python skills/econ-research/scripts/verify_references.py --bib references.bib [--json]

For each DOI, fetch the Crossref record and report:
  PASS  the record exists and the entry's title, year, first author, journal,
        volume and pages (when given) agree with it;
  WARN  the record exists but a field differs (the canonical value is shown);
  FAIL  no record for the DOI, or the title does not match the record;
  SKIP  a .bib entry without a DOI (check it by hand).

Standard library only. Read-only on the .bib file. Sends only the DOI to
Crossref, with a generic User-Agent and no personal details. It cannot prove
a paper says what a summary claims; it only confirms bibliographic metadata.
Exit status is 1 if any entry FAILs, 0 otherwise.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Callable, Optional

CROSSREF = "https://api.crossref.org/works/"
USER_AGENT = "econ-research-reference-checker/0.1"
Fetcher = Callable[[str], Optional[dict]]


def fetch_crossref(doi: str, timeout: float = 20.0) -> Optional[dict]:
    """Return the Crossref 'message' for a DOI, or None if Crossref has no record."""
    url = CROSSREF + urllib.parse.quote(doi, safe="/")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.load(resp).get("message")
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def clean_doi(raw: str) -> str:
    doi = raw.strip().strip("{}").strip()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi, flags=re.I)
    return doi.lower()


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"\\[a-zA-Z]+|[{}$\\]", " ", text)
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def similarity(a: str, b: str) -> float:
    ta, tb = set(normalize(a).split()), set(normalize(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def parse_bib(text: str) -> list[dict]:
    """Minimal BibTeX parser: returns [{'type', 'key', 'fields': {name: value}}]."""
    entries = []
    for match in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        etype, key = match.group(1).lower(), match.group(2)
        if etype in {"comment", "preamble", "string"}:
            continue
        i, depth = match.end(), 1
        while i < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        entries.append({"type": etype, "key": key, "fields": parse_fields(text[match.end():i - 1])})
    return entries


def parse_fields(body: str) -> dict:
    fields, i = {}, 0
    pattern = re.compile(r"\s*([A-Za-z][\w-]*)\s*=\s*")
    while True:
        m = pattern.match(body, i)
        if not m:
            break
        name, i = m.group(1).lower(), m.end()
        if i < len(body) and body[i] == "{":
            depth, start = 1, i + 1
            i += 1
            while i < len(body) and depth:
                depth += {"{": 1, "}": -1}.get(body[i], 0)
                i += 1
            value = body[start:i - 1]
        elif i < len(body) and body[i] == '"':
            end = body.find('"', i + 1)
            value, i = body[i + 1:end], end + 1
        else:
            m2 = re.match(r"[^,]*", body[i:])
            value, i = m2.group(0), i + m2.end()
        fields[name] = " ".join(value.split())
        comma = body.find(",", i)
        if comma == -1:
            break
        i = comma + 1
    return fields


def record_year(rec: dict) -> Optional[int]:
    for key in ("published-print", "published-online", "issued", "published"):
        parts = (rec.get(key) or {}).get("date-parts") or [[None]]
        if parts and parts[0] and parts[0][0]:
            return int(parts[0][0])
    return None


def first(values) -> str:
    return values[0] if values else ""


def compare(fields: dict, rec: dict) -> tuple[str, list[str]]:
    notes, status = [], "PASS"
    canon_title = first(rec.get("title"))
    if fields.get("title"):
        sim = similarity(fields["title"], canon_title)
        if sim < 0.5:
            return "FAIL", [f"title does not match record: {canon_title!r}"]
        if sim < 0.85:
            status = "WARN"
            notes.append(f"title differs; record: {canon_title!r}")
    year = record_year(rec)
    if fields.get("year") and year and str(year) not in fields["year"]:
        status = "WARN"
        notes.append(f"year {fields['year']} vs record {year}")
    authors = rec.get("author") or []
    if fields.get("author") and authors:
        bib_first = normalize(fields["author"].split(" and ")[0])
        rec_family = normalize(authors[0].get("family", ""))
        if rec_family and rec_family not in bib_first:
            status = "WARN"
            notes.append(f"first author vs record {authors[0].get('family')!r}")
    journal = fields.get("journal") or fields.get("booktitle")
    canon_journal = first(rec.get("container-title"))
    if journal and canon_journal and similarity(journal, canon_journal) < 0.6:
        status = "WARN"
        notes.append(f"venue vs record {canon_journal!r}")
    for field, rkey in (("volume", "volume"), ("pages", "page")):
        mine, theirs = fields.get(field), rec.get(rkey)
        if mine and theirs and normalize(mine).replace(" ", "") != normalize(theirs).replace(" ", ""):
            status = "WARN"
            notes.append(f"{field} {mine} vs record {theirs}")
    return status, notes


def describe(rec: dict) -> str:
    authors = ", ".join(a.get("family", "") for a in (rec.get("author") or [])[:4])
    return f"{authors} ({record_year(rec)}). {first(rec.get('title'))}. {first(rec.get('container-title'))}"


def check_doi(doi: str, fields: dict, fetch: Fetcher) -> dict:
    try:
        rec = fetch(doi)
    except (urllib.error.URLError, TimeoutError, OSError) as err:
        return {"doi": doi, "status": "ERROR", "notes": [f"lookup failed: {err}"]}
    if rec is None:
        return {"doi": doi, "status": "FAIL", "notes": ["no Crossref record for this DOI"]}
    status, notes = compare(fields, rec)
    return {"doi": doi, "status": status, "notes": notes, "record": describe(rec)}


def run(dois: list[str], bib: Optional[Path], fetch: Fetcher) -> list[dict]:
    results = []
    for doi in dois:
        results.append({"key": None, **check_doi(clean_doi(doi), {}, fetch)})
    if bib:
        for entry in parse_bib(bib.read_text(encoding="utf-8")):
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
    return 1 if any(r["status"] == "FAIL" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
