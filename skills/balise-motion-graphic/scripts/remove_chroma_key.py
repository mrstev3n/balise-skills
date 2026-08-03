#!/usr/bin/env python3
"""Remove a flat chroma-key background and write a PNG/WebP with alpha."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def roots() -> list[Path]:
    found = []
    if os.environ.get("MOTION_ASSET_TOOLS_HOME"):
        found.append(Path(os.environ["MOTION_ASSET_TOOLS_HOME"]).expanduser())
    found.append(Path.cwd() / ".motion-asset-tools")
    if sys.platform == "win32":
        found.append(Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local")) / "motion-asset-tools")
    elif sys.platform == "darwin":
        found.append(Path.home() / "Library/Application Support/motion-asset-tools")
    else:
        found.append(Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share")) / "motion-asset-tools")
    return found


def venv_python() -> Path | None:
    relative = Path("venv/Scripts/python.exe" if sys.platform == "win32" else "venv/bin/python")
    return next((root / relative for root in roots() if (root / relative).exists()), None)


def has_pillow() -> bool:
    try:
        import PIL  # noqa: F401
        return True
    except ImportError:
        return False


def magick() -> str | None:
    return shutil.which("magick") or (None if sys.platform == "win32" else shutil.which("convert"))


def identify_command(command: str) -> list[str]:
    if Path(command).name.lower().startswith("magick"):
        return [command, "identify"]
    identify = shutil.which("identify")
    if not identify:
        raise RuntimeError("ImageMagick identify command is unavailable")
    return [identify]


def reexec_isolated(args: argparse.Namespace) -> None:
    if args.backend == "imagemagick" or has_pillow() or os.environ.get("MOTION_ASSET_REEXEC"):
        return
    python = venv_python()
    if python:
        env = dict(os.environ, MOTION_ASSET_REEXEC="1")
        raise SystemExit(subprocess.run([str(python), str(Path(__file__).resolve()), *sys.argv[1:]], env=env).returncode)


def parse_color(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"#?([0-9a-fA-F]{6})", value.strip())
    if not match:
        raise ValueError("key must be auto-border or #RRGGBB")
    raw = match.group(1)
    return tuple(int(raw[i : i + 2], 16) for i in (0, 2, 4))


def hex_color(color: tuple[int, int, int]) -> str:
    return "#%02x%02x%02x" % color


def border_key(image, key: str) -> tuple[int, int, int]:
    if key != "auto-border":
        return parse_color(key)
    rgb = image.convert("RGB")
    width, height = rgb.size
    samples = []
    for x in range(0, width, max(1, width // 32)):
        samples += [rgb.getpixel((x, 0)), rgb.getpixel((x, height - 1))]
    for y in range(0, height, max(1, height // 32)):
        samples += [rgb.getpixel((0, y)), rgb.getpixel((width - 1, y))]
    return tuple(sorted(channel)[len(samples) // 2] for channel in zip(*samples))


def despill(rgb: tuple[int, int, int], key: tuple[int, int, int], alpha: int) -> tuple[int, int, int]:
    if alpha in (0, 255):
        return rgb
    dominant = max(range(3), key=lambda i: key[i] - min(key[(i + 1) % 3], key[(i + 2) % 3]))
    values = list(rgb)
    neighbor = max(values[(dominant + 1) % 3], values[(dominant + 2) % 3])
    if values[dominant] > neighbor:
        mix = 1.0 - alpha / 255.0
        values[dominant] = round(values[dominant] * (1 - mix) + neighbor * mix)
    return tuple(values)


def checkerboard(image, path: Path) -> None:
    from PIL import Image, ImageDraw
    cell = max(8, min(image.size) // 24)
    board = Image.new("RGBA", image.size, (236, 236, 236, 255))
    draw = ImageDraw.Draw(board)
    for y in range(0, image.height, cell):
        for x in range(0, image.width, cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(188, 188, 188, 255))
    board.alpha_composite(image)
    path.parent.mkdir(parents=True, exist_ok=True)
    board.convert("RGB").save(path)


def with_pillow(args: argparse.Namespace) -> dict[str, object]:
    from PIL import Image, ImageFilter
    image = Image.open(args.input).convert("RGBA")
    key = border_key(image, args.key)
    alpha = Image.new("L", image.size, 0)
    pixels, matte = image.load(), alpha.load()
    for y in range(image.height):
        for x in range(image.width):
            red, green, blue, original_alpha = pixels[x, y]
            distance = math.dist((red, green, blue), key)
            value = 0 if distance <= 18 else 255 if distance >= 145 else round((distance - 18) / 127 * 255)
            value = round(value * original_alpha / 255)
            if args.despill:
                red, green, blue = despill((red, green, blue), key, value)
            pixels[x, y] = (red, green, blue, original_alpha)
            matte[x, y] = value
    if args.edge_contract:
        alpha = alpha.filter(ImageFilter.MinFilter(args.edge_contract * 2 + 1))
    image.putalpha(alpha)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output)
    if args.preview:
        checkerboard(image, args.preview)
    return {"backend": "pillow", "key": hex_color(key), "size": list(image.size), "output": str(args.output)}


def magick_key(command: str, source: Path, key: str) -> str:
    if key != "auto-border":
        return hex_color(parse_color(key))
    result = subprocess.run([command, str(source), "-format", "%[pixel:p{0,0}]", "info:"], check=True, capture_output=True, text=True)
    match = re.search(r"#([0-9A-Fa-f]{6})", result.stdout)
    if match:
        return f"#{match.group(1)}"
    match = re.search(r"s?rgba?\((\d+)[, ]+(\d+)[, ]+(\d+)", result.stdout)
    if not match:
        raise RuntimeError(f"could not parse border color: {result.stdout.strip()}")
    return hex_color(tuple(int(match.group(i)) for i in (1, 2, 3)))


def with_magick(args: argparse.Namespace) -> dict[str, object]:
    command = magick()
    if not command:
        raise RuntimeError("ImageMagick is unavailable")
    key = magick_key(command, args.input, args.key)
    operation = [command, str(args.input), "-alpha", "on", "-fuzz", "8%", "-transparent", key]
    if args.edge_contract:
        operation += ["-channel", "A", "-morphology", "Erode", f"Disk:{args.edge_contract}", "+channel"]
    if args.despill:
        print("ImageMagick fallback uses key removal only; use Pillow for soft despill.", file=sys.stderr)
    operation.append(str(args.output))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(operation, check=True)
    info = subprocess.run([*identify_command(command), "-format", "%w %h %[channels]", str(args.output)], check=True, capture_output=True, text=True).stdout.split()
    if len(info) < 3 or "a" not in info[2].lower():
        raise RuntimeError("output does not report an alpha channel")
    if args.preview:
        args.preview.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [command, "-size", f"{info[0]}x{info[1]}", "pattern:checkerboard", str(args.output), "-compose", "over", "-composite", str(args.preview)],
            check=True,
        )
    return {"backend": "imagemagick", "key": key.lower(), "size": [int(info[0]), int(info[1])], "channels": info[2], "despillApplied": False, "output": str(args.output)}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--key", default="auto-border")
    parser.add_argument("--backend", choices=("auto", "pillow", "imagemagick"), default="auto")
    parser.add_argument("--despill", action="store_true")
    parser.add_argument("--edge-contract", type=int, default=0)
    parser.add_argument("--preview", type=Path)
    return parser.parse_args()


def main() -> int:
    args = arguments()
    if not args.input.is_file():
        raise SystemExit(f"input does not exist: {args.input}")
    if args.output.suffix.lower() not in {".png", ".webp"}:
        raise SystemExit("output must be PNG or WebP")
    if not 0 <= args.edge_contract <= 8:
        raise SystemExit("--edge-contract must be between 0 and 8")
    reexec_isolated(args)
    try:
        if (args.backend == "pillow" and has_pillow()) or (args.backend == "auto" and has_pillow()):
            report = with_pillow(args)
        elif args.backend in {"auto", "imagemagick"} and magick():
            report = with_magick(args)
        else:
            setup = Path(__file__).with_name("setup_asset_pipeline.py")
            subprocess.run([sys.executable, str(setup), "--check", "--backend", args.backend], check=False)
            raise RuntimeError(f"no backend available; run {sys.executable} {setup} --install --backend {args.backend} --scope user")
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Chroma-key removal failed: {error}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
