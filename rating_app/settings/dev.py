from .base import *  # noqa

from rating_app.env import env

DEBUG = env.bool('DJANGO_DEBUG', default=False)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost'])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST', default=[])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rate_app',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
        "OPTIONS": {
            "pool": True,
        },
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
