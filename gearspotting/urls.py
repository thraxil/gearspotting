from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import os.path
from django.views.generic.simple import direct_to_template
admin.autodiscover()
import staticmedia

from gearspotting.gear.feeds import GearFeed
from gearspotting.musician.feeds import MusicianFeed

site_media_root = os.path.join(os.path.dirname(__file__), "../media")

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
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) + staticmedia.serve()

