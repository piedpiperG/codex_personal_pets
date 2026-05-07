# Muse

Muse is a local Codex custom pet created on 2026-05-07 from private reference photos.

## Package

The runtime package is:

```text
pets/muse/pet.json
pets/muse/spritesheet.webp
```

The manifest is:

```json
{
  "id": "muse",
  "displayName": "Muse",
  "description": "A chibi Codex companion inspired by the reference photos.",
  "spritesheetPath": "spritesheet.webp"
}
```

## Asset Contract

- Format: WebP
- Mode: RGBA
- Atlas size: 1536x1872
- Grid: 8 columns x 9 rows
- Cell size: 192x208
- Unused cells: transparent

Rows:

| Row | State | Frames |
| --- | --- | ---: |
| 0 | idle | 6 |
| 1 | running-right | 8 |
| 2 | running-left | 8 |
| 3 | waving | 4 |
| 4 | jumping | 5 |
| 5 | failed | 8 |
| 6 | waiting | 6 |
| 7 | running | 6 |
| 8 | review | 6 |

## Source Policy

Private reference photos were used locally but are not stored in this repository. The repository keeps:

- final Codex pet package
- contact sheet and validation JSON
- generated decoded row strips
- prompts used to produce the pet

## QA

Validation files:

```text
qa/muse/validation.json
qa/muse/review.json
qa/muse/contact-sheet.png
```

Both validation and frame review completed with no errors or warnings during packaging.
