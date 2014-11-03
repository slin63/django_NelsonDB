import os
import csv

def csv_extract_row():
  ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/extract_data/IBM_row_table.csv'), dialect='excel')
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
    exp.comments = 'Tissue Collection: %s || Inoculations: %s || Pathogen: %s || Notes: %s' % (exp.tissue_collection, exp.inoculations, exp.pathogen_isolate, exp.notes)
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
    if seed:
      if seedinv:
        info_dict = {"seed_id": seed.seed_id, "seed_name": seed.seed_name, "pedigree": seed.seed_pedigree, "population": row_population, "cross_type": seed.cross_type, "seed_comments": seed.comments, "weight": seedinv.weight_g, "stock_date": seedinv.inventory_date, "location_name": seedinv.location, "location_comments": seedinv.notes}

        with open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/extract_data/IBM_info.csv', 'wb') as f:  # Just use 'w' mode in 3.x
          w = csv.DictWriter(f, info_dict.keys())
          w.writeheader()
          w.writerow(info_dict)
    print(row)



if __name__ == '__main__':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_project.settings')
  from lab.models import Experiment, User, UserProfile, Taxonomy, Locality, Field, Passport, Collecting, People, Stock, Location, ObsRow, ObsPlant, ObsSelector, StockPacket, Location, Isolate, DiseaseInfo
  from legacy.models import Legacy_Seed, Legacy_People, Legacy_Experiment, Legacy_Seed_Inventory, Legacy_Plant, Legacy_Tissue
  csv_extract_row()
