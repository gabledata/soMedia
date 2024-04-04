A=ImportError
import os
import sys
if __name__=='__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE','soMedia.settings')
	try:from django.core.management import execute_from_command_line as B
	except A as C:raise A("Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?")from C
	B(sys.argv)