#!/usr/bin/env python3
"""Validate the Browse Visual References source catalog."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse


CATALOG_PATH = Path(__file__).resolve().parents[1] / "references" / "source-catalog.json"
FACET_FIELDS = ("deliverables", "patterns", "granularity", "content_formats", "contexts", "regions")
ACCESS_VALUES = {"public", "partial", "account-required", "subscription", "unstable"}
MCP_VALUES = {"none", "advertised"}
REQUIRED_FIELDS = {
    "id",
    "name",
    "url",
    "summary",
    *FACET_FIELDS,
    "best_for",
    "capture_targets",
    "access",
    "limitations",
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    try:
        data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read catalog: {exc}", file=sys.stderr)
        return 1

    vocabulary = data.get("vocabulary", {})
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        print("ERROR: sources must be a non-empty array", file=sys.stderr)
        return 1

    vocab_sets: dict[str, set[str]] = {}
    for field in FACET_FIELDS:
        values = vocabulary.get(field)
        if not isinstance(values, list) or not values or not all(isinstance(value, str) for value in values):
            fail(f"vocabulary.{field} must be a non-empty string array", errors)
            vocab_sets[field] = set()
        else:
            duplicates = sorted({value for value in values if values.count(value) > 1})
            if duplicates:
                fail(f"vocabulary.{field} has duplicates: {duplicates}", errors)
            vocab_sets[field] = set(values)

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    for index, source in enumerate(sources):
        label = source.get("id", f"index {index}") if isinstance(source, dict) else f"index {index}"
        if not isinstance(source, dict):
            fail(f"{label}: source must be an object", errors)
            continue

        missing = sorted(REQUIRED_FIELDS - source.keys())
        if missing:
            fail(f"{label}: missing fields {missing}", errors)

        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id or source_id in seen_ids:
            fail(f"{label}: id must be a unique non-empty string", errors)
        else:
            seen_ids.add(source_id)

        url = source.get("url")
        parsed = urlparse(url) if isinstance(url, str) else None
        normalized_url = url.rstrip("/") if isinstance(url, str) else ""
        if not parsed or parsed.scheme not in {"http", "https"} or not parsed.netloc:
            fail(f"{label}: url must be an absolute HTTP(S) URL", errors)
        elif normalized_url in seen_urls:
            fail(f"{label}: duplicate URL {url}", errors)
        else:
            seen_urls.add(normalized_url)

        for field in FACET_FIELDS:
            values = source.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(value, str) for value in values):
                fail(f"{label}: {field} must be a non-empty string array", errors)
                continue
            unknown = sorted(set(values) - vocab_sets.get(field, set()))
            if unknown:
                fail(f"{label}: unknown {field} values {unknown}", errors)

        for field in ("best_for", "capture_targets", "limitations"):
            values = source.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(value, str) and value for value in values):
                fail(f"{label}: {field} must be a non-empty string array", errors)

        access = source.get("access")
        if not isinstance(access, dict):
            fail(f"{label}: access must be an object", errors)
        else:
            if access.get("browser") not in ACCESS_VALUES:
                fail(f"{label}: invalid browser access {access.get('browser')!r}", errors)
            if access.get("mcp") not in MCP_VALUES:
                fail(f"{label}: invalid MCP status {access.get('mcp')!r}", errors)
            languages = access.get("languages")
            if not isinstance(languages, list) or not languages or not all(isinstance(value, str) for value in languages):
                fail(f"{label}: access.languages must be a non-empty string array", errors)

    expected_count = data.get("source_count")
    if expected_count != len(sources):
        fail(f"source_count is {expected_count!r}, expected {len(sources)}", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(sources)} sources and {len(seen_urls)} unique URLs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
