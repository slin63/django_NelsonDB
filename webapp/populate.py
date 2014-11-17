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

    add_exp_locality(experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country)
    add_exp_field(experiment_field_name, experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country)
    add_exp_experiment(experiment_field_name, experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country, experiment_name, experiment_user_username, experiment_startdate, experiment_purpose, experiment_comments)

def add_exp_locality(city, state, country):
  l = Locality.objects.get_or_create(city=city, state=state, country=country, zipcode='NULL')
  print(l)

def add_exp_field(field_name, city, state, country):
  f = Field.objects.get_or_create(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name)
  print(f)

def add_exp_experiment(field_name, city, state, country, experiment_name, username, startdate, purpose, comments):
  e = Experiment.objects.get_or_create(field=Field.objects.get(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name), user=User.objects.get(username=username), name=experiment_name, start_date=startdate, purpose=purpose, comments=comments)
  print(e)

#----------------------------------------------------------
#----------------------------------------------------------

def add_dummies():
  s = People.objects.get_or_create(organization='No Source')
  f = Field.objects.get_or_create(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field')
  e = Experiment.objects.get_or_create(user=User.objects.get(username='unknown'), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), name='No Experiment')
  o = ObsSelector.objects.get_or_create(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), name='No Experiment'))
  l = Location.objects.get_or_create(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL', zipcode='NULL'), location_name='Unknown', box_name='Unknown')
  t = Taxonomy.objects.get_or_create(genus='No Taxonomy', species='No Taxonomy', population='No Taxonomy', common_name='No Taxonomy', alias='No Taxonomy', race='No Taxonomy', subtaxa='No Taxonomy')
  c = Collecting.objects.get_or_create(obs_selector=ObsSelector.objects.get(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), name='No Experiment')), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), user=User.objects.get(username='unknown_person'), collection_date='No Date', collection_method='No Collection', comments='No Collection')
  p = Passport.objects.get_or_create(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.get(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), name='No Experiment')), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), user=User.objects.get(username='unknown_person'), collection_date='No Date', collection_method='No Collection', comments='No Collection'), people=People.objects.get(organization='No Source'), taxonomy=Taxonomy.objects.get(genus='No Taxonomy', species='No Taxonomy', population='No Taxonomy', common_name='No Taxonomy', alias='No Taxonomy', race='No Taxonomy', subtaxa='No Taxonomy'))
  s = Stock.objects.get_or_create(seed_id=0, seed_name='No Seed', cross_type='No Seed', pedigree='No Seed', stock_status='No Seed', stock_date='No Seed', comments='No Seed', passport=Passport.objects.get(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.get(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), name='No Experiment')), field=Field.objects.get(locality=Locality.objects.get(city='NULL', state='NULL', country='NULL'), field_name='No Field'), user=User.objects.get(username='unknown_person'), collection_date='No Date', collection_method='No Collection', comments='No Collection'), people=People.objects.get(organization='No Source'), taxonomy=Taxonomy.objects.get(genus='No Taxonomy', species='No Taxonomy', population='No Taxonomy', common_name='No Taxonomy', alias='No Taxonomy', race='No Taxonomy', subtaxa='No Taxonomy')))

def row_loader():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_row_table_t1.1.csv'), dialect='excel')
  for row in ifile:
    row_row_id = row['row_id'].replace(u'\xa0', u' ')
    row_row_name = row['row_name'].replace(u'\xa0', u' ')
    row_experiment_name = row['experiment_id'].replace(u'\xa0', u' ')
    row_stock_seed_id = row['source_seed_id'].replace(u'\xa0', u' ')
    row_range = row['range'].replace(u'\xa0', u' ')
    row_plot = row['plot'].replace(u'\xa0', u' ')
    row_block = row['block'].replace(u'\xa0', u' ')
    row_rep = row['rep'].replace(u'\xa0', u' ')
    row_population = row['pop'].replace(u'\xa0', u' ')
    row_purpose = row['purpose'].replace(u'\xa0', u' ')
    row_notes = row['notes'].replace(u'\xa0', u' ')
    row_comments = "Purpose: %s || Notes: %s" % (row_purpose, row_notes)
    row_kernel_num = row['kernel_num'].replace(u'\xa0', u' ')
    row_stock_pedigree = row['pedigree'].replace(u'\xa0', u' ')
    print(row_row_id)

def csv_import_row_01():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_row_table_t1.1.csv'), dialect='excel')
  for row in ifile:
    row_row_id = row['row_id'].replace(u'\xa0', u' ')
    row_row_name = row['row_name'].replace(u'\xa0', u' ')
    row_experiment_name = row['experiment_id'].replace(u'\xa0', u' ')
    row_stock_seed_id = row['source_seed_id'].replace(u'\xa0', u' ')
    row_range = row['range'].replace(u'\xa0', u' ')
    row_plot = row['plot'].replace(u'\xa0', u' ')
    row_block = row['block'].replace(u'\xa0', u' ')
    row_rep = row['rep'].replace(u'\xa0', u' ')
    row_population = row['pop'].replace(u'\xa0', u' ')
    row_purpose = row['purpose'].replace(u'\xa0', u' ')
    row_notes = row['notes'].replace(u'\xa0', u' ')
    row_comments = "Purpose: %s || Notes: %s" % (row_purpose, row_notes)
    row_kernel_num = row['kernel_num'].replace(u'\xa0', u' ')
    row_stock_pedigree = row['pedigree'].replace(u'\xa0', u' ')

    exp = Legacy_Experiment.objects.get(experiment_id=row_experiment_name)
    if row_stock_seed_id != 0:
      try:
        seed = Legacy_Seed.objects.get(seed_id=row_stock_seed_id)
        if seed.seed_person_id:
          seed_person_value = Legacy_People.objects.get(person_id = seed.seed_person_id)
          person = seed_person_value.person_name
        else:
          person = 'unknown_person'
        if seed.line_num:
          seed.seed_name = seed.line_num
        if seed:
          seed.comments = 'Notes: %s || Lot: %s || Accession: %s' % (seed.notes, seed.lot, seed.accession)
        if seed.plant_id_origin:
          try:
            plant = Legacy_Plant.objects.get(plant_id=seed.plant_id_origin)
          except Legacy_Plant.DoesNotExist:
            plant = None
      except (Legacy_Seed.DoesNotExist, IndexError):
        seed = None
      try:
        seedinv = Legacy_Seed_Inventory.objects.filter(seed_id=row_stock_seed_id)[0]
      except (Legacy_Seed_Inventory.DoesNotExist, IndexError):
        seedinv = None
    else:
      seed = None
      plant = None
      seedinv = None

    add_row_taxonomy(row_population)
    add_row_obs_selector(row_experiment_name)
    if seed:
      add_row_collecting(person, exp.harvest_date)
      add_row_people(seed.program_origin)
      add_row_passport(person, exp.harvest_date, row_population, seed.program_origin)
      if seedinv:
        add_row_stock(row_stock_pedigree, seed.seed_id, seed.seed_name, seed.cross_type, seed.comments, seedinv.inventory_date, person, exp.harvest_date, row_population, seed.program_origin)
        add_row_row(row_stock_pedigree, seed.seed_id, seed.seed_name, seed.cross_type, seed.comments, seedinv.inventory_date, person, exp.harvest_date, row_population, seed.program_origin, row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, row_experiment_name, exp.harvest_date, exp.planting_date)
      else:
        add_row_stock(row_stock_pedigree, seed.seed_id, seed.seed_name, seed.cross_type, seed.comments, 'Not Inventoried', person, exp.harvest_date, row_population, seed.program_origin)
        add_row_row(row_stock_pedigree, seed.seed_id, seed.seed_name, seed.cross_type, seed.comments, 'Not Inventoried', person, exp.harvest_date, row_population, seed.program_origin, row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, row_experiment_name, exp.harvest_date, exp.planting_date)
      if seed.plant_id_origin:
        if plant:
          add_row_obs_selector(row_experiment_name)
          add_row_plant(row_stock_pedigree, seed.seed_id, row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, row_experiment_name, exp.harvest_date, exp.planting_date, plant.plant_id, plant.plant_name, plant.notes)
    else:
      add_row_row_nostock('No Seed', 0, row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, row_experiment_name, exp.harvest_date, exp.planting_date)
    if seedinv:
      add_row_location(seedinv.location, seedinv.notes)
      if seed:
        add_row_stock_packet(seed.seed_id, row_stock_pedigree, seedinv.location, seedinv.notes, seedinv.weight_g)

def add_row_taxonomy(population):
  t = Taxonomy.objects.get_or_create(genus='Zea', species='Zea mays', population=population, common_name='Maize')
  print(t)

def add_row_obs_selector(experiment_name):
  o = ObsSelector.objects.create(experiment=Experiment.objects.get(name=experiment_name))
  print(o)

def add_row_collecting(person, collection_date):
  c = Collecting.objects.get_or_create(obs_selector=ObsSelector.objects.all().order_by("-id")[0], user=User.objects.get(username=person), field = Field.objects.get(field_name='No Field'), collection_date=collection_date, collection_method='Manual field harvest. Husks removed and all ears were collected.')
  print(c)

def add_row_people(organization):
  p = People.objects.get_or_create(organization=organization)
  print(p)

def add_row_passport(person, collection_date, population, organization):
  p = Passport.objects.get_or_create(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.all().order_by("-id")[0], user=User.objects.get(username=person), collection_date=collection_date),  taxonomy=Taxonomy.objects.get(population=population), people=People.objects.get(organization=organization))
  print(p)

def add_row_stock(pedigree, seed_id, seed_name, cross_type, comments, stock_date, person, collection_date, population, organization):
  s = Stock.objects.get_or_create(passport=Passport.objects.get(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.all().order_by("-id")[0], user=User.objects.get(username=person), collection_date=collection_date),  taxonomy=Taxonomy.objects.get(population=population), people=People.objects.get(organization=organization)), seed_id=seed_id, seed_name=seed_name, cross_type=cross_type, stock_date=stock_date, pedigree=pedigree, stock_status='In Legacy Data', comments=comments)
  print(s)

def add_row_row(pedigree, seed_id, seed_name, cross_type, comments, stock_date, person, collection_date, population, organization, row_id, row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, exp_name, harvest_date, planting_date):
  r = ObsRow.objects.get_or_create(obs_selector=ObsSelector.objects.all().order_by("-id")[0], field=Field.objects.get(experiment__name=exp_name), stock=Stock.objects.get(passport=Passport.objects.get(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.all().order_by("-id")[0], user=User.objects.get(username=person), collection_date=collection_date),  taxonomy=Taxonomy.objects.get(population=population), people=People.objects.get(organization=organization)), seed_id=seed_id, seed_name=seed_name, cross_type=cross_type, stock_date=stock_date, pedigree=pedigree, stock_status='In Legacy Data', comments=comments), row_id=row_id, row_name=row_name, range_num=row_range, plot=row_plot, block=row_block, rep=row_rep, kernel_num=row_kernel_num, comments=row_comments, planting_date=planting_date, harvest_date=harvest_date)
  print(r)

def add_row_row_nostock(pedigree, seed_id, row_id, row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, exp_name, harvest_date, planting_date):
  r = ObsRow.objects.get_or_create(obs_selector=ObsSelector.objects.all().order_by("-id")[0], field=Field.objects.get(experiment__name=exp_name), stock=Stock.objects.get(seed_id=seed_id, pedigree=pedigree), row_id=row_id, row_name=row_name, range_num=row_range, plot=row_plot, block=row_block, rep=row_rep, kernel_num=row_kernel_num, comments=row_comments, planting_date=planting_date, harvest_date=harvest_date)
  print(r)

def add_row_plant(pedigree, seed_id, row_id, row_name, row_range, row_plot, row_block, row_rep, row_comments, row_kernel_num, exp_name, harvest_date, planting_date, plant_id, plant_num, plant_comments):
  p = ObsPlant.objects.get_or_create(obs_row=ObsRow.objects.filter(stock=Stock.objects.filter(seed_id=seed_id, pedigree=pedigree)[0], row_id=row_id, row_name=row_name, range_num=row_range, plot=row_plot, block=row_block, rep=row_rep, kernel_num=row_kernel_num, comments=row_comments, planting_date=planting_date, harvest_date=harvest_date)[0], obs_selector=ObsSelector.objects.all().order_by("-id")[0], plant_id=plant_id, plant_num=plant_num, comments=plant_comments)
  print(p)

def add_row_location(building_name, comments):
  l = Location.objects.get_or_create(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA', zipcode='NULL'), building_name=building_name, comments=comments, box_name='Unknown')
  print(l)

def add_row_stock_packet(seed_id, pedigree, building_name, comments, weight):
  p = StockPacket.objects.get_or_create(stock=Stock.objects.filter(seed_id=seed_id, pedigree=pedigree)[0], location=Location.objects.get(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA', zipcode='NULL'), building_name=building_name, comments=comments, box_name='Unknown'), weight=weight)
  print(p)

#------------------------------------
#------------------------------------

def csv_import_isolate():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_isolate_table.csv'), dialect='excel')
  for row in ifile:
    isolate_id = row['isolate_id']
    isolate_name = row['isolate_name']
    taxonomy_genus = row['scientific_name']
    taxonomy_alias = row['other_sname']
    taxonomy_race = row['pathotype_race']
    disease_info_common_name = row['disease_common_name']
    field_name = row['collection_site']
    city = row['city']
    state = row['state']
    country = row['country']
    collection_date = row['collection_date']
    isolate_plant_organ = row['plant_organ']
    collection_user = row['collector']
    people_organization = row['provider']
    location_n80c_boxname = row['n80c']
    location_4c_boxname = row['4c']
    isolate_comments = row['notes']
    subtaxa = row['mating_type']

    add_iso_disease_info(disease_info_common_name)
    add_iso_taxonomy(taxonomy_genus, taxonomy_alias, taxonomy_race, subtaxa)
    add_iso_locality(city, state, country)
    add_iso_field(city, state, country, field_name)
    add_iso_collecting(collection_date, collection_user, field_name, city, state, country)
    add_iso_passport(collection_date, collection_user, field_name, city, state, country, taxonomy_genus, taxonomy_alias, taxonomy_race, subtaxa)
    if location_n80c_boxname:
      add_location_n80c(location_n80c_boxname)
      add_isolate_n80c(isolate_id, isolate_name, isolate_plant_organ, isolate_comments, collection_date, collection_user, field_name, city, state, country, taxonomy_genus, taxonomy_alias, taxonomy_race, subtaxa, location_n80c_boxname, disease_info_common_name)
    #if location_4c_boxname:
    #  add_location_4c(location_4c_boxname)
    #  add_isolate_4c(isolate_id, isolate_name, isolate_plant_organ, isolate_comments, collection_date, collection_user, field_name, city, state, country, taxonomy_genus, taxonomy_alias, taxonomy_race, subtaxa, location_4c_boxname, disease_info_common_name)

def add_iso_disease_info(common_name):
  d = DiseaseInfo.objects.get_or_create(common_name=common_name)
  print(d)

def add_iso_taxonomy(genus, alias, race, subtaxa):
  t = Taxonomy.objects.get_or_create(genus=genus, alias=alias, race=race, subtaxa=subtaxa)
  print(t)

def add_iso_locality(city, state, country):
  y = Locality.objects.get_or_create(city=city, state=state, country=country, zipcode='NULL')
  print(y)

def add_iso_field(city, state, country, field_name):
  f = Field.objects.get_or_create(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name)
  print(f)

def add_iso_collecting(date, username, field_name, city, state, country):
  c = Collecting.objects.get_or_create(obs_selector=ObsSelector.objects.get(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(field_name='No Field'))), user=User.objects.get(username=username), field=Field.objects.get(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name), collection_date=date)
  print(c)

def add_iso_passport(date, username, field_name, city, state, country, genus, alias, race, subtaxa):
  p = Passport.objects.get_or_create(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.get(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(field_name='No Field'))), user=User.objects.get(username=username), field=Field.objects.get(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name), collection_date=date), people=People.objects.get(organization='No Source'), taxonomy=Taxonomy.objects.get(genus=genus, alias=alias, race=race, subtaxa=subtaxa))
  print(p)

def add_location_n80c(box_name):
  l = Location.objects.get_or_create(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA'), location_name='Freezer -80c', box_name=box_name)
  print(l)

def add_location_4c(box_name):
  l = Location.objects.get_or_create(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA'), location_name='Freezer 4c', box_name=box_name)
  print(l)

def add_isolate_n80c(isolate_id, isolate_name, plant_organ, comments, date, username, field_name, city, state, country, genus, alias, race, subtaxa, box_name, common_name):
  i = Isolate.objects.get_or_create(passport=Passport.objects.get(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.get(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(field_name='No Field'))), user=User.objects.get(username=username), field=Field.objects.get(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name), collection_date=date), people=People.objects.get(organization='No Source'), taxonomy=Taxonomy.objects.get(genus=genus, alias=alias, race=race, subtaxa=subtaxa)), location=Location.objects.get(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA'), location_name='Freezer -80c', box_name=box_name), disease_info=DiseaseInfo.objects.get(common_name=common_name), isolate_id=isolate_id, isolate_name=isolate_name, plant_organ=plant_organ, comments=comments)
  print(i)

def add_isolate_4c(isolate_id, isolate_name, plant_organ, comments, date, username, field_name, city, state, country, genus, alias, race, subtaxa, box_name, common_name):
  i = Isolate.objects.get_or_create(passport=Passport.objects.get(collecting=Collecting.objects.get(obs_selector=ObsSelector.objects.get(experiment=Experiment.objects.get(user=User.objects.get(username='unknown'), field=Field.objects.get(field_name='No Field'))), user=User.objects.get(username=username), field=Field.objects.get(locality=Locality.objects.get(city=city, state=state, country=country), field_name=field_name), collection_date=date), people=People.objects.get(organization='No Source'), taxonomy=Taxonomy.objects.get(genus=genus, alias=alias, race=race, subtaxa=subtaxa)), location=Location.objects.get(locality=Locality.objects.get(city='Ithaca', state='NY', country='USA'), location_name='Freezer 4c', box_name=box_name), disease_info=DiseaseInfo.objects.get(common_name=common_name), isolate_id=isolate_id, isolate_name=isolate_name, plant_organ=plant_organ, comments=comments)
  print(i)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def phenotype_loader():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_phenotype_table.csv'), dialect='excel')
  for row in ifile:
    phenotype_id = row['phenotype_id'].replace(u'\xa0', u' ')
    row_id = row['entity_id'].replace(u'\xa0', u' ')
    entity_type = row['entity_type'].replace(u'\xa0', u' ')
    plant_id = row['entity_name'].replace(u'\xa0', u' ')
    experiment_name = row['experiment_id'].replace(u'\xa0', u' ')
    parameter = row['trait_id'].replace(u'\xa0', u' ')
    value = row['phenotype_value'].replace(u'\xa0', u' ')
    time = row['phenotype_date'].replace(u'\xa0', u' ')
    plate_id = row['plate_id'].replace(u'\xa0', u' ')
    person_id = row['phenotype_person_id'].replace(u'\xa0', u' ')
    scoring_order = row['scoring_order'].replace(u'\xa0', u' ')
    comments = row['notes'].replace(u'\xa0', u' ')
    print(phenotype_id)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def csv_import_phenotype():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_phenotype_table.csv'), dialect='excel')
  for row in ifile:
    phenotype_id = row['phenotype_id']
    row_id = row['entity_id']
    entity_type = row['entity_type']
    plant_id = row['entity_name']
    experiment_name = row['experiment_id']
    parameter = row['trait_id']
    value = row['phenotype_value']
    time = row['phenotype_date']
    plate_id = row['plate_id']
    person_id = row['phenotype_person_id']
    scoring_order = row['scoring_order']
    comments = row['notes']

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def post_stock_status_change():
  i = 1
  go = True
  while go is True:
    try:
      stockpacket = StockPacket.objects.get(id=i)
      stock = stockpacket.stock
      stock.stock_status = 'Legacy Inventory'
      stock.save()
      i = i + 1
      print(i)
    except (StockPacket.DoesNotExist, IndexError):
      go = False
      print('Done')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def post_isolate_taxonomy_change():
  i = 1
  go = True
  while go is True:
    try:
      isolate = Isolate.objects.get(id=i)
      taxonomy = isolate.passport.taxonomy
      taxonomy.common_name = 'Isolate'
      taxonomy.save()
      i = i + 1
      print(i)
    except (Isolate.DoesNotExist, IndexError):
      go = False
      print('Done')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def post_isolate_passport_fix():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_isolate_table.csv'), dialect='excel')
  for row in ifile:
    isolate_id = row['isolate_id']
    isolate_name = row['isolate_name']
    isolate_plant_organ = row['plant_organ']
    people_organization = row['provider']
    isolate_comments = row['notes']

    try:
      isolate = Isolate.objects.get(isolate_id=isolate_id, isolate_name=isolate_name, plant_organ=isolate_plant_organ, comments=isolate_comments)
      people = isolate.passport.people
      people.organization = people_organization
      people.save()
      print(people_organization)
    except (Isolate.DoesNotExist, IndexError):
      print('X')

#-------------------------------------------------------------------------
# Start execution here!
#-------------------------------------------------------------------------

if __name__ == '__main__':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_project.settings')
  from lab.models import Experiment, User, UserProfile, Taxonomy, Locality, Field, Passport, Collecting, People, Stock, Location, ObsRow, ObsPlant, ObsSelector, StockPacket, Location, Isolate, DiseaseInfo
  from legacy.models import Legacy_Seed, Legacy_People, Legacy_Experiment, Legacy_Seed_Inventory, Legacy_Plant, Legacy_Tissue
  #csv_import_people()
  #csv_import_experiment()
  #add_dummies()
  #csv_import_isolate()
  #row_loader()
  #csv_import_row_01()
  #post_stock_status_change()
  #post_isolate_taxonomy_change()
  post_isolate_passport_fix()
