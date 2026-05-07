# Workflow

Use this repository as the working root for future Codex personal pet work:

```text
D:\codex_personal_pets
```

## Add A New Pet

1. Create the pet with the Codex hatch-pet workflow.
2. Do not commit private reference photos.
3. Copy the final package into:

```text
pets/<pet-id>/pet.json
pets/<pet-id>/spritesheet.webp
```

4. Copy QA artifacts into:

```text
qa/<pet-id>/contact-sheet.png
qa/<pet-id>/review.json
qa/<pet-id>/validation.json
```

5. Copy useful source artifacts into:

```text
source/<pet-id>/decoded/
source/<pet-id>/prompts/
```

6. Validate:

```powershell
python .\scripts\validate_pet.py .\pets\<pet-id>
```

7. Install locally:

```powershell
.\scripts\install_pet.ps1 -PetName <pet-id>
```

8. Commit and push:

```powershell
git status -sb
git add .
git commit -m "Add <pet-id> Codex pet"
git push
```

## Privacy

Keep raw personal images outside git. If a future workflow needs a local holding folder, use `raw_references/`; it is ignored.
