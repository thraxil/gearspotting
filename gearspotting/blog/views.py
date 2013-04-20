from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.sitemaps import ping_google


def index(request):
    return render(
        request,
        "blog/index.html",
        {'posts': Post.objects.all()},
    )


def add_post(request):
    if request.method == 'POST':
        if not request.POST.get('body', False):
            return redirect("/blog/post/")
        title = request.POST.get('title', 'no title')
        slug = slugify(title)
        Post.objects.create(
            author=request.user,
            body=request.POST.get('body', ''),
            title=title,
            slug=slug,
        )
        try:
            ping_google('/sitemap.xml')
        except:
            pass
        return redirect("/blog/")
    return render(
        request,
        "blog/add_post.html",
        {},
    )


def post(request, year, month, day, username, slug):
    author = get_object_or_404(User, username=username)
    post = get_object_or_404(
        Post,
        author=author,
        slug=slug,
    )
    return render(
        request,
        "blog/post.html",
        {'post': post},
    )
