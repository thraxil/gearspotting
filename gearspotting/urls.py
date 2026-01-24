import django.views.static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import gearspotting.main.views as mainviews
from gearspotting.blog.feeds import BlogFeed
from gearspotting.blog.models import Post
from gearspotting.gear.feeds import GearFeed
from gearspotting.gear.models import Gear
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.musician.feeds import MusicianFeed
from gearspotting.musician.models import Musician
from gearspotting.musiciangear.models import MusicianGear
from gearspotting.photo.models import Photo

admin.autodiscover()

gear_info_dict = {
    "queryset": Gear.objects.all(),
    "date_field": "modified",
}
musician_info_dict = {
    "queryset": Musician.objects.all(),
    "date_field": "modified",
}
musiciangear_info_dict = {
    "queryset": MusicianGear.objects.all(),
    "date_field": "modified",
}
manufacturer_info_dict = {
    "queryset": Manufacturer.objects.all(),
    "date_field": "modified",
}
photo_info_dict = {
    "queryset": Photo.objects.all(),
    "date_field": "modified",
}
post_info_dict = {
    "queryset": Post.objects.all(),
    "date_field": "modified",
}

urlpatterns = [
    path("", mainviews.IndexView.as_view(), name="index"),
    path("smoketest/", include("smoketest.urls")),
    path("search/", mainviews.SearchView.as_view(), name="search"),
    path("gear/", include("gearspotting.gear.urls", namespace="gear")),
    path("blog/", include("gearspotting.blog.urls", namespace="blog")),
    path(
        "musician/",
        include("gearspotting.musician.urls", namespace="musician"),
    ),
    path(
        "musiciangear/",
        include("gearspotting.musiciangear.urls", namespace="musiciangear"),
    ),
    path(
        "manufacturer/",
        include("gearspotting.manufacturer.urls", namespace="manufacturer"),
    ),
    path("photos/", include("gearspotting.photo.urls", namespace="photo")),
    path("feeds/gear/", GearFeed(), name="gear_feed"),
    path("feeds/musician/", MusicianFeed(), name="musician_feed"),
    path("feeds/blog/", BlogFeed(), name="blog_feed"),
    path(
        "uploads/<path:path>/",
        django.views.static.serve,
        {"document_root": settings.MEDIA_ROOT},
        name="uploads",
    ),
    path("__debug__/", include("debug_toolbar.urls")),
]
