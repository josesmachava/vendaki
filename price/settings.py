"""
Django settings for price project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o8s*r3ikgpdfdfg5!_0hhn(3&mmxd1_o_htb+2%+u@&c-4-l9n#0c6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']

ROOT_URLCONF = 'price.urls'
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_SANDBOX_MODE_IN_DEBUG=False
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'crispy_bootstrap5',
    's3direct',
    'tinymce',

    'about',
    'account',
    'price',
    'dashboard',
    'store',
    'payment',

]
SITE_ID = 1

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
AUTH_USER_MODEL = 'account.User'

LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = 'signin'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",

]

ROOT_URLCONF = 'price.urls'

GRAPHENE = {
    'SCHEMA': 'price.schema.schema'  # Where your Graphene schema lives
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'price/templates')
        ],

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # PyPugJS part:
            'loaders': [
                ('pypugjs.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
            'builtins': [
                'pypugjs.ext.django.templatetags',
            ],
        },
    },
]

WSGI_APPLICATION = 'price.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config()}
#
try:

    from .settings_local import *

except Exception as e:
    pass
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
CORS_ORIGIN_ALLOW_ALL = True

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-pt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'price', 'static'),
)
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]


# Bucket name
AWS_STORAGE_BUCKET_NAME = 'kutivacontent'

# The region of your bucket, more info:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
AWS_S3_REGION_NAME = 'eu-west-1'

# The endpoint of your bucket, more info:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
AWS_S3_ENDPOINT_URL = 'https://s3.eu-west-1.amazonaws.com'

S3DIRECT_DESTINATIONS = {
    'images': {
        # "key" [required] The location to upload file
        #       1. String: folder path to upload to
        #       2. Function: generate folder path + filename using a function
        'key': 'uploads/images',

        # "auth" [optional] Limit to specfic Django users
        #        Function: ACL function
        'auth': lambda u: u.is_staff,

        # "allowed" [optional] Limit to specific mime types
        #           List: list of mime types
        'allowed': ['image/jpeg', 'image/png', 'video/mp4'],

        # "bucket" [optional] Bucket if different from AWS_STORAGE_BUCKET_NAME
        #          String: bucket name
        # 'bucket': 'custom-bucket',

        # "endpoint" [optional] Endpoint if different from AWS_S3_ENDPOINT_URL
        #            String: endpoint URL
        #  'endpoint': 'custom-endpoint',

        # "region" [optional] Region if different from AWS_S3_REGION_NAME
        #          String: region name
        # 'region': 'custom-region', # Default is 'AWS_S3_REGION_NAME'

        # "acl" [optional] Custom ACL for object, default is 'public-read'
        #       String: ACL
        'acl': 'private',

        # "cache_control" [optional] Custom cache control header
        #                 String: header
        'cache_control': 'max-age=2592000',

        # "content_disposition" [optional] Custom content disposition header
        #                       String: header
        'content_disposition': lambda x: 'attachment; filename="{}"'.format(x),

        # "content_length_range" [optional] Limit file size
        #                        Tuple: (from, to) in bytes
        'content_length_range': (1000, 120000000),

        # "server_side_encryption" [optional] Use serverside encryption
        #                          String: encrytion standard
        'server_side_encryption': 'AES256',

        # "allow_existence_optimization" [optional] Checks to see if file already exists,
        #                                returns the URL to the object if so (no upload)
        #                                Boolean: True, False
        'allow_existence_optimization': False,
    },
    'pdf': {
        # "key" [required] The location to upload file
        #       1. String: folder path to upload to
        #       2. Function: generate folder path + filename using a function
        'key': 'uploads/files',

        # "auth" [optional] Limit to specfic Django users
        #        Function: ACL function
        'auth': lambda u: u.is_staff,

        # "allowed" [optional] Limit to specific mime types
        #           List: list of mime types
        'allowed': ['application/pdf', 'application/zip', 'audio/mpeg'],

        # "bucket" [optional] Bucket if different from AWS_STORAGE_BUCKET_NAME
        #          String: bucket name
        # 'bucket': 'custom-bucket',

        # "endpoint" [optional] Endpoint if different from AWS_S3_ENDPOINT_URL
        #            String: endpoint URL
        #  'endpoint': 'custom-endpoint',

        # "region" [optional] Region if different from AWS_S3_REGION_NAME
        #          String: region name
        # 'region': 'custom-region', # Default is 'AWS_S3_REGION_NAME'

        # "acl" [optional] Custom ACL for object, default is 'public-read'
        #       String: ACL
        'acl': 'private',

        # "cache_control" [optional] Custom cache control header
        #                 String: header
        'cache_control': 'max-age=2592000',

        # "content_disposition" [optional] Custom content disposition header
        #                       String: header
        'content_disposition': lambda x: 'attachment; filename="{}"'.format(x),

        # "content_length_range" [optional] Limit file size
        #                        Tuple: (from, to) in bytes
        'content_length_range': (1, 120000000),

        # "server_side_encryption" [optional] Use serverside encryption
        #                          String: encrytion standard
        'server_side_encryption': 'AES256',

        # "allow_existence_optimization" [optional] Checks to see if file already exists,
        #                                returns the URL to the object if so (no upload)
        #                                Boolean: True, False
        'allow_existence_optimization': False,
    },
    'audio': {
        # "key" [required] The location to upload file
        #       1. String: folder path to upload to
        #       2. Function: generate folder path + filename using a function
        'key': 'uploads/files',

        # "auth" [optional] Limit to specfic Django users
        #        Function: ACL function
        'auth': lambda u: u.is_staff,

        # "allowed" [optional] Limit to specific mime types
        #           List: list of mime types
        'allowed': ['audio/mpeg', 'audio/mp3'],

        # "bucket" [optional] Bucket if different from AWS_STORAGE_BUCKET_NAME
        #          String: bucket name
        # 'bucket': 'custom-bucket',

        # "endpoint" [optional] Endpoint if different from AWS_S3_ENDPOINT_URL
        #            String: endpoint URL
        #  'endpoint': 'custom-endpoint',

        # "region" [optional] Region if different from AWS_S3_REGION_NAME
        #          String: region name
        # 'region': 'custom-region', # Default is 'AWS_S3_REGION_NAME'

        # "acl" [optional] Custom ACL for object, default is 'public-read'
        #       String: ACL
        'acl': 'private',

        # "cache_control" [optional] Custom cache control header
        #                 String: header
        'cache_control': 'max-age=2592000',

        # "content_disposition" [optional] Custom content disposition header
        #                       String: header
        'content_disposition': lambda x: 'attachment; filename="{}"'.format(x),

        # "content_length_range" [optional] Limit file size
        #                        Tuple: (from, to) in bytes
        'content_length_range': (1000, 120000000),

        # "server_side_encryption" [optional] Use serverside encryption
        #                          String: encrytion standard
        'server_side_encryption': 'AES256',

        # "allow_existence_optimization" [optional] Checks to see if file already exists,
        #                                returns the URL to the object if so (no upload)
        #                                Boolean: True, False
        'allow_existence_optimization': False,
    },
    'example_destination_two': {
        'key': lambda filename, args: args + '/' + filename,
        'key_args': 'uploads/images',
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
