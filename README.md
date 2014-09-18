django_NelsonDB
===============
Legacy Branch

Hosted at http://nmorales3142.pythonanywhere.com/

The Legacy application is running directly off of the current NelsonDB table schema. The FKs are being incorporated slowly, but the integrity of the data needs to be cleaned up, before it can be imported. So far the Seed, Seed_Inventory, and Experiment tables are being worked on.

Nick's django front-end for Nelson lab DB

Now running Mysql

To run this:

1. Set up the development environment following these steps http://www.tangowithdjango.com/book/chapters/requirements.html#installing-the-software
2. pip install django-like and pillow. Make sure mine_project/mine_project/settings.py shows the following

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
  	'legacy',
)

3. In the command line, cd to the project directory and enter "python manage.py syncdb"
4. To populate the database, edit populate_experiment.py to reflect the location of person.csv, experiment.csv, and seed.csv on your computer. Enter in the command line "python populate_experiment.py" to populate the experiment and people tables, as well as to populate the seed inventory with what is available. 
5. Type "python manage.py runserver" 

This project is modeled after the tango_with_django project, where there are separate "applications" in the overall project.
Currently there are two applications, one called "mine" and can be found at mine_project/mine, the other called "legacy" can be found at mine_project/legacy.
The overall project is found at mine_project/mine_project.

This project is running the django "media server" to store images locally, which means the python library "pillow" must be pip installed.

A simple guide to django is this: 
URL (mine/urls.py) -> View (mine/views.py) -> Template (templates/mine/example.html)
AJAX is essentailly: Jquery script, mapped to HTML id -> URL -> View -> Template


MySQL:
I am using XAMPP to run a mysql database. I like XAMPP because it uses phpMyadmin to interface the database directly. 
To populate the legacy database, use the sql code in the legacy_data folder.
To populate the new database, use the populate_experiment.py script.
Note, both the new and old database are running on the same Mysql database. 
