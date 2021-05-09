from django.conf import settings
from .base import *

DEBUG = True

ALLOWED_HOST = []

DATABASES = {
    'default': {
        'ENGINE': settings.ENGINE,
        'NAME': settings.NAME,
        'USER': settings.USER,
        'PASSWORD': settings.PASSWORD,
        'HOST': settings.HOST,
        'PORT': settings.PORT,
    }
}

STATIC_URL = '/static/'




