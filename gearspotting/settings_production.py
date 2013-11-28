# flake8: noqa
from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/gearspotting/gearspotting/gearspotting/templates",
)

MEDIA_ROOT = '/var/www/gearspotting/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/gearspotting/gearspotting/sitemedia'),
)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATICFILES_DIRS = ()
STATIC_ROOT = "/var/www/gearspotting/gearspotting/media/"

try:
    from local_settings import *
except ImportError:
    pass
