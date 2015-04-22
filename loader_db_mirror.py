import os
import csv
from collections import OrderedDict
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
import django
django.setup()
from lab.models import User, Experiment, Locality, MaizeSample, ObsTracker, ObsTrackerSource, ObsSample, Separation, ObsExtract, MeasurementParameter, Measurement

def user_id_mirror():
    user_file = User.objects.all()
    user_id = 1
    for row in user_file:
        user_id = user_id + 1
    return user_id

def user_hash_mirror():
    user_hash_table = OrderedDict({})
    #--- Key = (hash(username))
    #--- Value = (user_id)

    user_file = User.objects.all()
    for row in user_file:
        user_hash_table[(hash(row.username))] = (row.id)
    return user_hash_table

def experiment_id_mirror():
    experiment_file = Experiment.objects.all()
    experiment_id = 1
    for row in experiment_file:
        experiment_id = experiment_id + 1
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
    #--- Key = (hash(user_id, field_id, name, start_date, purpose, comments))
    #--- Value = (id)

    experiment_file = Experiment.objects.all()
    for row in experiment_file:
        experiment_hash_table[(hash((row.user_id, row.field_id, row.name, row.start_date, row.purpose, row.comments)))] = (row.id)
    return experiment_hash_table

def experiment_name_mirror():
    experiment_name_table = OrderedDict({})
    #--- Key = (name)
    #--- Value = (id, user_id, field_id, name, start_date, purpose, comments)

    experiment_file = Experiment.objects.all()
    for row in experiment_file:
        experiment_name_table[(row.name)] = (row.id, row.user_id, row.field_id, row.name, row.start_date, row.purpose, row.comments)
    return experiment_name_table

def locality_id_mirror():
    locality_file = Locality.objects.all()
    locality_id = 1
    for row in locality_file:
        locality_id = locality_id + 1
    return locality_id

def locality_table_mirror():
    locality_table = OrderedDict({})
    #--- Key = (locality_id, city, state, country, zipcode)
    #--- Value = (locality_id)

    locality_file = Locality.objects.all()
    for row in locality_file:
        locality_table[(row.id, row.city, row.state, row.country, row.zipcode)] = (row.id)
    return locality_table

def locality_hash_mirror():
    locality_hash_table = OrderedDict({})
    #--- Key = (hash(city, state, country, zipcode))
    #--- Value = (locality_id)

    locality_file = Locality.objects.all()
    for row in locality_file:
        locality_hash_table[(hash((row.city, row.state, row.country, row.zipcode)))] = (row.id)
    return locality_hash_table

def obs_tracker_id_mirror():
    obs_tracker_file = ObsTracker.objects.all()
    obs_tracker_id = 1
    for row in obs_tracker_file:
        obs_tracker_id = obs_tracker_id + 1
    return obs_tracker_id

def obs_tracker_table_mirror():
    obs_tracker_table = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, location_id, obs_culture_id, obs_dna_id, obs_env_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id, maize_sample_id, obs_extract_id)
    #--- Value = (obs_tracker_id)

    obs_tracker_file = ObsTracker.objects.all()
    for row in obs_tracker_file:
        obs_tracker_table[(row.id, row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.location_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_row_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id, 1, 1)] = (row.id)
    return obs_tracker_table

def obs_tracker_hash_mirror():
    obs_tracker_hash_table = OrderedDict({})
    #--- Key = (hash(obs_entity_type, experiment_id, field_id, isolate_id, location_id, obs_culture_id, obs_dna_id, obs_env_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id, maize_sample_id, obs_extract_id))
    #--- Value = (obs_tracker_id)

    obs_tracker_file = ObsTracker.objects.all()
    for row in obs_tracker_file:
        obs_tracker_hash_table[(hash((row.obs_entity_type, row.experiment_id, row.field_id, row.isolate_id, row.location_id, row.obs_culture_id, row.obs_dna_id, row.obs_env_id, row.obs_microbe_id, row.obs_plant_id, row.obs_plate_id, row.obs_row_id, row.obs_sample_id, row.obs_tissue_id, row.obs_well_id, row.stock_id, row.user_id, 1, 1)))] = (row.id)
    return obs_tracker_hash_table

def obs_sample_id_mirror():
    obs_sample_file = ObsSample.objects.all()
    obs_sample_id = 1
    for row in obs_sample_file:
        obs_sample_id = obs_sample_id + 1
    return obs_sample_id

def obs_sample_table_mirror():
    obs_sample_table = OrderedDict({})
    #--- Key = (obs_sample_id, sample_id, sample_type, weight, kernel_num, photo, comments)
    #--- Value = (obs_sample_id)

    obs_sample_file = ObsSample.objects.all()
    for row in obs_sample_file:
        obs_sample_table[(row.id, row.sample_id, row.sample_type, row.weight, row.kernel_num, "", row.comments)] = (row.id)
    return obs_sample_table

def obs_sample_hash_mirror():
    obs_sample_hash_table = OrderedDict({})
    #--- Key = (hash(sample_id, sample_type, weight, kernel_num, photo, comments))
    #--- Value = (obs_sample_id)

    obs_sample_file = ObsSample.objects.all()
    for row in obs_sample_file:
        obs_sample_hash_table[(hash((row.sample_id, row.sample_type, row.weight, row.kernel_num, "", row.comments)))] = (row.id)
    return obs_sample_hash_table

def measurement_parameter_id_mirror():
    measurement_param_file = MeasurementParameter.objects.all()
    measurement_param_id = 1
    for row in measurement_param_file:
        measurement_param_id = measurement_param_id + 1
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
    #--- Key = (hash(parameter, parameter_type, unit, protocol, trait_id_buckler))
    #--- Value = (measurement_param_id)

    measurement_param_file = MeasurementParameter.objects.all()
    for row in measurement_param_file:
        measurement_param_hash_table[(hash((row.parameter, row.parameter_type, row.unit_of_measure, row.protocol, row.trait_id_buckler)))] = (row.id)
    return measurement_param_hash_table

def measurement_id_mirror():
    measurement_file = Measurement.objects.all()
    measurement_id = 1
    for row in measurement_file:
        measurement_id = measurement_id + 1
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
    #--- Key = (hash(obs_tracker_id, user_id, measurement_param_id, time_of_measurement, value, comments))
    #--- Value = (measurement_id)

    measurement_file = Measurement.objects.all()
    for row in measurement_file:
        measurement_hash_table[(hash((row.obs_tracker_id, row.user_id, row.measurement_parameter_id, row.time_of_measurement, row.value, row.comments)))] = (row.id)
    return measurement_hash_table

def maize_sample_id_mirror():
    maize_file = MaizeSample.objects.all()
    maize_sample_id = 1
    for row in maize_file:
        maize_sample_id = maize_sample_id + 1
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
    #--- Key = (hash(locality_id, maize_id, type_of_source, sample_source, weight, description, photo, comments))
    #--- Value = (maize_sample_id)

    maize_file = MaizeSample.objects.all()
    for row in maize_file:
        maize_sample_hash_table[(hash((row.locality_id, row.maize_id, row.type_of_source, row.sample_source, row.weight, row.description, row.photo, row.comments)))] = (row.id)
    return maize_sample_hash_table

def maize_sample_maize_id_mirror():
    maize_id_table = OrderedDict({})
    #--- Key = (maize_id)
    #--- Value = (maize_sample_id, locality_id, maize_id, type_of_source, sample_source, weight, description, photo, comments)

    maize_file = MaizeSample.objects.all()
    for row in maize_file:
        maize_id_table[(row.maize_id)] = (row.id, row.locality_id, row.maize_id, row.type_of_source, row.sample_source, row.weight, row.description, row.photo, row.comments)
    return maize_id_table

def obs_extract_id_mirror():
    extract_file = ObsExtract.objects.all()
    obs_extract_id = 1
    for row in extract_file:
        obs_extract_id = obs_extract_id + 1
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
    #--- Key = (hash(extract_id, weight, rep, grind_method, solvent, comments))
    #--- Value = (obs_extract_id)

    extract_file = ObsExtract.objects.all()
    for row in extract_file:
        obs_extract_hash_table[(hash((row.extract_id, row.weight, row.rep, row.grind_method, row.solvent, row.comments)))] = (row.id)
    return obs_extract_hash_table

def separation_id_mirror():
    separation_file = Separation.objects.all()
    separation_id = 1
    for row in separation_file:
        separation_id = separation_id + 1
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
    #--- Key = (hash(sample_id, separation_type, apparatus, SG, light_weight, intermediate_weight, heavy_weight, light_percent, intermediate_percent, heavy_percent, operating_factor, comments))
    #--- Value = (separation_id)

    separation_file = Separation.objects.all()
    for row in separation_file:
        separation_hash_table[(hash((row.obs_sample_id, row.separation_type, row.apparatus, row.SG, row.light_weight, row.intermediate_weight, row.heavy_weight, row.light_percent, row.intermediate_percent, row.heavy_percent, row.operating_factor, row.comments)))] = (row.id)
    return separation_hash_table
