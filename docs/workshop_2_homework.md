# Workshop 2 — Homework

Welcome to your second homework! It has two parts:

1. [Part 1 — Research: Workshop 2 concepts](#part-1--research-workshop-2-concepts)
2. [Part 2 — Python exercises](#part-2--python-exercises)

**Deadline:** before Workshop 3.

**How to submit:** push everything to the **same** GitHub repository you created for
Homework 1, then re-send the repository link to your instructor.

Put this homework in its own folder so it does not mix with Homework 1:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_2_homework
cd workshop_2_homework
# ...create your answers.md and exercise files in here...
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 2 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Part 1 — Research: Workshop 2 concepts

Create a file called `answers.md` and answer the following questions **in your own
words** (1–3 sentences each is enough). It is fine to be wrong — we will review the
answers together in the next workshop.

### Getting input from the user

1. What does the `input()` function do? What **data type** does it always return — even
   if the user types `42`?
2. Why do we often wrap `input()` in `int(...)` or `float(...)`? What goes wrong if we
   forget to?
3. What does the `type()` function tell you, and why is it handy when something is not
   behaving the way you expect?

### Working with strings

4. What do the string methods `.upper()`, `.lower()`, and `.strip()` each do? Give a
   short example for one of them.
5. What do the escape sequences `\n` and `\t` mean inside a string?

### Booleans and truthiness

6. A comparison like `age >= 18` produces a value. What **data type** is that value?
7. Why is `bool("")` `False`, but `bool("0")` and `bool(" ")` are both `True`?
   (Hint: think about *empty* versus *not empty*.)

### Floats and constants

8. Why does `0.1 + 0.2 == 0.3` print `False`? What is `round()` useful for here?
9. Some programmers write names like `MAX_SCORE` in ALL_CAPS. What does that naming
   **convention** signal to other programmers, and why shouldn't you change such a value
   later?

---

## Part 2 — Python exercises

Create the files below and write Python code to solve each task. Use only what we have
covered so far: **variables, data types, type casting, operators, `input()`, string
methods, f-strings, `bool()`, `round()`, and constants.**

> We have **not** learned `if`, loops, functions, or lists yet — you do not need any of
> them for this homework. When you need a `True`/`False` answer, just **print the
> boolean**, the way we did with "is even" in Homework 1.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — Greeting

Ask the user for their `name` with `input()`. They might accidentally type extra spaces,
so clean the text with `.strip()`. Then print a greeting on **two lines** using an
f-string, the escape sequence `\n`, and `.upper()`.

Example run:

```
What is your name?
   nino
Welcome!
HELLO, NINO!
```

### `exercise_2.py` — Years to 100

Ask the user for their `age`. Remember that `input()` gives you a **string**, so cast it
to an `int`. Print how many years are left until they turn 100, using an f-string.

Example run:

```
How old are you?
21
You will turn 100 in 79 years.
```

### `exercise_3.py` — Celsius → Fahrenheit

Ask for a temperature in Celsius and cast it to a `float`. Convert it to Fahrenheit with
the formula `celsius * 9 / 5 + 32`. Print the result **rounded to 1 decimal place** with
`round()`.

Example run:

```
Temperature in Celsius:
36.6
36.6°C is 97.9°F
```

### `exercise_4.py` — Truthy or falsy

First **guess** in a comment whether each value below is truthy (`True`) or falsy
(`False`). Then check your guesses using the self-documenting f-string we saw in class.
Finally, print the `type()` of any one of the values.

```python
# Guess first! Write True or False next to each line:
# bool("")    -> ?
# bool("0")   -> ?
# bool(" ")   -> ?
# bool(0)     -> ?
# bool(-5)    -> ?

print(f"{bool("") = }")
print(f"{bool("0") = }")
print(f"{bool(" ") = }")
print(f"{bool(0) = }")
print(f"{bool(-5) = }")

print(type("0"))
```

How many did you guess correctly?

### `exercise_5.py` — Circle area

Define a constant `PI = 3.14159` (note the ALL_CAPS name — that means "do not change
me"). Ask the user for a circle's `radius` and cast it to a `float`. Calculate the area
with `PI * radius ** 2` and print it **rounded to 2 decimal places**.

Example run:

```
Radius:
5
A circle with radius 5.0 has area 78.54
```

### `exercise_6.py` — Fix the bug (bonus)

The program below is supposed to tell the user how old they will be next year, but it
**crashes**. Explain in a comment **why** it crashes, then fix it so it works.

```python
age = input("How old are you?\n")
print("Next year you will be", age + 1, "years old.")
```

> Hint: what data type does `input()` give back? Can you add the number `1` to that?

---

## Checklist before you submit

- [ ] `answers.md` with the Workshop 2 questions answered
- [ ] `exercise_1.py` … `exercise_6.py` written and runnable
- [ ] Everything pushed to your GitHub repository (inside a `workshop_2_homework/` folder)
- [ ] Repository link sent to the instructor

---

## Helpful links

- String methods: https://docs.python.org/3/library/stdtypes.html#string-methods
- `input()` reference: https://docs.python.org/3/library/functions.html#input
- `round()` reference: https://docs.python.org/3/library/functions.html#round
- Truth value testing (truthiness): https://docs.python.org/3/library/stdtypes.html#truth-value-testing
- f-strings tutorial: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
