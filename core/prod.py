from .base import *
from .database_gen import database_config
import dj_database_url  

DEBUG = False
ALLOWED_HOSTS = ["96.30.199.51"]
ENV = "PROD"

DATABASES = database_config(ENV)

db_from_env = dj_database_url.config(conn_max_age=500)  
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (  
    os.path.join(BASE_DIR, 'static'),
)