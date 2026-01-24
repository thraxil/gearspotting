from django.urls import re_path
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.musiciangear.models import MusicianGear
from gearspotting.musiciangear.views import (
    AddLinkView,
    AddPhotoView,
    EditLinksView,
    EditPhotosView,
)

urlpatterns = [
    re_path(r"^$", ListView.as_view(model=MusicianGear)),
    re_path(r"^create/?$", CreateView.as_view(model=MusicianGear, fields=["musician", "gear", "description"])),
    re_path(
        r"^(?P<pk>\d+)/update/?$",
        UpdateView.as_view(model=MusicianGear, fields=["musician", "gear", "description"]),
    ),
    re_path(
        r"^(?P<pk>\d+)/delete/?$",
        DeleteView.as_view(model=MusicianGear, success_url="/musiciangear/"),
    ),
    re_path(r"^(?P<pk>\d+)/$", DetailView.as_view(model=MusicianGear)),
    re_path(r"^(?P<pk>\d+)/edit_links/?$", EditLinksView.as_view()),
    re_path(r"^(?P<pk>\d+)/edit_photos/?$", EditPhotosView.as_view()),
    re_path(r"^(?P<pk>\d+)/add_link/$", AddLinkView.as_view()),
    re_path(r"^(?P<pk>\d+)/add_photo/$", AddPhotoView.as_view()),
]
