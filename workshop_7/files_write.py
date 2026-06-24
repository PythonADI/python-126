"""
Writing to a text file.

open(path, "w") opens a file for WRITING. "w" starts the file fresh — any old
contents are wiped. The `with` block closes the file for you automatically when
it ends, even if something goes wrong.
"""

shopping = ["milk", "bread", "eggs"]

# "w" = write (overwrite). Each \n starts a new line in the file.
with open("shopping.txt", "w") as f:
    for item in shopping:
        f.write(item + "\n")

print("Wrote shopping.txt")

# "a" = append — add to the end without erasing what is already there.
with open("shopping.txt", "a") as f:
    f.write("butter\n")

print("Added one more line.")
