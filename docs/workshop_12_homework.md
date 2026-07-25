# Workshop 12 — Homework

Welcome to your twelfth homework! Last week your pages only *talked* — this week
they **listen**. A **form** lets the visitor send data back to your Python, and
**Django Forms** check that data before you trust it: the browser can send
*anything*, and your job is to validate it. This homework builds a small
**guestbook** where visitors leave you messages — and Django politely refuses
the bad ones.

**Deadline:** before Workshop 13.

**How to submit:** push everything to the **same** GitHub repository you used for
the previous homeworks, then re-send the repository link to your instructor.

Like last week, all the exercises live inside **one Django project**. Put it in
its own folder:

```bash
cd python-homework        # the repo from Homework 1
mkdir workshop_12_homework
cd workshop_12_homework
```

When you are done, commit and push from the repository folder:

```bash
git add .
git commit -m "Add workshop 12 homework"
git push
```

> If a command fails, read the error message carefully — it usually tells you what is
> wrong. If you are still stuck, take a screenshot and bring it to the next workshop.

---

## Setup — continue the project from Homework 11

This homework **continues** the `mysite` project you built last week. The
easiest way: **copy** your whole `workshop_11_homework/mysite` folder into
`workshop_12_homework/` (in your file manager, or with `cp -r` / drag-and-drop),
so you keep the `pages` app and every view you already wrote.

If you prefer a fresh start, re-create it with the same commands as last week —
inside `workshop_12_homework/`, one at a time:

```bash
python -m pip install django
django-admin startproject mysite
cd mysite
python manage.py startapp pages
```

…and don't forget to add `"pages"` to `INSTALLED_APPS` in `mysite/settings.py`,
exactly like in Homework 11.

Either way, check that the server still starts:

```bash
python manage.py runserver
```

Two reminders while you work:

- `runserver` reloads by itself when you save — but if you create a **new file**
  (like `pages/forms.py`) and Django can't see it, stop the server with `Ctrl+C`
  and start it again.
- The yellow error page is your friend: the first line names the exact error,
  just like a normal Python traceback.

---

## Web form exercises

Use everything we have covered so far: **variables, f-strings, `if`/`else`,
loops, lists, dictionaries, functions, classes** — plus last week's views and
templates — plus this week's new material:

- **The `<form>` tag** — HTML that collects input and sends it to the server.
  `method` says *how* to send (`get` or `post`), `action` says *where* (leave it
  out to send to the same address), and every input's `name` becomes the key
  the data arrives under.
- **GET vs POST** — `method="get"` puts the data **in the URL**
  (`/search/?q=khachapuri` — you can see and bookmark it); `method="post"` puts
  it **in the request body** (hidden from the URL — right for anything that
  changes or saves something).
- **`{% csrf_token %}`** — a required hidden input inside every POST form; it
  proves the form really came from *your* site. Forget it and Django answers
  **403 Forbidden**.
- **`forms.Form`** — a class describing your form in Python:
  `name = forms.CharField()`, `age = forms.IntegerField()`. Each field knows
  what HTML input to draw *and* how to check the answer.
- **`{{ form.as_p }}`** — put a form object in the context, and this renders
  all its fields as HTML paragraphs — labels, inputs, and error messages, for
  free.
- **`is_valid()` and `cleaned_data`** — `form.is_valid()` runs every check and
  answers `True`/`False`; after that, `form.cleaned_data` is a **dict** of the
  data converted to real Python types (an `IntegerField` gives you an `int`,
  not the string `"25"`).
- **`form.errors`** — when validation fails, each field's complaints live here;
  re-render the same template and `{{ form.as_p }}` shows them next to the
  fields.
- **`redirect()`** — `return redirect("/somewhere/")` tells the browser "go ask
  for this address with a fresh GET" (import it with
  `from django.shortcuts import render, redirect`).

Test each exercise by opening its address in the browser while `runserver` is
running.

### Exercise 1 — A search form (GET)

Make a template `pages/templates/search.html` with a plain HTML form:

```html
<h1>ძებნა</h1>
<form method="get">
  <input type="text" name="q">
  <button type="submit">ძებნა</button>
</form>
```

Write a view `search` at the address `search/` that reads what arrived with
`request.GET.get("q", "")`. If something arrived — echo it back; otherwise just
show the form. Then **look at the URL bar** after you press the button: with
`method="get"`, your data travels in the address itself.

Example run — open http://127.0.0.1:8000/search/ , type `khachapuri`, press
ძებნა. The address becomes:

```
http://127.0.0.1:8000/search/?q=khachapuri
```

and the page shows:

```
შენ მოძებნე: khachapuri
```

> Hint: in `pages/views.py`:
>
> ```python
> def search(request):
>     query = request.GET.get("q", "")
>     if query:
>         return HttpResponse(f"<h1>შენ მოძებნე: {query}</h1>")
>     return render(request, "search.html")
> ```
>
> and in `mysite/urls.py` add `path("search/", views.search)`. Change `q` in
> the URL bar by hand — `?q=lobiani` — and refresh: the form is just a URL
> builder!

### Exercise 2 — The guestbook form (POST + `forms.Form`)

Now the Django way. Create a **new file** `pages/forms.py`:

```python
from django import forms


class GuestbookForm(forms.Form):
    name = forms.CharField(max_length=50)
    message = forms.CharField()
```

Make a template `pages/templates/guestbook.html` that renders it — note the
`{% csrf_token %}`, it is **not optional**:

```html
<h1>სტუმართა წიგნი</h1>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">გაგზავნა</button>
</form>
```

Write a view `guestbook` at the address `guestbook/`. On a normal visit (GET),
show an **empty** form. When the form comes back (POST), build the form **from
the data** — `GuestbookForm(request.POST)` — and if `is_valid()`, thank the
visitor by name.

Example run — open http://127.0.0.1:8000/guestbook/ , fill in `nino` and
`გამარჯობა ყველას!`, press გაგზავნა:

```
გმადლობთ, nino!
```

> Hint: in `pages/views.py`:
>
> ```python
> from pages.forms import GuestbookForm
>
>
> def guestbook(request):
>     if request.method == "POST":
>         form = GuestbookForm(request.POST)
>         if form.is_valid():
>             name = form.cleaned_data["name"]
>             return HttpResponse(f"<h1>გმადლობთ, {name}!</h1>")
>     else:
>         form = GuestbookForm()
>     return render(request, "guestbook.html", {"form": form})
> ```
>
> plus `path("guestbook/", views.guestbook)` in `mysite/urls.py`. One view,
> two moods: GET builds an *empty* form, POST builds a *bound* one and checks
> it.

### Exercise 3 — Validation you can feel

Add one line to `GuestbookForm`:

```python
age = forms.IntegerField(min_value=6)
```

Change **nothing else** — then go break it. Submit `abc` as the age. Submit
`3`. Submit an empty name. Django refuses every time and `{{ form.as_p }}`
prints the reason next to the field — that is `form.errors` at work, and your
view already re-renders the bound form when `is_valid()` is `False`.

Example run — open http://127.0.0.1:8000/guestbook/ , type `giorgi`, a message,
and age `abc`:

```
Age:  Enter a whole number.
```

and with age `3`:

```
Age:  Ensure this value is greater than or equal to 6.
```

The page still shows what you typed — a bound form remembers.

> Hint: nothing to change in the view — that is the point. When `is_valid()`
> answers `False`, the `if` is skipped, the function reaches
> `return render(...)` with the **bound** form, and `as_p` draws the errors.
> Curious what the errors look like in Python? Add a temporary
> `print(form.errors)` right after `is_valid()` and watch the `runserver`
> terminal.

### Exercise 4 — Your own rule with `clean_message`

Built-in checks are not always enough. Add a method to `GuestbookForm` that
rejects messages shorter than **5 characters** — with your own error message
(Georgian welcome!):

Example run — submit the message `ok`:

```
Message:  შეტყობინება ძალიან მოკლეა — მინიმუმ 5 ასო!
```

and the message `გამარჯობა ყველას!` passes as before.

> Hint: in `pages/forms.py`, inside the class, after the fields:
>
> ```python
>     def clean_message(self):
>         message = self.cleaned_data["message"]
>         if len(message) < 5:
>             raise forms.ValidationError(
>                 "შეტყობინება ძალიან მოკლეა — მინიმუმ 5 ასო!"
>             )
>         return message
> ```
>
> The name matters: `clean_` + the field name, and Django calls it by itself
> during `is_valid()`. Always `return` the value at the end — that is what
> lands in `cleaned_data`.

### Exercise 5 — Post/Redirect/Get (bonus)

Let's actually *keep* the messages. At the top of `pages/views.py` (outside any
function) make a module-level list, and change the view: on valid POST,
**append** `"{name}: {message}"` to the list and `redirect("/guestbook/")`
instead of returning a thank-you page. Show the list in `guestbook.html` with a
`{% for %}` loop under the form.

Then try the experiment: submit a message and press **refresh** (F5). The
message appears **once**, not twice.

Why? Without the redirect, refresh repeats your last request — the POST — and
submits the form again, duplicating the entry (the browser even warns you with
a "resubmit?" dialog). With `redirect()`, the last request the browser
remembers is a harmless **GET**, so refresh just re-reads the page. That is the
**Post/Redirect/Get** pattern, and nearly every real website uses it.

Example run — after nino and giorgi both wrote:

```
სტუმართა წიგნი
[the form]
• nino: გამარჯობა ყველას!
• giorgi: khachapuri > everything
```

(The list lives in the server's memory, so it empties when `runserver`
restarts — real storage is called a *database*, and it gets its turn soon.)

> Hint: in `pages/views.py`:
>
> ```python
> from django.shortcuts import render, redirect
> from pages.forms import GuestbookForm
>
> GUESTBOOK = []
>
>
> def guestbook(request):
>     if request.method == "POST":
>         form = GuestbookForm(request.POST)
>         if form.is_valid():
>             name = form.cleaned_data["name"]
>             message = form.cleaned_data["message"]
>             GUESTBOOK.append(f"{name}: {message}")
>             return redirect("/guestbook/")
>     else:
>         form = GuestbookForm()
>     context = {"form": form, "entries": GUESTBOOK}
>     return render(request, "guestbook.html", context)
> ```
>
> and in `guestbook.html`, under the form:
>
> ```html
> <ul>
>   {% for entry in entries %}
>     <li>{{ entry }}</li>
>   {% endfor %}
> </ul>
> ```

---

## Checklist before you submit

- [ ] `python manage.py runserver` starts with no errors
- [ ] `/search/?q=khachapuri` echoes the query, and you saw the data in the URL bar
- [ ] `/guestbook/` shows the form, and a valid submission answers `გმადლობთ, {name}!` (or, with the bonus, adds to the list)
- [ ] Age `abc` and age `3` both show an error message on the page instead of crashing
- [ ] A 2-character message shows **your own** Georgian error message
- [ ] Every POST form template contains `{% csrf_token %}`
- [ ] The whole `mysite` project folder is pushed inside `workshop_12_homework/`
- [ ] You did **not** commit a `venv/` folder or `__pycache__/` folders (they are machine-generated and huge)
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Your first form (MDN, very beginner-friendly): https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form
- Sending form data — GET vs POST (MDN): https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Sending_and_retrieving_form_data
- Working with forms (Django topic guide): https://docs.djangoproject.com/en/6.0/topics/forms/
- Form fields reference (`CharField`, `IntegerField`, …): https://docs.djangoproject.com/en/6.0/ref/forms/fields/
- Form and field validation (`clean_<field>`): https://docs.djangoproject.com/en/6.0/ref/forms/validation/
- CSRF protection — why the token exists: https://docs.djangoproject.com/en/6.0/ref/csrf/
- Django Girls — Django Forms chapter: https://tutorial.djangogirls.org/en/django_forms/
- Django Girls — HTML forms extension: https://tutorial.djangogirls.org/en/homework_create_more_models/
