import os
import sys
import csv
from collections import OrderedDict
import time

#sys.path.append('/data/srv/nelsondb/app/webapp')
sys.path.append('C:/Users/Nicolas/Documents/GitHub/django_NelsonDB')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
import django
django.setup()
from lab.models import User, Experiment, Locality, MaizeSample, ObsTracker, ObsTrackerSource, ObsSample, Separation, ObsExtract, MeasurementParameter, Measurement, Medium, Citation, ObsPlot, ObsPlant, ObsSample, ObsEnv, ObsMicrobe, ObsCulture, ObsDNA, ObsExtract, ObsPlate, ObsWell, ObsTissue, Stock, Location, Locality, Field, Collecting, IsolateStock, Passport, People, Taxonomy, DiseaseInfo, Isolate, StockPacket, ObsTrackerSource

def user_id_mirror():
    user_id = User.objects.latest('id').id + 1
    return user_id

def user_hash_mirror():
    user_hash_table = OrderedDict({})
    #--- Key = (username)
    #--- Value = (user_id)

    user_file = User.objects.all()
    for row in user_file:
        user_hash_table[row.username] = row.id
    return user_hash_table

def experiment_id_mirror():
    experiment_id = Experiment.objects.latest('id').id + 1
    return experiment_id

def experiment_table_mirror():
    experiment_table = OrderedDict({})
    #--- Key = (experiment_id, user_id, field_id, name, start_date, purpose, comments)
    #--- Value = (experiment_id)

    experiment_file = Experiment.objects.all()
    for row in experiment_file:
        experiment_table[(row.id, row.user_id, row.field_id, row.name, row.start_date, row.purpose, row.comments)] = (row.id)
    return experiment_table

def experiment_hash_mirror():
    experiment_hash_table = OrderedDict({})
    #--- Key = (user_id + field_id + name + start_date + purpose + comments)
    #--- Value = (id)

    experiment_file = Experiment.objects.all()
    for row in experiment_file:
        experiment_hash = str(row.user_id) + str(row.field_id) + row.name + row.start_date + row.purpose + row.comments
        experiment_hash.rstrip('\r')
        experiment_hash.rstrip('\n')
        experiment_hash_table[experiment_hash] = row.id
    return experiment_hash_table

def experiment_name_mirror():
    experiment_name_table = OrderedDict({})
    #--- Key = (name)
    #--- Value = (id, user_id, field_id, name, start_date, purpose, comments)

    experiment_file = Experiment.objects.all()
    for row in experiment_file:
        experiment_name_table[row.name] = (row.id, row.user_id, row.field_id, row.name, row.start_date, row.purpose, row.comments)
    return experiment_name_table

def field_name_mirror():
    field_name_table = OrderedDict({})
    #--- Key = (field_name)
    #--- Value = (id, locality_id, field_name, field_num, comments)

    field_file = Field.objects.all()
    for row in field_file:
        field_name_table[row.field_name] = (row.id, row.locality_id, row.field_name, row.field_num, row.comments)
    return field_name_table

def field_hash_mirror():
    field_hash_table = OrderedDict({})
    #--- Key = (locality_id + field_name + field_num + comments)
    #--- Value = (id)

    field_file = Field.objects.all()
    for row in field_file:
        field_hash = str(row.locality_id) + row.field_name + row.field_num + row.comments
        field_hash.rstrip('\r')
        field_hash.rstrip('\n')
        field_hash_table[field_hash] = row.id
    return field_hash_table

def field_id_mirror():
    field_id = Field.objects.latest('id').id + 1
    return field_id

def locality_id_mirror():
    locality_id = Locality.objects.latest('id').id + 1
    return locality_id

def locality_table_mirror():
    locality_table = OrderedDict({})
    #--- Key = (locality_id, city, state, country, zipcode)
    #--- Value = (locality_id)

    locality_file = Locality.objects.all()
    for row in locality_file:
        locality_table[(row.id, row.city, row.county, row.state, row.country, row.zipcode)] = (row.id)
    return locality_table

def locality_hash_mirror():
    locality_hash_table = OrderedDict({})
    #--- Key = (city + state + country + zipcode)
    #--- Value = (locality_id)

    locality_file = Locality.objects.all()
    for row in locality_file:
        locality_hash = row.city + row.state + row.county + row.country + row.zipcode
        locality_hash.rstrip('\r')
        locality_hash.rstrip('\n')
        locality_hash_table[locality_hash] = row.id
    return locality_hash_table

def obs_tracker_id_mirror():
    obs_tracker_id = ObsTracker.objects.latest('id').id + 1
    return obs_tracker_id

def obs_tracker_table_mirror():
    obs_tracker_table = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    obs_tracker_file = ObsTracker.objects.all()
    for row in obs_tracker_file:
        obs_tracker_table[(row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)] = (row.id)
    return obs_tracker_table

def obs_tracker_hash_mirror():
    obs_tracker_hash_table = OrderedDict({})
    #--- Key = (obs_entity_type + experiment_id + field_id + isolate_id + isolatestock_id + location_id + maize_sample_id + obs_culture_id + obs_dna_id + obs_env_id + obs_extract_id + obs_microbe_id + obs_plant_id + obs_plate_id + obs_plot_id + obs_sample_id + obs_tissue_id + obs_well_id + stock_id + user_id)
    #--- Value = (obs_tracker_id)

    obs_tracker_file = ObsTracker.objects.all()
    for row in obs_tracker_file:
        tracker_hash = row.obs_entity_type + str(row.experiment_id) + str(row.field_id) + str(row.isolate_id) + str(row.isolatestock_id) + str(row.location_id) + str(row.maize_sample_id) + str(row.obs_culture_id) + str(row.obs_dna_id) + str(row.obs_env_id) + str(row.obs_extract_id) + str(row.obs_microbe_id) + str(row.obs_plant_id) + str(row.obs_plate_id) + str(row.obs_plot_id) + str(row.obs_sample_id) + str(row.obs_tissue_id) + str(row.obs_well_id) + str(row.stock_id) + str(row.user_id)
        tracker_hash = tracker_hash.replace('None', '1')
        obs_tracker_hash_table[tracker_hash] = row.id
    return obs_tracker_hash_table

def obs_tracker_plot_id_mirror():
    obs_tracker_plot_id_table = OrderedDict({})
    #--- Key = (plot_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    ot = OrderedDict({})
    #--- Key = (obs_plot_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_plot_file = ObsPlot.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plot').order_by('obs_plot_id')
    for row in obs_tracker_file:
        ot[row.obs_plot_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_plot_file:
        if row.id in ot:
            obs_tracker_plot_id_table[row.plot_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_plot_id_table

def obs_tracker_obs_plot_id_mirror():
    obs_tracker_obs_plot_id_table = OrderedDict({})
    #--- Key = (obs_plot_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plot')
    for row in obs_tracker_file:
        obs_tracker_obs_plot_id_table[row.obs_plot_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_plot_id_table

def obs_tracker_plant_id_mirror():
    obs_tracker_plant_id_table = OrderedDict({})
    #--- Key = (plant_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_plant_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_plant_file = ObsPlant.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plant').order_by('obs_plant_id')
    for row in obs_tracker_file:
        ot[row.obs_plant_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_plant_file:
        if row.id in ot:
            obs_tracker_plant_id_table[row.plant_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_plant_id_table

def obs_tracker_obs_plant_id_mirror():
    obs_tracker_obs_plant_id_table = OrderedDict({})
    #--- Key = (obs_plant_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plant')
    for row in obs_tracker_file:
        obs_tracker_obs_plant_id_table[row.obs_plant_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_plant_id_table

def obs_tracker_env_id_mirror():
    obs_tracker_env_id_table = OrderedDict({})
    #--- Key = (env_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_env_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_env_file = ObsEnv.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='env').order_by('obs_env_id')
    for row in obs_tracker_file:
        ot[row.obs_env_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_env_file:
        if row.id in ot:
            obs_tracker_env_id_table[row.environment_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_env_id_table

def obs_tracker_sample_id_mirror():
    obs_tracker_sample_id_table = OrderedDict({})
    #--- Key = (sample_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_sample_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_sample_file = ObsSample.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='sample').order_by('obs_sample_id')
    for row in obs_tracker_file:
        ot[row.obs_sample_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_sample_file:
        if row.id in ot:
            obs_tracker_sample_id_table[row.sample_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_sample_id_table

def obs_tracker_obs_sample_id_mirror():
    obs_tracker_obs_sample_id_table = OrderedDict({})
    #--- Key = (obs_sample_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='sample')
    for row in obs_tracker_file:
        obs_tracker_obs_sample_id_table[row.obs_sample_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_sample_id_table

def obs_tracker_microbe_id_mirror():
    obs_tracker_microbe_id_table = OrderedDict({})
    #--- Key = (microbe_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_microbe_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_microbe_file = ObsMicrobe.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='microbe').order_by('obs_microbe_id')
    for row in obs_tracker_file:
        ot[row.obs_microbe_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_microbe_file:
        if row.id in ot:
            obs_tracker_microbe_id_table[row.microbe_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_microbe_id_table

def obs_tracker_obs_microbe_id_mirror():
    obs_tracker_obs_microbe_id_table = OrderedDict({})
    #--- Key = (obs_microbe_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='microbe')
    for row in obs_tracker_file:
        obs_tracker_obs_microbe_id_table[row.obs_microbe_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_microbe_id_table

def obs_tracker_well_id_mirror():
    obs_tracker_well_id_table = OrderedDict({})
    #--- Key = (well_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_well_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_well_file = ObsWell.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='well').order_by('obs_well_id')
    for row in obs_tracker_file:
        ot[row.obs_well_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_well_file:
        if row.id in ot:
            obs_tracker_well_id_table[row.well_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_well_id_table

def obs_tracker_obs_well_id_mirror():
    obs_tracker_obs_well_id_table = OrderedDict({})
    #--- Key = (obs_well_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='well')
    for row in obs_tracker_file:
        obs_tracker_obs_well_id_table[row.obs_well_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_well_id_table

def obs_tracker_plate_id_mirror():
    obs_tracker_plate_id_table = OrderedDict({})
    #--- Key = (plate_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    ot = OrderedDict({})
    #--- Key = (obs_plate_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_plate_file = ObsPlate.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plate').order_by('obs_plate_id')
    for row in obs_tracker_file:
        ot[row.obs_plate_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_plate_file:
        if row.id in ot:
            obs_tracker_plate_id_table[row.plate_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_plate_id_table

def obs_tracker_obs_plate_id_mirror():
    obs_tracker_obs_plate_id_table = OrderedDict({})
    #--- Key = (obs_plate_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plate')
    for row in obs_tracker_file:
        obs_tracker_obs_plate_id_table[row.obs_plate_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_plate_id_table

def obs_tracker_seed_id_mirror():
    obs_tracker_seed_id_table = OrderedDict({})
    #--- Key = (seed_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    ot = OrderedDict({})
    #--- Key = (stock_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    stock_file = Stock.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='stock').order_by('stock_id')
    for row in obs_tracker_file:
        ot[row.stock_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in stock_file:
        if row.id in ot:
            obs_tracker_seed_id_table[row.seed_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_seed_id_table

def obs_tracker_stock_id_mirror():
    obs_tracker_stock_id_table = OrderedDict({})
    #--- Key = (stock_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='stock')
    for row in obs_tracker_file:
        obs_tracker_stock_id_table[row.stock_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_stock_id_table

def obs_tracker_dna_id_mirror():
    obs_tracker_dna_id_table = OrderedDict({})
    #--- Key = (dna_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_dna_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_dna_file = ObsDNA.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='dna').order_by('obs_dna_id')
    for row in obs_tracker_file:
        ot[row.obs_dna_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_dna_file:
        if row.id in ot:
            obs_tracker_dna_id_table[row.dna_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_dna_id_table

def obs_tracker_tissue_id_mirror():
    obs_tracker_tissue_id_table = OrderedDict({})
    #--- Key = (tissue_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_tissue_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tissue_file = ObsTissue.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='tissue').order_by('obs_tissue_id')
    for row in obs_tracker_file:
        ot[row.obs_tissue_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_tissue_file:
        if row.id in ot:
            obs_tracker_tissue_id_table[row.tissue_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_tissue_id_table

def obs_tracker_obs_tissue_id_mirror():
    obs_tracker_obs_tissue_id_table = OrderedDict({})
    #--- Key = (obs_tissue_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='tissue')
    for row in obs_tracker_file:
        obs_tracker_obs_tissue_id_table[row.obs_tissue_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_tissue_id_table

def obs_tracker_culture_id_mirror():
    obs_tracker_culture_id_table = OrderedDict({})
    #--- Key = (culture_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_culture_id)
    #--- Value = (obs_tracker_id)

    obs_culture_file = ObsCulture.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='culture').order_by('obs_culture_id')
    for row in obs_tracker_file:
        ot[row.obs_culture_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_culture_file:
        if row.id in ot:
            obs_tracker_culture_id_table[row.culture_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_culture_id_table

def obs_tracker_obs_culture_id_mirror():
    obs_tracker_obs_culture_id_table = OrderedDict({})
    #--- Key = (obs_culture_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='culture')
    for row in obs_tracker_file:
        obs_tracker_obs_culture_id_table[row.obs_culture_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    return obs_tracker_obs_culture_id_table

def obs_tracker_extract_id_mirror():
    obs_tracker_extract_id_table = OrderedDict({})
    #--- Key = (extract_id)
    #--- Value = (obs_tracker_id)
    ot = OrderedDict({})
    #--- Key = (obs_extract_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, isolatestock_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_plot_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)

    obs_extract_file = ObsExtract.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='extract').order_by('obs_extract_id')
    for row in obs_tracker_file:
        ot[row.obs_extract_id] = (row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.isolatestock_id, row.location_id, row.maize_sample_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_extract_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_plot_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id)
    for row in obs_extract_file:
        if row.id in ot:
            obs_tracker_extract_id_table[row.extract_id] = (ot[row.id][0], ot[row.id][1], ot[row.id][2], ot[row.id][3], ot[row.id][4], ot[row.id][5], ot[row.id][6], ot[row.id][7], ot[row.id][8], ot[row.id][9], ot[row.id][10], ot[row.id][11], ot[row.id][12], ot[row.id][13], ot[row.id][14], ot[row.id][15], ot[row.id][16], ot[row.id][17], ot[row.id][18], ot[row.id][19], ot[row.id][20])
    return obs_tracker_extract_id_table

def plant_id_mirror():
    plant_id_table = OrderedDict({})
    #--- Key = (plot_id)
    #--- Value = (obs_plant_id, plant_id, plant_num, comments)

    obs_plant_file = ObsPlant.objects.all()
    for row in obs_plant_file:
        plant_id_table[row.plant_id] = (row.id, row.plant_id, row.plant_num, row.comments)
    return plant_id_table

def culture_id_mirror():
    culture_id_table = OrderedDict({})
    #--- Key = (culture_id)
    #--- Value = (obs_culture_id, medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, comments, num_colonies, num_microbes)

    obs_culture_file = ObsCulture.objects.all()
    for row in obs_culture_file:
        culture_id_table[row.culture_id] = (row.id, row.medium_id, row.culture_id, row.culture_name, row.microbe_type, row.plating_cycle, row.dilution, row.image_filename, row.comments, row.num_colonies, row.num_microbes)
    return culture_id_table

def microbe_id_mirror():
    microbe_id_table = OrderedDict({})
    #--- Key = (microbe_id)
    #--- Value = (obs_microbe_id, microbe_id, microbe_type, comments)

    obs_microbe_file = ObsMicrobe.objects.all()
    for row in obs_microbe_file:
        microbe_id_table[row.microbe_id] = (row.id, row.microbe_id, row.microbe_type, row.comments)
    return microbe_id_table

def tissue_id_mirror():
    tissue_id_table = OrderedDict({})
    #--- Key = (tissue_id)
    #--- Value = (obs_tissue_id, tissue_id, tissue_type, tissue_name, date_ground, comments)

    obs_tissue_file = ObsTissue.objects.all()
    for row in obs_tissue_file:
        tissue_id_table[row.tissue_id] = (row.id, row.tissue_id, row.tissue_type, row.tissue_name, row.date_ground, row.comments)
    return tissue_id_table

def well_id_mirror():
    well_id_table = OrderedDict({})
    #--- Key = (well_id)
    #--- Value = (obs_well_id, well_id, well, well_inventory, tube_label, comments)

    obs_well_file = ObsWell.objects.all()
    for row in obs_well_file:
        well_id_table[row.well_id] = (row.id, row.well_id, row.well, row.well_inventory, row.tube_label, row.comments)
    return well_id_table

def dna_id_mirror():
    dna_id_table = OrderedDict({})
    #--- Key = (dna_id)
    #--- Value = (obs_dna_id, dna_id, extraction_method, date, tube_id, tube_type, comments)

    obs_dna_file = ObsDNA.objects.all()
    for row in obs_dna_file:
        dna_id_table[row.dna_id] = (row.id, row.dna_id, row.extraction_method, row.date, row.tube_id, row.tube_type, row.comments)
    return dna_id_table

def plate_id_mirror():
    plate_id_table = OrderedDict({})
    #--- Key = (plate_id)
    #--- Value = (obs_plate_id, plate_id, plate_name, date, contents, rep, plate_type, plate_status, comments)

    obs_plate_file = ObsPlate.objects.all()
    for row in obs_plate_file:
        plate_id_table[row.plate_id] = (row.id, row.plate_id, row.plate_name, row.date, row.contents, row.rep, row.plate_type, row.plate_status, row.comments)
    return plate_id_table

def sample_id_mirror():
    sample_id_table = OrderedDict({})
    #--- Key = (sample_id)
    #--- Value = (obs_sample_id, sample_id, sample_type, sample_name, weight, volume, density, kernel_num, photo, comments)

    obs_sample_file = ObsSample.objects.all()
    for row in obs_sample_file:
        sample_id_table[row.sample_id] = (row.id, row.sample_id, row.sample_type, row.sample_name, row.weight, row.volume, row.density, row.kernel_num, row.photo, row.comments)
    return sample_id_table

def plot_id_mirror():
    plot_id_table = OrderedDict({})
    #--- Key = (plot_id)
    #--- Value = (obs_plot_id, plot_id, plot_name, range_num, plot, block, rep, kernel_num, planting_date, harvest_date, comments)

    obs_plot_file = ObsPlot.objects.all()
    for row in obs_plot_file:
        plot_id_table[row.plot_id] = (row.id, row.plot_id, row.plot_name, row.range_num, row.plot, row.block, row.rep, row.kernel_num, row.planting_date, row.harvest_date, row.comments)
    return plot_id_table

def env_id_mirror():
    env_id_table = OrderedDict({})
    #--- Key = (environment_id)
    #--- Value = (obs_env_id, environment_id, longitude, latitude, comments)

    obs_env_file = ObsEnv.objects.all()
    for row in obs_env_file:
        env_id_table[row.environment_id] = (row.id, row.environment_id, row.longitude, row.latitude, row.comments)
    return env_id_table

def isolate_id_mirror():
    isolate_id_table = OrderedDict({})
    #--- Key = (isolate_id)
    #--- Value = (isolate_table_id, isolate_id, stock_date, extract_color, organism, comments)

    isolate_file = Isolate.objects.all()
    for row in isolate_file:
        isolate_id_table[row.isolate_id] = (row.id, row.isolate_id, row.stock_date, row.extract_color, row.organism, row.comments)
    return isolate_id_table

def isolatestock_id_mirror():
    isolatestock_id_table = OrderedDict({})
    #--- Key = (isolatestock_id)
    #--- Value = (isolatestock_table_id, passport_id, location_id, disease_info_id, isolatestock_id, isolatestock_name, plant_organ, comments)

    isolatestock_file = IsolateStock.objects.all()
    for row in isolatestock_file:
        isolatestock_id_table[row.isolatestock_id] = (row.id, row.passport_id, row.locality_id, row.disease_info_id, row.isolatestock_id, row.isolatestock_name, row.plant_organ, row.comments)
    return isolatestock_id_table

def disease_name_mirror():
    disease_name_table = OrderedDict({})
    #--- Key = (common_name)
    #--- Value = (disease_info_id, common_name, abbrev, comments)

    disease_file = DiseaseInfo.objects.all()
    for row in disease_file:
        disease_name_table[row.common_name] = (row.id, row.common_name, row.abbrev, row.comments)
    return disease_name_table

def plot_id_seed_id_mirror():
    plot_id_seed_id_table = OrderedDict({})
    #--- Key = (plot_id)
    #--- Value = (seed_id)
    obs_tracker_obs_plot_id_table = OrderedDict({})
    #--- Key = (obs_plot_id)
    #--- Value = (seed_id)

    obs_plot_file = ObsPlot.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plot')
    for obs_tracker in obs_tracker_file:
        obs_tracker_obs_plot_id_table[(obs_tracker.obs_plot_id)] = (obs_tracker.stock.seed_id)
    for obs_plot in obs_plot_file:
        if (obs_plot.id) in obs_tracker_obs_plot_id_table:
            plot_id = obs_plot.plot_id
            plot_id.rstrip('\r')
            plot_id.rstrip('\n')
            plot_id_seed_id_table[plot_id] = (obs_tracker_obs_plot_id_table[(obs_plot.id)])
    return plot_id_seed_id_table

def plot_id_stock_id_mirror():
    plot_id_stock_id_table = OrderedDict({})
    #--- Key = (plot_id)
    #--- Value = (stock_id)
    obs_tracker_obs_plot_id_table = OrderedDict({})
    #--- Key = (obs_plot_id)
    #--- Value = (stock_id)

    obs_plot_file = ObsPlot.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plot')
    for obs_tracker in obs_tracker_file:
        obs_tracker_obs_plot_id_table[(obs_tracker.obs_plot_id)] = (obs_tracker.stock_id)
    for obs_plot in obs_plot_file:
        if (obs_plot.id) in obs_tracker_obs_plot_id_table:
            plot_id = obs_plot.plot_id
            plot_id.rstrip('\r')
            plot_id.rstrip('\n')
            plot_id_stock_id_table[plot_id] = (obs_tracker_obs_plot_id_table[(obs_plot.id)])
    return plot_id_stock_id_table

def plot_id_field_id_mirror():
    plot_id_field_id_table = OrderedDict({})
    #--- Key = (plot_id)
    #--- Value = (field_id)
    obs_tracker_obs_plot_id_table = OrderedDict({})
    #--- Key = (obs_plot_id)
    #--- Value = (field_id)

    obs_plot_file = ObsPlot.objects.all()
    obs_tracker_file = ObsTracker.objects.filter(obs_entity_type='plot')
    for obs_tracker in obs_tracker_file:
        obs_tracker_obs_plot_id_table[(obs_tracker.obs_plot_id)] = (obs_tracker.field_id)
    for obs_plot in obs_plot_file:
        if (obs_plot.id) in obs_tracker_obs_plot_id_table:
            plot_id = obs_plot.plot_id
            plot_id.rstrip('\r')
            plot_id.rstrip('\n')
            plot_id_field_id_table[plot_id] = (obs_tracker_obs_plot_id_table[(obs_plot.id)])
    return plot_id_field_id_table

def seed_id_mirror():
    seed_id_table = OrderedDict({})
    #--- Key = (seed_id)
    #--- Value = (stock_id, passport_id, seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, comments)

    stock_file = Stock.objects.all()
    for stock in stock_file:
        seed_id_table[stock.seed_id] = (stock.id, stock.passport_id, stock.seed_id, stock.seed_name, stock.cross_type, stock.pedigree, stock.stock_status, stock.stock_date, stock.inoculated, stock.comments)
    return seed_id_table

def obs_sample_id_mirror():
    obs_sample_id = ObsSample.objects.latest('id').id + 1
    return obs_sample_id

def obs_sample_table_mirror():
    obs_sample_table = OrderedDict({})
    #--- Key = (obs_sample_id, sample_id, sample_type, weight, kernel_num, photo, comments)
    #--- Value = (obs_sample_id)

    obs_sample_file = ObsSample.objects.all()
    for row in obs_sample_file:
        obs_sample_table[(row.id, row.sample_id, row.sample_type, row.weight, row.kernel_num, row.photo, row.comments)] = (row.id)
    return obs_sample_table

def obs_sample_hash_mirror():
    obs_sample_hash_table = OrderedDict({})
    #--- Key = (sample_id + sample_type + sample_name + weight + volume + density + kernel_num + photo + comments)
    #--- Value = (obs_sample_id)

    obs_sample_file = ObsSample.objects.all()
    for row in obs_sample_file:
        sample_hash = row.sample_id + row.sample_type + row.sample_name + row.weight + row.volume + row.density + row.kernel_num + row.photo + row.comments
        obs_sample_hash_table[sample_hash] = row.id
    return obs_sample_hash_table

def measurement_parameter_id_mirror():
    measurement_param_id = MeasurementParameter.objects.latest('id').id + 1
    return measurement_param_id

def measurement_parameter_table_mirror():
    measurement_param_table = OrderedDict({})
    #--- Key = (measurement_param_id, parameter, parameter_type, unit, protocol, trait_id_buckler)
    #--- Value = (measurement_param_id)

    measurement_param_file = MeasurementParameter.objects.all()
    for row in measurement_param_file:
        measurement_param_table[(row.id, row.parameter, row.parameter_type, row.unit_of_measure, row.protocol, row.trait_id_buckler)] = (row.id)
    return measurement_param_table

def measurement_parameter_hash_mirror():
    measurement_param_hash_table = OrderedDict({})
    #--- Key = (parameter + parameter_type + unit + protocol + trait_id_buckler)
    #--- Value = (measurement_param_id)

    measurement_param_file = MeasurementParameter.objects.all()
    for row in measurement_param_file:
        param_hash = row.parameter + row.parameter_type + row.unit_of_measure + row.protocol + row.trait_id_buckler
        measurement_param_hash_table[param_hash] = row.id
    return measurement_param_hash_table

def measurement_parameter_name_mirror():
    measurement_param_name_table = OrderedDict({})
    #--- Key = (parameter)
    #--- Value = (measurement_param_id, parameter, parameter_type, unit, protocol, trait_id_buckler)

    measurement_param_file = MeasurementParameter.objects.all()
    for row in measurement_param_file:
        measurement_param_name_table[row.parameter] = (row.id, row.parameter, row.parameter_type, row.unit_of_measure, row.protocol, row.trait_id_buckler)
    return measurement_param_name_table

def measurement_id_mirror():
    measurement_id = Measurement.objects.latest('id').id + 1
    return measurement_id

def measurement_table_mirror():
    measurement_table = OrderedDict({})
    #--- Key = (measurement_id, obs_tracker_id, user_id, measurement_param_id, time_of_measurement, value, comments)
    #--- Value = (measurement_id)

    measurement_file = Measurement.objects.all()
    for row in measurement_file:
        measurement_table[(row.id, row.obs_tracker_id, row.user_id, row.measurement_parameter_id, row.time_of_measurement, row.value, row.comments)] = (row.id)
    return measurement_table

def measurement_hash_mirror():
    measurement_hash_table = OrderedDict({})
    #--- Key = (obs_tracker_id + user_id + measurement_param_id + time_of_measurement + value + comments)
    #--- Value = (measurement_id)

    measurement_file = Measurement.objects.all()
    for row in measurement_file:
        measurement_hash = str(row.obs_tracker_id) + str(row.measurement_parameter_id) + row.time_of_measurement + row.value + row.comments
        measurement_hash_table[measurement_hash] = row.id
    return measurement_hash_table

def maize_sample_id_mirror():
    maize_sample_id = MaizeSample.objects.latest('id').id + 1
    return maize_sample_id

def maize_sample_table_mirror():
    maize_sample_table = OrderedDict({})
    #--- Key = (maize_sample_id, locality_id, maize_id, type_of_source, sample_source, weight, description, photo, comments)
    #--- Value = (maize_sample_id)

    maize_file = MaizeSample.objects.all()
    for row in maize_file:
        maize_sample_table[(row.id, row.locality_id, row.maize_id, row.type_of_source, row.sample_source, row.weight, row.description, row.photo, row.comments)] = (row.id)
    return maize_sample_table

def maize_sample_hash_mirror():
    maize_sample_hash_table = OrderedDict({})
    #--- Key = (locality_id + maize_id + type_of_source + sample_source + weight + description + photo + comments)
    #--- Value = (maize_sample_id)

    maize_file = MaizeSample.objects.all()
    for row in maize_file:
        maize_hash = row.maize_id + row.gps_altitude + row.county + row.weight + row.appearance + row.photo + row.gps_accuracy + row.gps_latitude + row.gps_longitude + row.harvest_date + row.maize_variety + row.moisture_content + row.seed_source + row.source_type + row.storage_conditions + row.storage_months + row.sub_location + row.village
        maize_sample_hash_table[maize_hash] = row.id
    return maize_sample_hash_table

def maize_id_mirror():
    maize_id_table = OrderedDict({})
    #--- Key = (maize_id)
    #--- Value = (maize_sample_id, locality_id, maize_id, type_of_source, sample_source, weight, description, photo, comments)

    maize_file = MaizeSample.objects.all()
    for row in maize_file:
        maize_id = row.maize_id
        maize_id_table[maize_id] = (row.id, row.maize_id, row.gps_altitude, row.county, row.weight, row.appearance, row.photo, row.gps_accuracy, row.gps_latitude, row.gps_longitude, row.harvest_date, row.maize_variety, row.moisture_content, row.seed_source, row.source_type, row.storage_conditions, row.storage_months, row.sub_location, row.village)
    return maize_id_table

def obs_extract_id_mirror():
    obs_extract_id = ObsExtract.objects.latest('id').id + 1
    return obs_extract_id

def obs_extract_table_mirror():
    obs_extract_table = OrderedDict({})
    #--- Key = (obs_extract_id, extract_id, weight, rep, grind_method, solvent, comments)
    #--- Value = (obs_extract_id)

    extract_file = ObsExtract.objects.all()
    for row in extract_file:
        obs_extract_table[(row.id, row.extract_id, row.weight, row.rep, row.grind_method, row.solvent, row.comments)] = (row.id)
    return obs_extract_table

def obs_extract_hash_mirror():
    obs_extract_hash_table = OrderedDict({})
    #--- Key = (extract_id + weight + rep + grind_method + solvent + comments)
    #--- Value = (obs_extract_id)

    extract_file = ObsExtract.objects.all()
    for row in extract_file:
        extract_hash = row.extract_id + row.weight + row.rep + row.grind_method + row.solvent + row.comments
        extract_hash.rstrip('\r')
        extract_hash.rstrip('\n')
        obs_extract_hash_table[extract_hash] = row.id
    return obs_extract_hash_table

def separation_id_mirror():
    separation_id = Separation.objects.latest('id').id + 1
    return separation_id

def separation_table_mirror():
    separation_table = OrderedDict({})
    #--- Key = (separation_id, sample_id, separation_type, apparatus, SG, light_weight, intermediate_weight, heavy_weight, light_percent, intermediate_percent, heavy_percent, operating_factor, comments)
    #--- Value = (separation_id)

    separation_file = Separation.objects.all()
    for row in separation_file:
        separation_table[(row.id, row.obs_sample_id, row.separation_type, row.apparatus, row.SG, row.light_weight, row.intermediate_weight, row.heavy_weight, row.light_percent, row.intermediate_percent, row.heavy_percent, row.operating_factor, row.comments)] = (row.id)
    return separation_table

def separation_hash_mirror():
    separation_hash_table = OrderedDict({})
    #--- Key = (sample_id + separation_type + apparatus + SG + light_weight + intermediate_weight + heavy_weight + light_percent + intermediate_percent + heavy_percent + operating_factor + comments)
    #--- Value = (separation_id)

    separation_file = Separation.objects.all()
    for row in separation_file:
        separation_hash = str(row.obs_sample_id) + row.separation_type + row.apparatus + row.SG + row.light_weight + row.intermediate_weight + row.heavy_weight + row.light_percent + row.intermediate_percent + row.heavy_percent + row.operating_factor + row.comments
        separation_hash.rstrip('\r')
        separation_hash.rstrip('\n')
        separation_hash_table[separation_hash] = row.id
    return separation_hash_table

def citation_hash_mirror():
    citation_hash_table = OrderedDict({})
    #--- Key = (citation_type + title + url + pubmed_id + comments)
    #--- Value = (citation_id)

    citation_file = Citation.objects.all()
    for row in citation_file:
        citation_hash = row.citation_type + row.title + row.url + row.pubmed_id + row.comments
        citation_hash.rstrip('\r')
        citation_hash.rstrip('\n')
        citation_hash_table[citation_hash] = row.id
    return citation_hash_table

def citation_id_mirror():
    citation_id = Citation.objects.latest('id').id + 1
    return citation_id

def medium_hash_mirror():
    medium_hash_table = OrderedDict({})
    #--- Key = (citation_id + media_name + media_type + media_description + media_preparation + comments)
    #--- Value = (medium_id)

    medium_file = Medium.objects.all()
    for row in medium_file:
        medium_hash = str(row.citation_id) + row.media_name + row.media_type + row.media_description + row.media_preparation + row.comments
        medium_hash_table[medium_hash] = row.id
    return medium_hash_table

def medium_id_mirror():
    medium_id = Medium.objects.latest('id').id + 1
    return medium_id

def medium_name_mirror():
    medium_id_table = OrderedDict({})
    #--- Key = (medium_id, citation_id, media_name, media_type, media_description, media_preparation, comments)
    #--- Value = (media_name)

    medium_file = Medium.objects.all()
    for row in medium_file:
        media_name = row.media_name
        medium_id_table[media_name] = (row.id, row.citation_id, row.media_name, row.media_type, row.media_description, row.media_preparation, row.comments)
    return medium_id_table

def obs_culture_hash_mirror():
    obs_culture_hash_table = OrderedDict({})
    #--- Key = (medium_id + culture_id + culture_name + microbe_type + plating_cycle + dilution + image_filename + comments + num_colonies + num_microbes)
    #--- Value = (obs_culture_id)

    culture_file = ObsCulture.objects.all()
    for row in culture_file:
        culture_hash = str(row.medium_id) + row.culture_id + row.culture_name + row.microbe_type + row.plating_cycle + row.dilution + row.image_filename + row.comments + row.num_colonies + row.num_microbes
        obs_culture_hash_table[culture_hash] = row.id
    return obs_culture_hash_table

def obs_culture_id_mirror():
    obs_culture_id = ObsCulture.objects.latest('id').id + 1
    return obs_culture_id

def obs_tissue_hash_mirror():
    obs_tissue_hash_table = OrderedDict({})
    #--- Key = (tissue_id + tissue_type + tissue_name + date_ground + comments)
    #--- Value = (obs_tissue_id)

    tissue_file = ObsTissue.objects.all()
    for row in tissue_file:
        tissue_hash = row.tissue_id + row.tissue_type + row.tissue_name + row.date_ground + row.comments
        obs_tissue_hash_table[tissue_hash] = row.id
    return obs_tissue_hash_table

def obs_tissue_id_mirror():
    obs_tissue_id = ObsTissue.objects.latest('id').id + 1
    return obs_tissue_id

def location_hash_mirror():
    location_hash_table = OrderedDict({})
    #--- Key = (locality_id + building_name + location_name + room + shelf + column + box_name + comments)
    #--- Value = (location_id)

    location_file = Location.objects.all()
    for row in location_file:
        location_hash = str(row.locality_id) + row.building_name + row.location_name + row.room + row.shelf + row.column + row.box_name + row.comments
        location_hash_table[location_hash] = row.id
    return location_hash_table

def location_name_mirror():
    location_name_table = OrderedDict({})
    #--- Key = (location_id, locality_id, building_name, location_name, room, shelf, column, box_name, comments)
    #--- Value = (location_name)

    location_file = Location.objects.all()
    for row in location_file:
        location_name_table[row.location_name] = (row.id, row.locality_id, row.building_name, row.location_name, row.room, row.shelf, row.column, row.box_name, row.comments)
    return location_name_table

def location_id_mirror():
    location_id = Location.objects.latest('id').id + 1
    return location_id

def obs_plate_hash_mirror():
    obs_plate_hash_table = OrderedDict({})
    #--- Key = (plate_id + plate_name + date + contents + rep + plate_type + plate_status + comments)
    #--- Value = (obs_plate_id)

    plate_file = ObsPlate.objects.all()
    for row in plate_file:
        plate_hash = row.plate_id + row.plate_name + row.date + row.contents + row.rep + row.plate_type + row.plate_status + row.comments
        plate_hash.rstrip('\r')
        plate_hash.rstrip('\n')
        obs_plate_hash_table[plate_hash] = row.id
    return obs_plate_hash_table

def obs_plate_id_mirror():
    plate_id = ObsPlate.objects.latest('id').id + 1
    return plate_id

def obs_dna_hash_mirror():
    obs_dna_hash_table = OrderedDict({})
    #--- Key = (dna_id + extraction_method + date + tube_id + tube_type + comments)
    #--- Value = (obs_dna_id)

    dna_file = ObsDNA.objects.all()
    for row in dna_file:
        dna_hash = row.dna_id + row.extraction_method + row.date + row.tube_id + row.tube_type + row.comments
        dna_hash.rstrip('\r')
        dna_hash.rstrip('\n')
        obs_dna_hash_table[dna_hash] = row.id
    return obs_dna_hash_table

def obs_dna_id_mirror():
    obs_dna_id = ObsDNA.objects.latest('id').id + 1
    return obs_dna_id

def obs_microbe_hash_mirror():
    obs_microbe_hash_table = OrderedDict({})
    #--- Key = (microbe_id + microbe_type + comments)
    #--- Value = (obs_microbe_id)

    microbe_file = ObsMicrobe.objects.all()
    for row in microbe_file:
        microbe_hash = row.microbe_id + row.microbe_type + row.comments
        obs_microbe_hash_table[microbe_hash] = row.id
    return obs_microbe_hash_table

def obs_microbe_id_mirror():
    obs_microbe_id = ObsMicrobe.objects.latest('id').id + 1
    return obs_microbe_id

def collecting_hash_mirror():
    collecting_hash_table = OrderedDict({})
    #--- Key = (user_id + collection_date, collection_method + comments)
    #--- Value = (collecting_id)

    collecting_file = Collecting.objects.all()
    for row in collecting_file:
        collecting_hash = str(row.user_id) + row.collection_date + row.collection_method + row.comments
        collecting_hash_table[collecting_hash] = row.id
    return collecting_hash_table

def collecting_id_mirror():
    collecting_id = Collecting.objects.latest('id').id + 1
    return collecting_id

def passport_hash_mirror():
    passport_hash_table = OrderedDict({})
    #--- Key = (collecting_id + people_id, taxonomy_id)
    #--- Value = (passport_id)

    passport_file = Passport.objects.all()
    for row in passport_file:
        passport_hash = str(row.collecting_id) + str(row.people_id) + str(row.taxonomy_id)
        passport_hash_table[passport_hash] = row.id
    return passport_hash_table

def passport_id_mirror():
    passport_id = Passport.objects.latest('id').id + 1
    return passport_id

def isolatestock_hash_mirror():
    isolatestock_hash_table = OrderedDict({})
    #--- Key = (passport_id + location_id + disease_info_id + isolatestock_id + isolatestock_name + plant_organ + comments)
    #--- Value = (isolatestock_table_id)

    isolatestock_file = IsolateStock.objects.all()
    for row in isolatestock_file:
        isolatestock_hash = str(row.passport_id) + str(row.locality_id) + str(row.disease_info_id) + row.isolatestock_id + row.isolatestock_name + row.plant_organ + row.comments
        isolatestock_hash.rstrip('\r')
        isolatestock_hash.rstrip('\n')
        isolatestock_hash_table[isolatestock_hash] = row.id
    return isolatestock_hash_table

def isolatestock_table_id_mirror():
    isolatestock_table_id = IsolateStock.objects.latest('id').id + 1
    return isolatestock_table_id

def isolate_hash_mirror():
    isolate_hash_table = OrderedDict({})
    #--- Key = (isolate_id + date + extract_color + organism + comments)
    #--- Value = (isolate_table_id)

    isolate_file = Isolate.objects.all()
    for row in isolate_file:
        isolate_hash = row.isolate_id + row.stock_date + row.extract_color + row.organism +  row.comments
        isolate_hash.rstrip('\r')
        isolate_hash.rstrip('\n')
        isolate_hash_table[isolate_hash] = row.id
    return isolate_hash_table

def isolate_table_id_mirror():
    isolate_table_id = Isolate.objects.latest('id').id + 1
    return isolate_table_id

def stock_hash_mirror():
    stock_hash_table = OrderedDict({})
    #--- Key = (passport_id + seed_id + seed_name + cross_type + pedigree + stock_status + stock_date + inoculated + comments)
    #--- Value = (stock_id)

    stock_file = Stock.objects.all()
    for row in stock_file:
        stock_hash = str(row.passport_id) + row.seed_id + row.seed_name + row.cross_type + row.pedigree + row.stock_status + row.stock_date + str(row.inoculated) + row.comments
        stock_hash_table[stock_hash] = row.id
    return stock_hash_table

def stock_id_mirror():
    stock_id = Stock.objects.latest('id').id + 1
    return stock_id

def obs_plot_hash_mirror():
    obs_plot_hash_table = OrderedDict({})
    #--- Key = (plot_id + plot_name + range_num + plot + block + rep + kernel_num + planting_date + harvest_date + comments)
    #--- Value = (obs_plot_id)

    row_file = ObsPlot.objects.all()
    for row in row_file:
        obs_plot_hash = row.plot_id + row.plot_name + row.range_num + row.row_num + row.plot + row.block + row.rep + row.kernel_num + row.planting_date + row.harvest_date + row.comments
        obs_plot_hash_table[obs_plot_hash] = row.id
    return obs_plot_hash_table

def obs_plot_id_mirror():
    obs_plot_id = ObsPlot.objects.latest('id').id + 1
    return obs_plot_id

def obs_well_hash_mirror():
    obs_well_hash_table = OrderedDict({})
    #--- Key = (well_id + well + well_inventory + tube_label + comments)
    #--- Value = (obs_well_id)

    well_file = ObsWell.objects.all()
    for row in well_file:
        obs_well_hash = row.well_id + row.well + row.well_inventory + row.tube_label + row.comments
        obs_well_hash_table[obs_well_hash] = row.id
    return obs_well_hash_table

def obs_well_id_mirror():
    obs_well_id = ObsWell.objects.latest('id').id + 1
    return obs_well_id

def obs_env_hash_mirror():
    obs_env_hash_table = OrderedDict({})
    #--- Key = (environment_id + longitude + latitude + comments)
    #--- Value = (obs_env_id)

    env_file = ObsEnv.objects.all()
    for row in env_file:
        obs_env_hash = row.environment_id + row.longitude + row.latitude + row.comments
        obs_env_hash_table[obs_env_hash] = row.id
    return obs_env_hash_table

def obs_env_id_mirror():
    obs_env_id = ObsEnv.objects.latest('id').id + 1
    return obs_env_id

def obs_plant_hash_mirror():
    obs_plant_hash_table = OrderedDict({})
    #--- Key = (plot_id + plot_name + range_num + plot + block + rep + kernel_num + planting_date + harvest_date + comments)
    #--- Value = (obs_plot_id)

    row_file = ObsPlant.objects.all()
    for row in row_file:
        obs_plant_hash = row.plant_id + row.plant_num + row.comments
        obs_plant_hash_table[obs_plant_hash] = row.id
    return obs_plant_hash_table

def obs_plant_id_mirror():
    obs_plant_id = ObsPlant.objects.latest('id').id + 1
    return obs_plant_id

def people_hash_mirror():
    people_hash_table = OrderedDict({})
    #--- Key = (first_name + last_name + organization + phone + email + comments)
    #--- Value = (people_id)

    people_file = People.objects.all()
    for row in people_file:
        people_hash = row.first_name + row.last_name + row.organization + row.phone + row.email + row.comments
        people_hash_table[people_hash] = row.id
    return people_hash_table

def people_id_mirror():
    people_id = People.objects.latest('id').id + 1
    return people_id

def taxonomy_hash_mirror():
    taxonomy_hash_table = OrderedDict({})
    #--- Key = (binomial + species + population + common_name + alias + race + subtaxa)
    #--- Value = (taxonomy_id)

    taxonomy_file = Taxonomy.objects.all()
    for row in taxonomy_file:
        taxonomy_hash = row.binomial + row.population + row.common_name + row.alias + row.race + row.subtaxa
        taxonomy_hash_table[taxonomy_hash] = row.id
    return taxonomy_hash_table

def taxonomy_id_mirror():
    taxonomy_id = Taxonomy.objects.latest('id').id + 1
    return taxonomy_id

def stockpacket_hash_mirror():
    stockpacket_hash_table = OrderedDict({})
    #--- Key = (stock_id + location_id + weight + num_seeds + comments)
    #--- Value = (stockpacket_id)

    packet_file = StockPacket.objects.all()
    for row in packet_file:
        packet_hash = str(row.stock_id) + str(row.location_id) + row.weight + row.num_seeds + row.comments
        stockpacket_hash_table[packet_hash] = row.id
    return stockpacket_hash_table

def stockpacket_id_mirror():
    stockpacket_id = StockPacket.objects.latest('id').id + 1
    return stockpacket_id

def obs_tracker_source_hash_mirror():
    obs_tracker_source_hash_table = OrderedDict({})
    #--- Key = (source_obs_id, target_obs_id, relationship)
    #--- Value = (obs_tracker_id)

    source_file = ObsTrackerSource.objects.all()
    for row in source_file:
        source_hash = str(row.source_obs_id) + str(row.target_obs_id) + str(row.relationship)
        obs_tracker_source_hash_table[source_hash] = row.id
    return obs_tracker_source_hash_table

def obs_tracker_source_id_mirror():
    obs_tracker_source_id = ObsTrackerSource.objects.latest('id').id + 1
    return obs_tracker_source_id
