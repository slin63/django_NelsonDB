
import os
import csv
from collections import OrderedDict
import time

def migrate():
  start = time.clock()
  #--- Takes 2.5 minutes to run this through, on my computer.
  #--- The old populate.py script takes ~20 hours, on my computer. Not recommended to run that.

#-----------------------------------------------
#- Define output dictionaries
#-----------------------------------------------
  experiment_table = OrderedDict({})
  #--- Key = (experiment_id, user_id, field_id, name, start_date, purpose, comments)
  #--- Value = (experiment_id)
  locality_table = OrderedDict({})
  #--- Key = (locality_id, city, state, country, zipcode)
  #--- Value = (locality_id)
  field_table = OrderedDict({})
  #--- Key = (field_id, locality_id, field_name)
  #--- Value = (field_id)
  people_table = OrderedDict({})
  #--- Key = (people_id, organization)
  #--- Value = (people_id)
  location_table = OrderedDict({})
  #--- Key = (location_id, locality_id, building_name, location_name, box_name)
  #--- Value = (location_id)
  obs_selector_table = OrderedDict({})
  #--- Key = (obs_selector_id, experiment_id)
  #--- Value = (obs_selector_id)
  obs_row_table = OrderedDict({})
  #--- Key = (obs_row_id, obs_selector_id, field_id, stock_id, row_id, row_name, range_num, plot, block, rep, kernel_num, planting_date, harvest_date, comments)
  #--- Value = (obs_row_id)
  obs_plant_table = OrderedDict({})
  #--- Key = (obs_plant_id, obs_selector_id, obs_row_id, plant_id, plant_num, comments)
  #--- Value = (obs_plant_id)
  taxonomy_table = OrderedDict({})
  #--- Key = (taxonomy_id, genus, species, population, common_name, alias, race, subtaxa)
  #--- Value = (taxonomy_id)
  collecting_table = OrderedDict({})
  #--- Key = (collecting_id, obs_selector_id, user_id, field_id, collection_date, collection_method, comments)
  #--- Value = (collecting_id)
  passport_table = OrderedDict({})
  #--- Key = (passport_id, collecting_id, people_id, taxonomy_id)
  #--- Value = (passport_id)
  stock_table = OrderedDict({})
  #--- Key = (stock_id, passport_id, seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, comments)
  #--- Value = (stock_id)
  stock_packet_table = OrderedDict({})
  #--- Key = (stock_packet_id, stock_id, location_id, weight, comments)
  #--- Value = (stock_packet_id)
  isolate_table = OrderedDict({})
  #--- Key = (isolate_id, passport_id, location_id, disease_info_id, isolate_id, isolate_name, plant_organ, comments)
  #--- Value = (isolate_id)
  disease_info_table = OrderedDict({})
  #--- Key = (disease_info_id, common_name)
  #--- Value = (disease_info_id)
  measurement_table = OrderedDict({})
  #--- Key = (measurement_id, obs_selector_id, user_id, measurement_param_id, time_of_measurement, value, comments)
  #--- Value = (measurement_id)
  measurement_param_table = OrderedDict({})
  #--- Key = (measurement_param_id, parameter, parameter_type, unit, protocol, trait_id_buckler)
  #--- Value = (measurement_param_id)

  stock_not_inventoried = OrderedDict({})
  #--- Key = (legacy_seed_id)
  #--- Value = (legacy values)
  row_source_seed_not_in_seed = OrderedDict({})
  #--- Key = (count)
  #--- Value = (legacy values)
  row_no_source_seed = OrderedDict({})
  #--- Key = (count)
  #--- Value = (legacy values)
  phenotype_row_not_in_row = OrderedDict({})
  #--- Key = (count)
  #--- Value = (legacy values)
  legacy_seed_not_in_stock = OrderedDict({})
  #--- Key = (count)
  #--- Value = (legacy_values)
  legacy_seedinv_not_in_stock = OrderedDict({})
  #--- Key = (count)
  #--- Value = (legacy_values)

#-------------------------------------------------
#- Define intermediary dictionaries and legacy data dictionaries
#-------------------------------------------------
  experiment_name_table = OrderedDict({})
  #--- Key = (name)
  #--- Value = (id, user_id, field_id, name, start_date, purpose, comments)
  experiment_field_table = OrderedDict({})
  #--- Key = (name)
  #--- Value = (field_id)
  obs_row_intermed_table = OrderedDict({})
  #--- Key = (row_id)
  #--- Value = (id, obs_selector_id, field_id, stock_id, row_id, row_name, range_num, plot, block, rep, kernel_num, planting_date, harvest_date, comments)
  stock_seed_id_table = OrderedDict({})
  #--- Key = (seed_id)
  #--- Value = (stock_id)
  collecting_hash_table = OrderedDict({})
  #--- Key = (hash(obs_selector_id, user_id, field_id, collection_date, collection_method, comments))
  #--- Value = (collecting_id)
  passport_hash_table = OrderedDict({})
  #--- Key = (hash(collecting_hash_id, people_hash_id, taxonomy_hash_id))
  #--- Value = (passport_id)
  stock_hash_table = OrderedDict({})
  #--- Key = (hash(passport_hash_id, seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, comments))
  #--- Value = (stock_id)
  taxonomy_hash_table = OrderedDict({})
  #--- Key = (hash(genus, species, population, common_name, alias, race, subtaxa))
  #--- Value = (taxonomy_id)
  people_hash_table = OrderedDict({})
  #--- Key = (hash(organization))
  #--- Value = (people_id)
  location_hash_table = OrderedDict({})
  #--- Key = (hash(locality_id, building_name, location_name, box_name))
  #--- Value = (location_id)
  stock_packet_hash_table = OrderedDict({})
  #--- Key = (hash(stock_hash_id, location_hash_id, weight, comments))
  #--- Value = (stock_id)
  obs_selector_hash_table = OrderedDict({})
  #--- Key = (hash(obs_selector_id, experiment_id))
  #--- Value = (obs_selector_id)
  user_hash_table = OrderedDict({})
  #--- Key = (hash(username))
  #--- Value = (user_id)
  measurement_hash_table = OrderedDict({})
  #--- Key = (hash(obs_selector_id, user_id, measurement_param_hash_id, time_of_measurement, value, comments))
  #--- Value = (measurement_id)
  measurement_param_hash_table = OrderedDict({})
  #--- Key = (hash(parameter, trait_id_buckler))
  #--- Value = (measurement_param_id)
  locality_hash_table = OrderedDict({})
  #--- Key = (hash(city, state, country, zipcode))
  #--- Value = (locality_id)
  field_hash_table = OrderedDict({})
  #--- Key = (hash(locality_id, field_name))
  #--- Value = (field_id)
  field_name_table = OrderedDict({})
  #--- Key = (field_name)
  #--- Value = (id)
  experiment_hash_table = OrderedDict({})
  #--- Key = (hash(user_id, field_id, name, start_date, purpose, comments))
  #--- Value = (experiment_id)
  disease_info_hash_table = OrderedDict({})
  #--- Key = (hash(common_name))
  #--- Value = (disease_info_id)
  isolate_hash_table = OrderedDict({})
  #--- Key = (hash(passport_id, location_id, disease_info_id, isolate_id, isolate_name, plant_organ, comments))
  #--- Value = (isolate_id)

  legacy_experiment_table = OrderedDict({})
  #--- Key = (legacy_exp_id)
  #--- Value = (legacy_exp_id, legacy_exp_location, legacy_exp_planting_date, legacy_exp_tissue_collection, legacy_exp_inoculations, legacy_exp_inoculation_date1, legacy_exp_inoculation_date2, legacy_exp_inoculation_date3, legacy_exp_pathogen_isolate, legacy_exp_harvest_date, legacy_exp_description, legacy_exp_notes)
  legacy_seed_table = OrderedDict({})
  #--- Key = (hash(legacy_seed_id))
  #--- Value = (legacy_seed_id, legacy_plant_id_origin, legacy_row_id_origin, legacy_experiment_id_origin, legacy_plant_name, legacy_row_name, legacy_seed_name, legacy_cross_type, legacy_male_parent_id, legacy_male_parent_name, legacy_program_origin, legacy_seed_pedigree, legacy_line_num, legacy_seed_person_id, legacy_seed_disease_info, legacy_seed_notes, legacy_seed_accession, legacy_seed_lot)
  legacy_people_table = OrderedDict({})
  #--- Key = (legacy_person_id)
  #--- Value = (legacy_person_id, legacy_person_name, legacy_first_name, legacy_last_name, legacy_title, legacy_address, legacy_phone, legacy_fax, legacy_email, legacy_URL, legacy_person_notes, legacy_peopleorg_id)
  legacy_plant_table = OrderedDict({})
  #--- Key = (legacy_plant_id)
  #--- Value = (legacy_plant_id, legacy_plant_row_id, legacy_plant_name, legacy_plant_notes)
  legacy_seedinv_table = OrderedDict({})
  #--- Key = (hash(legacy_seedinv_seed_id))
  #--- Value = (legacy_seedinv_id, legacy_seedinv_seed_id, legacy_seedinv_seed_name, legacy_seedinv_date, legacy_seedinv_person, legacy_seedinv_person_id, legacy_seedinv_location, legacy_seedinv_notes, legacy_seedinv_weight)

  measurement_parameter_info_table = OrderedDict({})
  #--- Key = (trait_id)
  #--- Value = (trait_id, trait, unit, description)

#-------------------------------------------------------------------
#- Load Legacy Data into dictionaries
#-------------------------------------------------------------------
  legacy_exp_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/legacy_experiment_table.csv'), dialect='excel')
  for row in legacy_exp_file:
    legacy_exp_id = row["experiment_id"]
    legacy_exp_location = row["location"]
    legacy_exp_planting_date = row["planting_date"]
    legacy_exp_tissue_collection = row["tissue_collection"]
    legacy_exp_inoculations = row["inoculations"]
    legacy_exp_inoculation_date1 = row["inoculation_date1"]
    legacy_exp_inoculation_date2 = row["inoculation_date2"]
    legacy_exp_inoculation_date3 = row["inoculation_date3"]
    legacy_exp_pathogen_isolate = row["pathogen_isolate"]
    legacy_exp_harvest_date = row["harvest_date"]
    legacy_exp_description = row["description"]
    legacy_exp_notes = row["notes"]

    legacy_experiment_table[(legacy_exp_id)] = (legacy_exp_id, legacy_exp_location, legacy_exp_planting_date, legacy_exp_tissue_collection, legacy_exp_inoculations, legacy_exp_inoculation_date1, legacy_exp_inoculation_date2, legacy_exp_inoculation_date3, legacy_exp_pathogen_isolate, legacy_exp_harvest_date, legacy_exp_description, legacy_exp_notes)

  legacy_seed_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/legacy_seed_table.csv'), dialect='excel')
  for row in legacy_seed_file:
    legacy_seed_id = row["seed_id"]
    legacy_plant_id_origin = row["plant_id_origin"]
    legacy_row_id_origin = row["row_id_origin"]
    legacy_experiment_id_origin = row["experiment_id_origin_id"]
    legacy_plant_name = row["plant_name"]
    legacy_row_name = row["row_name"]
    legacy_seed_name = row["seed_name"]
    legacy_cross_type = row["cross_type"]
    legacy_male_parent_id = row["male_parent_id"]
    legacy_male_parent_name = row["male_parent_name"]
    legacy_program_origin = row["program_origin"]
    legacy_seed_pedigree = row["seed_pedigree"]
    legacy_line_num = row["line_num"]
    legacy_seed_person_id = row["seed_person_id"]
    legacy_seed_disease_info = row["disease_info"]
    legacy_seed_notes = row["notes"]
    legacy_seed_accession = row["accession"]
    legacy_seed_lot = row["lot"]

    seed_id_hash = hash(legacy_seed_id)
    legacy_seed_table[(seed_id_hash)] = (legacy_seed_id, legacy_plant_id_origin, legacy_row_id_origin, legacy_experiment_id_origin, legacy_plant_name, legacy_row_name, legacy_seed_name, legacy_cross_type, legacy_male_parent_id, legacy_male_parent_name, legacy_program_origin, legacy_seed_pedigree, legacy_line_num, legacy_seed_person_id, legacy_seed_disease_info, legacy_seed_notes, legacy_seed_accession, legacy_seed_lot)

  legacy_people_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/legacy_people_table.csv'), dialect='excel')
  for row in legacy_people_file:
    legacy_person_id = row["person_id"]
    legacy_person_name = row["person_name"]
    legacy_first_name = row["first_name"]
    legacy_last_name = row["last_name"]
    legacy_title = row["title"]
    legacy_address = row["address"]
    legacy_phone = row["phone"]
    legacy_fax = row["fax"]
    legacy_email = row["email"]
    legacy_URL = row["URL"]
    legacy_person_notes = row["notes"]
    legacy_peopleorg_id = row["peopleorg_id"]

    legacy_people_table[(legacy_person_id)] = (legacy_person_id, legacy_person_name, legacy_first_name, legacy_last_name, legacy_title, legacy_address, legacy_phone, legacy_fax, legacy_email, legacy_URL, legacy_person_notes, legacy_peopleorg_id)

  legacy_plant_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/legacy_plant_table.csv'), dialect='excel')
  for row in legacy_plant_file:
    legacy_plant_id = row["plant_id"]
    legacy_plant_row_id = row["row_id"]
    legacy_plant_name = row["plant_name"]
    legacy_plant_notes = row["notes"]

    legacy_plant_table[(legacy_plant_id)] = (legacy_plant_id, legacy_plant_row_id, legacy_plant_name, legacy_plant_notes)

  legacy_seedinv_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/seedinv_clean.csv'), dialect='excel')
  for row in legacy_seedinv_file:
    legacy_seedinv_id = row["ID"]
    legacy_seedinv_seed_id = row["seed_id"]
    legacy_seedinv_seed_name = row["seed_name"]
    legacy_seedinv_date = row["inventory_date"]
    legacy_seedinv_person = row["inventory_person"]
    legacy_seedinv_person_id = row["seed_person_id"]
    legacy_seedinv_location = row["location"]
    legacy_seedinv_notes = row["notes"]
    legacy_seedinv_weight = row["weight_g"]

    seedinv_hash_seed_id = hash(legacy_seedinv_seed_id)
    legacy_seedinv_table[(seedinv_hash_seed_id)] = (legacy_seedinv_id, legacy_seedinv_seed_id, legacy_seedinv_seed_name, legacy_seedinv_date, legacy_seedinv_person, legacy_seedinv_person_id, legacy_seedinv_location, legacy_seedinv_notes, legacy_seedinv_weight)

#-------------------------------------------------------------------
#-This user_table is simply stored in memory and is not written to csv or the database.
#-Given that person.csv is the same file used to write people to the database, the user_ids in this user_table should match the user_ids in the database.
#-Users are added in a separate, direct to database, function because of the django auth set_password() command.
#-------------------------------------------------------------------
  user_id = 1

  user_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/person.csv'), dialect='excel')
  for row in user_file:
    username = row["user"]

    username_hash = hash(username)
    if (username_hash) in user_hash_table:
      pass
    else:
      user_hash_table[(username_hash)] = user_id
      print("User_id: %d" % (user_id))
      user_id = user_id + 1

#------------------------------------------------------------------------
#-Add all Dummies
#------------------------------------------------------------------------
  people_table[(1, 'No Source')] = 1
  locality_table[(1, 'NULL','NULL','NULL','NULL')] = 1
  field_table[(1, 1,'No Field')] = 1
  experiment_table[(1, user_hash_table[(hash('unknown'))],1,'No Experiment','No Experiment','No Experiment','No Experiment')] = 1
  experiment_name_table[('No Experiment')] = 1
  obs_selector_table[(1,1)] = 1
  location_table[(1, 1,'Unknown','Unknown','Unknown')] = 1
  taxonomy_table[(1, 'No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy')] = 1
  collecting_table[(1,1,user_hash_table[(hash('unknown'))],1,'No Collection','No Collection','No Collection')] = 1
  passport_table[(1,1,1,1)] = 1
  stock_table[(1,1,'0','No Seed','No Seed','No Seed','No Seed','No Seed','No Seed')] = 1

  taxonomy_hash = hash(('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy'))
  taxonomy_hash_table[(taxonomy_hash)] = 1
  collecting_hash = hash((1,user_hash_table[(hash('unknown'))],1,'No Collection','No Collection','No Collection'))
  collecting_hash_table[(collecting_hash)] = 1
  passport_hash = hash((1,1,1))
  passport_hash_table[(passport_hash)] = 1
  stock_hash = hash((1,'0','No Seed','No Seed','No Seed','No Seed','No Seed','No Seed'))
  stock_hash_table[(stock_hash)] = 1
  people_hash = hash(('No Source'))
  people_hash_table[(people_hash)] = 1
  location_hash = hash((1,'Unknown','Unknown','Unknown'))
  location_hash_table[(location_hash)] = 1
  obs_selector_hash = hash((1,1))
  obs_selector_hash_table[(obs_selector_hash)] = 1
  locality_hash = hash(('NULL','NULL','NULL','NULL'))
  locality_hash_table[(locality_hash)] = 1
  field_hash = hash((1,'No Field'))
  field_hash_table[(field_hash)] = 1
  field_name_table[('No Field')] = 1
  experiment_hash = hash((user_hash_table[(hash('unknown'))],1,'No Experiment','No Experiment','No Experiment','No Experiment'))
  experiment_hash_table[(experiment_hash)] = 1

#---------------------------------------------------------------------
#-Information from experiments.csv is extracted and saved to locality, field, and experiment dictionaries.
#---------------------------------------------------------------------
  experiment_id = experiment_table.values()[-1] + 1
  locality_id = locality_table.values()[-1] + 1
  field_id = field_table.values()[-1] + 1

  experiment_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/experiments.csv'), dialect='excel')
  for row in experiment_file:
    experiment_name = row['name']
    experiment_field_locality_city = row['city']
    experiment_field_locality_state = row['state']
    experiment_field_locality_country = row['country']
    experiment_field_name = row['field_name']
    experiment_user_username = row['person']
    experiment_startdate = row['date']
    experiment_purpose = row['desc']
    experiment_inoc = row['inoculations']
    experiment_tissue_coll = row['tissue_collection']
    experiment_pathogen = row['pathogen']
    experiment_notes = row['notes']

    #---Complete comment ----
    if experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_inoc != 'NULL' and experiment_inoc != '' and experiment_pathogen != 'NULL' and experiment_pathogen != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Tissue Collection: %s || Inoculations: %s || Pathogen: %s || Notes: %s" % (experiment_tissue_coll, experiment_inoc, experiment_pathogen, experiment_notes)
    #---No notes ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_inoc != 'NULL' and experiment_inoc != '' and experiment_pathogen != 'NULL' and experiment_pathogen != '':
      experiment_comments = "Tissue Collection: %s || Inoculations: %s || Pathogen: %s" % (experiment_tissue_coll, experiment_inoc, experiment_pathogen)
    #---No pathogen ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_inoc != 'NULL' and experiment_inoc != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Tissue Collection: %s || Inoculations: %s || Notes: %s" % (experiment_tissue_coll, experiment_inoc, experiment_notes)
    #---No inoc ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_pathogen != 'NULL' and experiment_pathogen != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Tissue Collection: %s || Pathogen: %s || Notes: %s" % (experiment_tissue_coll, experiment_pathogen, experiment_notes)
    #---No tissue collection ----
    elif experiment_inoc != 'NULL' and experiment_inoc != '' and experiment_pathogen != 'NULL' and experiment_pathogen != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Inoculations: %s || Pathogen: %s || Notes: %s" % (experiment_inoc, experiment_pathogen, experiment_notes)
    #---No notes, pathogen ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_inoc != 'NULL' and experiment_inoc != '':
      experiment_comments = "Tissue Collection: %s || Inoculations: %s" % (experiment_tissue_coll, experiment_inoc)
    #---No inoc, pathogen ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Tissue Collection: %s || Notes: %s" % (experiment_tissue_coll, experiment_notes)
    #---No tissue col, inoculation ----
    elif experiment_pathogen != 'NULL' and experiment_pathogen != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Pathogen: %s || Notes: %s" % (experiment_pathogen, experiment_notes)
    #---No inoc, notes ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_pathogen != 'NULL' and experiment_pathogen != '':
      experiment_comments = "Tissue Collection: %s || Pathogen: %s" % (experiment_tissue_coll, experiment_pathogen)
    #---No tissue coll, pathogen ----
    elif experiment_inoc != 'NULL' and experiment_inoc != '' and experiment_pathogen != 'NULL' and experiment_pathogen != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Inoculations: %s || Notes: %s" % (experiment_inoc, experiment_notes)
    #---No inoc, pathogen ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '' and experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Tissue Collection: %s || Notes: %s" % (experiment_tissue_coll, experiment_notes)
    #---No inoc, pathogen, notes ----
    elif experiment_tissue_coll != 'NULL' and experiment_tissue_coll != '':
      experiment_comments = "Tissue Collection: %s" % (experiment_tissue_coll)
    #---No tissue col, inoc, pathogen ----
    elif experiment_notes != 'NULL' and experiment_notes != '':
      experiment_comments = "Notes: %s" % (experiment_notes)
    #---No tissue coll, pathogen, notes ----
    elif experiment_inoc != 'NULL' and experiment_inoc != '':
      experiment_comments = "Inoculations: %s" % (experiment_inoc)
    #---No tissue coll, inoc, notes ----
    elif experiment_pathogen != 'NULL' and experiment_pathogen != '':
      experiment_comments = "Pathogen: %s" % (experiment_pathogen)
    else:
      experiment_comments = 'No Comments'

    #--- Check/add locality ----
    locality_experiment_hash = hash((experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country, 'NULL'))
    if (locality_experiment_hash) in locality_hash_table:
      pass
    else:
      locality_hash_table[(locality_experiment_hash)] = locality_id
      locality_table[(locality_id, experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country, 'NULL')] = locality_id
      print("Locality_id: %d" % (locality_id))
      locality_id = locality_id + 1

    #--- Check/add field---
    field_experiment_hash = hash((locality_hash_table[(locality_experiment_hash)], experiment_field_name))
    if (field_experiment_hash) in field_hash_table:
      pass
    else:
      field_hash_table[(field_experiment_hash)] = field_id
      field_name_table[(experiment_field_name)] = field_id
      field_table[(field_id, locality_hash_table[(locality_experiment_hash)], experiment_field_name)] = field_id
      print("Field_id: %d" % (field_id))
      field_id = field_id + 1

    #--- Check/add experiment ---
    experiment_exp_hash = hash((user_hash_table[(hash(experiment_user_username))], field_hash_table[(field_experiment_hash)], experiment_name, experiment_startdate, experiment_purpose, experiment_comments))
    if (experiment_exp_hash) in experiment_hash_table:
      pass
    else:
      experiment_hash_table[(experiment_exp_hash)] = experiment_id
      experiment_table[(experiment_id, user_hash_table[(hash(experiment_user_username))], field_hash_table[(field_experiment_hash)], experiment_name, experiment_startdate, experiment_purpose, experiment_comments)] = experiment_id
      experiment_name_table[experiment_name] = (experiment_id, user_hash_table[(hash(experiment_user_username))], field_hash_table[(field_experiment_hash)], experiment_name, experiment_startdate, experiment_purpose, experiment_comments)
      experiment_field_table[(experiment_name)] = field_hash_table[(field_experiment_hash)]
      print("Experiment_id: %d" % (experiment_id))
      experiment_id = experiment_id + 1

#------------------------------------------------------------------------
#- Information from row_table.csv is extracted
#- Seed_source_id is used to extract data from the legacy_seed and legacy_seedinventory tables. These variables are saved to obs_row, obs_selector, stock, stock_packet, passport, people, taxonomy, collecting, and location dictionaries.
#- Seed.plant_id_origin is used to extract data from the legacy_plant table. These variables are saved to obs_plant and obs_selector dictionaries.
#------------------------------------------------------------------------
  taxonomy_id = taxonomy_table.values()[-1] + 1
  obs_selector_id = obs_selector_table.values()[-1] + 1
  collecting_id = collecting_table.values()[-1] + 1
  people_id = people_table.values()[-1] + 1
  passport_id = passport_table.values()[-1] + 1
  stock_id = stock_table.values()[-1] + 1
  location_id = location_table.values()[-1] + 1
  obs_row_id = 1
  obs_plant_id = 1
  stock_packet_id = 1
  count_seed_not_in_seedinv = 1
  count_source_seed_not_in_seed = 1
  count_no_source_seed = 1

  row_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/nelson_lab_row_table_t1.1.csv'), dialect='excel')
  for row in row_file:
    row_row_id = row['row_id']
    row_row_name = row['row_name']
    row_experiment_name = row['experiment_id']
    row_stock_seed_id = row['source_seed_id']
    row_range = row['range']
    row_plot = row['plot']
    row_block = row['block']
    row_rep = row['rep']
    row_population = row['pop']
    row_purpose = row['purpose']
    row_notes = row['notes']
    row_kernel_num = row['kernel_num']
    row_stock_pedigree = row['pedigree']

    #--- Complete comment-----
    if row_purpose != 'NULL' and row_purpose != '' and row_notes != 'NULL' and row_notes != '':
      row_comments = "Purpose: %s || Notes: %s" % (row_purpose, row_notes)
    #--- No purpose----
    elif row_notes != 'NULL' and row_notes != '':
      row_comments = "Notes: %s" % (row_notes)
    #--- No notes-----
    elif row_purpose != 'NULL' and row_purpose != '':
      row_comments = "Purpose: %s" % (row_notes)
    else:
      row_comments = 'No Comments'

    if row_stock_seed_id != 0 and row_stock_seed_id !='':
      row_seed_id_hash = hash(row_stock_seed_id)
      if (row_seed_id_hash) in legacy_seed_table:
        seed = True
        if (legacy_seed_table[(row_seed_id_hash)][13]) in legacy_people_table:
          person = legacy_people_table[(legacy_seed_table[(row_seed_id_hash)][13])][1]
        else:
          person = 'unknown_person'
        if seed:
          legacy_seed_notes = legacy_seed_table[(row_seed_id_hash)][15]
          legacy_seed_lot = legacy_seed_table[(row_seed_id_hash)][17]
          legacy_seed_accession = legacy_seed_table[(row_seed_id_hash)][16]
          #---Complete comment---
          if legacy_seed_notes != 'NULL' and legacy_seed_notes != '' and legacy_seed_lot != 'NULL' and legacy_seed_lot != '' and legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
            seed_comments = 'Notes: %s || Lot: %s || Accession: %s' % (legacy_seed_notes, legacy_seed_lot, legacy_seed_accession)
          #---No accession---
          elif legacy_seed_notes != 'NULL' and legacy_seed_notes != '' and legacy_seed_lot != 'NULL' and legacy_seed_lot != '':
            seed_comments = 'Notes: %s || Lot: %s' % (legacy_seed_notes, legacy_seed_lot)
          #---No lot---
          elif legacy_seed_notes != 'NULL' and legacy_seed_notes != '' and legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
            seed_comments = 'Notes: %s || Accession: %s' % (legacy_seed_notes, legacy_seed_accession)
          #---No notes---
          elif legacy_seed_lot != 'NULL' and legacy_seed_lot != '' and legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
            seed_comments = 'Lot: %s || Accession: %s' % (legacy_seed_lot, legacy_seed_accession)
          #---No lot, accession---
          elif legacy_seed_notes != 'NULL' and legacy_seed_notes != '':
            seed_comments = 'Notes: %s' % (legacy_seed_notes)
          #---No notes, lot---
          elif legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
            seed_comments = 'Accession: %s' % (legacy_seed_accession)
          #---No notes, accession---
          elif legacy_seed_lot != 'NULL' and legacy_seed_lot != '':
            seed_comments = 'Lot: %s' % (legacy_seed_lot)
          else:
            seed_comments = 'No Comments'
        if legacy_seed_table[(row_seed_id_hash)][1] != 'NULL' and legacy_seed_table[(row_seed_id_hash)][1] != '':
          plant = True
        else:
          plant = False
        if (row_seed_id_hash) in legacy_seedinv_table:
          seedinv = True
        else:
          seedinv = False
          #--- Save to dictionary the seed_ids that are in seed, but not seedinv -----
          stock_not_inventoried[(count_seed_not_in_seedinv)] = (legacy_seed_table[(row_seed_id_hash)][0], legacy_seed_table[(row_seed_id_hash)][1], legacy_seed_table[(row_seed_id_hash)][2], legacy_seed_table[(row_seed_id_hash)][3], legacy_seed_table[(row_seed_id_hash)][4], legacy_seed_table[(row_seed_id_hash)][5], legacy_seed_table[(row_seed_id_hash)][6], legacy_seed_table[(row_seed_id_hash)][7], legacy_seed_table[(row_seed_id_hash)][8], legacy_seed_table[(row_seed_id_hash)][9], legacy_seed_table[(row_seed_id_hash)][10], legacy_seed_table[(row_seed_id_hash)][11], legacy_seed_table[(row_seed_id_hash)][12], legacy_seed_table[(row_seed_id_hash)][13], legacy_seed_table[(row_seed_id_hash)][14], legacy_seed_table[(row_seed_id_hash)][15], legacy_seed_table[(row_seed_id_hash)][16], legacy_seed_table[(row_seed_id_hash)][17])
          count_seed_not_in_seedinv = count_seed_not_in_seedinv + 1
      else:
        seed = False
        plant = False
        seedinv = False
        #--- Save to dictionary the rows with seed_ids which are not in legacy_seed ----
        row_source_seed_not_in_seed[(count_source_seed_not_in_seed)] = (row_row_id, row_row_name, row_experiment_name, row_stock_seed_id, row_range, row_plot, row_block, row_rep, row_population, row_purpose, row_notes, row_comments, row_kernel_num, row_stock_pedigree)
        count_source_seed_not_in_seed = count_source_seed_not_in_seed + 1
    else:
      seed = False
      plant = False
      seedinv = False
      #---- Save to dictinonary the rows with no source_seed ----
      row_no_source_seed[(count_no_source_seed)] = (row_row_id, row_row_name, row_experiment_name, row_stock_seed_id, row_range, row_plot, row_block, row_rep, row_population, row_purpose, row_notes, row_comments, row_kernel_num, row_stock_pedigree)
      count_no_source_seed = count_no_source_seed + 1

    #---- Check/add taxonomy to taxonomy_table ----
    taxonomy_row_hash = hash(('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa'))
    if (taxonomy_row_hash) in taxonomy_hash_table:
      pass
    else:
      taxonomy_hash_table[(taxonomy_row_hash)] = taxonomy_id
      taxonomy_table[(taxonomy_id, 'Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')] = taxonomy_id
      print("Taxonomy_id: %d" % (taxonomy_id))
      taxonomy_id = taxonomy_id + 1

    obs_selector_hash = hash((obs_selector_id, experiment_name_table[row_experiment_name][0]))
    obs_selector_hash_table[(obs_selector_hash)] = obs_selector_id
    obs_selector_table[(obs_selector_id, experiment_name_table[row_experiment_name][0])] = obs_selector_id
    print("ObsSelector: %d" % (obs_selector_id))
    obs_selector_id = obs_selector_id + 1

    if seed:
      collecting_row_hash = hash((obs_selector_hash_table[(obs_selector_hash)], user_hash_table[(hash(person))], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments'))
      collecting_hash_table[(collecting_row_hash)] = collecting_id
      collecting_table[(collecting_id, obs_selector_hash_table[(obs_selector_hash)], user_hash_table[(hash(person))], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')] = collecting_id
      print("Collecting_id: %d" % (collecting_id))
      collecting_id = collecting_id + 1

      people_row_hash = hash((legacy_seed_table[(row_seed_id_hash)][10]))
      if (people_row_hash) in people_hash_table:
        pass
      else:
        people_hash_table[(people_row_hash)] = people_id
        people_table[(people_id, legacy_seed_table[(row_seed_id_hash)][10])] = people_id
        print("People_id: %d" % (people_id))
        people_id = people_id + 1

      passport_row_hash = hash((collecting_hash_table[(collecting_row_hash)], people_hash_table[(people_row_hash)], taxonomy_hash_table[(taxonomy_row_hash)]))
      if (passport_row_hash) in passport_hash_table:
        pass
      else:
        passport_hash_table[(passport_row_hash)] = passport_id
        passport_table[(passport_id, collecting_hash_table[(collecting_row_hash)], people_hash_table[(people_row_hash)], taxonomy_hash_table[(taxonomy_row_hash)])] = passport_id
        print("Passport_id: %d" % (passport_id))
        passport_id = passport_id + 1

      if seedinv:
        stock_row_hash = hash((passport_hash_table[(passport_row_hash)], legacy_seed_table[(row_seed_id_hash)][0], legacy_seed_table[(row_seed_id_hash)][6], legacy_seed_table[(row_seed_id_hash)][7], legacy_seed_table[(row_seed_id_hash)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_seed_id_hash)][3], seed_comments))
        if (stock_row_hash) in stock_hash_table:
          pass
        else:
          stock_hash_table[(stock_row_hash)] = stock_id
          stock_table[(stock_id, passport_hash_table[(passport_row_hash)], legacy_seed_table[(row_seed_id_hash)][0], legacy_seed_table[(row_seed_id_hash)][6], legacy_seed_table[(row_seed_id_hash)][7], legacy_seed_table[(row_seed_id_hash)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_seed_id_hash)][3], seed_comments)] = stock_id
          stock_seed_id_table[(legacy_seed_table[(row_seed_id_hash)][0])] = (stock_id)
          print("Stock_id: %d" % (stock_id))
          stock_id = stock_id + 1

        obs_row_table[(obs_row_id, obs_selector_hash_table[(obs_selector_hash)], experiment_field_table[(row_experiment_name)], stock_hash_table[(stock_row_hash)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)] = obs_row_id
        obs_row_intermed_table[(row_row_id)] = (obs_row_id, obs_selector_hash_table[(obs_selector_hash)], experiment_field_table[(row_experiment_name)], stock_hash_table[(stock_row_hash)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)
        print("ObsRow_id: %d" % obs_row_id)
        obs_row_id = obs_row_id + 1

        locality_stockpacket_hash = hash(('Ithaca', 'NY', 'USA', 'NULL'))
        if (locality_stockpacket_hash) in locality_hash_table:
          pass
        else:
          locality_hash_table[(locality_stockpacket_hash)] = locality_id
          locality_table[(locality_id, 'Ithaca', 'NY', 'USA', 'NULL')] = locality_id
          print("Locality_id: %d" % (locality_id))
          locality_id = locality_id + 1

        location_row_hash = hash((locality_hash_table[(locality_stockpacket_hash)], legacy_seedinv_table[(row_seed_id_hash)][6], 'Cold Storage', 'Unknown'))
        if (location_row_hash) in location_hash_table:
          pass
        else:
          location_hash_table[(location_row_hash)] = location_id
          location_table[(location_id, locality_hash_table[(locality_stockpacket_hash)], legacy_seedinv_table[(row_seed_id_hash)][6], 'Cold Storage', 'Unknown')] = location_id
          print("Location_id: %d" % (location_id))
          location_id = location_id + 1

        stock_packet_hash = hash((stock_hash_table[(stock_row_hash)], location_hash_table[(location_row_hash)], legacy_seedinv_table[(row_seed_id_hash)][8], legacy_seedinv_table[(row_seed_id_hash)][7]))
        if (stock_packet_hash) in stock_packet_hash_table:
          pass
        else:
          stock_packet_hash_table[(stock_packet_hash)] = stock_packet_id
          stock_packet_table[(stock_packet_id, stock_hash_table[(stock_row_hash)], location_hash_table[(location_row_hash)], legacy_seedinv_table[(row_seed_id_hash)][8], legacy_seedinv_table[(row_seed_id_hash)][7])] = stock_packet_id
          print("Stockpacket_id: %d" % (stock_packet_id))
          stock_packet_id = stock_packet_id + 1

      #--------- No Seedinv --------------------------------
      else:
        stock_row_hash = hash((passport_hash_table[(passport_row_hash)], legacy_seed_table[(row_seed_id_hash)][0], legacy_seed_table[(row_seed_id_hash)][6], legacy_seed_table[(row_seed_id_hash)][7], legacy_seed_table[(row_seed_id_hash)][11], 'Not Inventoried', 'Not Inventoried', seed_comments))
        if (stock_row_hash) in stock_hash_table:
          pass
        else:
          stock_hash_table[(stock_row_hash)] = stock_id
          stock_table[(stock_id, passport_hash_table[(passport_row_hash)], legacy_seed_table[(row_seed_id_hash)][0], legacy_seed_table[(row_seed_id_hash)][6], legacy_seed_table[(row_seed_id_hash)][7], legacy_seed_table[(row_seed_id_hash)][11], 'Not Inventoried', 'Not Inventoried', seed_comments)] = stock_id
          stock_seed_id_table[(legacy_seed_table[(row_seed_id_hash)][0])] = (stock_id)
          print("Stock_id: %d" % (stock_id))
          stock_id = stock_id + 1

        obs_row_table[(obs_row_id, obs_selector_hash_table[(obs_selector_hash)], experiment_field_table[(row_experiment_name)], stock_hash_table[(stock_row_hash)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)] = obs_row_id
        obs_row_intermed_table[(row_row_id)] = (obs_row_id, obs_selector_hash_table[(obs_selector_hash)], experiment_field_table[(row_experiment_name)], stock_hash_table[(stock_row_hash)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)
        print("ObsRow_id: %d" % obs_row_id)
        obs_row_id = obs_row_id + 1

    #-------- No Legacy Seed info ----------------
    else:
      collecting_row_hash = hash((obs_selector_table[(1,1)], user_hash_table[(hash('unknown'))], 1, 'No Collecting', 'No Collecting', 'No Collecting'))
      if (collecting_row_hash) in collecting_hash_table:
        pass
      else:
        collecting_hash_table[(collecting_row_hash)] = collecting_id
        collecting_table[(collecting_id, obs_selector_table[(1,1)], user_hash_table[(hash('unknown'))], 1, 'No Collecting', 'No Collecting', 'No Collecting')] = collecting_id
        print("Collecting_id: %d" % (collecting_id))
        collecting_id = collecting_id + 1

      passport_row_hash = hash((collecting_hash_table[(collecting_row_hash)], 1, taxonomy_hash_table[(taxonomy_row_hash)]))
      if (passport_row_hash) in passport_hash_table:
        pass
      else:
        passport_hash_table[(passport_row_hash)] = passport_id
        passport_table[(passport_id, collecting_hash_table[(collecting_row_hash)], 1, taxonomy_hash_table[(taxonomy_row_hash)])] = passport_id
        print("Passport_id: %d" % passport_id)
        passport_id = passport_id + 1

      stock_row_hash = hash((passport_hash_table[(passport_row_hash)], 0, 'No Seed', 'No Seed', 'No Seed', 'Not Inventoried', 'Not Inventoried', 'No Seed'))
      if (stock_row_hash) in stock_hash_table:
        pass
      else:
        stock_hash_table[(stock_row_hash)] = stock_id
        stock_table[(stock_id, passport_hash_table[(passport_row_hash)], 0, 'No Seed', 'No Seed', 'No Seed', 'Not Inventoried', 'Not Inventoried', 'No Seed')] = stock_id
        print("Stock_id: %d" % stock_id)
        stock_id = stock_id + 1

      obs_row_table[(obs_row_id, obs_selector_hash_table[(obs_selector_hash)], experiment_field_table[(row_experiment_name)], stock_hash_table[(stock_row_hash)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)] = obs_row_id
      obs_row_intermed_table[(row_row_id)] = (obs_row_id, obs_selector_hash_table[(obs_selector_hash)], experiment_field_table[(row_experiment_name)], stock_hash_table[(stock_row_hash)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)
      print("ObsRow_id: %d" % obs_row_id)
      obs_row_id = obs_row_id + 1

    #---------- If there is plant info in the Legacy Plant table -----------------
    if seed:
      if plant:
        if (legacy_seed_table[(row_seed_id_hash)][1]) in legacy_plant_table:

          obs_selector_table[(obs_selector_id, experiment_name_table[row_experiment_name][0])] = obs_selector_id
          print("ObsSelector: %d" % (obs_selector_id))
          obs_selector_id = obs_selector_id + 1

          if (obs_selector_table.values()[-1], obs_row_intermed_table[(row_row_id)][0], legacy_plant_table[(legacy_seed_table[(row_seed_id_hash)][1])][0], legacy_plant_table[(legacy_seed_table[(row_seed_id_hash)][1])][2], legacy_plant_table[(legacy_seed_table[(row_seed_id_hash)][1])][3]) in obs_plant_table:
            pass
          else:
            obs_plant_table[(obs_plant_id, obs_selector_table.values()[-1], obs_row_intermed_table[(row_row_id)][0], legacy_plant_table[(legacy_seed_table[(row_seed_id_hash)][1])][0], legacy_plant_table[(legacy_seed_table[(row_seed_id_hash)][1])][2], legacy_plant_table[(legacy_seed_table[(row_seed_id_hash)][1])][3])] = obs_plant_id
            print("ObsPlant_id: %d" % (obs_plant_id))
            obs_plant_id = obs_plant_id + 1

#---------------------------------------------------------------------------
#- Info from isolate.csv is extracted and saved to disease_info, taxonomy, locality, field, collecting, passport, location, and isolate dictionaries.
#---------------------------------------------------------------------------

  isolate_table_id = 1
  disease_info_id = 1

  isolate_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/nelson_lab_isolate_table.csv'), dialect='excel')
  for row in isolate_file:
    isolate_id = row['isolate_id']
    isolate_name = row['isolate_name']
    isolate_taxonomy_genus = row['scientific_name']
    isolate_taxonomy_alias = row['other_sname']
    isolate_taxonomy_race = row['pathotype_race']
    disease_info_common_name = row['disease_common_name']
    isolate_field_name = row['collection_site']
    isolate_city = row['city']
    isolate_state = row['state']
    isolate_country = row['country']
    isolate_collection_date = row['collection_date']
    isolate_plant_organ = row['plant_organ']
    isolate_collection_user = row['collector']
    isolate_people_organization = row['provider']
    location_n80c_boxname = row['n80c']
    location_4c_boxname = row['4c']
    isolate_comments = row['notes']
    isolate_subtaxa = row['mating_type']

    disease_info_hash = hash((disease_info_common_name))
    if (disease_info_hash) in disease_info_hash_table:
      pass
    else:
      disease_info_hash_table[(disease_info_hash)] = disease_info_id
      disease_info_table[(disease_info_id, disease_info_common_name)] = disease_info_id
      print("Disease_info_id: %d" % (disease_info_id))
      disease_info_id = disease_info_id + 1

    taxonomy_isolate_hash = hash((isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa))
    if (taxonomy_isolate_hash) in taxonomy_hash_table:
      pass
    else:
      taxonomy_hash_table[(taxonomy_isolate_hash)] = taxonomy_id
      taxonomy_table[(taxonomy_id, isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa)] = taxonomy_id
      print("Taxonomy_id: %d" % (taxonomy_id))
      taxonomy_id = taxonomy_id + 1

    locality_isolate_hash= hash((isolate_city, isolate_state, isolate_country, 'NULL'))
    if (locality_isolate_hash) in locality_hash_table:
      pass
    else:
      locality_hash_table[(locality_isolate_hash)] = locality_id
      locality_table[(locality_id, isolate_city, isolate_state, isolate_country, 'NULL')] = locality_id
      print("Locality_id: %d" % (locality_id))
      locality_id = locality_id + 1

    field_isolate_hash = hash((locality_hash_table[(locality_isolate_hash)], isolate_field_name))
    if (field_isolate_hash) in field_hash_table:
      pass
    else:
      field_hash_table[(field_isolate_hash)] = field_id
      field_name_table[(isolate_field_name)] = field_id
      field_table[(field_id, locality_hash_table[(locality_isolate_hash)], isolate_field_name)] = field_id
      print("Field_id: %d" % (field_id))
      field_id = field_id + 1

    collecting_isolate_hash = hash((obs_selector_table[(1,1)], user_hash_table[(hash(isolate_collection_user))], field_hash_table[(field_isolate_hash)], isolate_collection_date, 'Unknown', 'No Comments'))
    if (collecting_isolate_hash) in collecting_hash_table:
      pass
    else:
      collecting_hash_table[(collecting_isolate_hash)] = collecting_id
      collecting_table[(collecting_id, obs_selector_table[(1,1)], user_hash_table[(hash(isolate_collection_user))], field_hash_table[(field_isolate_hash)], isolate_collection_date, 'Unknown', 'No Comments')] = collecting_id
      print("Collecting_id: %d" % (collecting_id))
      collecting_id = collecting_id + 1

    passport_isolate_hash = hash((collecting_hash_table[(collecting_isolate_hash)], 1, taxonomy_hash_table[(taxonomy_isolate_hash)]))
    if (passport_isolate_hash) in passport_hash_table:
      pass
    else:
      passport_hash_table[(passport_isolate_hash)] = passport_id
      passport_table[(passport_id, collecting_hash_table[(collecting_isolate_hash)], 1, taxonomy_hash_table[(taxonomy_isolate_hash)])] = passport_id
      print("Passport_id: %d" % (passport_id))
      passport_id = passport_id + 1

    #------------------- If location is in n80c freezer ----------------------
    if location_n80c_boxname != 'NULL' and location_n80c_boxname != '':
      location_isolate_hash = hash((locality_hash_table[(locality_isolate_hash)], 'Plant Science', 'Freezer -80C', location_n80c_boxname))
      if (location_isolate_hash) in location_hash_table:
        pass
      else:
        location_hash_table[(location_isolate_hash)] = location_id
        location_table[(location_id, locality_hash_table[(locality_isolate_hash)], 'Plant Science', 'Freezer -80C', location_n80c_boxname)] = location_id
        print("Location_id: %d" % (location_id))
        location_id = location_id + 1

      isolate_iso_hash = hash((passport_hash_table[(passport_isolate_hash)], location_hash_table[(location_isolate_hash)], disease_info_hash_table[(disease_info_hash)], isolate_id, isolate_name, isolate_comments))
      if (isolate_iso_hash) in isolate_hash_table:
        pass
      else:
        isolate_hash_table[(isolate_iso_hash)] = isolate_table_id
        isolate_table[(isolate_table_id, passport_hash_table[(passport_isolate_hash)], location_hash_table[(location_isolate_hash)], disease_info_hash_table[(disease_info_hash)], isolate_id, isolate_name, isolate_comments)] = isolate_table_id
        print("Isolate_table_id: %d" % (isolate_table_id))
        isolate_table_id = isolate_table_id + 1

    #-------------- If location is in 4c freezer -----------------------------------
    elif location_4c_boxname != 'NULL' and location_4c_boxname != '':
      location_isolate_hash = hash((locality_hash_table[(locality_isolate_hash)], 'Plant Science', 'Freezer 4C', location_4c_boxname))
      if (location_isolate_hash) in location_hash_table:
        pass
      else:
        location_hash_table[(location_isolate_hash)] = location_id
        location_table[(location_id, locality_hash_table[(locality_isolate_hash)], 'Plant Science', 'Freezer 4C', location_4c_boxname)] = location_id
        print("Location_id: %d" % (location_id))
        location_id = location_id + 1

      isolate_iso_hash = hash((passport_hash_table[(passport_isolate_hash)], location_hash_table[(location_isolate_hash)], disease_info_hash_table[(disease_info_hash)], isolate_id, isolate_name, isolate_comments))
      if (isolate_iso_hash) in isolate_hash_table:
        pass
      else:
        isolate_hash_table[(isolate_iso_hash)] = isolate_table_id
        isolate_table[(isolate_table_id, passport_hash_table[(passport_isolate_hash)], location_hash_table[(location_isolate_hash)], disease_info_hash_table[(disease_info_hash)], isolate_id, isolate_name, isolate_comments)] = isolate_table_id
        print("Isolate_table_id: %d" % (isolate_table_id))
        isolate_table_id = isolate_table_id + 1

    #-------------------- location not in -80c or 4c freezer ----------------------
    else:
      location_isolate_hash = hash((locality_hash_table[(locality_isolate_hash)], 'Unknown', 'Unknown', 'Unknown'))
      if (location_isolate_hash) in location_hash_table:
        pass
      else:
        location_hash_table[(location_isolate_hash)] = location_id
        location_table[(location_id, locality_hash_table[(locality_isolate_hash)], 'Unknown', 'Unknown', 'Unknown')] = location_id
        print("Location_id: %d" % (location_id))
        location_id = location_id + 1

      isolate_iso_hash = hash((passport_hash_table[(passport_isolate_hash)], location_hash_table[(location_isolate_hash)], disease_info_hash_table[(disease_info_hash)], isolate_id, isolate_name, isolate_comments))
      if (isolate_iso_hash) in isolate_hash_table:
        pass
      else:
        isolate_hash_table[(isolate_iso_hash)] = isolate_table_id
        isolate_table[(isolate_table_id, passport_hash_table[(passport_isolate_hash)], location_hash_table[(location_isolate_hash)], disease_info_hash_table[(disease_info_hash)], isolate_id, isolate_name, isolate_comments)] = isolate_table_id
        print("Isolate_table_id: %d" % (isolate_table_id))
        isolate_table_id = isolate_table_id + 1


#------------------------------------------------------------------------
#--- Load measurement param info into memory----
#------------------------------------------------------------------------

    param_info_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/measurement_parameter_info.csv'), dialect='excel')
    for row in param_info_file:
      param_info_parameter = row['trait_id']
      param_info_parameter_type = row['trait']
      param_info_unit = row['unit']
      param_info_protocol = row['description']

      measurement_parameter_info_table[(param_info_parameter)] = (param_info_parameter, param_info_parameter_type, param_info_unit, param_info_protocol)


#------------------------------------------------------------------------
#- Import phenotype.csv for row data and save data to measurement amd measurementparameter dictionaries
#------------------------------------------------------------------------

  measurement_param_id = 1
  measurement_id = 1
  measurement_not_in_row_count = 1

  phenotype_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/nelson_lab_phenotype_row_table.csv'), dialect='excel')
  for row in phenotype_file:
    phenotype_row_id = row['entity_id']
    phenotype_experiment_name = row['experiment_id']
    phenotype_trait_id = row['trait_id']
    phenotype_value = row['phenotype_value']
    phenotype_date = row['phenotype_date']
    phenotype_plate_id = row['plate_id']
    phenotype_person_id = row['phenotype_person_id']
    phenotype_scoring_order = row['scoring_order']
    phenotype_notes = row['notes']
    phenotype_changed = row['changed']
    phenotype_technical_rep = row['technical_rep']
    phenotype_biological_rep = row['biological_rep']
    phenotype_trait_id_buckler = row['trait_id_buckler']

    #---Complete comment----
    if phenotype_notes != 'NULL' and phenotype_notes != '' and phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '' and phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '' and phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Notes: %s || Scoreing Order: %s || Technical Rep: %s || Biological Rep: %s' % (phenotype_notes, phenotype_scoring_order, phenotype_technical_rep, phenotype_biological_rep)
    #---No scoring order----
    elif phenotype_notes != 'NULL' and phenotype_notes != '' and phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '' and phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Notes: %s || Technical Rep: %s || Biological Rep: %s' % (phenotype_notes, phenotype_technical_rep, phenotype_biological_rep)
    #---No notes-----
    elif phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '' and phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '' and phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Scoreing Order: %s || Technical Rep: %s || Biological Rep: %s' % (phenotype_scoring_order, phenotype_technical_rep, phenotype_biological_rep)
    #---No technical rep----
    elif phenotype_notes != 'NULL' and phenotype_notes != '' and phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '' and phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Notes: %s || Scoreing Order: %s || Biological Rep: %s' % (phenotype_notes, phenotype_scoring_order, phenotype_biological_rep)
    #---No biological rep----
    elif phenotype_notes != 'NULL' and phenotype_notes != '' and phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '' and phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '':
      phenotype_comments = 'Notes: %s || Scoreing Order: %s || Technical Rep: %s' % (phenotype_notes, phenotype_scoring_order, phenotype_technical_rep)
    #---No notes, scoring order---
    elif phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '' and phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Technical Rep: %s || Biological Rep: %s' % (phenotype_technical_rep, phenotype_biological_rep)
    #---No notes, technical rep----
    elif phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '' and phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Scoreing Order: %s || Biological Rep: %s' % (phenotype_scoring_order, phenotype_biological_rep)
    #---No notes, biological rep-----
    elif phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '' and phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '':
      phenotype_comments = 'Scoreing Order: %s || Technical Rep: %s' % (phenotype_scoring_order, phenotype_technical_rep)
    #---No technical rep, biological rep ----
    elif phenotype_notes != 'NULL' and phenotype_notes != '' and phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '':
      phenotype_comments = 'Notes: %s || Scoreing Order: %s' % (phenotype_notes, phenotype_scoring_order)
    #---No scoring order, technical rep----
    elif phenotype_notes != 'NULL' and phenotype_notes != '' and phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Notes: %s || Biological Rep: %s' % (phenotype_notes, phenotype_biological_rep)
    #---No scoring order, biological rep----
    elif phenotype_notes != 'NULL' and phenotype_notes != '' and phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '':
      phenotype_comments = 'Notes: %s || Technical Rep: %s' % (phenotype_notes, phenotype_technical_rep)
    #---No notes, scoring order, technical rep----
    elif phenotype_biological_rep != 'NULL' and phenotype_biological_rep != '':
      phenotype_comments = 'Biological Rep: %s' % (phenotype_biological_rep)
    #---No notes, scoring order, biological rep---
    elif phenotype_technical_rep != 'NULL' and phenotype_technical_rep != '':
      phenotype_comments = 'Technical Rep: %s' % (phenotype_technical_rep)
    #---No scoring order, technical rep, biological rep----
    elif phenotype_notes != 'NULL' and phenotype_notes != '':
      phenotype_comments = 'Notes: %s' % (phenotype_notes)
    #---No notes, technical rep, biological rep----
    elif phenotype_scoring_order != 'NULL' and phenotype_scoring_order != '':
      phenotype_comments = 'Scoreing Order: %s' % (phenotype_scoring_order)
    else:
      phenotype_comments = 'No Comments'


    #---- Translate person_id to person_name, so that user_hash_table[(person_name)] works -------
    if phenotype_person_id != '':
      phenotype_user = legacy_people_table[(phenotype_person_id)][1]
    else:
      phenotype_user = 'unknown_person'

    if (phenotype_trait_id) in measurement_parameter_info_table:
        measurement_param_hash = hash((phenotype_trait_id, measurement_parameter_info_table[(phenotype_trait_id)][1], measurement_parameter_info_table[(phenotype_trait_id)][2], measurement_parameter_info_table[(phenotype_trait_id)][3], phenotype_trait_id_buckler))
        if (measurement_param_hash) in measurement_param_hash_table:
          pass
        else:
          measurement_param_hash_table[(measurement_param_hash)] = measurement_param_id
          measurement_param_table[(measurement_param_id, phenotype_trait_id, measurement_parameter_info_table[(phenotype_trait_id)][1], measurement_parameter_info_table[(phenotype_trait_id)][2], measurement_parameter_info_table[(phenotype_trait_id)][3], phenotype_trait_id_buckler)] = measurement_param_id
          print("Measurement_param: %d" % (measurement_param_id))
          measurement_param_id = measurement_param_id + 1
    else:
        measurement_param_hash = hash((phenotype_trait_id, 'Unknown', 'Unknown', 'Unknown', phenotype_trait_id_buckler))
        if (measurement_param_hash) in measurement_param_hash_table:
          pass
        else:
          measurement_param_hash_table[(measurement_param_hash)] = measurement_param_id
          measurement_param_table[(measurement_param_id, phenotype_trait_id, 'Unknown', 'Unknown', 'Unknown', phenotype_trait_id_buckler)] = measurement_param_id
          print("Measurement_param: %d" % (measurement_param_id))
          measurement_param_id = measurement_param_id + 1

    if (phenotype_row_id) in obs_row_intermed_table:
      measurement_hash = hash((obs_row_intermed_table[(phenotype_row_id)][1], user_hash_table[(hash(phenotype_user))], measurement_param_hash_table[(measurement_param_hash)], phenotype_date, phenotype_value, phenotype_comments))
      if (measurement_hash) in measurement_hash_table:
        pass
      else:
        measurement_hash_table[(measurement_hash)] = measurement_id
        measurement_table[(measurement_id, obs_row_intermed_table[(phenotype_row_id)][1], user_hash_table[(hash(phenotype_user))], measurement_param_hash_table[(measurement_param_hash)], phenotype_date, phenotype_value, phenotype_comments)] = measurement_id
        print("Measurement: %d" % (measurement_id))
        measurement_id = measurement_id + 1
    else:
      phenotype_row_not_in_row[(measurement_not_in_row_count)] = (phenotype_row_id, phenotype_experiment_name, phenotype_trait_id, phenotype_value, phenotype_date, phenotype_plate_id, phenotype_person_id, phenotype_scoring_order, phenotype_notes, phenotype_changed, phenotype_technical_rep, phenotype_biological_rep, phenotype_trait_id_buckler)


#------------------------------------------------------------------------
#--- Check which seed_ids are in legacy_seed but not in stock_table ----
#------------------------------------------------------------------------
  legacy_seed_not_in_stock_count = 1

  legacy_seed_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/legacy_seed_table.csv'), dialect='excel')
  for row in legacy_seed_file:
    legacy_seed_id = row["seed_id"]
    legacy_plant_id_origin = row["plant_id_origin"]
    legacy_row_id_origin = row["row_id_origin"]
    legacy_experiment_id_origin = row["experiment_id_origin_id"]
    legacy_plant_name = row["plant_name"]
    legacy_row_name = row["row_name"]
    legacy_seed_name = row["seed_name"]
    legacy_cross_type = row["cross_type"]
    legacy_male_parent_id = row["male_parent_id"]
    legacy_male_parent_name = row["male_parent_name"]
    legacy_program_origin = row["program_origin"]
    legacy_seed_pedigree = row["seed_pedigree"]
    legacy_line_num = row["line_num"]
    legacy_seed_person_id = row["seed_person_id"]
    legacy_seed_disease_info = row["disease_info"]
    legacy_seed_notes = row["notes"]
    legacy_seed_accession = row["accession"]
    legacy_seed_lot = row["lot"]

    if (legacy_seed_id) in stock_table:
      pass
    else:
      #---Complete comment---
      if legacy_seed_notes != 'NULL' and legacy_seed_notes != '' and legacy_seed_lot != 'NULL' and legacy_seed_lot != '' and legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
        seed_comments = 'Notes: %s || Lot: %s || Accession: %s' % (legacy_seed_notes, legacy_seed_lot, legacy_seed_accession)
      #---No accession---
      elif legacy_seed_notes != 'NULL' and legacy_seed_notes != '' and legacy_seed_lot != 'NULL' and legacy_seed_lot != '':
        seed_comments = 'Notes: %s || Lot: %s' % (legacy_seed_notes, legacy_seed_lot)
      #---No lot---
      elif legacy_seed_notes != 'NULL' and legacy_seed_notes != '' and legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
        seed_comments = 'Notes: %s || Accession: %s' % (legacy_seed_notes, legacy_seed_accession)
      #---No notes---
      elif legacy_seed_lot != 'NULL' and legacy_seed_lot != '' and legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
        seed_comments = 'Lot: %s || Accession: %s' % (legacy_seed_lot, legacy_seed_accession)
      #---No lot, accession---
      elif legacy_seed_notes != 'NULL' and legacy_seed_notes != '':
        seed_comments = 'Notes: %s' % (legacy_seed_notes)
      #---No notes, lot---
      elif legacy_seed_accession != 'NULL' and legacy_seed_accession != '':
        seed_comments = 'Accession: %s' % (legacy_seed_accession)
      #---No notes, accession---
      elif legacy_seed_lot != 'NULL' and legacy_seed_lot != '':
        seed_comments = 'Lot: %s' % (legacy_seed_lot)
      else:
        seed_comments = 'No Comments'

      legacy_seed_not_in_stock[(legacy_seed_not_in_stock_count)] = (legacy_seed_id, legacy_plant_id_origin, legacy_row_id_origin, legacy_experiment_id_origin, legacy_plant_name, legacy_row_name, legacy_seed_name, legacy_cross_type, legacy_male_parent_id, legacy_male_parent_name, legacy_program_origin, legacy_seed_pedigree, legacy_line_num, legacy_seed_person_id, legacy_seed_disease_info, legacy_seed_notes, legacy_seed_accession, legacy_seed_lot)
      legacy_seed_not_in_stock_count = legacy_seed_not_in_stock_count + 1

      #-------------If an obs_row entry is found for row_id ---------------------
      if (legacy_row_id_origin) in obs_row_intermed_table:

        legacy_seed_collecting_hash = hash((obs_row_intermed_table[(legacy_row_id_origin)][1], user_hash_table[(hash(legacy_people_table[(legacy_seed_person_id)][1]))], field_name_table[(legacy_experiment_table[(legacy_experiment_id_origin)][1])], legacy_experiment_table[(legacy_experiment_id_origin)][9], 'Field Harvest', 'No Comments'))
        if (legacy_seed_collecting_hash) in collecting_hash_table:
          pass
        else:
          collecting_hash_table[(legacy_seed_collecting_hash)] = collecting_id
          collecting_table[(collecting_id, obs_row_intermed_table[(legacy_row_id_origin)][1], user_hash_table[(hash(legacy_people_table[(legacy_seed_person_id)][1]))], field_name_table[(legacy_experiment_table[(legacy_experiment_id_origin)][1])], legacy_experiment_table[(legacy_experiment_id_origin)][9], 'Field Harvest', 'No Comments')] = collecting_id
          collecting_id = collecting_id + 1

        taxonomy_hash = hash(('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy'))
        legacy_seed_people_hash = hash((legacy_program_origin))
        if (legacy_seed_people_hash) in people_hash_table:
          pass
        else:
          people_hash_table[(legacy_seed_people_hash)] = people_id
          people_table[(people_id, legacy_program_origin)] = people_id
          people_id = people_id + 1

        legacy_seed_passport_hash = hash((collecting_hash_table[(legacy_seed_collecting_hash)], people_hash_table[(legacy_seed_people_hash)], taxonomy_hash_table[(taxonomy_hash)]))
        if (legacy_seed_passport_hash) in passport_hash_table:
          pass
        else:
          passport_hash_table[(legacy_seed_passport_hash)] = passport_id
          passport_table[(passport_id, collecting_hash_table[(legacy_seed_collecting_hash)], people_hash_table[(legacy_seed_people_hash)], taxonomy_hash_table[(taxonomy_hash)])] = passport_id
          passport_id = passport_id + 1

        #------------ If in seedinv --------------------
        if (hash((legacy_seed_id))) in legacy_seedinv_table:

          legacy_seed_stock_hash = hash((passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Inventoried', legacy_seedinv_table[(hash((legacy_seed_id)))][3], seed_comments))
          if (legacy_seed_stock_hash) in stock_hash_table:
            pass
          else:
            stock_hash_table[(legacy_seed_stock_hash)] = stock_id
            stock_table[(stock_id, passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Inventoried', legacy_seedinv_table[(hash((legacy_seed_id)))][3], seed_comments)] = stock_id
            stock_id = stock_id + 1

          legacy_seed_locality_hash = hash(('Ithaca', 'NY', 'USA', 'NULL'))
          if (legacy_seed_locality_hash) in locality_hash_table:
            pass
          else:
            locality_hash_table[(legacy_seed_locality_hash)] = locality_id
            locality_table[(locality_id, 'Ithaca', 'NY', 'USA', 'NULL')] = locality_id
            locality_id = locality_id + 1

          legacy_seed_location_hash = hash((locality_hash_table[(legacy_seed_locality_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][6], 'Cold Storage', 'Unknown'))
          if (legacy_seed_location_hash) in location_hash_table:
            pass
          else:
            location_hash_table[(legacy_seed_location_hash)] = location_id
            location_table[(location_id, locality_hash_table[(legacy_seed_locality_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][6], 'Cold Storage', 'Unknown')] = location_id
            location_id = location_id + 1

          legacy_seed_stock_packet_hash = hash((stock_hash_table[(legacy_seed_stock_hash)], location_hash_table[(legacy_seed_location_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][8], legacy_seedinv_table[(hash((legacy_seed_id)))][7]))
          if (legacy_seed_stock_packet_hash) in stock_packet_hash_table:
            pass
          else:
            stock_packet_hash_table[(legacy_seed_stock_packet_hash)] = stock_packet_id
            stock_packet_table[(stock_packet_id, stock_hash_table[(legacy_seed_stock_hash)], location_hash_table[(legacy_seed_location_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][8], legacy_seedinv_table[(hash((legacy_seed_id)))][7])] = stock_packet_id
            stock_packet_id = stock_packet_id + 1

        #-------- Not in seedinv --------------
        else:
          legacy_seed_stock_hash = hash((passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Not Inventoried', 'Not Invetoried', seed_comments))
          if (legacy_seed_stock_hash) in stock_hash_table:
            pass
          else:
            stock_hash_table[(legacy_seed_stock_hash)] = stock_id
            stock_table[(stock_id, passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Not Inventoried', 'Not Invetoried', seed_comments)] = stock_id
            stock_id = stock_id + 1

      #----------- No obs_row entry found for row_id -----------
      else:
        legacy_seed_collecting_hash = hash((1, user_hash_table[(hash(legacy_people_table[(legacy_seed_person_id)][1]))], field_name_table[(legacy_experiment_table[(legacy_experiment_id_origin)][1])], legacy_experiment_table[(legacy_experiment_id_origin)][9], 'Field Harvest', 'No Comments'))
        if (legacy_seed_collecting_hash) in collecting_hash_table:
          pass
        else:
          collecting_hash_table[(legacy_seed_collecting_hash)] = collecting_id
          collecting_table[(collecting_id, 1, user_hash_table[(hash(legacy_people_table[(legacy_seed_person_id)][1]))], field_name_table[(legacy_experiment_table[(legacy_experiment_id_origin)][1])], legacy_experiment_table[(legacy_experiment_id_origin)][9], 'Field Harvest', 'No Comments')] = collecting_id
          collecting_id = collecting_id + 1

        taxonomy_hash = hash(('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy'))
        legacy_seed_people_hash = hash((legacy_program_origin))
        if (legacy_seed_people_hash) in people_hash_table:
          pass
        else:
          people_hash_table[(legacy_seed_people_hash)] = people_id
          people_table[(people_id, legacy_program_origin)] = people_id
          people_id = people_id + 1

        legacy_seed_passport_hash = hash((collecting_hash_table[(legacy_seed_collecting_hash)], people_hash_table[(legacy_seed_people_hash)], taxonomy_hash_table[(taxonomy_hash)]))
        if (legacy_seed_passport_hash) in passport_hash_table:
          pass
        else:
          passport_hash_table[(legacy_seed_passport_hash)] = passport_id
          passport_table[(passport_id, collecting_hash_table[(legacy_seed_collecting_hash)], people_hash_table[(legacy_seed_people_hash)], taxonomy_hash_table[(taxonomy_hash)])] = passport_id
          passport_id = passport_id + 1

        #------------ If in seedinv --------------------
        if (hash((legacy_seed_id))) in legacy_seedinv_table:

          legacy_seed_stock_hash = hash((passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Inventoried', legacy_seedinv_table[(hash((legacy_seed_id)))][3], seed_comments))
          if (legacy_seed_stock_hash) in stock_hash_table:
            pass
          else:
            stock_hash_table[(legacy_seed_stock_hash)] = stock_id
            stock_table[(stock_id, passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Inventoried', legacy_seedinv_table[(hash((legacy_seed_id)))][3], seed_comments)] = stock_id
            stock_id = stock_id + 1

          legacy_seed_locality_hash = hash(('Ithaca', 'NY', 'USA', 'NULL'))
          if (legacy_seed_locality_hash) in locality_hash_table:
            pass
          else:
            locality_hash_table[(legacy_seed_locality_hash)] = locality_id
            locality_table[(locality_id, 'Ithaca', 'NY', 'USA', 'NULL')] = locality_id
            locality_id = locality_id + 1

          legacy_seed_location_hash = hash((locality_hash_table[(legacy_seed_locality_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][6], 'Cold Storage', 'Unknown'))
          if (legacy_seed_location_hash) in location_hash_table:
            pass
          else:
            location_hash_table[(legacy_seed_location_hash)] = location_id
            location_table[(location_id, locality_hash_table[(legacy_seed_locality_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][6], 'Cold Storage', 'Unknown')] = location_id
            location_id = location_id + 1

          legacy_seed_stock_packet_hash = hash((stock_hash_table[(legacy_seed_stock_hash)], location_hash_table[(legacy_seed_location_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][8], legacy_seedinv_table[(hash((legacy_seed_id)))][7]))
          if (legacy_seed_stock_packet_hash) in stock_packet_hash_table:
            pass
          else:
            stock_packet_hash_table[(legacy_seed_stock_packet_hash)] = stock_packet_id
            stock_packet_table[(stock_packet_id, stock_hash_table[(legacy_seed_stock_hash)], location_hash_table[(legacy_seed_location_hash)], legacy_seedinv_table[(hash((legacy_seed_id)))][8], legacy_seedinv_table[(hash((legacy_seed_id)))][7])] = stock_packet_id
            stock_packet_id = stock_packet_id + 1

        #-------- Not in seedinv --------------
        else:
          legacy_seed_stock_hash = hash((passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Not Inventoried', 'Not Invetoried', seed_comments))
          if (legacy_seed_stock_hash) in stock_hash_table:
            pass
          else:
            stock_hash_table[(legacy_seed_stock_hash)] = stock_id
            stock_table[(stock_id, passport_hash_table[(legacy_seed_passport_hash)], legacy_seed_id, legacy_seed_name, legacy_cross_type, legacy_seed_pedigree, 'Not Inventoried', 'Not Invetoried', seed_comments)] = stock_id
            stock_id = stock_id + 1




#------------------------------------------------------------------------
#--- Check which seed_ids are in legacy_seedinv but not in stock_table ----
#------------------------------------------------------------------------
  legacy_seedinv_not_in_stock_count = 1

  legacy_seedinv_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/seedinv_clean.csv'), dialect='excel')
  for row in legacy_seedinv_file:
    legacy_seedinv_id = row["ID"]
    legacy_seedinv_seed_id = row["seed_id"]
    legacy_seedinv_seed_name = row["seed_name"]
    legacy_seedinv_date = row["inventory_date"]
    legacy_seedinv_person = row["inventory_person"]
    legacy_seedinv_person_id = row["seed_person_id"]
    legacy_seedinv_location = row["location"]
    legacy_seedinv_notes = row["notes"]
    legacy_seedinv_weight = row["weight_g"]

    if (legacy_seedinv_seed_id) in stock_seed_id_table:
      pass
    else:
      legacy_seedinv_not_in_stock[(legacy_seedinv_not_in_stock_count)] = (legacy_seedinv_seed_id, legacy_seedinv_seed_name, legacy_seedinv_date, legacy_seedinv_person, legacy_seedinv_person_id, legacy_seedinv_location, legacy_seedinv_notes, legacy_seedinv_weight)
      legacy_seedinv_not_in_stock_count = legacy_seedinv_not_in_stock_count + 1


#------------------------------------------------------------------------
#-The output dictionaries are written to csv files.
#------------------------------------------------------------------------

  writer = csv.writer(open('data/csv_from_script/locality.csv', 'wb'))
  for key in locality_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/field.csv', 'wb'))
  for key in field_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/experiment.csv', 'wb'))
  for key in experiment_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/obs_selector.csv', 'wb'))
  for key in obs_selector_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/taxonomy.csv', 'wb'))
  for key in taxonomy_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/people.csv', 'wb'))
  for key in people_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/collecting.csv', 'wb'))
  for key in collecting_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/passport.csv', 'wb'))
  for key in passport_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/stock.csv', 'wb'))
  for key in stock_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/stock_packet.csv', 'wb'))
  for key in stock_packet_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/obs_row.csv', 'wb'))
  for key in obs_row_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/obs_plant.csv', 'wb'))
  for key in obs_plant_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/location.csv', 'wb'))
  for key in location_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/isolate.csv', 'wb'))
  for key in isolate_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/disease_info.csv', 'wb'))
  for key in disease_info_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/measurement_parameter.csv', 'wb'))
  for key in measurement_param_table.iterkeys():
    writer.writerow(key)
  writer = csv.writer(open('data/csv_from_script/measurement.csv', 'wb'))
  for key in measurement_table.iterkeys():
    writer.writerow(key)

  writer = csv.writer(open('data/csv_from_script/checks/row_source_seed_not_in_seed.csv', 'wb'))
  for key, value in row_source_seed_not_in_seed.items():
    writer.writerow([value])
  writer = csv.writer(open('data/csv_from_script/checks/row_no_source_seed.csv', 'wb'))
  for key, value in row_no_source_seed.items():
    writer.writerow([value])
  writer = csv.writer(open('data/csv_from_script/checks/stock_not_inventoried.csv', 'wb'))
  for key, value in stock_not_inventoried.items():
    writer.writerow([value])
  writer = csv.writer(open('data/csv_from_script/checks/phenotype_row_not_in_row.csv', 'wb'))
  for key, value in phenotype_row_not_in_row.items():
    writer.writerow([value])
  writer = csv.writer(open('data/csv_from_script/checks/legacy_seed_not_in_stock.csv', 'wb'))
  for key, value in legacy_seed_not_in_stock.items():
    writer.writerow([value])
  writer = csv.writer(open('data/csv_from_script/checks/legacy_seedinv_not_in_stock.csv', 'wb'))
  for key, value in legacy_seedinv_not_in_stock.items():
    writer.writerow([value])

  print('Done')

  #---- Computing-time testing -------------------------
  end = time.clock()
  print(end-start)

#------------------------------------------------------------------------
#- Exectution begins here by loading application dependencies
#------------------------------------------------------------------------

if __name__ == '__main__':
  migrate()
