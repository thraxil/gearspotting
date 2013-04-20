from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
import os.path
from django.views.generic.simple import direct_to_template
admin.autodiscover()
import staticmedia

from gearspotting.gear.feeds import GearFeed
from gearspotting.musician.feeds import MusicianFeed
from gearspotting.gear.models import Gear
from gearspotting.musician.models import Musician
from gearspotting.musiciangear.models import MusicianGear
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.photo.models import Photo

site_media_root = os.path.join(os.path.dirname(__file__), "../media")

gear_info_dict = {
    'queryset': Gear.objects.all(),
    'date_field': 'modified',
}
musician_info_dict = {
    'queryset': Musician.objects.all(),
    'date_field': 'modified',
}
musiciangear_info_dict = {
    'queryset': MusicianGear.objects.all(),
    'date_field': 'modified',
}
manufacturer_info_dict = {
    'queryset': Manufacturer.objects.all(),
    'date_field': 'modified',
}
photo_info_dict = {
    'queryset': Photo.objects.all(),
    'date_field': 'modified',
}

sitemaps = {
    'gear': GenericSitemap(gear_info_dict, priority=0.6),
    'musicians': GenericSitemap(musician_info_dict, priority=0.6),
    'musiciangears': GenericSitemap(musiciangear_info_dict, priority=0.6),
    'manufacturers': GenericSitemap(manufacturer_info_dict, priority=0.6),
    'photos': GenericSitemap(photo_info_dict, priority=0.6),
}

urlpatterns = patterns(
    '',
    (r'^$', 'gearspotting.main.views.index'),
    (r'^tag/$', 'gearspotting.main.views.tags'),
    (r'^search/$', 'gearspotting.main.views.search'),
    (r'^accounts/', include('userena.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^munin/',include('munin.urls')),
    (r'^gear/',include('gearspotting.gear.urls')),
    (r'^musician/',include('gearspotting.musician.urls')),
    (r'^musiciangear/',include('gearspotting.musiciangear.urls')),
    (r'^manufacturer/',include('gearspotting.manufacturer.urls')),
    (r'^photos/',include('gearspotting.photo.urls')),
    (r'^feeds/gear/$', GearFeed()),
    (r'^feeds/musician/$', MusicianFeed()),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) + staticmedia.serve()

