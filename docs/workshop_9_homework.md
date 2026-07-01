# Workshop 9 — Homework

Welcome to your ninth homework! Last week you built your first **classes**. This
week we make those objects do much more: **print nicely** (`__str__` /
`__repr__`), **compare** with `==` (`__eq__`), **share data** across every object
(class attributes), **reuse each other's code** (inheritance and `super()`), and
expose **computed values** as if they were plain attributes (`@property`). Several
tasks build on last week's classes — but now your objects are far more powerful.

**Deadline:** before Workshop 10.

**How to submit:** push everything to the **same** GitHub repository you used for
the previous homeworks, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with the earlier ones:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_9_homework
cd workshop_9_homework
# ...create your exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 9 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Python exercises

Create the files below and write Python code to solve each task. Use everything we
have covered so far: **variables, f-strings, `input()`, `int()` / `float()`,
`if` / `elif` / `else`, `and` / `or` / `not`, `while`, `for` + `range()`, `+=`,
`len()`, string methods, lists, dictionaries, tuples, files (`open`), `try` /
`except`, comprehensions, modules (`import`), and classes (`class`, `__init__`,
`self`, methods)** — plus this week's new material:

- **`__str__` / `__repr__`** — special ("dunder") methods that decide how your
  object prints. `__str__` is the friendly text for `print()`; `__repr__` is the
  exact, developer-facing text used in the REPL and inside lists. Both **return**
  a string.
- **`__eq__`** — decide when two objects count as equal: `def __eq__(self, other):`
  returns `True`/`False` by comparing their data. Now `==` and `in` work on your type.
- **Class attributes** — a value written straight in the class body (not on
  `self`) is **shared** by every object. Perfect for constants and for counting
  how many objects exist: `Thing.count += 1` inside `__init__`.
- **Inheritance** — `class Dog(Animal):` makes `Dog` a kind of `Animal`; it gets
  all of `Animal`'s methods and can **override** any of them.
- **`super().__init__(...)`** — inside a subclass's `__init__`, run the parent's
  setup first, then add the subclass's own attributes.
- **`@property`** — turn a method into a computed attribute you read **without
  parentheses**: `rect.area` instead of `rect.area()`.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — A class that prints nicely

Define a class `Book` with a `title` and an `author`. Add a `__str__(self)` method
that **returns** a sentence like `"Python 101 by nino"`. Build two books and
`print` each one.

Example run:

```
Python 101 by nino
Clean Code by giorgi
```

> Hint: `def __str__(self):` then `return f"{self.title} by {self.author}"`. Once
> `__str__` exists, `print(book)` uses it automatically.

### `exercise_2.py` — When are two things equal?

Define a class `Coordinate` with an `x` and a `y`. Add `__eq__(self, other)` so
that two coordinates are equal when **both** parts match. Print the result of
comparing an equal pair and an unequal pair.

Example run:

```
True
False
```

> Hint: `def __eq__(self, other): return self.x == other.x and self.y == other.y`.
> Build `a = Coordinate(3, 7)`, `b = Coordinate(3, 7)`, `c = Coordinate(9, 0)`,
> then `print(a == b)` and `print(a == c)`.

### `exercise_3.py` — Count how many you made

Give a class (say `Robot`) a **class attribute** `count = 0` written in the class
body. In `__init__`, do `Robot.count += 1`. Build three robots, then print how
many were made using `Robot.count`.

Example run:

```
Made 3 robots.
```

> Hint: `count = 0` goes directly under `class Robot:` — not on `self`. Each new
> robot bumps the shared counter with `Robot.count += 1`.

### `exercise_4.py` — A family of classes

Write a base class `Animal` with a method `speak(self)` that returns a generic
sound. Write **two** subclasses (for example `Dog` and `Cat`) that **override**
`speak`. Build one of each and print what each says.

Example run:

```
Rex says woof
Whiskers says meow
```

> Hint: `class Dog(Animal):` puts the parent in the parentheses. Give `Animal` an
> `__init__` that stores `self.name`, and let the subclasses reuse it — only
> `speak` needs to change.

### `exercise_5.py` — Build on the parent

Write a base class `Vehicle` with `__init__(self, brand)`. Write a subclass `Car`
whose `__init__` **also** takes `doors`, calls `super().__init__(brand)` to reuse
the parent's setup, and then stores `self.doors`. Print a car's brand and doors.

Example run:

```
Toyota with 4 doors
```

> Hint: `class Car(Vehicle):` then
> `def __init__(self, brand, doors): super().__init__(brand); self.doors = doors`.
> After that, `self.brand` exists (the parent set it) and so does `self.doors`.

### `exercise_6.py` — A computed value

Write a class `Rectangle` with a `width` and a `height`. Add an `@property` called
`area` that **returns** `width * height`. Build a rectangle and print its area —
with **no parentheses** (`rect.area`, not `rect.area()`).

Example run:

```
Area: 12
```

> Hint: put `@property` on the line directly above `def area(self):`. Then read it
> like an attribute: `print(f"Area: {rect.area}")`.

### `exercise_7.py` — Put it together

Write a base class `Shape` and two subclasses `Square` and `Circle`. Each subclass
stores what it needs (a side, or a radius) and has its own `@property area` and a
`__str__`. Put a few shapes in a **list** and print each one.

Example run:

```
Square with area 16
Circle with area 28.27
```

> Hint: give `Shape` a `__str__` that uses `self.area`, and let each subclass fill
> in its own `area`. A circle's area is `math.pi * r * r` (`import math`). Format
> to two decimals with `f"{self.area:.2f}"`.

### `exercise_8.py` — A library that remembers (bonus)

Combine **classes**, **json**, and **error handling**. Write a class `Library`
whose `__init__` tries to `json.load` a list of books from `library.json` (each
book is a small dict like `{"title": ..., "author": ...}`); catch
`FileNotFoundError` and start with an empty list if the file is missing. Add a
method `add(self, title, author)` that appends a book dict and saves the whole
list back with `json.dump`, and a method `show(self)` that prints every book as
`"title by author"`. Run the program two or three times, adding a book each time,
and watch the shelf grow.

Example first run:

```
0 book(s) on the shelf.
Add a title: The Hobbit
Add an author: tolkien
Saved!
```

Example second run:

```
1 book(s) on the shelf.
- The Hobbit by tolkien
Add a title: Dune
Add an author: herbert
Saved!
```

> Hint: in `__init__`, wrap the read in
> `try: ... except FileNotFoundError: self.books = []`. In `add`, do
> `self.books.append({"title": title, "author": author})`, then re-open
> `library.json` in `"w"` mode and `json.dump(self.books, f)`.

---

## Checklist before you submit

- [ ] `exercise_1.py` … `exercise_8.py` written and run without errors using `python exercise_N.py`
- [ ] Everything is pushed inside the `workshop_9_homework/` folder of your repository
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Classes (tutorial): https://docs.python.org/3/tutorial/classes.html
- Inheritance: https://docs.python.org/3/tutorial/classes.html#inheritance
- `super()`: https://docs.python.org/3/library/functions.html#super
- Special (dunder) methods, incl. `__str__` / `__repr__` / `__eq__`: https://docs.python.org/3/reference/datamodel.html#special-method-names
- `__str__` vs `__repr__`: https://docs.python.org/3/reference/datamodel.html#object.__repr__
- `@property`: https://docs.python.org/3/library/functions.html#property
- `json` module: https://docs.python.org/3/library/json.html
