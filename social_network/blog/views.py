from django.shortcuts import render
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

    return render(
        request,
        'home.html',
        {
            'posts': Post.objects.all().order_by('-created_at')
        }
    )
