from base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app_boilerplate',
        'USER': 'app_boilerplate',
        'HOST': 'localhost',
        'PASSWORD': 'secret',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB;'
        }
    }
}

INTERNAL_IPS = (
    '127.0.0.1',
)
