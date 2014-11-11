django_NelsonDB
===============

Django front-end for Nelson lab DB

Now running Mysql

To run this:

1. Set up the development environment following these steps http://www.tangowithdjango.com/book/chapters/requirements.html#installing-the-software
2. pip install -r requirements.txt
3. In the command line, cd to the project directory and enter "python manage.py syncdb"
4. To populate the legacy database tables, use the sql code in the legacy_data folder
4. To populate the lab database tables, use the script populate.py
5. Type "python manage.py runserver" 
