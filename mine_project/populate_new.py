
import os
import csv
from collections import OrderedDict
import time

def migrate():
  start = time.clock()
  #--- Using row_test.csv table (538 tuples) took 38.6s
  #--- Extrapolating, the complete row.csv (65000 tuples) would take 78 minutes
  #--- Actually takes 218 minutes to run this through, on my computer.
  #--- The old populate.py script takes ~20 hours, on my computer.

#-----------------------------------------------
#- Define output dictionaries
#-----------------------------------------------
  experiment_table = OrderedDict({})
  locality_table = OrderedDict({})
  field_table = OrderedDict({})
  people_table = OrderedDict({})
  location_table = OrderedDict({})
  obs_selector_table = OrderedDict({})
  obs_row_table = OrderedDict({})
  obs_plant_table = OrderedDict({})
  taxonomy_table = OrderedDict({})
  collecting_table = OrderedDict({})
  passport_table = OrderedDict({})
  stock_table = OrderedDict({})
  stock_packet_table = OrderedDict({})
  isolate_table = OrderedDict({})
  disease_info_table = OrderedDict({})

#-------------------------------------------------
#- Define intermediary dictionaries and legacy data dictionaries
#-------------------------------------------------
  experiment_name_table = OrderedDict({})
  experiment_field_table = OrderedDict({})
  obs_row_intermed_table = OrderedDict({})

  legacy_experiment_table = OrderedDict({})
  legacy_seed_table = OrderedDict({})
  legacy_people_table = OrderedDict({})
  legacy_plant_table = OrderedDict({})
  legacy_seedinv_table = OrderedDict({})

#-------------------------------------------------------------------
#- Load Legacy Data into dictionaries
#-------------------------------------------------------------------
  legacy_exp_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/legacy_experiment_table.csv'), dialect='excel')
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

  legacy_seed_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/legacy_seed_table.csv'), dialect='excel')
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

    legacy_seed_table[(legacy_seed_id)] = (legacy_seed_id, legacy_plant_id_origin, legacy_row_id_origin, legacy_experiment_id_origin, legacy_plant_name, legacy_row_name, legacy_seed_name, legacy_cross_type, legacy_male_parent_id, legacy_male_parent_name, legacy_program_origin, legacy_seed_pedigree, legacy_line_num, legacy_seed_person_id, legacy_seed_disease_info, legacy_seed_notes, legacy_seed_accession, legacy_seed_lot)

  legacy_people_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/legacy_people_table.csv'), dialect='excel')
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

  legacy_plant_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/legacy_plant_table.csv'), dialect='excel')
  for row in legacy_plant_file:
    legacy_plant_id = row["plant_id"]
    legacy_plant_row_id = row["row_id"]
    legacy_plant_name = row["plant_name"]
    legacy_plant_notes = row["notes"]

    legacy_plant_table[(legacy_plant_id)] = (legacy_plant_id, legacy_plant_row_id, legacy_plant_name, legacy_plant_notes)

  legacy_seedinv_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/legacy_seedinv_table.csv'), dialect='excel')
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

    legacy_seedinv_table[(legacy_seedinv_seed_id)] = (legacy_seedinv_id, legacy_seedinv_seed_id, legacy_seedinv_seed_name, legacy_seedinv_date, legacy_seedinv_person, legacy_seedinv_person_id, legacy_seedinv_location, legacy_seedinv_notes, legacy_seedinv_weight)

#-------------------------------------------------------------------
#-This user_table is simply stored in memory and is not written to csv or the database.
#-Given that person.csv is the same file used to write people to the database, the user_ids in this user_table should match the user_ids in the database.
#-Users are added in a separate, direct to database, function because of the django auth set_password() command.
#-------------------------------------------------------------------
  user_table = {}
  user_id = 1

  user_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/person.csv'), dialect='excel')
  for row in user_file:
    username = row["user"]

    if (username) in user_table:
      pass
    else:
      user_table[(username)] = user_id
      print("User_id: %d" % (user_id))
      user_id = user_id + 1

#------------------------------------------------------------------------
#-Add all Dummies
#------------------------------------------------------------------------
  people_table['No Source'] = 1
  locality_table[('NULL','NULL','NULL','NULL')] = 1
  field_table[(1,'No Field')] = 1
  experiment_table[(user_table['unknown'],1,'No Experiment','No Experiment','No Experiment','No Experiment')] = 1
  experiment_name_table[('No Experiment')] = 1
  obs_selector_table[(1,1)] = 1
  location_table[(1,'Unknown','Unknown','Unknown')] = 1
  taxonomy_table[('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy')] = 1
  collecting_table[(1,user_table['unknown'],1,'No Collection','No Collection','No Collection')] = 1
  passport_table[(1,1,1)] = 1
  stock_table[(1,'0','No Seed','No Seed','No Seed','No Seed','No Seed','No Seed')] = 1

#---------------------------------------------------------------------
#-Information from experiments.csv is extracted and saved to locality, field, and experiment dictionaries.
#---------------------------------------------------------------------
  experiment_id = experiment_table.values()[-1] + 1
  locality_id = locality_table.values()[-1] + 1
  field_id = field_table.values()[-1] + 1

  experiment_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/experiments.csv'), dialect='excel')
  for row in experiment_file:
    experiment_name = row['name']
    experiment_field_locality_city = row['city']
    experiment_field_locality_state = row['state']
    experiment_field_locality_country = row['country']
    experiment_field_name = row['field_name']
    experiment_user_username = row['person']
    experiment_startdate = row['date']
    experiment_purpose = row['desc']
    experiment_comments = "Tissue Collection: %s || Inoculations: %s || Pathogen: %s || Notes: %s" % (row['tissue_collection'], row['inoculations'], row['pathogen'], row['notes'])

    if (experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country, 'NULL') in locality_table:
      pass
    else:
      locality_table[(experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country, 'NULL')] = locality_id
      print("Locality_id: %d" % (locality_id))
      locality_id = locality_id + 1

    field_locality_id = locality_table[(experiment_field_locality_city, experiment_field_locality_state, experiment_field_locality_country, 'NULL')]
    if (field_locality_id, experiment_field_name) in field_table:
      pass
    else:
      field_table[(field_locality_id, experiment_field_name)] = field_id
      print("Field_id: %d" % (field_id))
      field_id = field_id + 1

    experiment_field_id = field_table[(field_locality_id, experiment_field_name)]
    experiment_user = user_table[(experiment_user_username)]
    if (experiment_user, experiment_field_id, experiment_name, experiment_startdate, experiment_purpose, experiment_comments) in experiment_table:
      pass
    else:
      experiment_table[(experiment_user, experiment_field_id, experiment_name, experiment_startdate, experiment_purpose, experiment_comments)] = experiment_id
      experiment_name_table[experiment_name] = (experiment_id, experiment_user, experiment_field_id, experiment_name, experiment_startdate, experiment_purpose, experiment_comments)
      experiment_field_table[(experiment_name)] = experiment_field_id
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

  row_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_row_table_t1.1.csv'), dialect='excel')
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
    row_comments = "Purpose: %s || Notes: %s" % (row_purpose, row_notes)
    row_kernel_num = row['kernel_num']
    row_stock_pedigree = row['pedigree']

    if row_stock_seed_id != 0:
      if (row_stock_seed_id) in legacy_seed_table:
        seed = True
        if (legacy_seed_table[(row_stock_seed_id)][13]) in legacy_people_table:
          person = legacy_people_table[(legacy_seed_table[(row_stock_seed_id)][13])][1]
        else:
          person = 'unknown_person'
        if seed:
          seed_comments = 'Notes: %s || Lot: %s || Accession: %s' % (legacy_seed_table[(row_stock_seed_id)][15], legacy_seed_table[(row_stock_seed_id)][17], legacy_seed_table[(row_stock_seed_id)][16])
        if legacy_seed_table[(row_stock_seed_id)][1] != 'NULL' and legacy_seed_table[(row_stock_seed_id)][1] != '':
          plant = True
        else:
          plant = False
        if (row_stock_seed_id) in legacy_seedinv_table:
          seedinv = True
        else:
          seedinv = False
      else:
        seed = False
        plant = False
        seedinv = False
        #----------------- Add function here to print to txt the seed_ids that are in seed_inv, but not seed -----

    else:
      seed = False
      plant = False
      seedinv = False


    if ('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa') in taxonomy_table:
      pass
    else:
      taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')] = taxonomy_id
      print("Taxonomy_id: %d" % (taxonomy_id))
      taxonomy_id = taxonomy_id + 1

    obs_selector_table[(obs_selector_id, experiment_name_table[row_experiment_name][0])] = obs_selector_id
    print("ObsSelector: %d" % (obs_selector_id))
    obs_selector_id = obs_selector_id + 1

    if seed:
      collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')] = collecting_id
      print("Collecting_id: %d" % (collecting_id))
      collecting_id = collecting_id + 1

      if (legacy_seed_table[(row_stock_seed_id)][10]) in people_table:
        pass
      else:
        people_table[(legacy_seed_table[(row_stock_seed_id)][10])] = people_id

      if (collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')]) in passport_table:
        pass
      else:
        passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])] = passport_id
        print("Passport_id: %d" % (passport_id))
        passport_id = passport_id + 1

      if seedinv:
        if (passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_stock_seed_id)][3], seed_comments) in stock_table:
          pass
        else:
          stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_stock_seed_id)][3], seed_comments)] = stock_id
          print("Stock_id: %d" % (stock_id))
          stock_id = stock_id + 1

        obs_row_table[(obs_selector_table.values()[-1], experiment_field_table[(row_experiment_name)], stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_stock_seed_id)][3], seed_comments)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)] = obs_row_id
        obs_row_intermed_table[(row_row_id, row_row_name)] = (obs_row_id, obs_selector_table.values()[-1], experiment_field_table[(row_experiment_name)], stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_stock_seed_id)][3], seed_comments)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)
        print("ObsRow_id: %d" % obs_row_id)
        obs_row_id = obs_row_id + 1

        if (locality_table[('Ithaca', 'NY', 'USA', 'NULL')], legacy_seedinv_table[(row_stock_seed_id)][6], 'Cold Storage', 'Unknown') in location_table:
          pass
        else:
          location_table[(locality_table[('Ithaca', 'NY', 'USA', 'NULL')], legacy_seedinv_table[(row_stock_seed_id)][6], 'Cold Storage', 'Unknown')] = location_id
          print("Location_id: %d" % (location_id))
          location_id = location_id + 1

        if (stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_stock_seed_id)][3], seed_comments)], location_table[(locality_table[('Ithaca', 'NY', 'USA', 'NULL')], legacy_seedinv_table[(row_stock_seed_id)][6], 'Cold Storage', 'Unknown')], legacy_seedinv_table[(row_stock_seed_id)][8], legacy_seedinv_table[(row_stock_seed_id)][7]) in stock_packet_table:
          pass
        else:
          stock_packet_table[(stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Legacy Inventoried', legacy_seedinv_table[(row_stock_seed_id)][3], seed_comments)], location_table[(locality_table[('Ithaca', 'NY', 'USA', 'NULL')], legacy_seedinv_table[(row_stock_seed_id)][6], 'Cold Storage', 'Unknown')], legacy_seedinv_table[(row_stock_seed_id)][8], legacy_seedinv_table[(row_stock_seed_id)][7])] = stock_packet_id
          print("Stockpacket_id: %d" % (stock_packet_id))
          stock_packet_id = stock_packet_id + 1

      #--------- No Seedinv --------------------------------
      else:
        if (passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Not Inventoried', 'Not Inventoried', seed_comments) in stock_table:
          pass
        else:
          stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Not Inventoried', 'Not Inventoried', seed_comments)] = stock_id
          print("Stock_id: %d" % (stock_id))
          stock_id = stock_id + 1

        obs_row_table[(obs_selector_table.values()[-1], experiment_field_table[(row_experiment_name)], stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Not Inventoried', 'Not Inventoried', seed_comments)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)] = obs_row_id
        obs_row_intermed_table[(row_row_id, row_row_name)] = (obs_row_id, obs_selector_table.values()[-1], experiment_field_table[(row_experiment_name)], stock_table[(passport_table[(collecting_table[(obs_selector_table.values()[-1], user_table[person], 1, legacy_experiment_table[(row_experiment_name)][9], 'Field Harvest', 'No comments')], people_table[(legacy_seed_table[(row_stock_seed_id)][10])], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')])], legacy_seed_table[(row_stock_seed_id)][0], legacy_seed_table[(row_stock_seed_id)][6], legacy_seed_table[(row_stock_seed_id)][7], legacy_seed_table[(row_stock_seed_id)][11], 'Not Inventoried', 'Not Inventoried', seed_comments)], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)
        print("ObsRow_id: %d" % obs_row_id)
        obs_row_id = obs_row_id + 1

    #-------- No Legacy Seed info ----------------
    else:
      if (obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting') in collecting_table:
        pass
      else:
        collecting_table[(obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting')] = collecting_id
        print("Collecting_id: %d" % (collecting_id))
        collecting_id = collecting_id + 1

      if (collecting_table[(obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting')], people_table[('No Source')], taxonomy_table[('Zea', 'Zea mays', row_population, 'Maize', 'No Alias', 'No Race', 'No Subtaxa')]) in passport_table:
        pass
      else:
        passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting')], people_table[('No Source')], taxonomy_table[('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy')])] = passport_id
        print("Passport_id: %d" % passport_id)
        passport_id = passport_id + 1

      if (passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting')], people_table[('No Source')], taxonomy_table[('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy')])], 0, 'No Seed', 'No Seed', 'No Seed', 'Not Inventoried', 'Not Inventoried', 'No Seed') in stock_table:
        pass
      else:
        stock_table[(passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting')], people_table[('No Source')], taxonomy_table[('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy')])], 0, 'No Seed', 'No Seed', 'No Seed', 'Not Inventoried', 'Not Inventoried', 'No Seed')] = stock_id
        print("Stock_id: %d" % stock_id)
        stock_id = stock_id + 1

      obs_row_table[(obs_selector_table.values()[-1], experiment_field_table[(row_experiment_name)], stock_table[(passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting')], people_table[('No Source')], taxonomy_table[('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy')])], 0, 'No Seed', 'No Seed', 'No Seed', 'Not Inventoried', 'Not Inventoried', 'No Seed')], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)] = obs_row_id
      obs_row_intermed_table[(row_row_id, row_row_name)] = (obs_row_id, obs_selector_table.values()[-1], experiment_field_table[(row_experiment_name)], stock_table[(passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table['unknown'], 1, 'No Collecting', 'No Collecting', 'No Collecting')], people_table[('No Source')], taxonomy_table[('No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy','No Taxonomy')])], 0, 'No Seed', 'No Seed', 'No Seed', 'Not Inventoried', 'Not Inventoried', 'No Seed')], row_row_id, row_row_name, row_range, row_plot, row_block, row_rep, row_kernel_num, legacy_experiment_table[(row_experiment_name)][2], legacy_experiment_table[(row_experiment_name)][9], row_comments)
      print("ObsRow_id: %d" % obs_row_id)
      obs_row_id = obs_row_id + 1

    #---------- If there is plant info in the Legacy Plant table -----------------
    if seed:
      if plant:
        if (legacy_seed_table[(row_stock_seed_id)][1]) in legacy_plant_table:

          obs_selector_table[(obs_selector_id, experiment_name_table[row_experiment_name][0])] = obs_selector_id
          print("ObsSelector: %d" % (obs_selector_id))
          obs_selector_id = obs_selector_id + 1

          if seedinv:

            if (obs_selector_table.values()[-1], obs_row_intermed_table[(row_row_id, row_row_name)][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][2], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][3]) in obs_plant_table:
              pass
            else:
              obs_plant_table[(obs_selector_table.values()[-1], obs_row_intermed_table[(row_row_id, row_row_name)][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][2], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][3])] = obs_plant_id
              print("ObsPlant_id: %d" % (obs_plant_id))
              obs_plant_id = obs_plant_id + 1

          #-------- No Seedinv -----------------
          else:
            if (obs_selector_table.values()[-1], obs_row_intermed_table[(row_row_id, row_row_name)][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][2], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][3]) in obs_plant_table:
              pass
            else:
              obs_plant_table[(obs_selector_table.values()[-1], obs_row_intermed_table[(row_row_id, row_row_name)][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][0], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][2], legacy_plant_table[(legacy_seed_table[(row_stock_seed_id)][1])][3])] = obs_plant_id
              print("ObsPlant_id: %d" % (obs_plant_id))
              obs_plant_id = obs_plant_id + 1

#---------------------------------------------------------------------------
#- Info from isolate.csv is extracted and saved to disease_info, taxonomy, locality, field, collecting, passport, location, and isolate dictionaries.
#---------------------------------------------------------------------------

  isolate_table_id = 1
  disease_info_id = 1

  isolate_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/nelson_lab_isolate_table.csv'), dialect='excel')
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

    if (disease_info_common_name) in disease_info_table:
      pass
    else:
      disease_info_table[(disease_info_common_name)] = disease_info_id
      print("Disease_info_id: %d" % (disease_info_id))
      disease_info_id = disease_info_id + 1

    if (isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa) in taxonomy_table:
      pass
    else:
      taxonomy_table[(isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa)] = taxonomy_id
      print("Taxonomy_id: %d" % (taxonomy_id))
      taxonomy_id = taxonomy_id + 1

    if (isolate_city, isolate_state, isolate_country) in locality_table:
      pass
    else:
      locality_table[(isolate_city, isolate_state, isolate_country)] = locality_id
      print("Locality_id: %d" % (locality_id))
      locality_id = locality_id + 1

    if (locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name) in field_table:
      pass
    else:
      field_table[(locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name)] = field_id
      print("Field_id: %d" % (field_id))
      field_id = field_id + 1

    if (obs_selector_table[(1,1)], user_table[(isolate_collection_user)], field_table[(locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name)], isolate_collection_date, 'Unknown', 'No Comments') in collecting_table:
      pass
    else:
      collecting_table[(obs_selector_table[(1,1)], user_table[(isolate_collection_user)], field_table[(locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name)], isolate_collection_date, 'Unknown', 'No Comments')] = collecting_id
      print("Collecting_id: %d" % (collecting_id))
      collecting_id = collecting_id + 1

    if (collecting_table[(obs_selector_table[(1,1)], user_table[(isolate_collection_user)], field_table[(locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name)], isolate_collection_date, 'Unknown', 'No Comments')], people_table[('No Source')], taxonomy_table[(isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa)]) in passport_table:
      pass
    else:
      passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table[(isolate_collection_user)], field_table[(locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name)], isolate_collection_date, 'Unknown', 'No Comments')], people_table[('No Source')], taxonomy_table[(isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa)])] = passport_id
      print("Passport_id: %d" % (passport_id))
      passport_id = passport_id + 1

    if location_n80c_boxname:
      if (locality_table[(isolate_city, isolate_state, isolate_country)], 'Plant Science', 'Freezer -80C', location_n80c_boxname) in location_table:
        pass
      else:
        location_table[(locality_table[(isolate_city, isolate_state, isolate_country)], 'Plant Science', 'Freezer -80C', location_n80c_boxname)] = location_id
        print("Location_id: %d" % (location_id))
        location_id = location_id + 1

      if (passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table[(isolate_collection_user)], field_table[(locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name)], isolate_collection_date, 'Unknown', 'No Comments')], people_table[('No Source')], taxonomy_table[(isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa)])], location_table[(locality_table[(isolate_city, isolate_state, isolate_country)], 'Plant Science', 'Freezer -80C', location_n80c_boxname)], disease_info_table[(disease_info_common_name)], isolate_id, isolate_name, isolate_comments) in isolate_table:
        pass
      else:
        isolate_table[(passport_table[(collecting_table[(obs_selector_table[(1,1)], user_table[(isolate_collection_user)], field_table[(locality_table[(isolate_city, isolate_state, isolate_country)], isolate_field_name)], isolate_collection_date, 'Unknown', 'No Comments')], people_table[('No Source')], taxonomy_table[(isolate_taxonomy_genus, 'Unknown', 'Unknown', 'Isolate', isolate_taxonomy_alias, isolate_taxonomy_race, isolate_subtaxa)])], location_table[(locality_table[(isolate_city, isolate_state, isolate_country)], 'Plant Science', 'Freezer -80C', location_n80c_boxname)], disease_info_table[(disease_info_common_name)], isolate_id, isolate_name, isolate_comments)] = isolate_table_id
        print("Isolate_table_id: %d" % (isolate_table_id))
        isolate_table_id = isolate_table_id + 1

#------------------------------------------------------------------------
#-The output dictionaries are written to csv files.
#------------------------------------------------------------------------

  writer = csv.writer(open('csv_from_script/locality.csv', 'wb'))
  for key, value in locality_table.items():
    writer.writerow([value, key])
  print('Locality Done')
  writer = csv.writer(open('csv_from_script/field.csv', 'wb'))
  for key, value in field_table.items():
    writer.writerow([value, key])
  print('Field Done')
  writer = csv.writer(open('csv_from_script/experiment.csv', 'wb'))
  for key, value in experiment_table.items():
    writer.writerow([value, key])
  print('Experiment Done')
  writer = csv.writer(open('csv_from_script/obs_selector.csv', 'wb'))
  for key, value in obs_selector_table.items():
    writer.writerow([value, key])
  print('ObsSelector Done')
  writer = csv.writer(open('csv_from_script/taxonomy.csv', 'wb'))
  for key, value in taxonomy_table.items():
    writer.writerow([value, key])
  print('Taxonomy Done')
  writer = csv.writer(open('csv_from_script/people.csv', 'wb'))
  for key, value in people_table.items():
    writer.writerow([value, key])
  print('People Done')
  writer = csv.writer(open('csv_from_script/collecting.csv', 'wb'))
  for key, value in collecting_table.items():
    writer.writerow([value, key])
  print('Colleting Done')
  writer = csv.writer(open('csv_from_script/passport.csv', 'wb'))
  for key, value in passport_table.items():
    writer.writerow([value, key])
  print('Passport Done')
  writer = csv.writer(open('csv_from_script/stock.csv', 'wb'))
  for key, value in stock_table.items():
    writer.writerow([value, key])
  print('Stock Done')
  writer = csv.writer(open('csv_from_script/stock_packet.csv', 'wb'))
  for key, value in stock_packet_table.items():
    writer.writerow([value, key])
  print('Stock Packet Done')
  writer = csv.writer(open('csv_from_script/obs_row.csv', 'wb'))
  for key, value in obs_row_table.items():
    writer.writerow([value, key])
  print('ObsRow Done')
  writer = csv.writer(open('csv_from_script/obs_plant.csv', 'wb'))
  for key, value in obs_plant_table.items():
    writer.writerow([value, key])
  print('ObsPlant Done')
  writer = csv.writer(open('csv_from_script/location.csv', 'wb'))
  for key, value in location_table.items():
    writer.writerow([value, key])
  print('Location Done')
  writer = csv.writer(open('csv_from_script/isolate.csv', 'wb'))
  for key, value in isolate_table.items():
    writer.writerow([value, key])
  print('Isolate Done')
  writer = csv.writer(open('csv_from_script/disease_info.csv', 'wb'))
  for key, value in disease_info_table.items():
    writer.writerow([value, key])
  print('DiseaseInfo Done')

  #---- Computing-time testing -------------------------
  end = time.clock()
  print(end-start)

#------------------------------------------------------------------------
#- Exectution begins here by loading application dependencies
#------------------------------------------------------------------------

if __name__ == '__main__':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_project.settings')
  import django
  django.setup()
  from lab.models import Experiment, User, UserProfile, Taxonomy, Locality, Field, Passport, Collecting, People, Stock, Location, ObsRow, ObsPlant, ObsSelector, StockPacket, Location, Isolate, DiseaseInfo
  from legacy.models import Legacy_Seed, Legacy_People, Legacy_Experiment, Legacy_Seed_Inventory, Legacy_Plant, Legacy_Tissue
  migrate()
