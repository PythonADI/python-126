# Workshop 1 — Homework

Welcome to your first homework! It has three parts:

1. [Part 1 — Research: Git & GitHub](#part-1--research-git--github)
2. [Part 2 — Put your homework on GitHub](#part-2--put-your-homework-on-github)
3. [Part 3 — Python exercises](#part-3--python-exercises)

**Deadline:** before Workshop 2.

**How to submit:** push everything to a GitHub repository (see Part 2) and send the
repository link to your instructor.

---

## Part 1 — Research: Git & GitHub

Create a file called `answers.md` and answer the following questions **in your own
words** (1–3 sentences each is enough). Use the links at the bottom if you get stuck.

### What is Git?

1. What is **Git** and what problem does it solve?
2. What is a **version control system** (VCS)?
3. What is a **repository** (repo)?
4. What is a **commit**? Why do we write a **commit message**?
5. What is the difference between `git add` and `git commit`?
6. What does `git push` do? What does `git pull` do?
7. What is a **branch** and why is it useful?

### What is GitHub?

8. What is **GitHub** and how is it different from **Git**?
9. Name two alternatives to GitHub (e.g. other websites that host Git repos).
10. What is the difference between a **public** and a **private** repository?
11. What is a `README.md` file and what is it used for?
12. What is a `.gitignore` file and why would you not want to commit every file?

> Tip: answer honestly from what you understand. It is fine to be wrong — we will
> review the answers together in the next workshop.

---

## Part 2 — Put your homework on GitHub

Follow these steps. If a command fails, read the error message carefully — it usually
tells you what is wrong.

### 1. Install the tools

- Install **Git**: https://git-scm.com/downloads
- Create a free **GitHub account**: https://github.com/signup

Check that Git is installed by running this in your terminal:

```bash
git --version
```

You should see something like `git version 2.43.0`.

### 2. Tell Git who you are (only needed once per computer)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 3. Create a repository on GitHub

1. Click the **+** in the top-right corner of GitHub → **New repository**.
2. Name it `python-homework` (or anything you like).
3. Keep it **Public**, check **Add a README file**, then click **Create repository**.

### 4. Get the repository onto your computer

Copy the repo URL (green **Code** button) and run:

```bash
git clone https://github.com/your-username/python-homework.git
cd python-homework
```

### 5. Add your homework files

Put your `answers.md` (Part 1) and your Python files (Part 3) inside this folder.

### 6. Commit and push

```bash
git add .
git commit -m "Add workshop 1 homework"
git push
```

Refresh your repository page on GitHub — your files should be there. 🎉

> If you get stuck, take a screenshot of the error and bring it to the next workshop.

---

## Part 3 — Python exercises

Create the files below and write Python code to solve each task. Use only what we
covered in Workshop 1: **variables, data types, type casting, and arithmetic /
comparison operators**.

Run each file with:

```bash
python exercise_1.py
```

### `exercise_1.py` — About me

Create variables for your `name` (str), `age` (int), and `height` in meters (float).
Print a sentence using an **f-string**, for example:

```
My name is Nino, I am 21 years old and 1.65 meters tall.
```

### `exercise_2.py` — Fix the bug

The code below crashes. Explain in a comment **why** it crashes, then fix it using
**type casting** so it prints `30`.

```python
a = 10
b = "20"
print(a + b)
```

### `exercise_3.py` — Rectangle

Create two variables `width` and `height` (numbers of your choice). Calculate and
print the **area** (`width * height`) and the **perimeter** (`2 * (width + height)`).

### `exercise_4.py` — Odd or even

Create a variable `number`. Use the **modulus** operator (`%`) and a **comparison**
operator to print whether the number is even. The result should be a boolean, e.g.:

```python
number = 7
print("Is even:", number % 2 == 0)   # Is even: False
```

### `exercise_5.py` — Seconds in a day (bonus)

There are 60 seconds in a minute, 60 minutes in an hour, and 24 hours in a day.
Using variables and multiplication, calculate and print how many **seconds are in a
day**. Then print how many seconds are in **a week**.

---

## Checklist before you submit

- [ ] `answers.md` with the Git / GitHub questions answered
- [ ] `exercise_1.py` … `exercise_5.py` written and runnable
- [ ] Everything pushed to your GitHub repository
- [ ] Repository link sent to the instructor

---

## Helpful links

- Git handbook (short): https://docs.github.com/en/get-started/using-git/about-git
- "Hello World" GitHub guide: https://docs.github.com/en/get-started/start-your-journey/hello-world
- Git cheat sheet (PDF): https://education.github.com/git-cheat-sheet-education.pdf
- Interactive Git practice: https://learngitbranching.js.org/
