"""
json — saving a whole dictionary to a file, and loading it back.

Last week you wrote text to files line by line. But how do you save a whole
dictionary? `json` (from the standard library) turns a dict into text and
back again, so your data survives between runs. It pairs perfectly with the
files and dictionaries you already know.
"""

import json

profile = {
    "name": "nino",
    "age": 21,
    "hobbies": ["chess", "piano"],
}

# WRITE: dump the dict into a file as JSON text
with open("profile.json", "w") as f:
    json.dump(profile, f, indent=2)

print("Saved profile.json")

# READ: load it back into a real Python dictionary
with open("profile.json", "r") as f:
    loaded = json.load(f)

print(loaded)                    # {'name': 'nino', 'age': 21, ...}
print(loaded["name"])            # nino — it's a normal dict again
print(loaded["hobbies"][0])      # chess

# json.dumps (with an "s") makes a STRING instead of writing a file —
# handy for a quick look. indent=2 pretty-prints it.
print(json.dumps(profile, indent=2))
