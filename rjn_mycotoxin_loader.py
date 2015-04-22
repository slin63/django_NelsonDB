
import os
import csv
from collections import OrderedDict
import time
import loader_db_mirror

def migrate():

    locality_table = OrderedDict({})
    #--- Key = (locality_id, city, state, country, zipcode)
    #--- Value = (locality_id)
    obs_tracker_table = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, location_id, obs_culture_id, obs_dna_id, obs_env_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id, maize_sample_id, obs_extract_id)
    #--- Value = (obs_tracker_id)
    obs_sample_table = OrderedDict({})
    #--- Key = (obs_sample_id, sample_id, sample_type, weight, kernel_num, photo, comments)
    #--- Value = (obs_sample_id)
    measurement_table = OrderedDict({})
    #--- Key = (measurement_id, obs_tracker_id, user_id, measurement_param_id, time_of_measurement, value, comments)
    #--- Value = (measurement_id)
    measurement_param_table = OrderedDict({})
    #--- Key = (measurement_param_id, parameter, parameter_type, unit, protocol, trait_id_buckler)
    #--- Value = (measurement_param_id)
    experiment_table = OrderedDict({})
    #--- Key = (experiment_id, user_id, field_id, name, start_date, purpose, comments)
    #--- Value = (experiment_id)

    maize_sample_table = OrderedDict({})
    #--- Key = (maize_sample_id, locality_id, maize_id, type_of_source, sample_source, weight, description, photo, comments)
    #--- Value = (maize_sample_id)
    separation_table = OrderedDict({})
    #--- Key = (separation_id, sample_id, separation_type, apparatus, SG, light_weight, intermediate_weight, heavy_weight, light_percent, intermediate_percent, heavy_percent, operating_factor, comments)
    #--- Value = (separation_id)
    obs_extract_table = OrderedDict({})
    #--- Key = (obs_extract_id, extract_id, weight, rep, grind_method, solvent, comments)
    #--- Value = (obs_extract_id)

    locality_hash_table = OrderedDict({})
    #--- Key = (hash(city, state, country, zipcode))
    #--- Value = (locality_id)
    maize_id_table = OrderedDict({})
    #--- Key = (maize_id)
    #--- Value = (maize_sample_id, locality_id, maize_id, type_of_source, sample_source, weight, description, photo, comments)
    maize_sample_hash_table = OrderedDict({})
    #--- Key = (hash(locality_id, maize_id, type_of_source, sample_source, weight, description, photo, comments))
    #--- Value = (maize_sample_id)
    obs_tracker_hash_table = OrderedDict({})
    #--- Key = (hash(obs_entity_type, experiment_id, field_id, isolate_id, location_id, obs_culture_id, obs_dna_id, obs_env_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id, maize_sample_id, obs_extract_id))
    #--- Value = (obs_tracker_id)
    obs_sample_hash_table = OrderedDict({})
    #--- Key = (hash(sample_id, sample_type, weight, kernel_num, photo, comments))
    #--- Value = (obs_sample_id)
    obs_sample_id_table = OrderedDict({})
    #--- Key = (sample_id)
    #--- Value = (obs_sample_id, sample_id, sample_type, weight, kernel_num, photo, comments)
    obs_tracker_sample_id_table = OrderedDict({})
    #--- Key = (sample_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, location_id, obs_culture_id, obs_dna_id, obs_env_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id, maize_sample_id, obs_extract_id)
    obs_tracker_maize_id_table = OrderedDict({})
    #--- Key = (maize_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, location_id, obs_culture_id, obs_dna_id, obs_env_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id, maize_sample_id, obs_extract_id)
    obs_tracker_extract_id_table = OrderedDict({})
    #--- Key = (extract_id)
    #--- Value = (obs_tracker_id, obs_entity_type, experiment_id, field_id, isolate_id, location_id, obs_culture_id, obs_dna_id, obs_env_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id, maize_sample_id, obs_extract_id)
    obs_extract_hash_table = OrderedDict({})
    #--- Key = (hash(extract_id, weight, rep, grind_method, solvent, comments))
    #--- Value = (obs_extract_id)
    obs_extract_id_table = OrderedDict({})
    #--- Key = (extract_id)
    #--- Value = (obs_extract_id, extract_id, fraction, weight, rep, grind_method, solvent, comments)
    separation_hash_table = OrderedDict({})
    #--- Key = (hash(sample_id, separation_type, apparatus, SG, light_weight, intermediate_weight, heavy_weight, light_percent, intermediate_percent, heavy_percent, operating_factor, comments))
    #--- Value = (separation_id)
    measurement_param_hash_table = OrderedDict({})
    #--- Key = (hash(parameter, parameter_type, unit, protocol, trait_id_buckler))
    #--- Value = (measurement_param_id)
    measurement_param_name_table = OrderedDict({})
    #--- Key = (measurement_param_id, parameter, parameter_type, unit, protocol, trait_id_buckler)
    #--- Value = (parameter)
    measurement_hash_table = OrderedDict({})
    #--- Key = (hash(obs_tracker_id, user_id, measurement_param_id, time_of_measurement, value, comments))
    #--- Value = (measurement_id)
    user_hash_table = OrderedDict({})
    #--- Key = (hash(username))
    #--- Value = (user_id)
    experiment_name_table = OrderedDict({})
    #--- Key = (name)
    #--- Value = (id, user_id, field_id, name, start_date, purpose, comments)
    experiment_hash_table = OrderedDict({})
    #--- Key = (hash(user_id, field_id, name, start_date, purpose, comments))
    #--- Value = (id)

    experiment_id = loader_db_mirror.experiment_id_mirror()
    experiment_hash_table = loader_db_mirror.experiment_hash_mirror()
    experiment_table = loader_db_mirror.experiment_table_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    obs_tracker_table = loader_db_mirror.obs_tracker_table_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()

    locality_id = loader_db_mirror.locality_id_mirror()
    locality_table = loader_db_mirror.locality_table_mirror()
    locality_hash_table = loader_db_mirror.locality_hash_mirror()

    obs_sample_id = loader_db_mirror.obs_sample_id_mirror()
    obs_sample_table = loader_db_mirror.obs_sample_table_mirror()
    obs_sample_hash_table = loader_db_mirror.obs_sample_hash_mirror()

    measurement_param_id = loader_db_mirror.measurement_parameter_id_mirror()
    measurement_param_table = loader_db_mirror.measurement_parameter_table_mirror()
    measurement_param_hash_table = loader_db_mirror.measurement_parameter_hash_mirror()

    measurement_id = loader_db_mirror.measurement_id_mirror()
    measurement_table = loader_db_mirror.measurement_table_mirror()
    measurement_hash_table = loader_db_mirror.measurement_hash_mirror()

    maize_sample_id = loader_db_mirror.maize_sample_id_mirror()
    maize_sample_table = loader_db_mirror.maize_sample_table_mirror()
    maize_sample_hash_table = loader_db_mirror.maize_sample_hash_mirror()
    maize_id_table = loader_db_mirror.maize_sample_maize_id_mirror()

    obs_extract_id = loader_db_mirror.obs_extract_id_mirror()
    obs_extract_table = loader_db_mirror.obs_extract_table_mirror()
    obs_extract_hash_table = loader_db_mirror.obs_extract_hash_mirror()

    user_id = loader_db_mirror.user_id_mirror()
    user_hash_table = loader_db_mirror.user_hash_mirror()

    separation_id = loader_db_mirror.separation_id_mirror()
    separation_table = loader_db_mirror.separation_table_mirror()
    separation_hash_table = loader_db_mirror.separation_hash_mirror()

    #maize_sample_table[(1,1,'No Maize','No Maize','No Maize','No Maize','No Maize','No Maize','No Maize')] = 1
    #maize_sample_hash_table[(hash((1,'No Maize','No Maize','No Maize','No Maize','No Maize','No Maize','No Maize')))] = 1
    #maize_id_table[('No Maize')] = (1,'No Maize','No Maize','No Maize','No Maize','No Maize','No Maize','No Maize','No Maize')
    #obs_extract_table[(1,'No Extract','No Extract','No Extract','No Extract','No Extract','No Extract','No Extract')] = 1
    #obs_extract_hash_table[(hash(('No Extract','No Extract','No Extract','No Extract','No Extract','No Extract','No Extract')))] = 1

    maize_sample_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/DataDumps/kenya_mycotoxin/template_maize.csv'), dialect='excel')
    for row in maize_sample_file:
        maize_id = row["Maize ID"]
        type_of_source = row["Type of Source"]
        sample_source = row["Sample Source"]
        city = row["City"]
        state = row["State"]
        country = row["Country"]
        zipcode = row["Zipcode"]
        weight = row["Weight"]
        description = row["Description"]
        photo = row["Photo"]
        comments = row["Comments"]

        locality_hash = hash((city, state, country, zipcode))
        if (locality_hash) in locality_hash_table:
            pass
        else:
            locality_hash_table[(locality_hash)] = locality_id
            locality_table[(locality_id, city, state, country, zipcode)] = locality_id
            locality_id = locality_id + 1

        maize_sample_hash = hash((locality_hash_table[(locality_hash)], maize_id, type_of_source, sample_source, weight, description, photo, comments))
        if (maize_sample_hash) in maize_sample_hash_table:
            pass
        else:
            maize_sample_hash_table[(maize_sample_hash)] = maize_sample_id
            maize_sample_table[(maize_sample_id, locality_hash_table[(locality_hash)], maize_id, type_of_source, sample_source, weight, description, photo, comments)] = maize_sample_id
            maize_id_table[(maize_id)] = (maize_sample_id, locality_hash_table[(locality_hash)], maize_id, type_of_source, sample_source, weight, description, photo, comments)
            maize_sample_id = maize_sample_id + 1

        obs_tracker_maize_id_table_hash = hash(('maize', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, maize_sample_hash_table[(maize_sample_hash)], 1))
        if (obs_tracker_maize_id_table_hash) in obs_tracker_hash_table:
            pass
        else:
            obs_tracker_hash_table[(obs_tracker_maize_id_table_hash)] = obs_tracker_id
            obs_tracker_table[(obs_tracker_id, 'maize', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, maize_sample_hash_table[(maize_sample_hash)], 1)] = obs_tracker_id
            obs_tracker_maize_id_table[(maize_id)] = (obs_tracker_id, 'maize', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, maize_sample_hash_table[(maize_sample_hash)], 1)
            obs_tracker_id = obs_tracker_id + 1

    sample_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/DataDumps/kenya_mycotoxin/template_sample.csv'), dialect='excel')
    for row in sample_file:
        sample_id = row["Sample ID"]
        source_sample_id = row["Source Sample ID"]
        maize_id = row["Source Maize ID"]
        sample_type = row["Sample Type"]
        weight = row["Weight"]
        kernel_num = row["Kernel Num"]
        photo = row["Photo"]
        comments = row["Comments"]

        sample_hash = hash((sample_id, sample_type, weight, kernel_num, photo, comments))
        if (sample_hash) in obs_sample_hash_table:
            pass
        else:
            obs_sample_hash_table[(sample_hash)] = obs_sample_id
            obs_sample_table[(obs_sample_id, sample_id, sample_type, weight, kernel_num, photo, comments)] = obs_sample_id
            obs_sample_id_table[(sample_id)] = (obs_sample_id, sample_id, sample_type, weight, kernel_num, photo, comments)
            obs_sample_id = obs_sample_id + 1

        obs_tracker_sample_id_table_hash = hash(('sample', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_sample_hash_table[(sample_hash)], 1, 1, 1, 1, maize_id_table[(maize_id)][0], 1))
        if (obs_tracker_sample_id_table_hash) in obs_tracker_hash_table:
            pass
        else:
            obs_tracker_hash_table[(obs_tracker_sample_id_table_hash)] = obs_tracker_id
            obs_tracker_table[(obs_tracker_id, 'sample', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_sample_hash_table[(sample_hash)], 1, 1, 1, 1, maize_id_table[(maize_id)][0], 1)] = obs_tracker_id
            obs_tracker_sample_id_table[(sample_id)] = (obs_tracker_id, 'sample', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_sample_hash_table[(sample_hash)], 1, 1, 1, 1, maize_id_table[(maize_id)][0], 1)
            obs_tracker_id = obs_tracker_id + 1

    floatation_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/DataDumps/kenya_mycotoxin/template_floatation.csv'), dialect='excel')
    for row in floatation_file:
        sample_id = row["Sample ID"]
        separation_type = "Floatation"
        apparatus = "Beaker with fluid"
        SG = row["SG"]
        light_weight = row["Float Weight"]
        intermediate_weight = ""
        heavy_weight = row["Sink Weight"]
        light_percent = row["Float Percent"]
        intermediate_percent = ""
        heavy_percent = ""
        operating_factor = ""
        comments = row["Comments"]

        float_hash = hash((obs_sample_id_table[(sample_id)][0], separation_type, apparatus, SG, light_weight, intermediate_weight, heavy_weight, light_percent, intermediate_percent, heavy_percent, operating_factor, comments))
        if (float_hash) in separation_hash_table:
            pass
        else:
            separation_hash_table[(float_hash)] = separation_id
            separation_table[(separation_id, obs_sample_id_table[(sample_id)][0], separation_type, apparatus, SG, light_weight, intermediate_weight, heavy_weight, light_percent, intermediate_percent, heavy_percent, operating_factor, comments)] = separation_id
            separation_id = separation_id + 1

    extract_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/DataDumps/kenya_mycotoxin/template_extract.csv'), dialect='excel')
    for row in extract_file:
        extract_id = row["Extract ID"]
        sample_id = row["Source Sample ID"]
        weight = row["Weight"]
        rep = row["Rep"]
        grind_method = row["Grind Method"]
        solvent = row["Solvent"]
        comments = row["Extract Comments"]

        extract_hash = hash((extract_id, weight, rep, grind_method, solvent, comments))
        if (extract_hash) in obs_extract_hash_table:
            pass
        else:
            obs_extract_hash_table[(extract_hash)] = obs_extract_id
            obs_extract_table[(obs_extract_id, extract_id, weight, rep, grind_method, solvent, comments)] = obs_extract_id
            obs_extract_id_table[(extract_id)] = (obs_extract_id, extract_id, weight, rep, grind_method, solvent, comments)
            obs_extract_id = obs_extract_id + 1

        obs_tracker_extract_id_table_hash = hash(('extract', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_sample_id_table[(sample_id)][0], 1, 1, 1, 1, maize_id_table[(maize_id)][0], obs_extract_hash_table[(extract_hash)]))
        if (obs_tracker_extract_id_table_hash) in obs_tracker_hash_table:
            pass
        else:
            obs_tracker_hash_table[(obs_tracker_extract_id_table_hash)] = obs_tracker_id
            obs_tracker_table[(obs_tracker_id, 'extract', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_sample_id_table[(sample_id)][0], 1, 1, 1, 1, maize_id_table[(maize_id)][0], obs_extract_hash_table[(extract_hash)])] = obs_tracker_id
            obs_tracker_extract_id_table[(extract_id)] = (obs_tracker_id, 'extract', experiment_name_table[('15RK')][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_sample_id_table[(sample_id)][0], 1, 1, 1, 1, maize_id_table[(maize_id)][0], obs_extract_hash_table[(extract_hash)])
            obs_tracker_id = obs_tracker_id + 1

    toxin_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/DataDumps/kenya_mycotoxin/template_parameter.csv'), dialect='excel')
    for row in toxin_file:
        parameter = row["Parameter"]
        parameter_type = row["Parameter Type"]
        protocol = row["Protocol"]
        units = row["Unit of Measure"]
        trait_id_buckler = row["Trait ID Buckler"]

        parameter_hash = hash((parameter, parameter_type, protocol, units, trait_id_buckler))
        if (parameter_hash) in measurement_param_hash_table:
            pass
        else:
            measurement_param_hash_table[(parameter_hash)] = measurement_param_id
            measurement_param_table[(measurement_param_id, parameter, parameter_type, protocol, units, trait_id_buckler)] = measurement_param_id
            measurement_param_name_table[(parameter)] = (measurement_param_id, parameter, parameter_type, protocol, units, trait_id_buckler)
            measurement_param_id = measurement_param_id + 1

    toxin_file = csv.DictReader(open('C://Users/Nicolas/Documents/GitHub/DataDumps/kenya_mycotoxin/template_measurement.csv'), dialect='excel')
    for row in toxin_file:
        extract_id = row["Extract ID"]
        parameter = row["Parameter"]
        username = row["Username"]
        date = row["DateTime"]
        value = row["Value"]
        comments = row["Measurement Comments"]

        measurement_hash = hash((obs_tracker_extract_id_table[(extract_id)][0], user_hash_table[(hash(username))], measurement_param_name_table[(parameter)][0], date, value, comments))
        if (measurement_hash) in measurement_hash_table:
            pass
        else:
            measurement_hash_table[(measurement_hash)] = measurement_id
            measurement_table[(measurement_id, obs_tracker_extract_id_table[(extract_id)][0], user_hash_table[(hash(username))], measurement_param_name_table[(parameter)][0], date, value, comments)] = measurement_id
            measurement_id = measurement_id + 1


    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/experiment.csv', 'wb'))
    for key in experiment_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/locality.csv', 'wb'))
    for key in locality_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/maize_sample.csv', 'wb'))
    for key in maize_sample_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/obs_tracker.csv', 'wb'))
    for key in obs_tracker_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/obs_sample.csv', 'wb'))
    for key in obs_sample_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/separation.csv', 'wb'))
    for key in separation_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/obs_extract.csv', 'wb'))
    for key in obs_extract_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/measurement_parameter.csv', 'wb'))
    for key in measurement_param_table.iterkeys():
        writer.writerow(key)
    writer = csv.writer(open('C://Users/Nicolas/Documents/GitHub/DataDumps/csv_from_script_mycotoxin/measurement.csv', 'wb'))
    for key in measurement_table.iterkeys():
        try:
            writer.writerow(key)
        except UnicodeEncodeError:
            pass

#------------------------------------------------------------------------
#- Exectution begins here by loading application dependencies
#------------------------------------------------------------------------

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
    import django
    django.setup()
    from lab.models import User, Experiment, Locality, MaizeSample, ObsTracker, ObsTrackerSource, ObsSample, Separation, ObsExtract, MeasurementParameter, Measurement
    migrate()
