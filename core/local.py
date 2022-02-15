from .base import *
import django_heroku
from .database_gen import database_config

DEBUG = True
ALLOWED_HOSTS = ['*']
ENV = "DEV"

DATABASES = database_config(ENV)

__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'

STATICFILES_DIRS = (  
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(__STATIC_PATH, '../static/')

django_heroku.settings(locals())