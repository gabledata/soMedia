import os
from django.core.wsgi import get_wsgi_application as A
os.environ.setdefault('DJANGO_SETTINGS_MODULE','soMedia.settings')
B=A()