"""
A tiny notes app that ties it all together:
  - reads existing notes from a file (handling the case where it does not exist),
  - lets you add a new note,
  - writes everything back.

Run it a few times — your notes survive between runs because they live in a file.
"""

FILENAME = "notes.txt"

# Define 
def load_notes():
    # The file may not exist yet on the very first run — catch that and
    # start with an empty list instead of crashing.
    
    # Error handling block in case file doesn't exist
    try:
        # open file in read mode as "f"
        with open(FILENAME, "r") as f:
            
            return [line.strip() for line in f if line.strip()]
        # except file not be found
    except FileNotFoundError:
        # return empty list
        return []


# define save notes
def save_notes(notes):
    # open FILENAME, but in write mode as "f"
    with open(FILENAME, "w") as f:
        # add note in notes file
        for note in notes:
            f.write(note + "\n")


notes = load_notes()
# Print the lengh of notes
print(f"You have {len(notes)} note(s):")
# Print each note enumerated. For example: 1. note1
for i, note in enumerate(notes, start=1):
    print(f"{i}. {note}")

# asks user to add a new note
new_note = input("Add a note (leave empty to skip): ").strip()

# if note is new in notes, add new_note and save it, print (Saved)
if new_note:
    notes.append(new_note)
    save_notes(notes)
    print("Saved!")
# If note already exists in notes, print ( Nothing added)
else:
    print("Nothing added.")