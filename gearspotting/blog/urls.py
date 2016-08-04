from django.conf.urls import url
from .views import IndexView, AddPostView, PostView


urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^post/$', AddPostView.as_view()),
    url((r'(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/'
         r'(?P<username>\w+)/(?P<slug>[\w\-]+)/$'),
        PostView.as_view()),
]
