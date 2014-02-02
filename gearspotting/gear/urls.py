from django.conf.urls.defaults import patterns, url
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gearspotting.gear.models import Gear
from gearspotting.gear.views import GearTagView

info_dict = {
    'queryset': Gear.objects.all(),
}

urlpatterns = patterns(
    '',
    (r'^$', 'gearspotting.gear.views.index'),
    (r'^create/?$', CreateView.as_view(model=Gear)),
    url(r'^tag/(?P<tag>[^/]+)/$', GearTagView.as_view(),
        name='gear_tag_detail'),
    url(r'^tag/$', 'gearspotting.gear.views.tags'),
    (r'^(?P<slug>[^/]+)/update/?$', UpdateView.as_view(model=Gear)),
    (r'^(?P<slug>[^/]+)/delete/?$', DeleteView.as_view(model=Gear)),
    (r'^(?P<slug>[^/]+)/$', DetailView.as_view(slug_field='slug', model=Gear)),
    (r'^(?P<slug>[^/]+)/edit_links/?$', 'gearspotting.gear.views.edit_links'),
    (r'^(?P<slug>[^/]+)/edit_photos/?$',
     'gearspotting.gear.views.edit_photos'),
    (r'^(?P<slug>[^/]+)/add_link/$', 'gearspotting.gear.views.add_link'),
    (r'^(?P<slug>[^/]+)/add_photo/$', 'gearspotting.gear.views.add_photo'),
)
