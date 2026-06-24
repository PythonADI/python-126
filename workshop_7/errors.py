"""
Handling errors with try / except.

Some lines can CRASH the program: turning "abc" into a number, or asking a
dictionary for a key that is not there. Instead of letting the whole program
die, we can `try` the risky line and catch the problem in `except`.
"""

# --- ValueError: bad conversion -------------------------------------------
# int("hello") crashes with ValueError. We catch it and ask politely.
# text = input("Type a number: ")
# try:
#     number = int(text)
# except ValueError:
#     print(f"'{text}' is not a number — using 0 instead.")
#     number = 0

# print(f"You gave me {number}.")


# --- KeyError: missing dictionary key -------------------------------------
# scores = {"nino": 90, "giorgi": 75}
# name = "luka"

# try:
#     print(f"{name}'s score is {scores[name]}")
# except KeyError:
#     print(f"No score recorded for {name}.")

# --- try / except / else / finally ----------------------------------------
# else runs only if NO error happened. finally runs no matter what.
try:
    age = int(input("რამდენი წლის ხარ?\n"))
except ValueError:
    print("That was not a whole number.")
else:
    print(f"Next year you will be {age + 1}.")
finally:
    print("Thanks for playing!")
