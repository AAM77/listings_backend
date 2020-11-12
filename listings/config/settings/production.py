from .base import *

STATIC_ROOT = APPS_DIR / 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(APPS_DIR, 'static')
)