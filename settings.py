# -*- coding: utf8 -*-
# Django settings for fuit project.

import os
import socket

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mikhail Baranov', 'mikhailb@avalon.ru'),
    # ('Your Name', 'your_email@example.com'),
)

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',     # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, 'data.db'),                          # Or path to database file if using sqlite3.
        'USER': '',                                 # Not used with sqlite3.
        'PASSWORD': '',                             # Not used sqlite3with sqlite3.
        'HOST': '',                                 # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                 # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'uploads')

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

if socket.gethostname() == 'fuit.avalon.ru':
    STATIC_URL = "http://s.fuit.avalon.ru/"
    MEDIA_URL = '/static/'
else:
    STATIC_URL = "/static/"
    MEDIA_URL = '/media/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
   #'/home/vita/projects/fuit/uploads/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l=-*8i$2%$am!j&vr*v(%)%pg@kzol2v68=9)+9a2+utwx$25a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",

    "django.core.context_processors.media",
    "django.core.context_processors.static",
    'django.core.context_processors.debug',

    'django.core.context_processors.request',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filebrowser',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.flatpages',

    'www',
    'news',
    'pages',
    'schedule',
    'process',
    'scientific',
    'staff',
    'profburo',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Grappelli

GRAPPELLI_ADMIN_TITLE = "ФУИТ СПбГПУ. Управление сайтом"

# TinyMCE Settings
TINYMCE_JS_URL = STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/'
TINYMCE_SETUP = STATIC_URL + 'grappelli/tinymce_setup/tinymce_setup.js'

TINYMCE_FILEBROWSER = True
TINYMCE_DEFAULT_CONFIG = {
    #'mode' : "textareas",
    'theme': "simple",
    #'theme_advanced_toolbar_location' : "top",
    #'theme_advanced_resizing' : True,
    'extended_valid_elements': "article[name|href|target|title|onclick],section",
}


# Filebrowser Settings
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_URL_TINYMCE = TINYMCE_JS_ROOT
