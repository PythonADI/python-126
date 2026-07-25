# Workshop 12 — Django Forms: design

**Date:** 2026-07-25
**Status:** approved for implementation (autonomous session — decisions recorded here for review)

## Goal

Teach absolute beginners how a Django form travels the full circle: how the
browser builds and sends form data, and how Django receives, binds, validates,
and answers it. The whole front-and-back process must be *shown*, not just
told — the deck carries animated, step-through visualizations.

## Where the course stands

- Workshop 11 introduced the web: request/response, views, `path()`,
  templates. Homework built `mysite` with a `pages` app.
- The live-coding project `social_network/` (sessions after W11) has models
  (`Post`, `Comment`, `Tag`), auth via `LoginView`, and a home feed. Crucially
  it creates posts from **raw `request.POST.get()`** with no validation, and
  the comment form posts to `comment/create/` — a URL that does not exist yet.
  That is the motivating "before" state this workshop fixes.
- Students know: variables, f-strings, conditionals, loops, lists, dicts,
  functions, classes/OOP, files, and W11's Django basics. Models/DB were seen
  in live sessions. They have **not** seen: decorators beyond `@login_required`
  as an incantation, class-based views internals, formsets, crispy-forms —
  keep all of those out.

## Numbering

**Workshop 12** — the next free number across `docs/`, `presentations/`, and
workshop folders. If the instructor's session count differs, renaming the two
files and the README line is the only change needed.

## Deliverables

### 1. `presentations/Workshop 12.html` — animated deck (the centerpiece)

Self-contained HTML in the exact house style of `Workshop 11.html`: same CSS
variable palette (`--ink/--mute/--paper`, Anton + Inter + Noto Sans Georgian),
same slide engine (fixed 1440×900 stage, `←/→/Space` navigation, `↓` steps
through in-slide demos, per-slide IIFEs with `_onEnter`/`_onStep`, `setCap`
captions, `onLines` code-line highlighting), bilingual English/Georgian
accents. ~16–20 slides:

1. Title — *Workshop 12 · Forms*.
2. Recap — the request/response circle from W11; where we left the social
   network.
3. The problem — live-code screenshot-style slide of
   `request.POST.get("title")`: empty titles, missing keys, trusting the
   browser. "The browser can send *anything*."
4. `<form>` anatomy — `method`, `action`, `name`; **animated viz**: typing
   into inputs assembles the URL-encoded body (`title=gamarjoba&content=...`)
   character by character.
5. GET vs POST — query string vs body; **interactive**: toggle the method and
   watch the same data move between URL bar and request body.
6. **The full lifecycle — the hero visualization.** A two-round-trip animated
   diagram stepped with `↓`: GET → view makes *unbound* form → template
   renders HTML → user types → POST (+ hidden CSRF input) → view makes
   *bound* form → `is_valid()` → **branch**: invalid → errors attach → same
   template re-renders with messages (red path) / valid → `cleaned_data` →
   save → `redirect` → fresh GET (green path). Every later slide zooms into
   one stop on this map.
7. CSRF — why the hidden input exists; mini-viz: an attacker's form vs yours,
   the token only matches on the real site.
8. The `Form` class — fields declared like model fields; `forms.CharField`,
   `IntegerField`, widgets; rendering with `{{ form.as_p }}`.
9. Bound vs unbound — `PostForm()` vs `PostForm(request.POST)`; the same
   class, two moods.
10. `is_valid()` and `cleaned_data` — **typed-data animation**: strings from
    the wire (`"7"`, `"on"`, `"2026-07-25"`) pass through fields and come out
    as `int`, `bool`, `date`.
11. Errors — what invalid looks like; `form.errors`, re-render, messages next
    to fields.
12. `clean_<field>` — one custom rule (e.g. title must not be all caps),
    raising `ValidationError`.
13. ModelForm — "the form already knows the model": `PostForm` from `Post`,
    `form.save()`; refactor of the social network's home view.
14. Post/Redirect/Get — **animated**: hitting refresh after a POST re-submits
    (double post appears in the feed); `redirect()` breaks the loop.
15. Recap — the lifecycle map again, all stops lit.
16. Homework slide.

### 2. Live-code "after" state in `social_network/`

The code the instructor codes toward during the session:

- `blog/forms.py` — `PostForm` (ModelForm over `Post`, fields
  `title`/`content`, Bootstrap classes + placeholders via `widgets`, a
  `clean_title` rejecting empty/whitespace or shouting titles) and
  `CommentForm` (ModelForm over `Comment`, `content` only).
- `blog/views.py` — `home_view` refactored to use `PostForm` (POST → validate
  → `save(commit=False)` → set `author` → save → `redirect('home')`; invalid
  → re-render with the bound form). New `comment_create` view wired at
  `comment/create/` (name `comment-create`) — fixing today's dead form.
- `templates/home.html` — render the post form's fields (`{{ form.title }}`,
  errors under each field) keeping the existing Bootstrap look; comment form
  action switches to `{% url %}`.
- `templates/login.html` untouched — it already demonstrates
  `{{ form.as_p }}` + `csrf_token` and is referenced in the deck.
- Constraint: keep everything else (pagination, prefetching) exactly as-is;
  this is a surgical refactor the instructor can diff live.

### 3. `docs/workshop_12_homework.md`

Same voice/structure as `workshop_12`'s predecessor (`workshop_11_homework.md`):
intro tying to the week's theme, deadline "before Workshop 13", same-repo
submission, setup section continuing the **`mysite` project from Homework 11**
(new folder `workshop_12_homework/` — copy or re-create the project). A
"new material" glossary (form tag, GET vs POST, `forms.Form`, `is_valid`,
`cleaned_data`, errors, csrf). Exercises (each with an "example run" and a
hint block, Georgian strings where natural):

1. **A plain HTML form** — a `<form method="get">` search box; the view reads
   `request.GET` and echoes it. See the data in the URL bar.
2. **Switch to POST + Django Form** — a `GuestbookForm` (`forms.Form`) with
   `name` (CharField) and `message`; render with `{{ form.as_p }}`,
   `csrf_token`; on valid POST show "გმადლობთ, {name}!".
3. **Validation you can feel** — add `age = forms.IntegerField(min_value=6)`;
   submit letters and watch Django refuse; display errors.
4. **`clean_` rule** — reject messages shorter than 5 characters with a
   custom `ValidationError` message.
5. **Bonus — Post/Redirect/Get** — store messages in a module-level list,
   redirect after success, render the guestbook; explain why refresh no
   longer duplicates.

Checklist + helpful links (MDN forms, Django forms topic guide, Django Girls
forms chapter).

### 4. `README.md`

Add `[Workshop 12 — Homework](./docs/workshop_12_homework.md)` after the
Workshop 11 line.

## Non-goals

- No formsets, crispy-forms, class-based form views, file uploads, or JS
  validation — beyond the audience.
- No new `workshop_12/` scripts folder: for the web workshops the runnable
  example *is* `social_network/`; standalone `.py` files can't demonstrate a
  request cycle.
- No changes to `db.sqlite3`, migrations, models, or auth flow.

## Verification

- `python manage.py check` clean; a Django test-client exercise (GET home
  after login, POST valid + invalid post, POST comment) passes against the
  refactored views.
- Deck opened in a real browser: no console errors, every slide reachable,
  every `↓` demo steps, house style matches Workshop 11 side by side.
- Docs re-read against the beginner constraint (CLAUDE.md): no language
  feature that hasn't been taught.
