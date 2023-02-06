from django.urls import re_path

from .views import AddPostView, IndexView, PostView

urlpatterns = [
    re_path(r"^$", IndexView.as_view()),
    re_path(r"^post/$", AddPostView.as_view()),
    re_path(
        (
            r"(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/"
            r"(?P<username>\w+)/(?P<slug>[\w\-]+)/$"
        ),
        PostView.as_view(),
    ),
]
