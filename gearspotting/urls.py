from django.conf.urls import patterns, include
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from gearspotting.gear.feeds import GearFeed
from gearspotting.musician.feeds import MusicianFeed
from gearspotting.blog.feeds import BlogFeed
from gearspotting.gear.models import Gear
from gearspotting.musician.models import Musician
from gearspotting.musiciangear.models import MusicianGear
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.photo.models import Photo
from gearspotting.blog.models import Post

import gearspotting.main.views as mainviews

admin.autodiscover()

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
post_info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'modified',
}

sitemaps = {
    'gear': GenericSitemap(gear_info_dict, priority=0.6),
    'musicians': GenericSitemap(musician_info_dict, priority=0.6),
    'musiciangears': GenericSitemap(musiciangear_info_dict, priority=0.6),
    'manufacturers': GenericSitemap(manufacturer_info_dict, priority=0.6),
    'photos': GenericSitemap(photo_info_dict, priority=0.6),
    'posts': GenericSitemap(post_info_dict, priority=0.6),
}

urlpatterns = patterns(
    '',
    (r'^$', mainviews.IndexView.as_view()),
    (r'smoketest/', include('smoketest.urls')),
    (r'^tag/$', mainviews.TagsView.as_view()),
    (r'^search/$', mainviews.SearchView.as_view()),
    (r'^accounts/', include('userena.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^gear/', include('gearspotting.gear.urls')),
    (r'^blog/', include('gearspotting.blog.urls')),
    (r'^musician/', include('gearspotting.musician.urls')),
    (r'^musiciangear/', include('gearspotting.musiciangear.urls')),
    (r'^manufacturer/', include('gearspotting.manufacturer.urls')),
    (r'^photos/', include('gearspotting.photo.urls')),
    (r'^feeds/gear/$', GearFeed()),
    (r'^feeds/musician/$', MusicianFeed()),
    (r'^feeds/blog/$', BlogFeed()),
    (r'^sitemap\.xml$',
     'django.contrib.sitemaps.views.sitemap',
     {'sitemaps': sitemaps}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
