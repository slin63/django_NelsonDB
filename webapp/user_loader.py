import os
import csv

#---------------------------------------------------
# Adds users to User and UserProfile models. Also sets password to 123123 for all users
#---------------------------------------------------

def csv_import_people():
    ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/person.csv'), dialect='excel')
    for row in ifile:
      user = row["user"]
      email = row["email"]
      first_name = row["first_name"]
      last_name = row["last_name"]
      phone = row["phone"]
      location = row["location"]
      title = row["title"]
      notes_file = row["notes"]
      web = row["web"]

      #--- Complete Comment ---
      if location != 'NULL' and location != '' and notes_file != 'NULL' and notes_file != '':
        notes = "%s || %s" % (location, notes_file)
      #--- No Location ---
      elif notes_file != 'NULL' and notes_file != '':
        notes = "%s" % (notes_file)
      #--- No Notes ---
      elif location != 'NULL' and location != '':
        notes = "%s" % (location)
      else:
        notes = 'No Notes'

      add_user(user, email, first_name, last_name)
      add_userpass(user)
      add_userp(user, phone, location, 'profile_images/underwater.jpg', title, web, notes)

def add_user(username, email, fname, lname):
  u = User.objects.get_or_create(username=username, email=email, first_name=fname, last_name=lname)[0]
  print(u)

def add_userpass(user):
  pa = User.objects.get(username = user)
  pa.set_password('123123')
  pa.save()

def add_userp(user, phone, org, pic, title, web, notes):
  p = UserProfile.objects.get_or_create(user=User.objects.get(username=user), phone=phone, organization=org, picture=pic, job_title=title, website=web, notes=notes)[0]

#-------------------------------------------------------------------------
# Start execution here!
#-------------------------------------------------------------------------

if __name__ == '__main__':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
  import django
  django.setup()
  from lab.models import User, UserProfile
  csv_import_people()
