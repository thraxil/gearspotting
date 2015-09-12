# Django settings for gearspotting project.
import os.path
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gearspotting',
        'HOST': '',
        'PORT': 5432,
        'USER': '',
        'PASSWORD': '',
    }
}

if 'test' in sys.argv or 'harvest' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            'HOST': '',
            'PORT': '',
            'USER': '',
            'PASSWORD': '', }}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = "/var/www/gearspotting/uploads/"
MEDIA_URL = '/uploads/'
ADMIN_MEDIA_PREFIX = '/media/'
STATIC_URL = "/media/"
SECRET_KEY = 'WHUHGASD%TYJMSAFDS'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django_statsd.middleware.GraphiteRequestTimingMiddleware',
    'django_statsd.middleware.GraphiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'gearspotting.urls'

TEMPLATE_DIRS = (
    "/var/www/gearspotting/gearspotting/templates/",
    os.path.join(os.path.dirname(__file__), "templates"),
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'taggit',
    'gearspotting.main',
    'gearspotting.musician',
    'gearspotting.gear',
    'gearspotting.photo',
    'gearspotting.link',
    'gearspotting.manufacturer',
    'gearspotting.musiciangear',
    'bootstrapform',
    'easy_thumbnails',
    'guardian',
    'userena',
    'gearspotting.profile',
    'django.contrib.sitemaps',
    'gearspotting.blog',
    'django_statsd',
    'gunicorn',
    'taggit_templatetags',
    'django_markwhat',
    'compressor',
    'smoketest',
]

ACCOUNT_ACTIVATION_DAYS = 7

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

THUMBNAIL_SUBDIR = "thumbs"
EMAIL_SUBJECT_PREFIX = "[gearspotting] "
EMAIL_HOST = 'localhost'
SERVER_EMAIL = "gearspotting@ccnmtl.columbia.edu"

# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', 'sitemedia'),
)

STATIC_URL = "/media/"
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../media/")),
)
STATIC_ROOT = ""
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'profile.MyProfile'

USERENA_DEFAULT_PRIVACY = "open"

STATSD_CLIENT = 'statsd.client'
STATSD_PREFIX = 'gearspotting'
STATSD_HOST = '127.0.0.1'
STATSD_PORT = 8125
STATSD_PATCHES = ['django_statsd.patches.db', ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}

ALLOWED_HOSTS = ['localhost', '.gearspotting.com']
RETICULUM_BASE = "http://reticulum.thraxil.org/"
RETICULUM_PUBLIC_BASE = "https://d2f33fmhbh7cs9.cloudfront.net/"
