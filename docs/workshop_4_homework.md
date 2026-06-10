# Workshop 4 — Homework

Welcome to your fourth homework! This time it is **all Python exercises** — and most of
them are last week's tasks, reborn as functions. You don't solve them again; you package
them.

**Deadline:** before Workshop 5.

**How to submit:** push everything to the **same** GitHub repository you used for the
previous homeworks, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with the earlier ones:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_4_homework
cd workshop_4_homework
# ...create your exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 4 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Python exercises

Create the files below and write Python code to solve each task. Use only what we have
covered so far: **variables, f-strings, `input()`, `int()` / `float()`, `round()`,
`len()`, `if` / `elif` / `else`, `and` / `or` / `not`, `while`, `for` + `range()`, `+=`,
`.strip()` / `.lower()` / `.title()`** — plus this week's new material: **`def`,
parameters, `return`, and default values**.

> We have **not** learned lists or dictionaries yet — you do not need them. Keep your
> solutions to the tools above.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — The greeting machine

Define a function `greet(name)` that prints a two-line greeting — the first line in
Georgian (see the example run below). Give the parameter a **default value** of
`"friend"`. Then call the function for `nino`, `giorgi`, and `mariami`, and once more
with **no argument at all**. The greeting text must exist in exactly one place in your
file.

Example run:

```
გამარჯობა, nino!
Welcome to the course.
გამარჯობა, giorgi!
Welcome to the course.
გამარჯობა, mariami!
Welcome to the course.
გამარჯობა, friend!
Welcome to the course.
```

> Hint: `def greet(name="friend"):` — defining it does nothing until you call
> `greet("nino")`. If you can fix a typo in the greeting by editing **one** line, you
> did it right.

### `exercise_2.py` — `is_even`, returned

Homework 3's "even or odd", packaged. Define a function `is_even(n)` that **returns**
`True` or `False` using the modulus operator (`%`) — no printing inside the function!
Then ask the user for a number with `input()` + `int()`, and use your function in an
`if` to print the verdict.

Example run:

```
Enter a number: 7
7 is odd
```

> Hint: a comparison already *is* a `True`/`False` value — the whole body can be one
> line: `return n % 2 == 0`. Then write `if is_even(number):`.

### `exercise_3.py` — The grade machine

Homework 3's letter grade, packaged. Define `letter_grade(score)` that returns `"A"`
(90 and above), `"B"` (80 and above), `"C"` (70 and above), or `"F"` (anything below).
Ask the user for a score and print the score together with the grade in one f-string.

Example run:

```
Enter your score: 83
Score 83 -> grade B
```

> Hint: `return` ends the function instantly — so plain `if`s work, no `elif` or `else`
> required. Your Workshop 3 chain is already correct: swap every `print` for a `return`.

### `exercise_4.py` — Temperature converter

Homework 2's Celsius → Fahrenheit converter, packaged. Define `to_fahrenheit(celsius)`
that **returns** the converted value rounded to 1 decimal place with `round()`. Read the
temperature with `float(input(...))` and print the result.

Example run:

```
Temperature in Celsius: 36.6
36.6C is 97.9F
```

> Hint: the Workshop 2 formula was `celsius * 9 / 5 + 32`; wrap it:
> `return round(celsius * 9 / 5 + 32, 1)` — return the rounded value, don't print
> inside the function.

### `exercise_5.py` — `count_vowels`

Homework 3's vowel counter, packaged. Define `count_vowels(word)` that loops with
`for char in word.lower():`, counts the vowels with `+=`, and **returns** the count.
Ask the user for a word and report the result.

Example run:

```
Enter a word: Programming
"Programming" has 3 vowels.
```

> Hint: same chained check as last week —
> `if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":` — but
> this time `return count` as the **last** line, *outside* the loop's indentation, or
> you'll return after the first letter.

### `exercise_6.py` — The bouncer's brain

The club from Homework 3 is back, but this time the decision lives in a function. Define
`door_decision(name, age)` that **returns** the right message — it must contain **no
print** at all:

- If they are **younger than 18** → `Sorry, no entry.`
- Otherwise, if they are **at least 21 _and_ their name is `nino`** → `Welcome, VIP!`
- Otherwise, if their age is **even _or_ their name is `giorgi`** → `Welcome! Free drink for you!`
- Otherwise → `Welcome!`

Ask for the visitor's name and age, clean the name with `.strip().lower()` **before**
calling the function, and print whatever comes back.

Example run:

```
What is your name?  Giorgi
How old are you? 21
Welcome! Free drink for you!
```

> Hint: check the rules top to bottom, each branch a single `return` — the first one
> reached wins. Decision in the function, conversation outside. If your function prints,
> it's a display, not a brain.

### `exercise_7.py` — Fix the silent machine (bonus)

The program below **crashes**. Run it, read the error message, explain in a comment
**why** it crashes, then fix the function by changing **one word** so the program prints
`total = 115`.

```python
def add(a, b):
    print(a + b)

total = add(10, 5) + 100
print(f"{total = }")
```

The broken version prints `15`, then crashes with
`TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`.

Example run after the fix:

```
total = 115
```

> Hint: `add` *shows* the sum but hands nothing back — a function without `return`
> returns `None`, and `None + 100` is the crash. The `15` you saw was the display
> lighting up, not a value coming back.

---

## Checklist before you submit

- [ ] All 7 files are written and run without errors using `python exercise_N.py`
- [ ] Everything is pushed inside the `workshop_4_homework/` folder of your repository
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Defining functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Default argument values: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
- The `return` statement: https://docs.python.org/3/reference/simple_stmts.html#the-return-statement
