import django.views.static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path

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
    re_path(r"^$", mainviews.IndexView.as_view()),
    re_path(r"smoketest/", include("smoketest.urls")),
    re_path(r"^search/$", mainviews.SearchView.as_view()),
    re_path(r"^gear/", include("gearspotting.gear.urls")),
    re_path(r"^blog/", include("gearspotting.blog.urls")),
    re_path(r"^musician/", include("gearspotting.musician.urls")),
    re_path(r"^musiciangear/", include("gearspotting.musiciangear.urls")),
    re_path(r"^manufacturer/", include("gearspotting.manufacturer.urls")),
    re_path(r"^photos/", include("gearspotting.photo.urls")),
    re_path(r"^feeds/gear/$", GearFeed()),
    re_path(r"^feeds/musician/$", MusicianFeed()),
    re_path(r"^feeds/blog/$", BlogFeed()),
    re_path(
        r"^uploads/(?P<path>.*)$",
        django.views.static.serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
    path("__debug__/", include("debug_toolbar.urls")),
]
