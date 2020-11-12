from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise

from .base import *


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
