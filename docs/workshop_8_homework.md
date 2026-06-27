# Workshop 8 — Homework

Welcome to your eighth homework! This week has **two** big new ideas:
**modules** (borrowing code from Python's standard library, and writing your own
files to import) and **classes** (building your own data type that bundles data
together with the functions that work on it). Several tasks build on old
homeworks — but now you can reach for ready-made tools and design your own
blueprints.

**Deadline:** before Workshop 9.

**How to submit:** push everything to the **same** GitHub repository you used for
the previous homeworks, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with the earlier ones:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_8_homework
cd workshop_8_homework
# ...create your exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 8 homework"
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
`except`, comprehensions, `def` / `return`** — plus this week's new material:

- **Modules** — `import math`, then `math.sqrt(x)`; `from random import randint`
  (no dot needed afterwards); `import datetime as dt` (a shorter nickname).
  Useful modules: `math` (`sqrt`, `pi`, `floor`, `ceil`), `random` (`randint`,
  `choice`, `shuffle`), `datetime` (`date.today()`), and `json`
  (`json.dump` / `json.load` to save and load a whole dictionary).
- **Your own module** — any `.py` file is a module. Put functions in one file and
  `import` it from another (both in the same folder). The
  `if __name__ == "__main__":` guard keeps a file's demo from running when it is
  imported.
- **Classes** — `class Dog:` is a blueprint; `rex = Dog("Rex", 3)` builds an
  **object** from it. `__init__(self, ...)` runs when the object is made and
  stores **attributes** with `self.name = name`. A **method** is a function
  inside the class whose first parameter is `self`. Reach attributes and call
  methods with a dot: `rex.name`, `rex.bark()`.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — Borrow from `math`

`import math` and use it to print: the square root of `144`, the value of `pi`,
and `7.3` rounded **down** with `math.floor`. Label each line.

Example run:

```
sqrt(144) = 12.0
pi = 3.141592653589793
floor(7.3) = 7
```

> Hint: `import math` at the top, then `math.sqrt(144)`, `math.pi`,
> `math.floor(7.3)`.

### `exercise_2.py` — Roll the dice

`from random import randint, choice`. Print a random dice roll between `1` and
`6`, and a random pick from a list of three foods. Run it a few times to see the
answers change.

Example run:

```
You rolled a 4
Tonight: pizza
```

> Hint: `randint(1, 6)` gives a whole number from 1 to 6 (both ends included);
> `choice(["pizza", "khinkali", "salad"])` picks one item at random.

### `exercise_3.py` — Your own module

Make **two** files. In `shapes.py`, write functions `square_area(side)` and
`triangle_area(base, height)` that **return** their results. In `exercise_3.py`,
`import shapes` and print the area of a square and a triangle.

Example run:

```
Square area: 25
Triangle area: 6.0
```

> Hint: keep both files in the same folder. In `exercise_3.py` write
> `import shapes`, then `shapes.square_area(5)`. Triangle area is
> `base * height / 2`.

### `exercise_4.py` — Save a profile with `json`

Build a dictionary describing yourself (at least `name`, `age`, and a list of
`hobbies`). Use `json.dump` to save it to `me.json`, then `json.load` to read it
back and print one value from the loaded dictionary.

Example run:

```
Saved me.json
Loaded back: nino, age 21
```

> Hint: `import json`. To save:
> `with open("me.json", "w") as f: json.dump(profile, f)`. To load:
> `with open("me.json") as f: data = json.load(f)` — `data` is a normal dict
> again, so `data["name"]` works.

### `exercise_5.py` — Your first class

Define a class `Student` with an `__init__` that stores a `name` and a `grade`.
Add a method `describe(self)` that **returns** a sentence like
`"nino is in grade 10"`. Build two students and print each one's description.

Example run:

```
nino is in grade 10
giorgi is in grade 11
```

> Hint: `def __init__(self, name, grade):` then `self.name = name` and
> `self.grade = grade`. In `describe` return an f-string using `self.name` and
> `self.grade`. Build one with `s = Student("nino", 10)` and call `s.describe()`.

### `exercise_6.py` — A class with behaviour

Define a class `Counter` that starts at `0`. Give it a method `increment(self)`
that adds one, and a method `value(self)` that returns the current count. Make a
counter, increment it three times, and print the value.

Example run:

```
3
```

> Hint: in `__init__` set `self.count = 0`. `increment` does `self.count += 1`.
> `value` does `return self.count`. Call `c.increment()` three times.

### `exercise_7.py` — A class that protects its data

Define a class `Wallet` that starts with a `balance` (default `0`). Add
`add(self, amount)` and `spend(self, amount)`. `spend` must **refuse** and print
a message if the amount is more than the balance, otherwise subtract it. Show
both a successful spend and a refused one.

Example run:

```
Balance: 50
Spent 20. Balance: 30
Cannot spend 100 — only 30 left.
```

> Hint: `def __init__(self, balance=0):`. In `spend`, use
> `if amount > self.balance:` to refuse, `else:` to do `self.balance -= amount`.

### `exercise_8.py` — Notes that remember (bonus)

Combine **classes**, **files**, **json**, and **error handling**. Write a class
`NoteBook` whose `__init__` tries to `json.load` a list of notes from
`notes.json` (catch `FileNotFoundError` and start with an empty list if the file
is missing). Add a method `add(self, note)` that appends a note and saves the
whole list back with `json.dump`. Run the program two or three times, adding a
note each time, and watch the list grow.

Example first run:

```
You have 0 note(s).
Add a note: buy milk
Saved!
```

Example second run:

```
You have 1 note(s).
1. buy milk
Add a note: call nino
Saved!
```

> Hint: in `__init__`, wrap the read in
> `try: ... except FileNotFoundError: self.notes = []`. In `add`, do
> `self.notes.append(note)` then re-open `notes.json` in `"w"` mode and
> `json.dump(self.notes, f)`.

---

## Checklist before you submit

- [ ] `exercise_1.py` … `exercise_8.py` (plus `shapes.py`) written and run without errors using `python exercise_N.py`
- [ ] Everything is pushed inside the `workshop_8_homework/` folder of your repository
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Modules (tutorial): https://docs.python.org/3/tutorial/modules.html
- The standard library tour: https://docs.python.org/3/tutorial/stdlib.html
- `math` module: https://docs.python.org/3/library/math.html
- `random` module: https://docs.python.org/3/library/random.html
- `json` module: https://docs.python.org/3/library/json.html
- Classes (tutorial): https://docs.python.org/3/tutorial/classes.html
