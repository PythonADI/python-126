# Workshop 5 — Lists · Design

**Date:** 2026-06-13
**Status:** Approved

## Goal

Add the fifth workshop to the beginners' Python course. Topic: **lists** — the first
collection type the course introduces. The previous homeworks (WS3, WS4) repeatedly tell
students *"we have not learned lists or dictionaries yet"*; this workshop fills that gap.
The Workshop 4 slide deck already ends by promising *"Workshop 05 — Lists. One name for
many values: store them, loop them, grow them."* — this workshop delivers on that promise.

## Course position (what students already know)

By the end of Workshop 4 students have: variables, data types, type casting, arithmetic /
comparison operators, strings + string methods (`.upper`, `.lower`, `.strip`, `.title`,
`.count`), f-strings, `input()`, `bool`, constants, `if`/`elif`/`else`, `and`/`or`/`not`,
`while`, `for`, `range`, `len`, looping over the characters of a string, `+=`/`-=`, and
functions (`def`, parameters, default values, `return`, `None`).

## Hard constraint

Per `CLAUDE.md`: **only use language features already introduced by this point.** Lists
are the only new concept. Specifically:

- **Allowed new list features:** literals `[...]`, empty `[]`, indexing `x[0]` / `x[-1]`,
  slicing `x[a:b]`, index assignment `x[i] = v`, `.append()`, `.insert()`, `.pop()`,
  `.remove()`, `.count()`, membership `in` / `not in`, iterating with `for item in x`,
  `len(x)`, building a list by `append` in a loop, `str.split()` / `str.join()`,
  `sum()` / `min()` / `max()` (used sparingly).
- **NOT allowed (not taught yet):** list comprehensions, `enumerate`, `break` / `continue`,
  `sorted()` with `key=`, dictionaries, tuples, sets, `zip`, slicing with a step in
  exercises, f-string `!r`. Index access in loops uses `for i in range(len(x))`.
- Python 3.12+. Mixed English/Georgian strings are intentional (bilingual course), not a
  bug to "fix".

## Deliverables (scope: "homework + slide", plus the example scripts that are the workshop)

1. `workshop_5/` — standalone example scripts, one concept each (the runnable "workshop").
2. `docs/workshop_5_homework.md` — homework, same format as WS3/WS4.
3. `presentations/Workshop 5.html` — slide deck, reusing the WS4 deck chrome.
4. `README.md` — add a `Workshop 5 — Homework` link.

Explicitly **out of scope:** a separate `docs/workshop_5.md` prose lesson (only WS1 has one;
WS2–WS4 do not).

## 1. Example scripts (`workshop_5/`)

Terse, runnable, one concept each, matching the existing house style (mostly hardcoded
data so each file runs non-interactively; occasional Georgian flavor; occasional
commented-out alternative line). 9 files:

| file | concept |
|---|---|
| `lists.py` | creating lists — empty, numbers, strings, mixed; printing whole list / in an f-string; a list is one value holding many |
| `indexing.py` | `x[0]`, `x[1]`, `x[-1]`, `len(x)`, last via `-1`, the `IndexError` gotcha (shown as a comment) |
| `slicing.py` | `x[1:4]`, `x[:3]`, `x[2:]`, `x[:]`; note it works on strings too |
| `methods.py` | mutating — `x[i] = v`, `.append()`, `.insert()`, `.pop()`, `.remove()`; the list grows and shrinks |
| `loop.py` | `for item in shopping:` print each; numbered output via `for i in range(len(x))` |
| `membership.py` | `in` / `not in` with `if`; `.count()` |
| `building.py` | start `result = []`, grow it inside a `for` loop (squares 1..n) |
| `list_functions.py` | a function that takes a list and returns a value — `total(numbers)` / `average(numbers)` (WS4 callback) |
| `split.py` | `text.split()` → list, `" ".join(words)` — the WS3 word-counter reborn as `len(text.split())` |

## 2. Homework (`docs/workshop_5_homework.md`)

Same structure as `workshop_4_homework.md`: intro, deadline "before Workshop 6", submit to
the same repo in a new `workshop_5_homework/` folder, a "use only what we have covered"
note that now includes lists, run instructions, then exercises with example runs + hints,
then a submit checklist and helpful links. 7 exercises + 1 bonus:

1. `exercise_1.py` — Build & describe a list (create ≥4 items, print whole list, `len`, first & last).
2. `exercise_2.py` — Numbered list (`1. nino`, `2. giorgi`, … via `range(len())` or a counter `+=`).
3. `exercise_3.py` — Sum & average of a list of numbers (loop + `len`, or `sum()`).
4. `exercise_4.py` — Collect `input()` into a list with `.append()` inside a loop; print the list + length.
5. `exercise_5.py` — Filter into a **new** list (keep the evens; `append` inside `for` + `if`).
6. `exercise_6.py` — Search / membership (`if item in list`; report found + how many times with `.count()`).
7. `exercise_7.py` — Package it: `def average(numbers)` returning the average (WS4 callback).
8. `exercise_8.py` (bonus) — Fix the bug: `for i in range(len(x) + 1)` → `IndexError`; explain in a comment & fix.

## 3. Slide deck (`presentations/Workshop 5.html`)

Reuse the WS4 deck's exact chrome (CSS variables, `.slide`/`.head`/`.code`/`.out`/`.note`/
`.warn`/`.cols2`/`.grid`/`.mtab`/`.recap`/`.title-wrap` classes, the overlay nav UI, and
the navigation `<script>`). Two-part structure, ~20 slides:

- **Cover** — `LISTS`, "Part 1 — collections · Part 2 — working with lists".
- **Part 1 — Lists as a collection:** why (one variable, many values) → creating →
  indexing (0-based, negative) → `len` + first/last → slicing → the `IndexError` gotcha.
- **Part 2 — Working with lists:** looping (ties to `for`) → membership (`in`) →
  growing/shrinking (`append`/`pop`/`insert`/`remove`, index assignment) → building a
  list in a loop (`[]` + `append`) → functions over lists (`total`/`average`, WS4 callback)
  → `split`/`join` (the word-counter reborn) → where lists show up → recap + teaser
  (Workshop 06) → end.
- Update the cover/footer slide counts to the deck's real slide total.

## 4. README

Add under the existing list:

```
[Workshop 5 — Homework](./docs/workshop_5_homework.md)
```

## Verification (adversarial, after build)

A Workflow fan-out:

1. **Execute** every `workshop_5/*.py` with Python 3.12 and report stderr / wrong output.
2. **Feature-creep scan** — read every new script + the homework and flag ANY construct not
   in the "allowed" list above (comprehensions, `break`, `enumerate`, dicts, etc.).
3. **Deck check** — validate `Workshop 5.html` structure against `Workshop 4.html`: every
   `.slide` well-formed, nav script intact, slide counts consistent, no leftover WS4 text.
4. **Homework proofread** — consistency of exercise prompts with example runs, format parity
   with WS3/WS4, working links.

Fix every confirmed finding, then commit.
