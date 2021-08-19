from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "baseball_v3",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": "5432",
    }
}

ALLOWED_HOSTS = ["baseball.timmartin.dev", "www.baseball.timmartin.dev"]

CORS_ALLOWED_ORIGINS = ["baseball.timmartin.dev", "www.baseball.timmartin.dev"]