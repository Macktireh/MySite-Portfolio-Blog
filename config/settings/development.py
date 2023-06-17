from .base import *


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    
    # 'PostgreSQL': {
    #     'ENGINE': env("ENGINE"),
    #     'NAME': env("POSTGRES_DB"),
    #     'USER': env("POSTGRES_USER"),
    #     'PASSWORD': env("POSTGRES_PASSWORD"),
    #     'HOST': env("POSTGRES_HOST"),
    #     'PORT': env("POSTGRES_PORT"),
    # }, 
}