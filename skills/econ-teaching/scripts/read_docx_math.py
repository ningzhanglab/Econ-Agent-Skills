#!/usr/bin/env python3
"""Read a Word (.docx) file as text while keeping its equations.

A plain-text export of a .docx drops every equation. Equations typed in Word's
equation editor are stored as Office Math (OMML) in word/document.xml; this
script renders them as LaTeX-like linear text between dollar signs, in reading
order with the surrounding paragraphs and tables.

Usage: python skills/econ-teaching/scripts/read_docx_math.py "notes.docx"
       python skills/econ-teaching/scripts/read_docx_math.py "notes.docx" -o notes.txt

Standard library only; the source file is opened read-only and never changed.

What it cannot do:
- Pictures and older embedded equation objects are images. They are marked
  [IMAGE name] or [EMBEDDED OBJECT name] and must be viewed before anything is
  said about them. The summary line on stderr counts them.
- The output is a reading aid, not typeset mathematics. Fractions print as
  (num)/(den), matrices as [matrix: a & b ; c & d]. Check a few equations
  against a rendered PDF of the same file when one exists.
- Headers, footers, footnotes, text boxes and tracked-change history are not read.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
V = "{urn:schemas-microsoft-com:vml}"

ACCENTS = {
    "̂": "\\hat", "^": "\\hat",
    "̃": "\\tilde", "~": "\\tilde",
    "̄": "\\bar", "̅": "\\bar", "¯": "\\bar",
    "̇": "\\dot", "⃗": "\\vec",
}


def _children(node: ET.Element, tag: str) -> list[ET.Element]:
    return [c for c in node if c.tag == M + tag]


def _part(node: ET.Element, tag: str) -> str:
    child = node.find(M + tag)
    return math_to_text(child) if child is not None else ""


def _group(text: str) -> str:
    return text if len(text) == 1 else "{" + text + "}"


def _property(node: ET.Element, prop: str, name: str, default: str) -> str:
    holder = node.find(M + prop)
    if holder is not None and holder.find(M + name) is not None:
        return holder.find(M + name).get(M + "val", default)
    return default


def math_to_text(node: ET.Element) -> str:
    """Render one Office Math subtree as linear text."""
    out: list[str] = []
    for c in node:
        tag = c.tag.replace(M, "")
        if c.tag == M + "r":
            out.append("".join(t.text or "" for t in c.iter(M + "t")))
        elif tag == "f":
            out.append("(" + _part(c, "num") + ")/(" + _part(c, "den") + ")")
        elif tag == "sSub":
            out.append(_part(c, "e") + "_" + _group(_part(c, "sub")))
        elif tag == "sSup":
            out.append(_part(c, "e") + "^" + _group(_part(c, "sup")))
        elif tag == "sSubSup":
            out.append(_part(c, "e") + "_" + _group(_part(c, "sub")) + "^" + _group(_part(c, "sup")))
        elif tag == "sPre":
            out.append("_" + _group(_part(c, "sub")) + "^" + _group(_part(c, "sup")) + _part(c, "e"))
        elif tag == "d":
            begin = _property(c, "dPr", "begChr", "(")
            end = _property(c, "dPr", "endChr", ")")
            out.append(begin + ", ".join(math_to_text(e) for e in _children(c, "e")) + end)
        elif tag == "rad":
            degree = _part(c, "deg")
            out.append("sqrt" + ("[" + degree + "]" if degree else "") + "(" + _part(c, "e") + ")")
        elif tag == "nary":
            symbol = _property(c, "naryPr", "chr", "∫")
            lower, upper = _part(c, "sub"), _part(c, "sup")
            out.append(symbol + ("_" + _group(lower) if lower else "") + ("^" + _group(upper) if upper else "") + " " + _part(c, "e"))
        elif tag == "acc":
            mark = _property(c, "accPr", "chr", "̂")
            out.append(ACCENTS.get(mark, "\\accent[" + mark + "]") + "{" + _part(c, "e") + "}")
        elif tag == "bar":
            out.append("\\bar{" + _part(c, "e") + "}")
        elif tag == "func":
            out.append(_part(c, "fName") + " " + _part(c, "e"))
        elif tag == "limLow":
            out.append(_part(c, "e") + "_{" + _part(c, "lim") + "}")
        elif tag == "limUpp":
            out.append(_part(c, "e") + "^{" + _part(c, "lim") + "}")
        elif tag == "m":
            rows = [" & ".join(math_to_text(e) for e in _children(row, "e")) for row in _children(c, "mr")]
            out.append("[matrix: " + " ; ".join(rows) + "]")
        elif tag == "eqArr":
            out.append(" ;; ".join(math_to_text(e) for e in _children(c, "e")))
        elif tag in ("groupChr", "box", "borderBox", "phant"):
            out.append(_part(c, "e"))
        elif tag.endswith("Pr"):
            continue
        else:
            out.append(math_to_text(c))
    return "".join(out)


class _Reader:
    def __init__(self, relationships: dict[str, str]):
        self.relationships = relationships
        self.equations = 0
        self.images = 0
        self.objects = 0

    def _walk(self, node: ET.Element, out: list[str]) -> None:
        for c in node:
            if c.tag in (M + "oMath", M + "oMathPara"):
                maths = [c] if c.tag == M + "oMath" else c.findall(M + "oMath")
                for one in maths:
                    self.equations += 1
                    out.append(" $" + math_to_text(one) + "$ ")
            elif c.tag == W + "t":
                out.append(c.text or "")
            elif c.tag == W + "tab":
                out.append("\t")
            elif c.tag == A + "blip":
                self.images += 1
                out.append(" [IMAGE " + self.relationships.get(c.get(R + "embed"), "?") + "] ")
            elif c.tag == V + "imagedata":
                self.objects += 1
                out.append(" [EMBEDDED OBJECT " + self.relationships.get(c.get(R + "id"), "?") + "] ")
            else:
                self._walk(c, out)

    def paragraph(self, node: ET.Element) -> str:
        out: list[str] = []
        self._walk(node, out)
        return "".join(out)

    def block(self, node: ET.Element, lines: list[str]) -> None:
        for c in node:
            if c.tag == W + "p":
                lines.append(self.paragraph(c))
            elif c.tag == W + "tbl":
                for row in c.iter(W + "tr"):
                    cells = [" ".join(self.paragraph(p) for p in cell.iter(W + "p")) for cell in row.findall(W + "tc")]
                    lines.append(" | ".join(cells))
            elif c.tag == W + "sdt":
                content = c.find(W + "sdtContent")
                if content is not None:
                    self.block(content, lines)


def read_docx(path: str | Path) -> tuple[str, dict[str, int]]:
    """Return (text, counts) where counts has equations, images and embedded_objects."""
    with zipfile.ZipFile(path) as archive:
        relationships: dict[str, str] = {}
        if "word/_rels/document.xml.rels" in archive.namelist():
            for rel in ET.fromstring(archive.read("word/_rels/document.xml.rels")):
                relationships[rel.get("Id")] = rel.get("Target")
        root = ET.fromstring(archive.read("word/document.xml"))
    body = root.find(W + "body")
    reader = _Reader(relationships)
    lines: list[str] = []
    if body is not None:
        reader.block(body, lines)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    counts = {"equations": reader.equations, "images": reader.images, "embedded_objects": reader.objects}
    return text, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("docx")
    parser.add_argument("-o", "--output", help="write the text here instead of standard output")
    args = parser.parse_args()
    try:
        text, counts = read_docx(args.docx)
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as error:
        print(f"ERROR: could not read {args.docx}: {error}", file=sys.stderr)
        return 1
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")
    print(
        f"{counts['equations']} equation(s) read; {counts['images']} image(s) and "
        f"{counts['embedded_objects']} embedded object(s) NOT read and need viewing.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
