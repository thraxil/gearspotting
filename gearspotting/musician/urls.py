from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gearspotting.musician.models import Musician, MusicianForm
from gearspotting.musician.views import (
    MusicianTagView, TagsView, AddLinkView, AddPhotoView,
    AddGearView, EditLinksView, EditPhotosView, EditGearView)

urlpatterns = [
    url(r'^$', ListView.as_view(model=Musician)),
    url(r'^create/?$', CreateView.as_view(
        form_class=MusicianForm, model=Musician)),
    url(r'^(?P<slug>[^/]+)/update/?$', UpdateView.as_view(
        form_class=MusicianForm, model=Musician)),
    url(r'^(?P<slug>[^/]+)/delete/?$', DeleteView.as_view(model=Musician)),
    url(r'^tag/(?P<tag>[^/]+)/$', MusicianTagView.as_view(),
        name='musician_tag_detail'),
    url(r'^tag/$', TagsView.as_view()),
    url(r'^(?P<slug>[^/]+)/add_link/$', AddLinkView.as_view()),
    url(r'^(?P<slug>[^/]+)/add_photo/$', AddPhotoView.as_view()),
    url(r'^(?P<slug>[^/]+)/add_gear/$', AddGearView.as_view()),
    url(r'^(?P<slug>[^/]+)/edit_links/?$', EditLinksView.as_view()),
    url(r'^(?P<slug>[^/]+)/edit_photos/?$', EditPhotosView.as_view()),
    url(r'^(?P<slug>[^/]+)/edit_gear/?$', EditGearView.as_view()),
    url(r'^(?P<slug>[^/]+)/$', DetailView.as_view(model=Musician)),
]
