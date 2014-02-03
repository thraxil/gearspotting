from django.conf.urls.defaults import patterns
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm
from gearspotting.manufacturer.views import (
    AddLinkView, AddGearView, EditLinksView)


urlpatterns = patterns(
    '',
    (r'^$', ListView.as_view(model=Manufacturer)),
    (r'^create/?$',
     CreateView.as_view(
         model=Manufacturer,
         form_class=ManufacturerForm)),
    (r'^(?P<slug>[^/]+)/update/?$',
     UpdateView.as_view(
         model=Manufacturer,
         form_class=ManufacturerForm)),
    (r'^(?P<slug>[^/]+)/delete/?$',
     DeleteView.as_view(model=Manufacturer)),
    (r'^(?P<slug>[^/]+)/edit_links/?$',
     EditLinksView.as_view()),
    (r'^(?P<slug>[^/]+)/add_gear/$',
     AddGearView.as_view()),
    (r'^(?P<slug>[^/]+)/$',
     DetailView.as_view(model=Manufacturer)),
    (r'^(?P<slug>[^/]+)/add_link/$',
     AddLinkView.as_view()),
)
