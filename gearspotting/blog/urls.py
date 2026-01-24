from django.urls import path

from .views import AddPostView, IndexView, PostView

app_name = "blog"
urlpatterns = [
    path("", IndexView.as_view(), name="blog_index"),
    path("post/", AddPostView.as_view(), name="blog_add_post"),
    path(
        "<int:year>/<int:month>/<int:day>/<str:username>/<slug:slug>/",
        PostView.as_view(),
        name="blog_post_detail",
    ),
]
