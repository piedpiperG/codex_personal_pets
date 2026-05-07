#!/usr/bin/env python3
"""Validate a local Codex custom pet package."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image


EXPECTED_SIZE = (1536, 1872)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_pet.py <pet-dir>", file=sys.stderr)
        return 2

    pet_dir = Path(sys.argv[1]).expanduser().resolve()
    manifest_path = pet_dir / "pet.json"
    if not manifest_path.is_file():
        print(f"missing manifest: {manifest_path}", file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    spritesheet_name = manifest.get("spritesheetPath")
    if not isinstance(spritesheet_name, str) or not spritesheet_name:
        print("manifest missing spritesheetPath", file=sys.stderr)
        return 1

    spritesheet_path = pet_dir / spritesheet_name
    if not spritesheet_path.is_file():
        print(f"missing spritesheet: {spritesheet_path}", file=sys.stderr)
        return 1

    with Image.open(spritesheet_path) as image:
        if image.size != EXPECTED_SIZE:
            print(f"bad size: {image.size}, expected {EXPECTED_SIZE}", file=sys.stderr)
            return 1
        if image.format not in {"WEBP", "PNG"}:
            print(f"bad format: {image.format}", file=sys.stderr)
            return 1
        if image.mode != "RGBA":
            print(f"bad mode: {image.mode}, expected RGBA", file=sys.stderr)
            return 1

        print(
            f"ok: {manifest.get('id', pet_dir.name)} {image.format} {image.mode} "
            f"{image.width}x{image.height}"
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
