"""
Modules — code someone else (or you) already wrote, ready to `import`.

Python ships with a huge "standard library": batteries included. You don't
re-invent square roots or random numbers — you import a module and use it.
Three ways to bring a module in are shown below.
"""

# 1) import the whole module, then reach inside with a dot
import math

print(math.sqrt(144))      # 12.0
print(math.pi)             # 3.141592653589793
print(math.floor(3.7))     # 3

# 2) import just the names you want — no dot needed afterwards
from random import randint, choice

print(randint(1, 6))                       # a dice roll: 1..6
print(choice(["heads", "tails"]))          # pick one at random

# 3) import with a shorter nickname (an alias)
import datetime as dt

today = dt.date.today()
print(today)                               # e.g. 2026-06-26
print(f"The year is {today.year}")

# A module is just a name you look things up in — exactly like a dictionary,
# but the dot `.` does the looking up instead of square brackets.
