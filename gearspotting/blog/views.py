from .models import Post
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify


def index(request):
    return render(
        request,
        "blog/index.html",
        {'posts': Post.objects.all()},
    )


def post(request):
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
        return redirect("/blog/")
    return render(
        request,
        "blog/add_post.html",
        {},
    )
