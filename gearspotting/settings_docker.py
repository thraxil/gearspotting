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
        celery=True,
        INSTALLED_APPS=INSTALLED_APPS,
        STATIC_ROOT=STATIC_ROOT,
        MIDDLEWARE=MIDDLEWARE,
    ))
