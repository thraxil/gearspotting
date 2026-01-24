# Django settings for gearspotting project.
import os.path
import sys
from pathlib import Path

base = Path(__file__).resolve().parent.parent
app = "gearspotting"

DEBUG = True

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": app,
        "HOST": "",
        "PORT": 5432,
        "USER": "",
        "PASSWORD": "",
        "ATOMIC_REQUESTS": True,
    }
}

if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
            "HOST": "",
            "PORT": "",
            "USER": "",
            "PASSWORD": "",
            "ATOMIC_REQUESTS": True,
        }
    }
    PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

TEST_RUNNER = "django.test.runner.DiscoverRunner"

ALLOWED_HOSTS = ["localhost", ".gearspotting.ccom", "127.0.0.1"]
USE_TZ = True
TIME_ZONE = "America/New_York"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = "/var/www/" + app + "/uploads/"
MEDIA_URL = "/uploads/"
SECRET_KEY = "you must override this"  # nosec
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(base, "gearspotting/templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]
MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = app + ".urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "debug_toolbar",
    "smoketest",
    "gunicorn",
    "gearspotting.main",
    "gearspotting.musician",
    "gearspotting.gear",
    "gearspotting.photo",
    "gearspotting.link",
    "gearspotting.manufacturer",
    "gearspotting.musiciangear",
    "bootstrapform",
    "gearspotting.profile",
    "gearspotting.blog",
    "gearspotting.tag",
]

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(base, "static"),
]
STATIC_ROOT = os.path.join(base, "staticfiles")
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

INTERNAL_IPS = ["127.0.0.1"]
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

THUMBNAIL_SUBDIR = "thumbs"
EMAIL_SUBJECT_PREFIX = "[" + app + "] "
EMAIL_HOST = "localhost"
SERVER_EMAIL = app + "@thraxil.org"
DEFAULT_FROM_EMAIL = SERVER_EMAIL


SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 265 * 5

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
}

RETICULUM_BASE = "https://reticulum.thraxil.org/"
RETICULUM_PUBLIC_BASE = "https://d2f33fmhbh7cs9.cloudfront.net/"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
