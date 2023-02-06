from django.urls import re_path
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.musician.models import Musician, MusicianForm
from gearspotting.musician.views import (AddGearView, AddLinkView,
                                         AddPhotoView, EditGearView,
                                         EditLinksView, EditPhotosView,
                                         MusicianTagView, TagsView)

urlpatterns = [
    re_path(r"^$", ListView.as_view(model=Musician)),
    re_path(
        r"^create/?$",
        CreateView.as_view(form_class=MusicianForm, model=Musician),
    ),
    re_path(
        r"^(?P<slug>[^/]+)/update/?$",
        UpdateView.as_view(form_class=MusicianForm, model=Musician),
    ),
    re_path(r"^(?P<slug>[^/]+)/delete/?$", DeleteView.as_view(model=Musician)),
    re_path(
        r"^tag/(?P<tag>[^/]+)/$",
        MusicianTagView.as_view(),
        name="musician_tag_detail",
    ),
    re_path(r"^tag/$", TagsView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/add_link/$", AddLinkView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/add_photo/$", AddPhotoView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/add_gear/$", AddGearView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/edit_links/?$", EditLinksView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/edit_photos/?$", EditPhotosView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/edit_gear/?$", EditGearView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/$", DetailView.as_view(model=Musician)),
]
