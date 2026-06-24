"""
Reading a text file.

open(path, "r") opens a file for READING ("r" is the default). Run
files_write.py first so that shopping.txt exists.
"""


# read the WHOLE file as one big string
# with open("shopping.txt", "r") as f:
#     contents = f.read()
# print(contents)

# print("=" * 20)
# usually nicer: loop line by line. Each line keeps its trailing "\n",
# so .strip() cleans it off.
# with open("shopping.txt", "r") as f:
#     for line in f:
#         print(f"- {line.strip()}")

# print("=" * 20)

# .readlines() gives you a list of lines — one string per line
with open("shopping.txt", "r") as f:
    lines = f.readlines()
print(lines)
print(f"There are {len(lines)} items on the list.")

