from django.urls import re_path
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.musiciangear.models import MusicianGear
from gearspotting.musiciangear.views import (AddLinkView, AddPhotoView,
                                             EditLinksView, EditPhotosView)

urlpatterns = [
    re_path(r"^$", ListView.as_view(model=MusicianGear)),
    re_path(r"^create/?$", CreateView.as_view(model=MusicianGear)),
    re_path(
        r"^(?P<object_id>\d+)/update/?$",
        UpdateView.as_view(model=MusicianGear),
    ),
    re_path(
        r"^(?P<object_id>\d+)/delete/?$",
        DeleteView.as_view(model=MusicianGear),
    ),
    re_path(r"^(?P<pk>\d+)/$", DetailView.as_view(model=MusicianGear)),
    re_path(r"^(?P<id>\d+)/edit_links/?$", EditLinksView.as_view()),
    re_path(r"^(?P<id>\d+)/edit_photos/?$", EditPhotosView.as_view()),
    re_path(r"^(?P<id>\d+)/add_link/$", AddLinkView.as_view()),
    re_path(r"^(?P<id>\d+)/add_photo/$", AddPhotoView.as_view()),
]
