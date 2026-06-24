"""
Tuples — a fixed, ordered collection. Like a list, but it cannot be changed
once created. Good for things that belong together and should stay put,
e.g. a point (x, y) or a person's (name, age).
"""

# create a tuple with parentheses
point = (3, 7)
print(point)
print(f"{point = }")

# indexing works exactly like a list
print(point[0])
print(point[1])
print(len(point))

# tuples are IMMUTABLE — this line would crash:
# point[0] = 99   # TypeError: 'tuple' object does not support item assignment

# unpacking: pull the items into separate variables in one line
x, y = point
print(f"x = {x}, y = {y}")

# tuples are handy for data that travels together
person = ("nino", 21)
name, age = person
print(f"{name} is {age} years old.")
