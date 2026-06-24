# Workshop 7 — Homework

Welcome to your seventh homework! This week pulls together **four** new tools:
**tuples** (a list that cannot change), **files** (saving your data so it survives after
the program ends), **error handling** (`try` / `except`, so a bad input does not crash
everything), and **comprehensions** (a one-line way to build a list or dict). Several tasks
revisit old homeworks — but now your data can be saved to disk and your programs refuse to
crash.

**Deadline:** before Workshop 8.

**How to submit:** push everything to the **same** GitHub repository you used for the
previous homeworks, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with the earlier ones:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_7_homework
cd workshop_7_homework
# ...create your exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 7 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Python exercises

Create the files below and write Python code to solve each task. Use only what we have
covered so far: **variables, f-strings, `input()`, `int()` / `float()`, `if` / `elif` /
`else`, `and` / `or` / `not`, `while`, `for` + `range()`, `+=`, `len()`, string methods,
lists, dictionaries, `def` / `return`** — plus this week's new material:

- **Tuples** — `(a, b, c)`, indexing `t[0]`, they **cannot** be changed, unpacking
  `x, y = point`, and returning several values from a function with `return a, b`.
- **Files** — `with open(path, "w") as f:` to write, `with open(path, "r") as f:` to read,
  `f.write(text)`, `f.read()`, `f.readlines()`, looping `for line in f:`, and `.strip()`
  to clean off the trailing newline. Modes: `"r"` read, `"w"` overwrite, `"a"` append.
- **Error handling** — `try:` / `except SomeError:` / `else:` / `finally:`, catching
  `ValueError` (bad `int()`), `KeyError` (missing dict key), and `FileNotFoundError`.
- **Comprehensions** — `[expr for item in seq]`, with a filter `[item for item in seq if …]`,
  and dict comprehensions `{key: value for item in seq}`.

> We have **not** learned sets yet — you do not need them. Keep your solutions to the tools
> above.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — A point that won't change

Make a tuple `point = (3, 7)`. Print the whole tuple, then print its two parts by
**unpacking** them into `x` and `y`. Then add a comment showing the line that **would**
crash and naming the error.

Example run:

```
(3, 7)
x = 3, y = 7
```

> Hint: unpack with `x, y = point`. The crashing line is `point[0] = 99` — uncomment it
> once to see the `TypeError`, then comment it back and note the error name in a comment.

### `exercise_2.py` — Two values at once

Write a function `high_and_low(numbers)` that **returns** both the largest and the smallest
value of a list, as in `return biggest, smallest`. Call it on a list of numbers and unpack
the result into two variables, then print them.

Example run:

```
highest: 99
lowest:  8
```

> Hint: inside the function, start `biggest = numbers[0]` and `smallest = numbers[0]`, loop
> with `for n in numbers:` and update them with `if`. `return biggest, smallest` hands back
> a **tuple**; unpack it with `high, low = high_and_low(scores)`.

### `exercise_3.py` — Save a list to a file

Start with a list of items (for example a shopping list). Open a file in **write** mode and
write **one item per line**. Then print a confirmation message.

Example run:

```
Wrote 3 items to shopping.txt
```

> Hint: `with open("shopping.txt", "w") as f:` then `for item in items: f.write(item +
> "\n")`. The `"\n"` is what puts each item on its own line. Open `shopping.txt` in your
> editor afterwards to check.

### `exercise_4.py` — Read it back

Open the file you made in `exercise_3.py` in **read** mode and print each line, cleaned up
with `.strip()`. Then print how many lines there were.

Example run:

```
- milk
- bread
- eggs
3 items total.
```

> Hint: loop with `for line in f:` and print `line.strip()`. To count, read them into a
> list with `lines = f.readlines()` and use `len(lines)` — or keep your own counter with
> `+= 1`.

### `exercise_5.py` — Don't crash on bad input

Ask the user for a number. Wrap the `int(...)` in a `try` / `except ValueError` so that
typing something that is **not** a number prints a friendly message instead of crashing.
If it worked, print the number doubled.

Example run:

```
Type a number: 8
Double is 16.
```

Another run:

```
Type a number: banana
'banana' is not a number.
```

> Hint: put `number = int(text)` inside `try:`. In `except ValueError:` print the friendly
> message. You can use `else:` for the "it worked" branch that doubles and prints.

### `exercise_6.py` — Look up without crashing

Make a dictionary of names to scores. Ask the user for a name and print that person's
score. Use `try` / `except KeyError` so that a name that is **not** in the dictionary
prints a fallback message instead of crashing.

Example run:

```
Whose score? nino
nino's score is 90.
```

Another run:

```
Whose score? luka
No score recorded for luka.
```

> Hint: `print(scores[name])` raises `KeyError` for a missing name — catch it. (You already
> know `scores.get(name)` does this too; this time practise it the `try` / `except` way.)

### `exercise_7.py` — Comprehensions

Start with `numbers = [1, 2, 3, 4, 5, 6]`. Using **comprehensions** (not plain loops),
build and print: (a) a list of every number doubled, (b) a list of only the **even**
numbers, and (c) a dictionary mapping each number to its square.

Example run:

```
[2, 4, 6, 8, 10, 12]
[2, 4, 6]
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
```

> Hint: `[n * 2 for n in numbers]`, then `[n for n in numbers if n % 2 == 0]`, then
> `{n: n * n for n in numbers}`.

### `exercise_8.py` — A note that survives (bonus)

Write a program that **remembers** notes between runs. On start, try to read `notes.txt`
and print the notes already in it; if the file does not exist yet, catch the
`FileNotFoundError` and start empty. Then ask the user for one new note, **append** it to
the file, and finish. Run it two or three times to watch the list grow.

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

> Hint: wrap the reading in `try: ... except FileNotFoundError: notes = []`. To add without
> erasing, open in append mode: `with open("notes.txt", "a") as f: f.write(note + "\n")`.

---

## Checklist before you submit

- [ ] `exercise_1.py` … `exercise_8.py` written and run without errors using `python exercise_N.py`
- [ ] Everything is pushed inside the `workshop_7_homework/` folder of your repository
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Tuples (tutorial): https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
- Reading and writing files: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- Errors and exceptions: https://docs.python.org/3/tutorial/errors.html
- `try` statement (reference): https://docs.python.org/3/reference/compound_stmts.html#try
- List comprehensions: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
