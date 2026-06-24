"""
A tiny notes app that ties it all together:
  - reads existing notes from a file (handling the case where it does not exist),
  - lets you add a new note,
  - writes everything back.

Run it a few times — your notes survive between runs because they live in a file.
"""

FILENAME = "notes.txt"


def load_notes():
    # The file may not exist yet on the very first run — catch that and
    # start with an empty list instead of crashing.
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open(FILENAME, "w") as f:
        for note in notes:
            f.write(note + "\n")


notes = load_notes()

print(f"You have {len(notes)} note(s):")
for i, note in enumerate(notes, start=1):
    print(f"{i}. {note}")

new_note = input("Add a note (leave empty to skip): ").strip()
if new_note:
    notes.append(new_note)
    save_notes(notes)
    print("Saved!")
else:
    print("Nothing added.")
