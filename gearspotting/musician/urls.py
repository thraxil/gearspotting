from django.conf.urls.defaults import patterns, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gearspotting.musician.models import Musician, MusicianForm
from gearspotting.musician.views import (
    MusicianTagView, TagsView)

urlpatterns = patterns(
    '',
    (r'^$', ListView.as_view(model=Musician)),
    (r'^create/?$',
     CreateView.as_view(
         form_class=MusicianForm, model=Musician)),
    (r'^(?P<slug>[^/]+)/update/?$',
     UpdateView.as_view(
         form_class=MusicianForm, model=Musician)),
    (r'^(?P<slug>[^/]+)/delete/?$', DeleteView.as_view(model=Musician)),
    url(r'^tag/(?P<tag>[^/]+)/$', MusicianTagView.as_view(),
        name='musician_tag_detail'),
    url(r'^tag/$', TagsView.as_view()),
    (r'^(?P<slug>[^/]+)/edit_links/?$',
     'gearspotting.musician.views.edit_links'),
    (r'^(?P<slug>[^/]+)/add_link/$', 'gearspotting.musician.views.add_link'),
    (r'^(?P<slug>[^/]+)/add_photo/$', 'gearspotting.musician.views.add_photo'),
    (r'^(?P<slug>[^/]+)/add_gear/$', 'gearspotting.musician.views.add_gear'),
    (r'^(?P<slug>[^/]+)/edit_photos/?$',
     'gearspotting.musician.views.edit_photos'),
    (r'^(?P<slug>[^/]+)/edit_gear/?$',
     'gearspotting.musician.views.edit_gear'),
    (r'^(?P<slug>[^/]+)/$', DetailView.as_view(model=Musician)),
)
