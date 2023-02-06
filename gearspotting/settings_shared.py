# Django settings for gearspotting project.
import os.path

from thraxilsettings.shared import common

base = os.path.dirname(__file__)
locals().update(common(app="gearspotting", base=base))

# extended common settings

ALLOWED_HOSTS += [".gearspotting.ccom", "127.0.0.1"]  # noqa

INSTALLED_APPS += [  # noqa
    "taggit",
    "gearspotting.main",
    "gearspotting.musician",
    "gearspotting.gear",
    "gearspotting.photo",
    "gearspotting.link",
    "gearspotting.manufacturer",
    "gearspotting.musiciangear",
    "bootstrapform",
    "gearspotting.profile",
    "django.contrib.sitemaps",
    "gearspotting.blog",
]

RETICULUM_BASE = "http://reticulum.thraxil.org/"
RETICULUM_PUBLIC_BASE = "https://d2f33fmhbh7cs9.cloudfront.net/"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
