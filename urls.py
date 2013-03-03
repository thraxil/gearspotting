from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import os.path
from django.views.generic.simple import direct_to_template
admin.autodiscover()
import staticmedia

from gearspotting.gear.feeds import GearFeed
from gearspotting.musician.feeds import MusicianFeed

site_media_root = os.path.join(os.path.dirname(__file__), "media")

urlpatterns = patterns(
    '',
    (r'^$', 'main.views.index'),
    (r'^tag/$', 'main.views.tags'),
    (r'^search/$', 'main.views.search'),
    (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^munin/',include('munin.urls')),
    (r'^gear/',include('gear.urls')),
    (r'^musician/',include('musician.urls')),
    (r'^musiciangear/',include('musiciangear.urls')),
    (r'^manufacturer/',include('manufacturer.urls')),
    (r'^photos/',include('photo.urls')),
    (r'^feeds/gear/$', GearFeed()),
    (r'^feeds/musician/$', MusicianFeed()),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) + staticmedia.serve()

