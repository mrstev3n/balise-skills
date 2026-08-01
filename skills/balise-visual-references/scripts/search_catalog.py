#!/usr/bin/env python3
"""Search the visual-reference catalog with cumulative facets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


CATALOG_PATH = Path(__file__).resolve().parents[1] / "references" / "source-catalog.json"
ARG_TO_FIELD = {
    "deliverable": "deliverables",
    "pattern": "patterns",
    "granularity": "granularity",
    "format": "content_formats",
    "context": "contexts",
    "region": "regions",
}
WEIGHTS = {
    "deliverables": 3,
    "patterns": 3,
    "granularity": 2,
    "content_formats": 1,
    "contexts": 1,
    "regions": 1,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    for argument in ARG_TO_FIELD:
        parser.add_argument(f"--{argument}", action="append", default=[])
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--require-all-facets", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    requested = {
        field: getattr(args, argument)
        for argument, field in ARG_TO_FIELD.items()
        if getattr(args, argument)
    }
    if not requested:
        print("ERROR: provide at least one facet", file=sys.stderr)
        return 2
    if args.limit < 1:
        print("ERROR: --limit must be positive", file=sys.stderr)
        return 2

    for field, values in requested.items():
        allowed = set(data["vocabulary"][field])
        unknown = sorted(set(values) - allowed)
        if unknown:
            print(f"ERROR: unknown {field}: {', '.join(unknown)}", file=sys.stderr)
            return 2

    results = []
    for source in data["sources"]:
        matched = {
            field: sorted(set(values) & set(source[field]))
            for field, values in requested.items()
        }
        matched_facets = sum(bool(values) for values in matched.values())
        if args.require_all_facets and matched_facets != len(requested):
            continue
        if matched_facets == 0:
            continue
        score = sum(WEIGHTS[field] * len(values) for field, values in matched.items())
        results.append(
            {
                "id": source["id"],
                "name": source["name"],
                "url": source["url"],
                "score": score,
                "matched": {field: values for field, values in matched.items() if values},
                "summary": source["summary"],
                "best_for": source["best_for"],
                "capture_targets": source["capture_targets"],
                "browser_access": source["access"]["browser"],
                "mcp": source["access"]["mcp"],
                "limitations": source["limitations"],
            }
        )

    results.sort(key=lambda item: (-item["score"], item["name"].casefold()))
    results = results[: args.limit]
    if args.as_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for result in results:
            facets = "; ".join(
                f"{field}={','.join(values)}" for field, values in result["matched"].items()
            )
            print(f"{result['score']:>2}  {result['name']}  {result['url']}")
            print(f"    {facets} | browser={result['browser_access']} | mcp={result['mcp']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
