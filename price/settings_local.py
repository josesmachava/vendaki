# Please copy this as a settings_local.py on the same directory and ensure to not add to version control, i.e. git ignore this file. Adjust the variables to meet your own settings
#To automate Local and Production server settings
import socket
import  os


if socket.gethostname() == 'josemachava':	#ensure your local machine hostname is used
    DEBUG = False
    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'eskina',
            'USER': 'josesmachava',
            'PASSWORD': '849394995Jose',
            'HOST': 'localhost',
            'PORT': '',

        }
    }

SECURE_SSL_REDIRECT = False

DEBUG_PROPAGATE_EXCEPTIONS = True
WHITENOISE_AUTOREFRESH = False