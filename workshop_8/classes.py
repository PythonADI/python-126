"""
Classes — your own data type.

A dictionary groups data. A class groups data AND the functions that work on
that data, and lets you stamp out many copies (objects) from one blueprint.

  class  = the blueprint (a Dog in general)
  object = one thing built from it (this specific dog, Rex)
"""


class Dog:
    # __init__ runs automatically when you make a new Dog. `self` is the
    # particular dog being built; we hang its data onto self.
    def __init__(self, name, age):
        self.name = name      # an attribute — data stored on the object
        self.age = age

    # a method — a function that belongs to the class. self is the dog
    # it was called on.
    def bark(self):
        return f"{self.name} says woof!"

    def human_years(self):
        return self.age * 7


# build two objects from the one blueprint — each keeps its own data
rex = Dog("Rex", 3) # instantiation
bella = Dog("Bella", 5)

print(rex.name)            # Rex        — reach an attribute with a dot
print(bella.age)           # 5
print(rex.bark())          # Rex says woof!   — call a method with ()
print(bella.bark())        # Bella says woof!
print(rex.human_years())   # 21

# Each object is independent: changing one doesn't touch the other.
rex.age = 4
print(rex.age)             # 4
print(bella.age)           # 5
