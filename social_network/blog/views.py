from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from blog.models import Post


@login_required
def home_view(request):
    print(f"{request.GET = }")
    print(request.GET.get("name"))
    print(f"{request.POST = }")
    print(f"{request.method = }")

    if request.method == "POST":
        post = Post.objects.create(
            author=request.user,
            title=request.POST.get("title"),
            content=request.POST.get("content")
        )
        print(post)
    try:
        p = int(request.GET.get("p", 1))
    except ValueError:
        return redirect('home')
    if p <= 0:
        # raise Http404("your request page does not exist")
        return redirect('home')
    start = (p - 1) * 10
    end = p * 10
    return render(
        request,
        'home.html',
        {
            'posts': (
                Post.objects.all()
                .order_by('-created_at')
                .select_related("author")
                .prefetch_related("comment_set", "comment_set__author", "tags")
                [start:end]
            ),
            'prev': p - 1,
            'next': p + 1,
            'p': p
        }
    )
