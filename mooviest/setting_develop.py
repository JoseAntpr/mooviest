from settings import *

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mooviest',
        'USER': 'root',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#Logs all SQL queries in debug
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        }
    },
    'loggers':{
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
