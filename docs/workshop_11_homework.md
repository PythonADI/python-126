# Workshop 11 — Homework

Welcome to your eleventh homework! This week your Python left the terminal and
moved to the **web**: a browser sends a **request**, a server answers with a
**response**, and **Django** turns plain Python functions into web pages. This
homework builds your first real website — one page at a time.

**Deadline:** before Workshop 12.

**How to submit:** push everything to the **same** GitHub repository you used for
the previous homeworks, then re-send the repository link to your instructor.

This week is different: instead of separate `exercise_N.py` files, **all the
exercises live inside one Django project**. Put it in its own folder:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_11_homework
cd workshop_11_homework
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 11 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Setup — install Django and start the project

Inside `workshop_11_homework/`, run these commands one at a time:

```bash
python -m pip install django
django-admin startproject mysite
cd mysite
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser — you should see Django's
welcome page with the rocket 🚀. That page is your server answering a request!

A few things to know while you work:

- If `python` is not found, try `python3` (macOS/Linux) or `py` (Windows).
- The red text about *"unapplied migrations"* is **normal this week** — databases
  arrive in a later workshop. Ignore it.
- `runserver` keeps running and **reloads by itself** every time you save a file.
  Leave it running in one terminal, edit code in your editor, and refresh the
  browser to see changes. Stop it with `Ctrl+C`.
- If the browser shows a yellow error page, don't panic — read the first line: it
  names the exact error and the line it happened on, just like a normal Python
  traceback.

Now create an **app** to hold your pages (run this in the folder that has
`manage.py`, in a second terminal or after stopping the server):

```bash
python manage.py startapp pages
```

and tell Django about it — open `mysite/settings.py`, find `INSTALLED_APPS`, and
add `"pages"` at the end of the list:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pages",          # ← add this line
]
```

`startapp` creates several files (`models.py`, `admin.py`, `tests.py`, …). This
week you only need **`pages/views.py`** — leave the rest alone; they get their
turn in later workshops.

---

## Web exercises

Use everything we have covered so far: **variables, f-strings, `if`/`else`,
loops, lists, dictionaries, functions** — plus this week's new material:

- **Request / response** — the browser asks for an address (`GET /about/`) and
  your Python answers with text (usually HTML).
- **A view** — a plain function in `pages/views.py` that takes `request` and
  **returns** a response: `return HttpResponse("<h1>hello</h1>")`
  (import it with `from django.http import HttpResponse`).
- **`path()`** — a line in `mysite/urls.py` that wires an address to a view:
  `path("about/", views.about)`. The empty string `""` is the home page.
- **`<str:name>`** — a placeholder inside a path,
  `path("hello/<str:name>/", views.hello)`; whatever the visitor typed there is
  handed to your view as an argument: `def hello(request, name):`.
- **Templates** — HTML files in `pages/templates/` with `{{ holes }}` that
  `render(request, "page.html", context)` fills in from a context **dict**;
  `{% for %} … {% endfor %}` repeats a piece of HTML for every item in a list.

Test each exercise by opening its address in the browser while `runserver` is
running.

### Exercise 1 — Your home page

In `pages/views.py`, write a view `home` that returns an `HttpResponse` with an
`<h1>` heading introducing you. Wire it to the empty path `""` in
`mysite/urls.py`.

Example run — open http://127.0.0.1:8000/ :

```
gamarjoba, I am nino!        ← shown big, because of <h1>
```

> Hint: in `pages/views.py`:
>
> ```python
> from django.http import HttpResponse
>
>
> def home(request):
>     return HttpResponse("<h1>gamarjoba, I am nino!</h1>")
> ```
>
> and in `mysite/urls.py` add an import and a path:
>
> ```python
> from django.contrib import admin
> from django.urls import path
> from pages import views
>
> urlpatterns = [
>     path("admin/", admin.site.urls),
>     path("", views.home),
> ]
> ```

### Exercise 2 — An about page

Add a view `about` at the address `about/`. Return a slightly bigger page: an
`<h1>` plus **two** `<p>` paragraphs — your hobby, your favorite food, anything.
A triple-quoted string (`"""..."""`) lets you write the HTML on several lines.

Example run — open http://127.0.0.1:8000/about/ :

```
About me
I am learning Python at workshop 11.
My favorite food is khachapuri.
```

> Hint: `def about(request):` returning
> `HttpResponse("""<h1>About me</h1> <p>...</p> <p>...</p>""")`, plus
> `path("about/", views.about)` in `mysite/urls.py`.

### Exercise 3 — Greet whoever visits

Add `path("hello/<str:name>/", views.hello)` and a view
`def hello(request, name):` that greets the visitor with an f-string. Try it
with **two different names** in the browser.

Example run — open http://127.0.0.1:8000/hello/nino/ :

```
გამარჯობა, nino!
```

and http://127.0.0.1:8000/hello/giorgi/ :

```
გამარჯობა, giorgi!
```

> Hint: `return HttpResponse(f"<h1>გამარჯობა, {name}!</h1>")`. You wrote the
> view once — the URL fills in `name` on every visit.

### Exercise 4 — Your favorites, from a template

Real pages are not written inside Python strings. Make a folder
`pages/templates/` and create `movies.html` inside it:

```html
<h1>{{ title }}</h1>
<ul>
  {% for movie in movies %}
    <li>{{ movie }}</li>
  {% endfor %}
</ul>
```

Then write a view `movies` that builds a context **dict** — a title plus a
**list of at least four** favorite movies (or books, or games — your choice) —
and returns `render(request, "movies.html", context)`. Wire it to `movies/`.

Example run — open http://127.0.0.1:8000/movies/ :

```
My favorite movies
• Interstellar
• Spirited Away
• The Matrix
• Coco
```

> Hint: in `pages/views.py` (note `render` is already imported at the top):
>
> ```python
> def movies(request):
>     context = {
>         "title": "My favorite movies",
>         "movies": ["Interstellar", "Spirited Away", "The Matrix", "Coco"],
>     }
>     return render(request, "movies.html", context)
> ```
>
> The folder must be named exactly `templates` inside `pages/`, and `"pages"`
> must be in `INSTALLED_APPS` — that is how Django finds your file.

### Exercise 5 — Multiplication table (bonus)

Combine **loops, lists, f-strings, and templates**. Add
`path("table/<int:n>/", views.table)`. In the view, build a list of ten rows
with a `for` loop — `"7 × 1 = 7"`, `"7 × 2 = 14"`, … — put it in a context
dict, and show it with a template that loops over the rows. Because the path
says `<int:n>`, Django hands you a real `int` — no `int()` needed.

Example run — open http://127.0.0.1:8000/table/7/ :

```
Table of 7
7 × 1 = 7
7 × 2 = 14
...
7 × 10 = 70
```

Try `/table/3/` and `/table/12/` — one view, every table.

> Hint: build the list first:
>
> ```python
> def table(request, n):
>     rows = []
>     for i in range(1, 11):
>         rows.append(f"{n} × {i} = {n * i}")
>     context = {"n": n, "rows": rows}
>     return render(request, "table.html", context)
> ```
>
> and in `pages/templates/table.html`, loop with
> `{% for row in rows %} <p>{{ row }}</p> {% endfor %}`.

---

## Checklist before you submit

- [ ] `python manage.py runserver` starts with no errors
- [ ] These addresses all work in the browser: `/`, `/about/`, `/hello/yourname/`, `/movies/` (and `/table/7/` if you did the bonus)
- [ ] The whole `mysite` project folder is pushed inside `workshop_11_homework/`
- [ ] You did **not** commit a `venv/` folder or `__pycache__/` folders (they are machine-generated and huge)
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- How the web works (MDN): https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works
- Installing Django: https://docs.djangoproject.com/en/6.0/intro/install/
- Official tutorial, part 1 (project + `runserver`): https://docs.djangoproject.com/en/6.0/intro/tutorial01/
- Writing views: https://docs.djangoproject.com/en/6.0/topics/http/views/
- URLs and `<str:name>` / `<int:n>` converters: https://docs.djangoproject.com/en/6.0/topics/http/urls/
- Templates (`{{ }}` and `{% for %}`): https://docs.djangoproject.com/en/6.0/ref/templates/language/
- Django Girls tutorial (very friendly, many languages): https://tutorial.djangogirls.org/
