from django.conf.urls.defaults import patterns
from gearspotting.musiciangear.models import MusicianGear
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


urlpatterns = patterns(
    '',
    (r'^$', ListView.as_view(model=MusicianGear)),
    (r'^create/?$', CreateView.as_view(model=MusicianGear)),
    (r'^(?P<object_id>\d+)/update/?$', UpdateView.as_view(model=MusicianGear)),
    (r'^(?P<object_id>\d+)/delete/?$', DeleteView.as_view(model=MusicianGear)),
    (r'^(?P<pk>\d+)/$', DetailView.as_view(model=MusicianGear)),
    (r'^(?P<id>\d+)/edit_links/?$',
     'gearspotting.musiciangear.views.edit_links'),
    (r'^(?P<id>\d+)/edit_photos/?$',
     'gearspotting.musiciangear.views.edit_photos'),
    (r'^(?P<id>\d+)/add_link/$',
     'gearspotting.musiciangear.views.add_link'),
    (r'^(?P<id>\d+)/add_photo/$',
     'gearspotting.musiciangear.views.add_photo'),
)
