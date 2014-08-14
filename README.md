django_NelsonDB
===============
Seed_inventory_revamp Branch

Nick's django front-end for Nelson lab DB

To run this:

1. Set up the development environment following these steps http://www.tangowithdjango.com/book/chapters/requirements.html#installing-the-software
2. pip install django-like, registration and pillow. Make sure mine_project/mine_project/settings.py shows the following

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

3. In the command line, cd to the project directory and enter "python manage.py syncdb"
4. To populate the database, edit populate_experiment.py to reflect the location of person.csv, experiment.csv, and seed.csv on your computer. Enter in the command line "python populate_experiment.py" to populate the experiment and people tables, as well as to populate the seed inventory with what is available. 
5. Type "python manage.py runserver" 

This project is modeled after the tango_with_django project, where there are separate "applications" in the overall project.
Currently there is only one application, called "mine" and can be found at mine_project/mine.
The overall project is found at mine_project/mine_project.

This project is running the django "media server" to store images locally, which means the python library "pillow" must be pip installed.

A simple guide to django is this: 
URL (mine/urls.py) -> View (mine/views.py) -> Template (templates/mine/example.html)
AJAX is essentailly: Jquery script, mapped to HTML id -> URL -> View -> Template
