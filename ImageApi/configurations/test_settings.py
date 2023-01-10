import tempfile

from ImageApi.settings import *
from django.core.management import call_command
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ImageApi.settings")
DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'my_database.sql3',
    }
}

DEBUG = False
TEMPLATE_DEBUG = False

django.setup()
call_command('migrate')
