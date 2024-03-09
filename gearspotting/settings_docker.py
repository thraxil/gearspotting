# flake8: noqa
import os
import os.path
import sys

from .settings_shared import *  # isort:skip

app = "gearspotting"
base = os.path.dirname(__file__)
celery = False

# required settings:
SECRET_KEY = os.environ["SECRET_KEY"]
CELERY_BROKER_URL = None
if celery:
    CELERY_BROKER_URL = os.environ["BROKER_URL"]

# optional/defaulted settings
DB_NAME = os.environ.get("DB_NAME", app)
DB_HOST = os.environ.get(
    "DB_HOST", os.environ.get("POSTGRESQL_PORT_5432_TCP_ADDR", "")
)
DB_PORT = int(
    os.environ.get(
        "DB_PORT", os.environ.get("POSTGRESQL_PORT_54342_TCP_PORT", 5432)
    )
)
DB_USER = os.environ.get("DB_USER", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY", "")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY", "")
AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = AWS_SECRET_KEY
AWS_DEFAULT_ACL = "public-read"

if "ALLOWED_HOSTS" in os.environ:
    ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")

TIME_ZONE = os.environ.get("TIME_ZONE", "America/New_York")

EMAIL_HOST = os.environ.get(
    "EMAIL_HOST", os.environ.get("POSTFIX_PORT_25_TCP_ADDR", "localhost")
)
EMAIL_PORT = os.environ.get(
    "EMAIL_PORT", os.environ.get("POSTFIX_PORT_25_TCP_PORT", 25)
)

SERVER_EMAIL = os.environ.get("SERVER_EMAIL", app + "@thraxil.org")

# -------------------------------------------

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DB_NAME,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
    }
}

if AWS_S3_CUSTOM_DOMAIN:
    AWS_PRELOAD_METADATA = True
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    S3_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    # static data, e.g. css, js, etc.
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATIC_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
}

RAVEN_DSN = os.environ.get("RAVEN_DSN", None)

if RAVEN_DSN:
    INSTALLED_APPS += [
        "raven.contrib.django.raven_compat",
    ]
    RAVEN_CONFIG = {
        "dsn": RAVEN_DSN,
    }
