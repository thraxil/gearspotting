from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.views.generic.base import TemplateView, View

from .models import Post


class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self):
        return dict(posts=Post.objects.all())


class AddPostView(View):
    template_name = "blog/add_post.html"

    def get(self, request):
        return render(request, self.template_name, dict())

    def post(self, request):
        if not request.POST.get("body", False):
            return redirect("/blog/post/")
        title = request.POST.get("title", "no title")
        slug = slugify(title)[:50]
        Post.objects.create(
            author=request.user,
            body=request.POST.get("body", ""),
            title=title,
            slug=slug,
        )
        return redirect("/blog/")


class PostView(TemplateView):
    template_name = "blog/post.html"

    def get_context_data(self, year, month, day, username, slug):
        author = get_object_or_404(User, username=username)
        post = get_object_or_404(
            Post,
            author=author,
            slug=slug,
        )
        return dict(post=post)
