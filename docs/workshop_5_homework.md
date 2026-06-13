# Workshop 5 — Homework

Welcome to your fifth homework! This week is **all about lists** — your first way to keep
many values in a single variable. Most of these tasks are old friends from earlier
homeworks, but this time the data lives in a list.

**Deadline:** before Workshop 6.

**How to submit:** push everything to the **same** GitHub repository you used for the
previous homeworks, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with the earlier ones:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_5_homework
cd workshop_5_homework
# ...create your exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 5 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Python exercises

Create the files below and write Python code to solve each task. Use only what we have
covered so far: **variables, f-strings, `input()`, `int()` / `float()`, `if` / `elif` /
`else`, `and` / `or` / `not`, `while`, `for` + `range()`, `+=`, `len()`, string methods,
`def` / `return`** — plus this week's new material: **lists** — creating them with
`[ ... ]`, indexing (`x[0]`, `x[-1]`), slicing (`x[1:3]`), looping with `for item in x`,
membership with `in`, `.append()`, `.insert()`, `.pop()`, `.remove()`, `.count()`, and
turning strings into lists with `.split()`.

> We have **not** learned dictionaries or list comprehensions yet — you do not need them.
> Keep your solutions to the tools above.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — Your list

Create a list called `shopping` with **at least four** items (strings of your choice).
Then print, on separate lines: the whole list, how many items it has using `len()`, the
**first** item, and the **last** item (use `-1`, don't hard-code the number).

Example run:

```
['milk', 'bread', 'eggs', 'cheese']
You have 4 items.
First: milk
Last: cheese
```

> Hint: the last item is always `shopping[-1]`, no matter how long the list is.

### `exercise_2.py` — Numbered list

Make a list of names. Using a `for` loop, print each name on its own line with a number
in front, starting at `1`.

Example run:

```
1. nino
2. giorgi
3. mariami
```

> Hint: loop over the positions with `for i in range(len(names)):` and print
> `f"{i + 1}. {names[i]}"`. Remember positions start at `0`, so add `1` for the label.

### `exercise_3.py` — Sum and average

Start with a list of numbers, for example `grades = [70, 85, 90, 60]`. Using a `for` loop
and a `total` variable you grow with `+=`, add them all up. Then print the **total** and
the **average** (the total divided by `len(grades)`).

Example run:

```
Total: 305
Average: 76.25
```

> Hint: start with `total = 0` *before* the loop. The average is `total / len(grades)`.

### `exercise_4.py` — Collect into a list

Ask the user **how many** items they want to add (`int(input(...))`). Start with an empty
list, then loop that many times, each time asking for one item with `input()` and adding
it with `.append()`. At the end, print the finished list and how many items it has.

Example run:

```
How many items? 3
Item: milk
Item: bread
Item: eggs
['milk', 'bread', 'eggs']
You added 3 items.
```

> Hint: `items = []` before the loop, then `items.append(input("Item: "))` inside a
> `for _ in range(n):` loop.

### `exercise_5.py` — Keep the evens

Start with a list of numbers. Build a **new** list that contains only the even ones, then
print it. The original list must stay unchanged.

Example run:

```
Original: [3, 8, 11, 4, 7, 10]
Evens: [8, 4, 10]
```

> Hint: make `evens = []`, loop over the original list with `for n in numbers:`, and
> `evens.append(n)` only when `n % 2 == 0`.

### `exercise_6.py` — Is it on the list?

Start with a list of words. Ask the user for a word (clean it with `.strip().lower()`),
then use `in` to tell them whether it is on the list, and use `.count()` to say how many
times it appears.

Example run:

```
Search for: milk
Yes — "milk" is on the list (2 times).
```

Another run:

```
Search for: khinkali
No — "khinkali" is not on the list.
```

> Hint: `if word in shopping:` chooses which message to print. Inside the "yes" branch,
> `shopping.count(word)` gives the number.

### `exercise_7.py` — Package the average

Last week you learned `def`. Define a function `average(numbers)` that takes a list and
**returns** its average (no printing inside the function!). Then call it on two different
lists and print both results.

Example run:

```
83.75
50.0
```

> Hint: inside the function, sum the list with a `for` loop into a `total`, then
> `return total / len(numbers)`. The function should work for *any* list you hand it.

### `exercise_8.py` — Fix the bug (bonus)

The program below is meant to print every item in the list, but it **crashes**. Run it,
read the error, explain in a comment **why** it crashes, then fix it by changing **one
character**.

```python
colors = ["red", "green", "blue"]

for i in range(len(colors) + 1):
    print(colors[i])
```

It prints `red`, `green`, `blue`, then crashes with
`IndexError: list index out of range`.

> Hint: the list has 3 items, at positions `0`, `1`, `2` — there is no position `3`. Look
> closely at the `+ 1`. Why does it ask for one index too many?

---

## Checklist before you submit

- [ ] `exercise_1.py` … `exercise_8.py` written and run without errors using `python exercise_N.py`
- [ ] Everything is pushed inside the `workshop_5_homework/` folder of your repository
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Lists (tutorial): https://docs.python.org/3/tutorial/introduction.html#lists
- More on lists & methods: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- `str.split()`: https://docs.python.org/3/library/stdtypes.html#str.split
- `len()` reference: https://docs.python.org/3/library/functions.html#len
