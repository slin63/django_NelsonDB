django_NelsonDB
===============

Nick's django front-end for Nelson lab DB

You need to ensure these are installed and included: 
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
	'django_like',
	'mine',
	'registration',
)

This project is modeled after the tango_with_django project, where there are separate "applications" in the overall project.
Currently there is only one application, called "mine" and can be found at mine_project/mine.
The overall project is found at mine_project/mine_project.

This project is running the django "media server" to store images locally, which means the python library "pillow" must be pip installed.

A simple guide to django is this: URL -> View -> Template 
AJAX is essentailly: Jquery script -> URL -> View -> Template

