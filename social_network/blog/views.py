from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import PostForm, CommentForm


@login_required
def home_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
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
            'form': form,
            'prev': p - 1,
            'next': p + 1,
            'p': p
        }
    )


@login_required
def comment_create(request):
    if request.method != "POST":
        return redirect('home')
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('home')
