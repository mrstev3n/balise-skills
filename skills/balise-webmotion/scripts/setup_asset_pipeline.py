#!/usr/bin/env python3
"""Inspect or install the local still-image asset pipeline.

The default installation is an isolated Pillow virtual environment. ImageMagick
installation is system-level and therefore requires both --scope system and
--allow-system.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def data_root(scope: str) -> Path:
    override = os.environ.get("MOTION_ASSET_TOOLS_HOME")
    if override:
        return Path(override).expanduser().resolve()
    if scope == "project":
        return (Path.cwd() / ".motion-asset-tools").resolve()
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
        return base / "motion-asset-tools"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "motion-asset-tools"
    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")) / "motion-asset-tools"


def venv_python(root: Path) -> Path:
    return root / "venv" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


def command_version(command: list[str]) -> str | None:
    try:
        result = subprocess.run(command, check=False, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return None
    text = (result.stdout or result.stderr).strip().splitlines()
    return text[0] if result.returncode == 0 and text else None


def pillow_version(python: Path | None = None) -> str | None:
    executable = str(python or Path(sys.executable))
    try:
        result = subprocess.run(
            [executable, "-c", "from PIL import __version__; print(__version__)"],
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def writable_parent(path: Path) -> bool:
    candidate = path
    while not candidate.exists() and candidate != candidate.parent:
        candidate = candidate.parent
    return candidate.is_dir() and os.access(candidate, os.W_OK)


def inventory(scope: str) -> dict[str, object]:
    root = data_root(scope)
    isolated_python = venv_python(root)
    magick = shutil.which("magick") or (None if sys.platform == "win32" else shutil.which("convert"))
    managers = [name for name in ("brew", "apt-get", "dnf", "pacman", "winget") if shutil.which(name)]
    current_pillow = pillow_version()
    isolated_pillow = pillow_version(isolated_python) if isolated_python.exists() else None
    return {
        "platform": platform.platform(),
        "python": sys.executable,
        "pythonVersion": platform.python_version(),
        "pillowCurrent": current_pillow,
        "pillowIsolated": isolated_pillow,
        "isolatedPython": str(isolated_python) if isolated_python.exists() else None,
        "imagemagick": magick,
        "imagemagickVersion": command_version([magick, "-version"]) if magick else None,
        "uv": shutil.which("uv"),
        "packageManagers": managers,
        "dataRoot": str(root),
        "dataRootWritable": writable_parent(root),
        "runningAsAdmin": bool(hasattr(os, "geteuid") and os.geteuid() == 0),
        "availableBackends": [
            name
            for name, available in (("pillow", bool(current_pillow or isolated_pillow)), ("imagemagick", bool(magick)))
            if available
        ],
    }


def run(command: list[str]) -> None:
    print("Running:", " ".join(command), file=sys.stderr)
    subprocess.run(command, check=True)


def install_pillow(scope: str, allow_system: bool) -> dict[str, object]:
    if scope == "system":
        if not allow_system:
            raise RuntimeError("System Pillow installation requires --allow-system.")
        run([sys.executable, "-m", "pip", "install", "Pillow"])
        return inventory(scope)

    root = data_root(scope)
    python = venv_python(root)
    root.mkdir(parents=True, exist_ok=True)
    if not python.exists():
        uv = shutil.which("uv")
        if uv:
            run([uv, "venv", str(root / "venv"), "--python", sys.executable])
        else:
            run([sys.executable, "-m", "venv", str(root / "venv")])
    uv = shutil.which("uv")
    if uv:
        run([uv, "pip", "install", "--python", str(python), "Pillow"])
    else:
        run([str(python), "-m", "pip", "install", "Pillow"])
    marker = root / "runtime.json"
    marker.write_text(json.dumps({"python": str(python), "backend": "pillow"}, indent=2) + "\n")
    return inventory(scope)


def imagemagick_install_command() -> list[str] | None:
    if shutil.which("brew"):
        return ["brew", "install", "imagemagick"]
    if shutil.which("apt-get"):
        return ["sudo", "apt-get", "install", "-y", "imagemagick"]
    if shutil.which("dnf"):
        return ["sudo", "dnf", "install", "-y", "ImageMagick"]
    if shutil.which("pacman"):
        return ["sudo", "pacman", "-S", "--needed", "imagemagick"]
    if shutil.which("winget"):
        return ["winget", "install", "--id", "ImageMagick.ImageMagick", "-e"]
    return None


def install_imagemagick(scope: str, allow_system: bool) -> dict[str, object]:
    if scope != "system" or not allow_system:
        raise RuntimeError("ImageMagick installation requires --scope system --allow-system.")
    command = imagemagick_install_command()
    if not command:
        raise RuntimeError("No supported package manager found. Install ImageMagick manually, then rerun --check.")
    run(command)
    return inventory(scope)


def backend_ready(state: dict[str, object], backend: str) -> bool:
    available = state["availableBackends"]
    return bool(available) if backend == "auto" else backend in available


def uninstall_hint(state: dict[str, object], scope: str) -> str:
    if scope in {"user", "project"} and state.get("isolatedPython"):
        return f"Remove the isolated runtime directory when no longer needed: {state['dataRoot']}"
    if state.get("imagemagick"):
        return "Use the same system package manager to uninstall ImageMagick."
    return "No isolated runtime is installed. Remove any later package with the installer that created it."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check", action="store_true", help="Inspect only (default).")
    action.add_argument("--install", action="store_true", help="Install a missing backend.")
    parser.add_argument("--backend", choices=("auto", "pillow", "imagemagick"), default="auto")
    parser.add_argument("--scope", choices=("user", "project", "system"), default="user")
    parser.add_argument("--allow-system", action="store_true", help="Confirm a system package-manager operation.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = inventory(args.scope)
    error = None
    if args.install and not backend_ready(state, args.backend):
        try:
            if args.backend == "imagemagick":
                state = install_imagemagick(args.scope, args.allow_system)
            else:
                state = install_pillow(args.scope, args.allow_system)
        except (RuntimeError, subprocess.CalledProcessError, OSError) as exc:
            error = str(exc)

    ready = backend_ready(state, args.backend)
    payload = {
        "ready": ready,
        "requestedBackend": args.backend,
        "scope": args.scope,
        "inventory": state,
        "verify": f"{sys.executable} {Path(__file__).resolve()} --check --backend {args.backend} --scope {args.scope}",
        "uninstall": uninstall_hint(state, args.scope),
        "error": error,
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Asset pipeline ready: {'yes' if ready else 'no'}")
        print(f"Python: {state['pythonVersion']} ({state['python']})")
        print(f"Pillow (current): {state['pillowCurrent'] or 'not installed'}")
        print(f"Pillow (isolated): {state['pillowIsolated'] or 'not installed'}")
        print(f"ImageMagick: {state['imagemagickVersion'] or 'not installed'}")
        print(f"Available backends: {', '.join(state['availableBackends']) or 'none'}")
        print(f"Runtime root: {state['dataRoot']}")
        print(f"Runtime root writable: {'yes' if state['dataRootWritable'] else 'no'}")
        if error:
            print(f"Error: {error}", file=sys.stderr)
        if not ready:
            print(
                f"Install with: {sys.executable} {Path(__file__).resolve()} --install "
                f"--backend {args.backend} --scope {args.scope}",
                file=sys.stderr,
            )
        print(f"Verify with: {payload['verify']}")
        print(f"Uninstall: {payload['uninstall']}")
    return 0 if ready else 2


if __name__ == "__main__":
    raise SystemExit(main())
