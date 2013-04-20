from .models import Post
from django.shortcuts import render


def index(request):
    return render(
        request,
        "blog/index.html",
        {'posts': Post.objects.all()},
    )
