#!/usr/bin/env python3
"""Audit raw UI values and CSS custom-property usage in source trees."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


SOURCE_EXTENSIONS = {
    ".css", ".scss", ".sass", ".less", ".styl",
    ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte",
    ".html", ".mdx", ".swift", ".kt", ".kts", ".xml",
}
IGNORED_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build", "coverage",
    ".next", ".nuxt", ".cache", "generated", "Pods",
}
COLOR_RE = re.compile(
    r"(?<![\w-])(?:#[0-9a-fA-F]{3,8}\b|(?:rgb|rgba|hsl|hsla|oklab|oklch|lab|lch|color)\([^()\n;{}]*\))"
)
DIMENSION_RE = re.compile(r"(?<![\w.-])-?(?:\d+\.\d+|\d+)(?:px|rem|em)\b")
VAR_RE = re.compile(r"var\(\s*(--[A-Za-z0-9_-]+)")
DECLARATION_RE = re.compile(r"(--[A-Za-z0-9_-]+)\s*:")


def iter_files(roots: Iterable[Path]) -> Iterable[Path]:
    for root in roots:
        if root.is_file():
            if root.suffix in SOURCE_EXTENSIONS:
                yield root
            continue
        for path in root.rglob("*"):
            if any(part in IGNORED_DIRS for part in path.parts):
                continue
            if path.is_file() and path.suffix in SOURCE_EXTENSIONS:
                yield path


def flatten_tokens(node: Any, prefix: tuple[str, ...] = ()) -> set[str]:
    names: set[str] = set()
    if not isinstance(node, dict):
        return names
    if "$value" in node:
        names.add(".".join(prefix))
        return names
    for key, value in node.items():
        if not key.startswith("$"):
            names.update(flatten_tokens(value, prefix + (key,)))
    return names


def load_expected_vars(path: Path | None, prefix: str) -> set[str]:
    if path is None:
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    normalized_prefix = prefix.strip("-")
    lead = f"--{normalized_prefix}-" if normalized_prefix else "--"
    return {lead + name.replace(".", "-") for name in flatten_tokens(data)}


def load_manifest_vars(path: Path | None) -> set[str]:
    if path is None:
        return set()
    text = path.read_text(encoding="utf-8")
    return set(DECLARATION_RE.findall(text))


def audit(
    roots: list[Path], expected_vars: set[str], dimensions: bool, report_unused: bool
) -> dict[str, Any]:
    raw_colors: list[dict[str, Any]] = []
    raw_dimensions: list[dict[str, Any]] = []
    used: Counter[str] = Counter()
    declared: Counter[str] = Counter()
    scanned = 0

    for path in sorted(set(iter_files(roots))):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        scanned += 1
        for number, line in enumerate(text.splitlines(), start=1):
            for match in COLOR_RE.finditer(line):
                raw_colors.append({"file": str(path), "line": number, "value": match.group(0)})
            if dimensions:
                for match in DIMENSION_RE.finditer(line):
                    value = match.group(0)
                    if value not in {"0px", "0rem", "0em"}:
                        raw_dimensions.append({"file": str(path), "line": number, "value": value})
            used.update(VAR_RE.findall(line))
            declared.update(DECLARATION_RE.findall(line))

    unknown = sorted(name for name in used if expected_vars and name not in expected_vars)
    unused = sorted(name for name in expected_vars if name not in used) if report_unused else []
    return {
        "files_scanned": scanned,
        "raw_colors": raw_colors,
        "raw_dimensions": raw_dimensions,
        "custom_properties_used": dict(sorted(used.items())),
        "custom_properties_declared": dict(sorted(declared.items())),
        "unmapped_custom_properties": unknown,
        "expected_but_unused": unused,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path, help="Files or directories to scan")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--manifest", type=Path, help="Generated CSS manifest containing actual token declarations")
    source.add_argument("--tokens", type=Path, help="DTCG JSON; CSS names are inferred heuristically")
    parser.add_argument("--css-prefix", default="", help="Prefix used only with --tokens, for example ds")
    parser.add_argument("--include-dimensions", action="store_true", help="Report px/rem/em literals")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit JSON")
    args = parser.parse_args()

    try:
        expected = load_manifest_vars(args.manifest) or load_expected_vars(args.tokens, args.css_prefix)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Unable to read token file: {exc}", file=sys.stderr)
        return 2

    report = audit(args.roots, expected, args.include_dimensions, bool(args.manifest))
    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Files scanned: {report['files_scanned']}")
        print(f"Raw colors: {len(report['raw_colors'])}")
        print(f"Raw dimensions: {len(report['raw_dimensions'])}")
        print(f"Custom properties used: {len(report['custom_properties_used'])}")
        print(f"Unmapped custom-property candidates: {len(report['unmapped_custom_properties'])}")
        print(f"Expected but unused: {len(report['expected_but_unused'])}")
        for item in report["raw_colors"]:
            print(f"  COLOR {item['file']}:{item['line']} {item['value']}")
        for item in report["raw_dimensions"]:
            print(f"  DIMENSION {item['file']}:{item['line']} {item['value']}")
        for name in report["unmapped_custom_properties"]:
            print(f"  UNMAPPED {name}")
    if report["files_scanned"] == 0:
        print("No supported source file found in the requested roots", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
