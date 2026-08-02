#!/usr/bin/env python3
"""Check core DTCG token invariants without replacing schema validation."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ALIAS_RE = re.compile(r"^\{([^{}]+)\}$")
KNOWN_TYPES = {
    "boolean",
    "border",
    "color",
    "cubicBezier",
    "dimension",
    "duration",
    "fontFamily",
    "fontWeight",
    "gradient",
    "link",
    "number",
    "shadow",
    "strokeStyle",
    "transition",
    "typography",
}


@dataclass
class Token:
    path: str
    value: Any
    token_type: str | None
    raw: dict[str, Any]
    aliases: list[str] = field(default_factory=list)


def find_aliases(value: Any) -> list[str]:
    aliases: list[str] = []
    if isinstance(value, str):
        match = ALIAS_RE.match(value)
        if match:
            aliases.append(match.group(1))
    elif isinstance(value, list):
        for item in value:
            aliases.extend(find_aliases(item))
    elif isinstance(value, dict):
        for item in value.values():
            aliases.extend(find_aliases(item))
    return aliases


def collect_tokens(
    node: Any,
    prefix: tuple[str, ...] = (),
    inherited_type: str | None = None,
    errors: list[str] | None = None,
) -> dict[str, Token]:
    if errors is None:
        errors = []
    tokens: dict[str, Token] = {}
    if not isinstance(node, dict):
        return tokens

    local_type = node.get("$type", inherited_type)
    if "$value" in node:
        path = ".".join(prefix)
        if not path:
            errors.append("A token cannot live at the document root")
            return tokens
        tokens[path] = Token(
            path=path,
            value=node["$value"],
            token_type=local_type,
            raw=node,
            aliases=find_aliases(node["$value"]),
        )
        return tokens

    root_token = node.get("$root")
    if root_token is not None:
        if not isinstance(root_token, dict) or "$value" not in root_token:
            errors.append(f"{'.'.join(prefix) or '<root>'}: $root must be a token object")
        elif not prefix:
            errors.append("Document-level $root has no addressable token path")
        else:
            root_type = root_token.get("$type", local_type)
            path = ".".join(prefix)
            tokens[path] = Token(
                path=path,
                value=root_token["$value"],
                token_type=root_type,
                raw=root_token,
                aliases=find_aliases(root_token["$value"]),
            )

    for key, child in node.items():
        if key.startswith("$"):
            continue
        if not isinstance(child, dict):
            errors.append(f"{'.'.join(prefix + (key,))}: group member must be an object")
            continue
        tokens.update(collect_tokens(child, prefix + (key,), local_type, errors))
    return tokens


def validate_value_shape(token: Token, errors: list[str]) -> None:
    value = token.value
    token_type = token.token_type
    if token.aliases and isinstance(value, str):
        return

    def fail(expected: str) -> None:
        errors.append(f"{token.path}: {token_type} value must be {expected}")

    if token_type == "boolean" and not isinstance(value, bool):
        fail("a boolean")
    elif token_type == "number" and (not isinstance(value, (int, float)) or isinstance(value, bool)):
        fail("a number")
    elif token_type == "fontFamily":
        if not isinstance(value, str) and not (
            isinstance(value, list) and value and all(isinstance(item, str) for item in value)
        ):
            fail("a string or non-empty string array")
    elif token_type == "fontWeight":
        if not isinstance(value, (str, int, float)) or isinstance(value, bool):
            fail("a named or numeric weight")
    elif token_type in {"dimension", "duration"}:
        allowed_units = {"px", "rem"} if token_type == "dimension" else {"ms", "s"}
        if not isinstance(value, dict):
            fail("an object with numeric value and unit")
        else:
            amount = value.get("value")
            unit = value.get("unit")
            if not isinstance(amount, (int, float)) or isinstance(amount, bool) or unit not in allowed_units:
                errors.append(
                    f"{token.path}: {token_type} requires numeric value and unit in {sorted(allowed_units)}"
                )
    elif token_type == "cubicBezier":
        if not (
            isinstance(value, list)
            and len(value) == 4
            and all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in value)
        ):
            fail("an array of four numbers")
    elif token_type == "color":
        if not isinstance(value, dict):
            fail("an object with colorSpace, components and optional alpha")
        else:
            components = value.get("components")
            alpha = value.get("alpha", 1)
            if not isinstance(value.get("colorSpace"), str):
                errors.append(f"{token.path}: colorSpace must be a string")
            if not isinstance(components, list) or not components:
                errors.append(f"{token.path}: color components must be a non-empty array")
            if not isinstance(alpha, (int, float)) or isinstance(alpha, bool):
                errors.append(f"{token.path}: color alpha must be numeric")
    elif token_type == "typography":
        required = {"fontFamily", "fontSize", "fontWeight", "letterSpacing", "lineHeight"}
        if not isinstance(value, dict) or not required.issubset(value):
            fail("an object containing fontFamily, fontSize, fontWeight, letterSpacing and lineHeight")
    elif token_type == "transition":
        required = {"duration", "delay", "timingFunction"}
        if not isinstance(value, dict) or not required.issubset(value):
            fail("an object containing duration, delay and timingFunction")
    elif token_type == "border":
        required = {"color", "width", "style"}
        if not isinstance(value, dict) or not required.issubset(value):
            fail("an object containing color, width and style")
    elif token_type == "shadow":
        values = value if isinstance(value, list) else [value]
        required = {"color", "offsetX", "offsetY", "blur", "spread"}
        if not values or any(not isinstance(item, dict) or not required.issubset(item) for item in values):
            fail("a shadow object or non-empty array of shadow objects")


def detect_cycles(tokens: dict[str, Token]) -> list[list[str]]:
    cycles: list[list[str]] = []
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(name: str) -> None:
        state[name] = 1
        stack.append(name)
        for target in tokens[name].aliases:
            if target not in tokens:
                continue
            if state.get(target, 0) == 0:
                visit(target)
            elif state.get(target) == 1:
                start = stack.index(target)
                cycle = stack[start:] + [target]
                if cycle not in cycles:
                    cycles.append(cycle)
        stack.pop()
        state[name] = 2

    for name in tokens:
        if state.get(name, 0) == 0:
            visit(name)
    return cycles


def validate(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return {"file": str(path), "tokens": 0, "errors": [str(exc)], "warnings": []}

    if not isinstance(data, dict):
        errors.append("Document root must be an object")
        return {"file": str(path), "tokens": 0, "errors": errors, "warnings": warnings}

    tokens = collect_tokens(data, errors=errors)
    if not tokens:
        errors.append("No token with $value found")

    for name, token in tokens.items():
        if token.token_type is None:
            errors.append(f"{name}: missing $type and no inherited group type")
        elif token.token_type not in KNOWN_TYPES:
            warnings.append(f"{name}: unknown or extension type {token.token_type!r}")

        validate_value_shape(token, errors)

        if "$description" not in token.raw:
            warnings.append(f"{name}: public usage may need $description")

        deprecated = token.raw.get("$deprecated")
        if deprecated is not None and not isinstance(deprecated, (bool, str)):
            errors.append(f"{name}: $deprecated must be a boolean or string")

        for target in token.aliases:
            if target not in tokens:
                errors.append(f"{name}: unresolved alias {{{target}}}")
            elif token.token_type and tokens[target].token_type:
                if token.token_type != tokens[target].token_type:
                    errors.append(
                        f"{name}: alias type {token.token_type!r} does not match "
                        f"{target} type {tokens[target].token_type!r}"
                    )

    def find_extends(node: Any, prefix: tuple[str, ...] = ()) -> None:
        if not isinstance(node, dict):
            return
        if "$extends" in node:
            warnings.append(
                f"{'.'.join(prefix) or '<root>'}: $extends found; verify inherited groups with the official schema/toolchain"
            )
        for key, child in node.items():
            if not key.startswith("$"):
                find_extends(child, prefix + (key,))

    find_extends(data)

    for cycle in detect_cycles(tokens):
        errors.append("Alias cycle: " + " -> ".join(cycle))

    return {
        "file": str(path),
        "tokens": len(tokens),
        "aliases": sum(len(token.aliases) for token in tokens.values()),
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="DTCG JSON files")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit JSON")
    args = parser.parse_args()

    reports = [validate(path) for path in args.files]
    if args.as_json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        for report in reports:
            print(
                f"{report['file']}: {report['tokens']} tokens, "
                f"{report.get('aliases', 0)} aliases, "
                f"{len(report['errors'])} errors, {len(report['warnings'])} warnings"
            )
            for message in report["errors"]:
                print(f"  ERROR: {message}")
            for message in report["warnings"]:
                print(f"  WARN: {message}")
    return 1 if any(report["errors"] for report in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
