#!/usr/bin/env python3
"""Extract sampled frames and a contact sheet from a local video using FFmpeg."""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, capture_output=True, text=True)


def probe_duration(video: Path) -> float:
    result = run([
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(video),
    ])
    try:
        duration = float(result.stdout.strip())
    except ValueError as error:
        raise RuntimeError("ffprobe did not return a valid duration") from error
    if not math.isfinite(duration) or duration <= 0:
        raise RuntimeError("video duration must be positive")
    return duration


def parse_timestamps(raw: str, duration: float) -> list[float]:
    timestamps: list[float] = []
    for value in raw.split(","):
        value = value.strip()
        if not value:
            continue
        try:
            timestamp = float(value)
        except ValueError as error:
            raise ValueError(f"invalid timestamp: {value}") from error
        if timestamp < 0 or timestamp >= duration:
            raise ValueError(
                f"timestamp {timestamp:g}s must be within 0 <= t < {duration:.3f}s"
            )
        timestamps.append(timestamp)
    if not timestamps:
        raise ValueError("provide at least one timestamp")
    return timestamps


def sampled_timestamps(duration: float, count: int) -> list[float]:
    if count < 2:
        raise ValueError("--frames must be at least 2")
    start = min(duration * 0.03, 0.25)
    end = max(start, duration - min(duration * 0.03, 0.25) - 0.001)
    if count == 2:
        return [start, end]
    return [start + (end - start) * index / (count - 1) for index in range(count)]


def ensure_tools() -> None:
    missing = [name for name in ("ffmpeg", "ffprobe") if shutil.which(name) is None]
    if missing:
        raise RuntimeError(f"missing required executable(s): {', '.join(missing)}")


def ensure_output(output_dir: Path, overwrite: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    managed = list(output_dir.glob("frame-*.png")) + [output_dir / "contact-sheet.png", output_dir / "manifest.json"]
    existing = [path for path in managed if path.exists()]
    if existing and not overwrite:
        names = ", ".join(path.name for path in existing[:5])
        raise RuntimeError(f"output already contains generated files ({names}); pass --overwrite")
    if overwrite:
        for path in existing:
            path.unlink()


def extract_frame(video: Path, output: Path, timestamp: float, width: int) -> bool:
    if output.exists():
        output.unlink()
    scale = f"scale={width}:-2:flags=lanczos" if width > 0 else "null"
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{timestamp:.6f}", "-i", str(video),
        "-frames:v", "1", "-vf", scale, str(output),
    ])
    return output.is_file() and output.stat().st_size > 0


def extract_sampled_frame(
    video: Path, output: Path, timestamp: float, width: int
) -> float:
    """Extract a sampled frame, backing off from EOF when needed."""
    candidates = [timestamp]
    candidates.extend(max(0.0, timestamp - offset) for offset in (0.02, 0.05, 0.1, 0.2, 0.5))
    candidates.append(0.0)
    for candidate in dict.fromkeys(candidates):
        if extract_frame(video, output, candidate, width):
            return candidate
    raise RuntimeError(f"ffmpeg produced no frame near {timestamp:.6f}s")


def create_contact_sheet(output_dir: Path, count: int, columns: int) -> Path:
    rows = math.ceil(count / columns)
    output = output_dir / "contact-sheet.png"
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-framerate", "1", "-i", str(output_dir / "frame-%03d.png"),
        "-frames:v", "1",
        "-vf", f"tile={columns}x{rows}:padding=12:margin=12:color=white",
        str(output),
    ])
    return output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract representative PNG frames and a contact sheet from a local video."
    )
    parser.add_argument("video", type=Path, help="source video file")
    parser.add_argument("output_dir", type=Path, help="project-local output directory")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--frames", type=int, default=16, help="regular sample count (default: 16)")
    group.add_argument("--timestamps", help="comma-separated timestamps in seconds")
    parser.add_argument("--columns", type=int, default=4, help="contact-sheet columns (default: 4)")
    parser.add_argument("--width", type=int, default=480, help="frame width in pixels; 0 keeps source width")
    parser.add_argument("--overwrite", action="store_true", help="replace files generated by this script")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    video = args.video.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()
    try:
        ensure_tools()
        if not video.is_file():
            raise RuntimeError(f"source video does not exist: {video}")
        if args.columns < 1:
            raise ValueError("--columns must be at least 1")
        if args.width < 0:
            raise ValueError("--width must be 0 or greater")
        duration = probe_duration(video)
        requested_timestamps = (
            parse_timestamps(args.timestamps, duration)
            if args.timestamps
            else sampled_timestamps(duration, args.frames)
        )
        ensure_output(output_dir, args.overwrite)
        timestamps: list[float] = []
        for index, timestamp in enumerate(requested_timestamps, start=1):
            output = output_dir / f"frame-{index:03d}.png"
            if args.timestamps:
                if not extract_frame(video, output, timestamp, args.width):
                    raise RuntimeError(f"ffmpeg produced no frame at explicit timestamp {timestamp:.6f}s")
                timestamps.append(timestamp)
            else:
                timestamps.append(extract_sampled_frame(video, output, timestamp, args.width))
        contact_sheet = create_contact_sheet(output_dir, len(timestamps), args.columns)
        manifest = {
            "source": str(video),
            "duration_seconds": round(duration, 6),
            "timestamps_seconds": [round(value, 6) for value in timestamps],
            "frame_width": args.width or "source",
            "contact_sheet": contact_sheet.name,
        }
        (output_dir / "manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except (RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        print(f"error: {detail}", file=sys.stderr)
        return 1
    print(f"Extracted {len(timestamps)} frames to {output_dir}")
    print(f"Contact sheet: {contact_sheet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
