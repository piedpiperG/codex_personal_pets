# Codex Personal Pets

Workspace for personal Codex custom pets.

Canonical local working path:

```text
D:\codex_personal_pets
```

## Pets

### Muse

Muse is a chibi Codex companion generated from private reference photos and packaged as a local Codex custom pet.

Installable package:

```text
pets/muse/pet.json
pets/muse/spritesheet.webp
```

QA preview:

```text
qa/muse/contact-sheet.png
```

The original reference photos are intentionally not committed. Keep raw personal photos outside this repository, or place them under `raw_references/`, which is ignored by git.

## Install

From this repository:

```powershell
.\scripts\install_pet.ps1 -PetName muse
```

This copies the package to:

```text
%USERPROFILE%\.codex\pets\muse
```

Restart Codex or refresh the pet picker if the pet does not appear immediately.

## Validate

```powershell
python .\scripts\validate_pet.py .\pets\muse
```

Expected result:

```text
ok: muse WEBP RGBA 1536x1872
```
