# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **teaching material for a beginners' Python course**, not an application. There is no build system, package, dependency file, or test suite. Each `.py` file is a standalone demonstration script meant to be read and run on its own to illustrate a single concept.

## Running code

Run any script directly with the interpreter — there is no entry point or shared module:

```bash
python workshop_2/strings.py
```

Targets Python 3.12+ (the scripts use f-string self-documenting expressions like `f"{x = }"` and quotes nested inside f-strings).

## Structure and conventions

- **`docs/workshop_N.md`** is the canonical lesson text; **`workshop_N/`** holds the runnable example scripts for that same lesson. These two pair up by number — when you add or change examples, keep the matching doc in sync, and vice versa. `README.md` is the index that links the docs together.
- **`presentations/Workshop N.html`** are self-contained slide exports for each workshop. **`resources/`** holds reference books (PDF), surfaced through `docs/resources.md`.
- Scripts within a workshop directory (e.g. `data_types.py`, `strings.py`, `boolean.py`) are independent — one concept each. They are not imported by anything.

## Writing examples (the important constraint)

The audience is absolute beginners. When adding or editing example code, **only use language features that have already been introduced by that point in the course.** Workshop 1 covers variables, data types, type casting, and arithmetic/comparison operators — examples there must not reach for loops, functions, or collections that haven't been taught yet. `docs/workshop_1_homework.md` shows the expected difficulty ceiling.

Some user-facing strings are intentionally in Georgian (e.g. `input("რამდენი წლის ხარ?\n")`); this is a bilingual course, so mixed English/Georgian prompts are expected, not a mistake to "fix."
