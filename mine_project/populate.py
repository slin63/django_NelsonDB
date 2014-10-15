import os
import csv

#---------------------------------------------------
# Adds users to User and UserProfile models. Also sets password to 123123 for all users
#---------------------------------------------------

def csv_import_people():
    ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/person.csv'), dialect='excel')
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
      notes = "%s || %s" % (location, notes_file)

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

#----------------------------------------------------------
#----------------------------------------------------------

def csv_import_experiment():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/experiments.csv'), dialect='excel')
  for row in ifile:
    experiment_name = row['name']
    experiment_field_locality_city = row['city']
    experiment_field_locality_state = row['state']
    experiment_field_locality_country = row['country']
    experiment_field_name = row['field_name']
    experiment_user_username = row['person']
    experiment_startdate = row['date']
    experiment_purpose = row['desc']
    experiment_comments = "Tissue Collection: %s || Inoculations: %s || Pathogen: %s || Notes: %s" % (row['tissue_collection'], row['inoculations'], row['pathogen'], row['notes'])

    add_locality(experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country)
    add_field(experiment_field_name, experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country)
    add_experiment(experiment_field_name, experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country, experiment_name, experiment_user_username, experiment_startdate, experiment_purpose, experiment_comments)

def add_locality(city, state, country):
  l = Locality.objects.get_or_create(city=city, state=state, country=country)
  print(l)

def add_field(field_name, city, state, country):
  f = Field.objects.get_or_create(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name)
  print(f)

def add_experiment(field_name, city, state, country, experiment_name, username, startdate, purpose, comments):
  e = Experiment.objects.get_or_create(field=Field.objects.get(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name), user=User.objects.get(username=username), name=experiment_name, start_date=startdate, purpose=purpose, comments=comments)
  print(e)

#----------------------------------------------------------
#----------------------------------------------------------

def add_dummies():
  s = Source.objects.get_or_create(source_name='No Source')

def csv_import_row_01():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_row_table_t1.1.csv'), dialect='excel')
  for row in ifile:
    row_row_id = row['row_id']
    row_row_name = row['row_name']
    row_experiment_name = row['experiment_id']
    row_stock_seed_id = row['source_seed_id']
    row_range = row['range']
    row_plot = row['plot']
    row_block = row['block']
    row_rep = row['rep']
    row_stock_passport_taxonomy_population = row['pop']
    row_comments = "Purpose: %s || Notes: %s" % (row['purpose'], row['notes'])
    row_kernel_num = row['kernel_num']
    row_stock_pedigree = row['pedigree']

    seed = Legacy_Seed.objects.get(seed_id=row_stock_seed_id)
    if seed.seed_person_id:
      seed_person_value = Legacy_People.objects.get(person_id = seed.seed_person_id)
      person = seed_person_value.person_name
    else:
      person = 'unknown_person'

    if seed.plant_id_origin:
      try:
        plant = Legacy_Plant.objects.get(plant_id=seed.plant_id_origin)
      except Legacy_Plant.DoesNotExist:
        plant = None

    exp = Legacy_Experiment.objects.get(experiment_id=row_experiment_name)

    try:
      seedinv = Legacy_Seed_Inventory.objects.filter(seed_id=row_stock_seed_id)[0]
    except Legacy_Seed_Inventory.DoesNotExist:
      seedinv = None  

    add_taxonomy(row_stock_passport_taxonomy_population)
    add_obs_selector(row_experiment_name)
    add_collecting(person, exp.harvest_date)
    add_passport(person, exp.harvest_date, row_stock_passport_taxonomy_population)
    add_stock(row_stock_pedigree, seed.seed_id, seed.seed_name, seed.cross_type, seedinv.inventory_date, person, exp.harvest_date, row_stock_passport_taxonomy_population)
    add_row(row_stock_pedigree, seed.seed_id, row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, row_experiment_name, exp.harvest_date, exp.planting_date)
    if seed.plant_id_origin:
      if plant:
        add_obs_selector(row_experiment_name)
        add_plant(row_stock_pedigree, seed.seed_id, row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, row_experiment_name, exp.harvest_date, exp.planting_date, plant.plant_id, plant.plant_name, plant.notes)
    add_location(seedinv.location, seedinv.notes)
    add_stock_packet(seed.seed_id, row_stock_pedigree, seedinv.location, seedinv.notes, seedinv.weight_g)

def add_taxonomy(population):
  t = Taxonomy.objects.get_or_create(genus='Zea', species='Zea mays', population=population, common_name='Maize')
  print(t)

def add_obs_selector(experiment_name):
  o = ObsSelector.objects.create(experiment=Experiment.objects.get(name=experiment_name))
  print(o)

def add_collecting(person, collection_date):
  c = Collecting.objects.get_or_create(obs_selector=ObsSelector.objects.all().order_by("-id")[0], user=User.objects.get(username=person), collection_date=collection_date, collection_method='Manual field harvest. Husks removed and all ears were collected.')
  print(c)

def add_passport(person, collection_date, population):
  p = Passport.objects.get_or_create(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.all().order_by("-id")[0], user=User.objects.get(username=person), collection_date=collection_date),  taxonomy=Taxonomy.objects.get(population=population), source=Source.objects.get(source_name='No Source'))
  print(p)

def add_stock(pedigree, seed_id, seed_name, cross_type, stock_date, person, collection_date, population):
  s = Stock.objects.get_or_create(passport=Passport.objects.get(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.all().order_by("-id")[0], user=User.objects.get(username=person), collection_date=collection_date),  taxonomy=Taxonomy.objects.get(population=population)), seed_id=seed_id, seed_name=seed_name, cross_type=cross_type, stock_date=stock_date, pedigree=pedigree, stock_status='In Legacy Data')
  print(s)

def add_row(pedigree, seed_id, row_id, row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, exp_name, harvest_date, planting_date):
  r = ObsRow.objects.get_or_create(obs_selector=ObsSelector.objects.all().order_by("-id")[0], field=Field.objects.get(experiment__name=exp_name), stock=Stock.objects.filter(seed_id=seed_id, pedigree=pedigree)[0], row_id=row_id, row_name=row_name, range_num=row_range, plot=row_plot, block=row_block, rep=row_rep, kernel_num=row_kernel_num, comments=row_comments, planting_date=planting_date, harvest_date=harvest_date)
  print(r)

def add_plant(pedigree, seed_id, row_id, row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, exp_name, harvest_date, planting_date, plant_id, plant_num, plant_comments):
  p = ObsPlant.objects.get_or_create(obs_row=ObsRow.objects.filter(stock=Stock.objects.filter(seed_id=seed_id, pedigree=pedigree)[0], row_id=row_id, row_name=row_name, range_num=row_range, plot=row_plot, block=row_block, rep=row_rep, kernel_num=row_kernel_num, comments=row_comments, planting_date=planting_date, harvest_date=harvest_date)[0], obs_selector=ObsSelector.objects.all().order_by("-id")[0], plant_id=plant_id, plant_num=plant_num, comments=plant_comments)
  print(p)

def add_location(building_name, comments):
  l = Location.objects.get_or_create(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA'), building_name=building_name, comments=comments)
  print(l)

def add_stock_packet(seed_id, pedigree, building_name, comments, weight):
  p = StockPacket.objects.get_or_create(stock=Stock.objects.filter(seed_id=seed_id, pedigree=pedigree)[0], location=Location.objects.get(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA'), building_name=building_name, comments=comments), weight=weight)
  print(p)

#------------------------------------
#------------------------------------

def csv_import_seed_01():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_seed_table_t1.2.csv'), dialect='excel')
  for row in ifile:
    stock_seed_id = row['seed_id']
    stock_row_id = row['row_id']


#-------------------------------------------------------------------------
# Start execution here!
#-------------------------------------------------------------------------

if __name__ == '__main__':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_project.settings')
  from mine.models import Experiment, User, UserProfile, Taxonomy, Locality, Field, Passport, Collecting, Source, Stock, Location, ObsRow, ObsPlant, ObsSelector, StockPacket, Location
  from legacy.models import Legacy_Seed, Legacy_People, Legacy_Experiment, Legacy_Seed_Inventory, Legacy_Plant, Legacy_Tissue
  #csv_import_people()
  csv_import_experiment()
  add_dummies()
  csv_import_row_01()
