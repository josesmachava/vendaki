# Please copy this as a settings_local.py on the same directory and ensure to not add to version control, i.e. git ignore this file. Adjust the variables to meet your own settings
#To automate Local and Production server settings
import socket
import  os

hostname = socket.gethostname()
if socket.gethostname() == hostname:	#ensure your local machine hostname is used
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'eskina',
    #         'USER': 'josesmachava',
    #         'PASSWORD': '849394995Jose',
    #         'HOST': 'localhost',
    #         'PORT': '',
    #
    #     }
    # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'sqlite3.db',  # Or path to database file if using sqlite3.
            'USER': '',  # Not used with sqlite3.
            'PASSWORD': '',  # Not used with sqlite3.
            'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',  # Set to empty string for default. Not used with sqlite3.
        }
    }
SECURE_SSL_REDIRECT = False
DEBUG=True
DEBUG_PROPAGATE_EXCEPTIONS = True
WHITENOISE_AUTOREFRESH = False