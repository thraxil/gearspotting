from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.musiciangear.models import MusicianGear
from gearspotting.musiciangear.views import (AddLinkView, AddPhotoView,
                                             EditLinksView, EditPhotosView)

urlpatterns = [
    url(r"^$", ListView.as_view(model=MusicianGear)),
    url(r"^create/?$", CreateView.as_view(model=MusicianGear)),
    url(
        r"^(?P<object_id>\d+)/update/?$",
        UpdateView.as_view(model=MusicianGear),
    ),
    url(
        r"^(?P<object_id>\d+)/delete/?$",
        DeleteView.as_view(model=MusicianGear),
    ),
    url(r"^(?P<pk>\d+)/$", DetailView.as_view(model=MusicianGear)),
    url(r"^(?P<id>\d+)/edit_links/?$", EditLinksView.as_view()),
    url(r"^(?P<id>\d+)/edit_photos/?$", EditPhotosView.as_view()),
    url(r"^(?P<id>\d+)/add_link/$", AddLinkView.as_view()),
    url(r"^(?P<id>\d+)/add_photo/$", AddPhotoView.as_view()),
]
