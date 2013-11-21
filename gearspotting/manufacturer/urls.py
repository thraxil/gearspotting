from django.conf.urls.defaults import patterns
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm

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
     'gearspotting.manufacturer.views.edit_links'),
    (r'^(?P<slug>[^/]+)/add_gear/$',
     'gearspotting.manufacturer.views.add_gear'),
    (r'^(?P<slug>[^/]+)/$',
     DetailView.as_view(model=Manufacturer)),
    (r'^(?P<slug>[^/]+)/add_link/$',
     'gearspotting.manufacturer.views.add_link'),
)
