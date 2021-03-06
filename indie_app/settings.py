import os

import cloudinary
import cloudinary.uploader
import cloudinary.api


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
# tweaked settings to prevent Django 1.5 detection in Django 1.7

DEBUG = True

TEMPLATE_DEBUG = DEBUG

# For internal purposes of switching settings components
DEVELOPMENT = True


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

# Empty list to store host allowed
ALLOWED_HOSTS = ['.bubbletime-gum-gum.herokuapp.com']


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "p466i8u&4vig6^t73d-lfminq747wpt=*d#_gtp5+t0nq#^#)n"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
    "pinax_theme_bootstrap.context_processors.theme",
    'indie_app.context_processors.consts',
]


MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "indie_app.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "indie_app.wsgi.application"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",

    # external
    "account",
    "eventlog",
    "metron",
    "south",
    "cloudinary",
    "social.apps.django_app.default",

    # project
    "indie_app",
    "_backend_api",
    "subscription",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'indie_app.log',
            'formatter': 'verbose'
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'product_extend': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

cloudinary.config( 
  cloud_name = "doqjl5owq", 
  api_key = "936571887474212", 
  api_secret = "RMBIzbb7sOzx1LREz7Uj0d22Ms0" 
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


ACCOUNT_OPEN_SIGNUP = True

ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False

ACCOUNT_EMAIL_UNIQUE = True
# ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_USE_AUTH_AUTHENTICATE = True
ACCOUNT_LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2

AUTHENTICATION_BACKENDS = [
    "social.backends.facebook.FacebookOAuth2",
    "social.backends.twitter.TwitterOAuth",
    "account.auth_backends.UsernameAuthenticationBackend",   
]

SOUTH_MIGRATION_MODULES = {
    'default': 'social.apps.django_app.default.south_migrations'
}

SOCIAL_AUTH_PIPELINE = [
    "social.pipeline.social_auth.social_details",
    "social.pipeline.social_auth.social_uid",
    "social.pipeline.social_auth.auth_allowed",
    "social.pipeline.social_auth.social_user",
    "social.pipeline.user.get_username",
    "indie_app.pipeline.prevent_dupes",
    "social.pipeline.user.create_user",
    "social.pipeline.social_auth.associate_user",
    "social.pipeline.social_auth.load_extra_data",
    "social.pipeline.user.user_details"
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
# SOCIAL_AUTH_USER_MODEL = 'indie_app.social.apps.django_app.default.models.CustomUser'
SOCIAL_LOGIN_REDIRECT_URL = '/'


SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'


SOCIAL_AUTH_TWITTER_KEY = os.environ.get("SOCIAL_AUTH_TWITTER_KEY")
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get("SOCIAL_AUTH_TWITTER_SECRET")

SOCIAL_AUTH_FACEBOOK_KEY = '1421811444777881'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b860d27e4724aa93b86c3b4570a82145'
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]

if DEVELOPMENT == True:

    try:
        from heroku_db_config import *
    except ImportError:
        pass
else: 
    try:
        from local_settings import *
    except ImportError:
        pass


