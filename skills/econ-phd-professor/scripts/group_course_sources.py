#!/usr/bin/env python3
"""Group same-stem TeX/PDF/Word files using local cloud metadata only.

Usage: python skills/econ-phd-professor/scripts/group_course_sources.py course-files.json [--output map.json]
Input is a JSON array with id, name, parent_id (or one-element parent_ids).
No network calls or file writes to Drive. Never infer identical content.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

FORMATS = {".pdf", ".tex", ".doc", ".docx"}


def group_sources(records: list[dict]) -> dict:
    groups = defaultdict(list)
    ungrouped = []
    for item in records:
        name = str(item.get("name") or item.get("title") or "")
        file_id = str(item.get("id") or item.get("file_id") or "")
        parent = str(item.get("parent_id") or "")
        if not parent:
            parents = item.get("parent_ids") or item.get("parents") or []
            if isinstance(parents, list) and len(parents) == 1:
                parent = str(parents[0])
        extension = Path(name).suffix.lower()
        if not file_id or not name or not parent or extension not in FORMATS:
            ungrouped.append({"id": file_id, "name": name, "reason": "missing metadata or unsupported format"})
            continue
        stem = name[:-len(Path(name).suffix)].casefold()
        groups[(parent, stem)].append({"id": file_id, "name": name, "format": extension, "parent_id": parent})
    docs = []
    for (parent, stem), members in sorted(groups.items()):
        members.sort(key=lambda x: (x["format"], x["name"].casefold(), x["id"]))
        formats = [x["format"] for x in members]
        docs.append({
            "parent_id": parent, "basename": stem, "files": members,
            "equivalence": "provisional" if len(members) > 1 else "not_assessed",
            "needs_review": len(set(formats)) != len(formats),
        })
    return {"logical_documents": docs, "ungrouped": ungrouped}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records = json.loads(args.manifest.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        parser.error("expected JSON array of file metadata")
    result = json.dumps(group_sources(records), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
