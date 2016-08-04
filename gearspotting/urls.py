import django.views.static
import django.contrib.sitemaps.views

from django.conf.urls import include, url
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

urlpatterns = [
    url(r'^$', mainviews.IndexView.as_view()),
    url(r'smoketest/', include('smoketest.urls')),
    url(r'^tag/$', mainviews.TagsView.as_view()),
    url(r'^search/$', mainviews.SearchView.as_view()),
    url(r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gear/', include('gearspotting.gear.urls')),
    url(r'^blog/', include('gearspotting.blog.urls')),
    url(r'^musician/', include('gearspotting.musician.urls')),
    url(r'^musiciangear/', include('gearspotting.musiciangear.urls')),
    url(r'^manufacturer/', include('gearspotting.manufacturer.urls')),
    url(r'^photos/', include('gearspotting.photo.urls')),
    url(r'^feeds/gear/$', GearFeed()),
    url(r'^feeds/musician/$', MusicianFeed()),
    url(r'^feeds/blog/$', BlogFeed()),
    url(r'^sitemap\.xml$', django.contrib.sitemaps.views.sitemap,
        {'sitemaps': sitemaps}),
    url(r'^uploads/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}),
]
