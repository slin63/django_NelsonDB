
import os
import csv
from collections import OrderedDict

def clean_legacy_seedinv():

  legacy_seedinv_bad = OrderedDict({})
  legacy_seedinv_clean = OrderedDict({})

  legacy_seedinv_clean[('header')] = ('ID','seed_id','seed_name','inventory_date','inventory_person','seed_person_id','location','notes','weight_g')
  legacy_seedinv_bad_id = 1

  legacy_seedinv_file = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/webapp/data/mine_data/legacy_seedinv_table.csv'), dialect='excel')
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

    if (legacy_seedinv_seed_id) in legacy_seedinv_clean:
      if legacy_seedinv_id > legacy_seedinv_clean[(legacy_seedinv_seed_id)][1] and legacy_seedinv_location != 'NULL':
        legacy_seedinv_clean[(legacy_seedinv_seed_id)] = (legacy_seedinv_id, legacy_seedinv_seed_id, legacy_seedinv_seed_name, legacy_seedinv_date, legacy_seedinv_person, legacy_seedinv_person_id, legacy_seedinv_location, legacy_seedinv_notes, legacy_seedinv_weight)
      else:
        legacy_seedinv_bad[(legacy_seedinv_seed_id)] = (legacy_seedinv_bad_id, legacy_seedinv_id, legacy_seedinv_seed_id, legacy_seedinv_seed_name, legacy_seedinv_date, legacy_seedinv_person, legacy_seedinv_person_id, legacy_seedinv_location, legacy_seedinv_notes, legacy_seedinv_weight)
        legacy_seedinv_bad_id = legacy_seedinv_bad_id + 1

    else:
      legacy_seedinv_clean[(legacy_seedinv_seed_id)] = (legacy_seedinv_id, legacy_seedinv_seed_id, legacy_seedinv_seed_name, legacy_seedinv_date, legacy_seedinv_person, legacy_seedinv_person_id, legacy_seedinv_location, legacy_seedinv_notes, legacy_seedinv_weight)



  #----------------------------------------------
  #----------------------------------------------

  writer = csv.writer(open('data/mine_data/seedinv_clean.csv', 'wb'))
  for value in legacy_seedinv_clean.itervalues():
    writer.writerow(value)
  writer = csv.writer(open('data/csv_from_script/checks/seedinv_bad.csv', 'wb'))
  for value in legacy_seedinv_bad.itervalues():
    writer.writerow(value)

#------------------------------------------------------------------------
#- Exectution begins here by loading application dependencies
#------------------------------------------------------------------------

if __name__ == '__main__':
  clean_legacy_seedinv()
