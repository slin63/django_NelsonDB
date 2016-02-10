import os
import sys

# root_path should return /path/to/site_directory
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Should lead to site-packages
sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'env/lib/python2.7/site-packages/')))

sys.path.insert(0, os.path.abspath(os.path.join(root_path)))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'webapp')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'webapp.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()