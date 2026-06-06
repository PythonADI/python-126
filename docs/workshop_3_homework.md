# Workshop 3 — Homework

Welcome to your third homework! This time it is **all Python exercises** — no research
questions.

**Deadline:** before Workshop 4.

**How to submit:** push everything to the **same** GitHub repository you used for the
previous homeworks, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with the earlier ones:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_3_homework
cd workshop_3_homework
# ...create your exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 3 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Python exercises

Create the files below and write Python code to solve each task. Use only what we have
covered so far: **variables, type casting, operators, `input()`, string methods,
f-strings**, and the new Workshop 3 tools — **`if` / `elif` / `else`, the boolean
operators `and` / `or` / `not`, `while` and `for` loops, `range()`, looping over the
characters of a string, `len()`, and the shortcuts `+=` / `-=`.**

> We have **not** learned functions or lists yet — you do not need them. Keep your
> solutions to the tools above.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — Even or odd

Ask the user for a whole `number` and cast it to an `int`. Using `if` / `else` and the
modulus operator (`%`), print a full sentence saying whether it is even or odd.

Example run:

```
Give me a number:
7
7 is odd.
```

### `exercise_2.py` — Letter grade

Ask the user for a `score` (an `int` from 0 to 100). Using an `if` / `elif` / `else`
chain, print the letter grade:

- `90` and above → `A`
- `80–89` → `B`
- `70–79` → `C`
- anything below `70` → `F`

Example run:

```
Your score:
84
Your grade is B
```

### `exercise_3.py` — Countdown

Ask the user for a starting number `n` and cast it to an `int`. Using a `while` loop and
`-=`, count down and print every number from `n` down to `1`. When the loop is finished,
print `Liftoff!`.

Example run:

```
Count down from:
3
3
2
1
Liftoff!
```

### `exercise_4.py` — Add them all up

Ask the user for a number `n`. Using a `for` loop, `range()`, and a `total` variable that
you grow with `+=`, add up every number from `1` to `n` and print the result.

Example run:

```
Add up to:
5
The sum of 1 to 5 is 15
```

> Hint: `range(1, n + 1)` gives you the numbers `1, 2, ... , n`. Start with `total = 0`
> *before* the loop.

### `exercise_5.py` — Count the vowels

Ask the user for a `word`. Clean it with `.strip().lower()`. Then loop over the word one
character at a time and count how many letters are vowels (`a`, `e`, `i`, `o`, `u`). Use a
counter and `+=`, and decide "is this a vowel?" with the `or` operator. At the end, print
the count, and also print how many letters the whole word has using `len()`.

Example run:

```
Type a word:
Programming
"programming" has 3 vowels out of 11 letters.
```

> Hint: inside the loop you are checking one character, e.g.
> `if char == "a" or char == "e" or ...:`

### `exercise_6.py` — Club entry

A club has these rules. Ask for the visitor's `age` (cast to `int`) and `name` (cleaned
with `.strip().lower()`), then use `if` / `elif` / `else` together with `and`, `or`, and
`not` to print the right message:

- If they are **younger than 18** → `Sorry, you cannot enter.`
- Otherwise, if they are **at least 21 _and_ their name is `nino`** → `Welcome, VIP!`
- Otherwise, if their age is **even _or_ their name is `giorgi`** → `You get a free drink!`
- Otherwise → `Welcome in. Enjoy your evening.`

Example run:

```
How old are you?
24
What is your name?
  Giorgi
You get a free drink!
```

### `exercise_7.py` — Fix the loop (bonus)

The program below is meant to count down from `5` to `1`, but it **never stops** — it
prints `5` forever. Explain in a comment **why** it loops forever, then fix it.

```python
n = 5
while n > 0:
    print(n)
    n += 1
```

> Hint: look closely at the line that changes `n`. Is the number getting closer to `0`,
> or further away? If you run this by accident, stop it with **Ctrl + C**.

---

## Checklist before you submit

- [ ] `exercise_1.py` … `exercise_7.py` written and runnable
- [ ] Everything pushed to your GitHub repository (inside a `workshop_3_homework/` folder)
- [ ] Repository link sent to the instructor

---

## Helpful links

- `if` / `elif` / `else`: https://docs.python.org/3/tutorial/controlflow.html#if-statements
- `for` loops and `range()`: https://docs.python.org/3/tutorial/controlflow.html#for-statements
- `while` loops: https://docs.python.org/3/reference/compound_stmts.html#while
- Boolean operators (`and` / `or` / `not`): https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
- `len()` reference: https://docs.python.org/3/library/functions.html#len
