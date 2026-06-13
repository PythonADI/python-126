# a string can become a list of words...
sentence = "now this has words"
words = sentence.split()
print(words)                  # ['now', 'this', 'has', 'words']
print(f"{len(words)} words")  # remember counting spaces by hand? not anymore

# ...and a list of words can become a string again
print(" ".join(words))
print("-".join(words))

# split on something other than a space
date = "2026-06-13"
print(date.split("-"))        # ['2026', '06', '13']
