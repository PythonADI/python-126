"""
List & dict comprehensions — a short way to build a new collection from an
old one. Anything a comprehension does, a normal for-loop can do too; the
comprehension is just a tidier one-liner.
"""
x = 2
numbers = [1, 2, 3, 4, 5]

# the long way: build a new list with a loop
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)

# the short way: a list comprehension. Read it as
# "n * 2 for each n in numbers".
doubled = [
    n * x
    for n in numbers
]
print(doubled)

# add a condition with `if` — keep only the items you want
evens = [
    n 
    for n in numbers 
    if n % 2 == 0
]
print(evens)



squares = {
    x: x * x
    for x in [1, 2, 3]
}
print(squares)                 # {1: 1, 2: 4, 3: 9}

# works on strings too
words = ["milk", "bread", "eggs"]
shouted = [w.upper() for w in words]
print(shouted)

# a dict comprehension builds a dictionary: {key: value for ...}
squares = {n: n * n for n in numbers}
print(squares)
print(f"5 squared is {squares[5]}")
