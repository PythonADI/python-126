# Workshop 6 — Homework

Welcome to your sixth homework! This week is **all about dictionaries** — your way to look
a value up by **name** instead of by number. A list answers *"what is at position 2?"*; a
dictionary answers *"what is nino's score?"*. Many of these tasks are old friends from the
list homework, but this time the data is keyed by name.

**Deadline:** before Workshop 7.

**How to submit:** push everything to the **same** GitHub repository you used for the
previous homeworks, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with the earlier ones:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_6_homework
cd workshop_6_homework
# ...create your exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 6 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Python exercises

Create the files below and write Python code to solve each task. Use only what we have
covered so far: **variables, f-strings, `input()`, `int()` / `float()`, `if` / `elif` /
`else`, `and` / `or` / `not`, `while`, `for` + `range()`, `+=`, `len()`, string methods,
lists (`[ ... ]`, indexing, `.append()`, `.split()`), `def` / `return`** — plus this
week's new material: **dictionaries** — creating them with `{key: value}`, looking up with
`d[key]`, safe lookup `d.get(key)` / `d.get(key, default)`, adding and updating with
`d[key] = value`, removing with `del d[key]` / `d.pop(key)`, membership `key in d` (which
checks the **keys**), `len(d)`, and looping with `for key in d`, `d.keys()`, `d.values()`,
and `for key, value in d.items()`.

> We have **not** learned list/dict comprehensions, tuples, or sets yet — you do not need
> them. Keep your solutions to the tools above.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — Your dictionary

Create a dictionary called `profile` describing one person, with **at least three**
key:value pairs (for example `name`, `age`, and `city`). Then print, on separate lines:
the whole dictionary, how many pairs it has using `len()`, and **one** value looked up by
its key.

Example run:

```
{'name': 'nino', 'age': 21, 'city': 'tbilisi'}
3 facts about this person.
City: tbilisi
```

> Hint: look a value up with `profile["city"]`. `len(profile)` counts the **pairs**, not
> the letters.

### `exercise_2.py` — Safe lookup

Make a dictionary that maps names to phone numbers (at least three). Ask the user for a
name (clean it with `.strip().lower()`), then tell them the number — or a friendly "not
found" message if that name is not in the phonebook.

Example run:

```
Whose number? nino
nino's number is 555-1234.
```

Another run:

```
Whose number? luka
Sorry, luka is not in the phonebook.
```

> Hint: `if name in phone:` chooses which message to print — remember `in` checks the
> **keys**. Inside the "yes" branch, `phone[name]` is the number. (You could also use
> `phone.get(name)` and check whether it came back as `None`.)

### `exercise_3.py` — Add and update

Start with a small prices dictionary, for example `prices = {"milk": 2, "bread": 1}`. Print
it, then **add** a new item, **update** the price of an item that is already there, and
print it again.

Example run:

```
Before: {'milk': 2, 'bread': 1}
After:  {'milk': 3, 'bread': 1, 'eggs': 4}
```

> Hint: `prices["eggs"] = 4` **adds** a new pair, while `prices["milk"] = 3` **updates**
> the existing one — exactly the same syntax. Whether it adds or replaces depends only on
> whether the key is already there.

### `exercise_4.py` — Print every pair

Take a dictionary of names to scores. Loop over it with
`for name, score in d.items():` and print each pair on its own line as `name: score`.

Example run:

```
nino: 90
giorgi: 75
mariami: 88
```

> Hint: `.items()` hands you **both at once** — the key goes into the first name, the value
> into the second. Print them with `print(f"{name}: {score}")`.

### `exercise_5.py` — Build a dictionary from input

Ask the user **how many** students to record (`int(input(...))`). Start with an empty
dictionary, then loop that many times, each time asking for a name and a score and storing
`scores[name] = int(score)`. At the end, print the finished dictionary and how many pairs
it holds.

Example run:

```
How many students? 2
Name: nino
Score: 90
Name: giorgi
Score: 75
{'nino': 90, 'giorgi': 75}
2 students recorded.
```

> Hint: `scores = {}` before the loop, then inside a `for _ in range(n):` loop read the
> name and score and write `scores[name] = int(score)`.

### `exercise_6.py` — Count the words (tally)

Start with a sentence, for example `sentence = "milk bread milk eggs milk"`. Split it into
words with `.split()`, then count how many times **each** word appears using a dictionary.
Print every word with its count.

Example run:

```
milk: 3
bread: 1
eggs: 1
```

> Hint: `counts = {}` before the loop. For each word do
> `counts[word] = counts.get(word, 0) + 1`. The `0` is the fallback the **first** time a
> word is seen — there is no count yet, so start from zero and add one.

### `exercise_7.py` — Package it

Define a function `total_price(cart)` that takes a dictionary of item → price and
**returns** the sum of all the prices (no printing inside the function!). Then call it on
two different carts and print both results.

Example run:

```
7
12
```

> Hint: inside the function start `total = 0`, then `for price in cart.values(): total +=
> price`, and finally `return total`. The function should work for *any* cart you hand it.

### `exercise_8.py` — Fix the bug (bonus)

The program below is meant to print a person's score, but it **crashes**. Run it, read the
error, explain in a comment **why** it crashes, then fix it so that a missing name prints a
sensible fallback instead of crashing.

```python
scores = {"nino": 90, "giorgi": 75}

name = "luka"
print(f"{name}'s score is {scores[name]}")
```

It crashes with `KeyError: 'luka'`.

> Hint: `"luka"` is not one of the keys, and `scores["luka"]` **demands** a key that does
> not exist. Ask politely instead: `scores.get(name, 0)` returns `0` when the name is
> missing, so the program prints a `0` rather than crashing.

---

## Checklist before you submit

- [ ] `exercise_1.py` … `exercise_8.py` written and run without errors using `python exercise_N.py`
- [ ] Everything is pushed inside the `workshop_6_homework/` folder of your repository
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Dictionaries (tutorial): https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- More on `dict` (reference): https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
- `dict.get()`: https://docs.python.org/3/library/stdtypes.html#dict.get
- Looping over pairs with `.items()`: https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
