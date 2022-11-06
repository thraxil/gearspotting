# flake8: noqa
from .settings_shared import *
from thraxilsettings.docker import common
import os
import os.path

app = 'gearspotting'
base = os.path.dirname(__file__)

locals().update(
    common(
        app=app,
        base=base,
        celery=False,
        INSTALLED_APPS=INSTALLED_APPS,
        STATIC_ROOT=STATIC_ROOT,
        MIDDLEWARE=MIDDLEWARE,
    ))
COMPRESS_OFFLINE_MANIFEST_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
