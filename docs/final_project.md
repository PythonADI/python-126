# Final Project — Your Own Django Website

Welcome to your **final project**! Everything you have learned — variables,
`if`/`else`, loops, functions, lists, dictionaries, files, classes, and now
Django — comes together in one real, working website that **you** design and
build.

This is not a homework with small separate exercises. It is one project with a
**theme you choose** and a **checklist of requirements** that everyone must
meet. Two students can build completely different sites and both get full
marks.

**Deadline:** two weeks after this project is assigned — your instructor will
announce the exact date.

**How to submit:** push everything to the **same** GitHub repository you used
for the homeworks, in its own folder, then re-send the repository link to your
instructor:

```bash
cd python-homework        # the repo from Homework 1
mkdir final_project
cd final_project
# ...your Django project lives in here...
```

Commit **as you go** — after every feature that works, not one giant commit at
the end. Your git history is part of the grade.

```bash
git add .
git commit -m "Add recipe detail page"
git push
```

**The demo:** after the deadline, you present your site to the instructor for
**5–10 minutes**: show the pages working, then walk through your code. You
must be able to explain **any line** you wrote — a part of the project you
cannot explain earns **0 points for that part**, no matter how well it works.

> If a command fails, read the error message carefully — it usually tells you
> what is wrong. If you are still stuck, ask **early** — do not wait until the
> last day.

---

## Step 0 — Pick your theme

Choose one of these themes (or invent your own). **Tell your instructor your
theme before you start** — it takes one message and saves you from starting
over.

Each theme comes with three example models — feel free to rename them or add
your own:

| Theme | Example models |
|---|---|
| 🍲 Recipe book | `Category`, `Recipe`, `Comment` |
| 🎬 Movie catalog | `Director`, `Movie`, `Review` |
| 📚 Home library | `Author`, `Book`, `Review` |
| 🎉 Event board | `Venue`, `Event`, `Comment` |
| 🐶 Pet adoption | `Shelter`, `Pet`, `AdoptionRequest` |
| ⚽ Sports league | `Team`, `Player`, `MatchReport` |
| 🎵 Music collection | `Artist`, `Album`, `Review` |
| ✈️ Travel diary | `Country`, `Trip`, `Comment` |

Your own idea is welcome — a khachapuri bakery, a board-game shelf, anything —
as long as it fits the same shape: one "grouping" model, one "main" model, and
one model where users react to the main one.

In the requirements below the examples use the **recipe book** theme — replace
`Recipe` with your own main model everywhere.

---

## Requirements

Work through these sections **in order** — each one builds on the previous.
The point values add up to 100; the bonus section at the end can add up to 15
more.

### 1. Project setup — 10 points

- Create the project and apps the same way as in class:

  ```bash
  python -m pip install django
  django-admin startproject mysite
  cd mysite
  python manage.py startapp users
  python manage.py startapp recipes      # name it after YOUR theme
  ```

- Both apps are added to `INSTALLED_APPS`.
- `python manage.py runserver` starts with **no errors**.
- No `venv/` or `__pycache__/` folders in the repository.
- Git history shows **steady progress** — many small commits with clear
  messages, not one "final project done" commit.

> **Exception, just for this project:** committing `db.sqlite3` is allowed —
> that way your sample data arrives together with your code.

### 2. Your own User model — do this FIRST (graded with section 3)

Before the **first** `migrate`, set up a custom user exactly like we did for
the social network in class:

```python
# users/models.py
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

```python
# mysite/settings.py
AUTH_USER_MODEL = "users.User"
```

> ⚠️ **Order matters.** Django must know about your `User` **before** the
> database is created. If you already ran `migrate` without it, the simplest
> fix at this stage is to delete `db.sqlite3` and the numbered files inside
> `migrations/` folders, then run `makemigrations` and `migrate` again.

### 3. Models and migrations — 20 points

In your theme app's `models.py`:

- **At least three models** in addition to `User` (like `Category`, `Recipe`,
  `Comment`).
- At least one `ForeignKey` **between your own models** — e.g. every `Recipe`
  belongs to a `Category`, every `Comment` belongs to a `Recipe`.
- At least one model has an `author` field — a `ForeignKey` to your `User` —
  so the site remembers **who** created what.
- At least one model records **when** it was created with
  `DateTimeField(auto_now_add=True)`.
- **Every** model has a `__str__` method that returns something readable.
- `makemigrations` and `migrate` run cleanly, and the generated `migrations/`
  files are committed.

Example run — in `python manage.py shell`:

```
>>> from recipes.models import Recipe
>>> Recipe.objects.all()
<QuerySet [<Recipe: ხაჭაპური აჭარულად>, <Recipe: Khinkali>]>
```

> Hint: this is the same shape as the class project —
>
> ```python
> from django.db import models
> from users.models import User
>
>
> class Category(models.Model):
>     name = models.CharField(max_length=30)
>
>     def __str__(self):
>         return self.name
>
>
> class Recipe(models.Model):
>     author = models.ForeignKey(User, on_delete=models.CASCADE)
>     category = models.ForeignKey(Category, on_delete=models.CASCADE)
>     title = models.CharField(max_length=60)
>     content = models.TextField()
>     created_at = models.DateTimeField(auto_now_add=True)
>
>     def __str__(self):
>         return self.title
> ```

### 4. Admin and sample data — 10 points

- All your models are registered in `admin.py`.
- You created a superuser (`python manage.py createsuperuser`).
- Through the admin panel you added **real-looking sample data**: at least
  **2 categories**, **5 main objects** (recipes), and **5 comments** spread
  across them. `asdf` and `test123` everywhere will cost points — make it look
  like a site someone actually uses.

### 5. Pages — views and URLs — 20 points

Your site has **at least four pages**, all written as plain view functions
(like in class — no shortcuts we have not covered):

1. **Home page** at `""` — lists all main objects, **newest first**.
2. **Detail page** at `recipe/<int:recipe_id>/` — shows one object: its title,
   content, author, date, and its comments.
3. **Filtered page** at `category/<int:category_id>/` — lists only the objects
   that belong to that category.
4. **Create page** — the form page from section 7.

Every `path(...)` has a `name=`, and pages link to each other with `<a>` tags —
a visitor can reach every page by clicking, without typing addresses.

Example run — open http://127.0.0.1:8000/recipe/3/ :

```
ხაჭაპური აჭარულად
by nino · 2026-07-20
Category: ცომეული
...the recipe text...

Comments:
giorgi: gemrielia! 🤤
```

> Hint: two ORM tools you need here, both one small step beyond `.all()`:
>
> ```python
> recipe = Recipe.objects.get(id=recipe_id)          # exactly one object
> recipes = Recipe.objects.filter(category=category) # only the matching ones
> ```
>
> Newest first is `.order_by("-created_at")` — the minus flips the order. And
> the comments of a recipe are `recipe.comment_set.all()`, just like
> `post.comment_set` in class.

### 6. Templates — 15 points

- Every page is rendered with `render(request, "….html", context)` — no HTML
  inside Python strings.
- Templates use `{{ }}` holes, a `{% for %}` loop, and at least one meaningful
  `{% if %}` — for example, the home page shows *"No recipes yet — add the
  first one!"* when the list is empty.
- Links carry data from the loop:
  `<a href="/recipe/{{ recipe.id }}/">{{ recipe.title }}</a>`.
- Styling with Bootstrap (like the class home page) is **encouraged but not
  graded** — a plain readable page loses no points.

### 7. Creating objects with a form — 10 points

At least one page has a real HTML `<form method="post">` that **creates an
object**, exactly the way the social network created posts in class:

- The form has `{% csrf_token %}` inside.
- The view reads the fields with `request.POST.get(...)`, creates the object
  with `objects.create(...)`, sets `author=request.user`, and finishes with
  `redirect(...)` — never with `render` after a successful POST.

Example run — fill the form, press **Submit**, land on the home page, and your
new recipe is at the top of the list.

> Hint: the skeleton from class:
>
> ```python
> if request.method == "POST":
>     Recipe.objects.create(
>         author=request.user,
>         title=request.POST.get("title"),
>         content=request.POST.get("content"),
>     )
>     return redirect("home")
> ```

### 8. Login and logout — 10 points

- `login/` and `logout/` work using Django's built-in views, like in class:

  ```python
  from django.contrib.auth import views as auth_views

  path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
  path("logout/", auth_views.LogoutView.as_view(), name="logout"),
  ```

- `settings.py` has `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`, and
  `LOGIN_URL` (all three were in the class project).
- The **create page is protected** with `@login_required` — a logged-out
  visitor is sent to the login page. Browsing (home, detail, category) stays
  open to everyone.
- Pages show who you are: the template greets `{{ user.username }}` when
  logged in, and shows a **Log in** link otherwise.

> Hint: in any template, `user` is already available:
>
> ```html
> {% if user.is_authenticated %}
>   <p>გამარჯობა, {{ user.username }}! <a href="/logout/">Log out</a></p>
> {% else %}
>   <a href="/login/">Log in</a>
> {% endif %}
> ```

### 9. The demo — 5 points

Bring your project to the demo session and be ready to:

- click through every page while `runserver` runs;
- explain any view, model, or template line the instructor points at;
- answer one small "what if" — e.g. *"how would you add a `rating` field to
  Comment?"* You do not have to code it live, just explain the steps.

---

## Bonus — up to 15 extra points

Only attempt these once **everything above works**. Each is independent.

### Bonus 1 — Sign-up page (+6)

Let visitors register themselves instead of being created by the superuser.
This uses one thing we have **not** covered — Django's ready-made
`UserCreationForm` — so here is the full recipe:

```python
# users/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
```

```html
<!-- templates/signup.html — same shape as login.html -->
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Sign up</button>
</form>
```

Because your project uses a custom `User`, the plain `UserCreationForm` will
complain — create this small subclass (in a new file `users/forms.py`, or at
the top of `users/views.py`):

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username",)
```

…and use `SignUpForm` instead of `UserCreationForm` in the view.

### Bonus 2 — Pagination (+4)

Show 5 objects per page and add **← previous / next →** links, using the
`?p=2` technique from the class project: read `request.GET.get("p", 1)`,
convert with `int()` inside `try`/`except`, and slice the queryset
`[start:end]`.

### Bonus 3 — Tags with `ManyToManyField` (+3)

Add a `Tag` model and `tags = models.ManyToManyField(Tag)` on your main model
(like the class project). Show the tags on the detail page and add a page
`tag/<int:tag_id>/` that lists every object carrying that tag.

### Bonus 4 — Search box (+2)

A small `<form method="get">` on the home page with one text input. The view
reads `request.GET.get("q")` and, when present, narrows the list with
`Recipe.objects.filter(title__contains=q)`.

---

## Grading summary

| Section | Points |
|---|---|
| 1. Project setup and git history | 10 |
| 2–3. Custom User, models and migrations | 20 |
| 4. Admin and sample data | 10 |
| 5. Views and URLs | 20 |
| 6. Templates | 15 |
| 7. Create form (POST) | 10 |
| 8. Login and logout | 10 |
| 9. Demo | 5 |
| **Total** | **100** |
| Bonus 1–4 | up to +15 |

Remember: a section you cannot explain at the demo earns **0**, no matter how
polished it looks.

---

## Checklist before you submit

- [ ] Your theme was confirmed with the instructor
- [ ] `python manage.py runserver` starts with no errors
- [ ] Home, detail, category, and create pages all work by clicking links
- [ ] A logged-out visitor can browse but cannot reach the create page
- [ ] Login and logout both work
- [ ] Sample data looks real (no `asdf` recipes)
- [ ] Every model has `__str__`, migrations are committed
- [ ] No `venv/` or `__pycache__/` in the repository (`db.sqlite3` is fine)
- [ ] Git history shows many small commits
- [ ] You re-sent your repository link to the instructor

---

## Helpful links

- Models: https://docs.djangoproject.com/en/6.0/topics/db/models/
- Making queries (`get`, `filter`, `order_by`): https://docs.djangoproject.com/en/6.0/topics/db/queries/
- The admin site: https://docs.djangoproject.com/en/6.0/intro/tutorial02/
- URLs and converters: https://docs.djangoproject.com/en/6.0/topics/http/urls/
- Templates (`{{ }}`, `{% for %}`, `{% if %}`): https://docs.djangoproject.com/en/6.0/ref/templates/language/
- Authentication (`LoginView`, `login_required`): https://docs.djangoproject.com/en/6.0/topics/auth/default/
- Customizing the user model: https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#substituting-a-custom-user-model
- Bootstrap (optional styling): https://getbootstrap.com/docs/5.3/getting-started/introduction/
