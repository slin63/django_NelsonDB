
import csv
from collections import OrderedDict
import time
import loader_db_mirror
from django.http import HttpResponseRedirect, HttpResponse
from lab.models import UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, People, Collecting, Field, Locality, Location, ObsRow, ObsPlant, ObsSample, ObsEnv, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, ObsMicrobe, ObsExtract, ObsTracker, ObsTrackerSource, Isolate, DiseaseInfo, Measurement, MeasurementParameter, Treatment, UploadQueue, Medium, Citation, Publication, MaizeSample, Separation, GlycerolStock, ObsTrackerSource
from django.db import IntegrityError, transaction

def seed_stock_loader_prep(upload_file, user):
    start = time.clock()

    #-- These are the tables that will hold the curated data that is then written to csv files --
    stock_new = OrderedDict({})
    #--- Key = (stock_id, passport_id, seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, comments)
    #--- Value = (stock_id)
    passport_new = OrderedDict({})
    #--- Key = (passport_id, collecting_id, people_id, taxonomy_id)
    #--- Value = (passport_id)
    collecting_new = OrderedDict({})
    #--- Key = (collecting_id, user_id, collection_date, collection_method, comments)
    #--- Value = (collecting_id)
    people_new = OrderedDict({})
    #--- Key = (people_id, first_name, last_name, organization, phone, email, comments)
    #--- Value = (people_id)
    taxonomy_new = OrderedDict({})
    #--- Key = (taxonomy_id, genus, species, population, common_name, alias, race, subtaxa)
    #--- Value = (taxonomy_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)
    obs_tracker_source_new = OrderedDict({})
    #--- Key = (obs_tracker_source_id, source_obs_id, target_obs_id)
    #--- Value = (obs_tracker_source_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    stock_hash_table = loader_db_mirror.stock_hash_mirror()
    stock_id = loader_db_mirror.stock_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    collecting_hash_table = loader_db_mirror.collecting_hash_mirror()
    collecting_id = loader_db_mirror.collecting_id_mirror()
    people_hash_table = loader_db_mirror.people_hash_mirror()
    people_id = loader_db_mirror.people_id_mirror()
    taxonomy_hash_table = loader_db_mirror.taxonomy_hash_mirror()
    taxonomy_id = loader_db_mirror.taxonomy_id_mirror()
    passport_hash_table = loader_db_mirror.passport_hash_mirror()
    passport_id = loader_db_mirror.passport_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()
    field_name_table = loader_db_mirror.field_name_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    obs_tracker_source_hash_table = loader_db_mirror.obs_tracker_source_hash_mirror()
    obs_tracker_source_id = loader_db_mirror.obs_tracker_source_id_mirror()

    error_count = 0
    row_id_error = OrderedDict({})
    plant_id_error = OrderedDict({})
    field_name_error = OrderedDict({})
    collecting_hash_exists = OrderedDict({})
    people_hash_exists = OrderedDict({})
    taxonomy_hash_exists = OrderedDict({})
    passport_hash_exists = OrderedDict({})
    stock_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    stock_file = csv.DictReader(upload_file)
    for row in stock_file:
        seed_id = row["Seed ID"]
        seed_name = row["Seed Name"]
        experiment_used = row["Used"]
        experiment_collected = row["Collected"]
        experiment_name = row["Experiment Name"]
        cross_type = row["Cross Type"]
        pedigree = row["Pedigree"]
        stock_status = row["Stock Status"]
        stock_date = row["Stock Date"]
        inoculated = row["Inoculated"]
        stock_comments = row["Stock Comments"]
        genus = row["Genus"]
        species = row["Species"]
        population = row["Population"]
        row_id = row["Row ID"]
        field_name = row["Field Name"]
        plant_id = row["Plant ID"]
        collection_username = row["Username"]
        collection_date = row["Collection Date"]
        collection_method = row["Method"]
        collection_comments = row["Collection Comments"]
        organization = row["Organization"]
        first_name = row["First Name"]
        last_name = row["Last Name"]
        phone = row["Phone"]
        email = row["Email"]
        source_comments = row["Source Comments"]

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments, genus, species, population, row_id, field_name, plant_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments)] = error_count
                error_count = error_count + 1
                obs_row_id = 1
        else:
            obs_row_id = 1

        if plant_id != '':
            plant_id_fix = plant_id + '\r'
            if plant_id in plant_id_table:
                obs_plant_id = plant_id_table[plant_id][0]
            elif plant_id_fix in plant_id_table:
                obs_plant_id = plant_id_table[plant_id_fix][0]
            else:
                plant_id_error[(seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments, genus, species, population, row_id, field_name, plant_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments)] = error_count
                error_count = error_count + 1
                obs_plant_id = 1
        else:
            obs_plant_id = 1

        if field_name != '':
            field_name_fix = field_name + '\r'
            if field_name in field_name_table:
                field_id = field_name_table[field_name][0]
            elif field_name_fix in field_name_table:
                field_id = field_name_table[field_name_fix][0]
            else:
                field_name_error[(seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments, genus, species, population, row_id, field_name, plant_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments)] = error_count
                error_count = error_count + 1
                field_id = 1
        else:
            field_id = 1

        if collection_username == '':
            collection_username = 'unknown_person'

        collecting_hash_fix = str(user_hash_table[collection_username]) + collection_date + collection_method + collection_comments + '\r'
        collecting_hash = str(user_hash_table[collection_username]) + collection_date + collection_method + collection_comments
        if collecting_hash not in collecting_hash_table and collecting_hash_fix not in collecting_hash_table:
            collecting_hash_table[collecting_hash] = collecting_id
            collecting_new[(collecting_id, user_hash_table[collection_username], collection_date, collection_method, collection_comments)] = collecting_id
            collecting_id = collecting_id + 1
        else:
            collecting_hash_exists[(user_hash_table[collection_username], collection_date, collection_method, collection_comments)] = collecting_id

        people_hash_fix = first_name + last_name + organization + phone + email + source_comments + '\r'
        people_hash = first_name + last_name + organization + phone + email + source_comments
        if people_hash not in people_hash_table and people_hash_fix not in people_hash_table:
            people_hash_table[people_hash] = people_id
            people_new[(people_id, first_name, last_name, organization, phone, email, source_comments)] = people_id
            people_id = people_id + 1
        else:
            people_hash_exists[(first_name, last_name, organization, phone, email, source_comments)] = people_id

        taxonomy_hash_fix = genus + species + population + 'Maize' + '' + '' + '' + '\r'
        taxonomy_hash = genus + species + population + 'Maize' + '' + '' + ''
        if taxonomy_hash not in taxonomy_hash_table and taxonomy_hash_fix not in taxonomy_hash_table:
            taxonomy_hash_table[taxonomy_hash] = taxonomy_id
            taxonomy_new[(taxonomy_id, genus, species, population, 'Maize', '', '', '')] = taxonomy_id
            taxonomy_id = taxonomy_id + 1
        else:
            taxonomy_hash_exists[(genus, species, population, 'Maize', '', '', '')] = taxonomy_id

        passport_hash_fix = str(collecting_hash_table[collecting_hash]) + str(people_hash_table[people_hash]) + str(taxonomy_hash_table[taxonomy_hash]) + '\r'
        passport_hash = str(collecting_hash_table[collecting_hash]) + str(people_hash_table[people_hash]) + str(taxonomy_hash_table[taxonomy_hash])
        if passport_hash not in passport_hash_table and passport_hash_fix not in passport_hash_table:
            passport_hash_table[passport_hash] = passport_id
            passport_new[(passport_id, collecting_hash_table[collecting_hash], people_hash_table[people_hash], taxonomy_hash_table[taxonomy_hash])] = passport_id
            passport_id = passport_id + 1
        else:
            passport_hash_exists[(collecting_hash_table[collecting_hash], people_hash_table[people_hash], taxonomy_hash_table[taxonomy_hash])] = passport_id

        stock_hash_fix = str(passport_hash_table[passport_hash]) + seed_id + seed_name + cross_type + pedigree + stock_status + stock_date + inoculated + stock_comments + '\r'
        stock_hash = str(passport_hash_table[passport_hash]) + seed_id + seed_name + cross_type + pedigree + stock_status + stock_date + inoculated + stock_comments
        if seed_id not in seed_id_table and seed_id + '\r' not in seed_id_table:
            if stock_hash not in stock_hash_table and stock_hash_fix not in stock_hash_table:
                stock_hash_table[stock_hash] = stock_id
                stock_new[(stock_id, passport_hash_table[passport_hash], seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments)] = stock_id
                seed_id_table[seed_id] = (stock_id, passport_hash_table[passport_hash], seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments)
                stock_id = stock_id + 1
            else:
                stock_hash_exists[(passport_hash_table[passport_hash], seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments)] = stock_id
        else:
            stock_hash_exists[(passport_hash_table[passport_hash], seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments)] = stock_id

        if experiment_name == '':
            experiment_name = 'No Experiment'

        if seed_id in seed_id_table:
            temp_stock_id = seed_id_table[seed_id][0]
        elif seed_id + '\r' in seed_id_table:
            temp_stock_id = seed_id_table[seed_id + '\r'][0]
        elif stock_hash in stock_hash_table:
            temp_stock_id = stock_hash_table[stock_hash]
        elif stock_hash_fix in stock_hash_table:
            temp_stock_id = stock_hash_table[stock_hash_fix]
        else:
            temp_stock_id = 1
            error_count = error_count + 1

        if experiment_used == '1':
            obs_tracker_stock_hash_fix = 'stock' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(temp_stock_id) + str(user_hash_table[user.username]) + '\r'
            obs_tracker_stock_hash = 'stock' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(temp_stock_id) + str(user_hash_table[user.username])
            if obs_tracker_stock_hash not in obs_tracker_hash_table and obs_tracker_stock_hash_fix not in obs_tracker_hash_table:
                obs_tracker_hash_table[obs_tracker_stock_hash] = obs_tracker_id
                obs_tracker_new[(obs_tracker_id, 'stock', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, 1, 1, temp_stock_id, user_hash_table[user.username])] = obs_tracker_id
                obs_tracker_id = obs_tracker_id + 1
            else:
                obs_tracker_hash_exists[('stock', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, 1, 1, temp_stock_id, user_hash_table[user.username])] = obs_tracker_id

        if experiment_collected == '1':
            obs_tracker_stock_hash_fix = 'stock' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(temp_stock_id) + str(user_hash_table[user.username]) + '\r'
            obs_tracker_stock_hash = 'stock' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(temp_stock_id) + str(user_hash_table[user.username])
            if obs_tracker_stock_hash not in obs_tracker_hash_table and obs_tracker_stock_hash_fix not in obs_tracker_hash_table:
                obs_tracker_hash_table[obs_tracker_stock_hash] = obs_tracker_id
                obs_tracker_new[(obs_tracker_id, 'stock', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, 1, 1, temp_stock_id, user_hash_table[user.username])] = obs_tracker_id
                obs_tracker_id = obs_tracker_id + 1
            else:
                obs_tracker_hash_exists[('stock', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, 1, 1, temp_stock_id, user_hash_table[user.username])] = obs_tracker_id

            obs_tracker_exp_hash = 'experiment' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(user_hash_table[user.username])
            if obs_tracker_exp_hash not in obs_tracker_hash_table:
                obs_tracker_hash_table[obs_tracker_exp_hash] = obs_tracker_id
                obs_tracker_new[(obs_tracker_id, 'experiment', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, user_hash_table[user.username])] = obs_tracker_id
                obs_tracker_id = obs_tracker_id + 1

            obs_tracker_source_hash = str(obs_tracker_hash_table[obs_tracker_exp_hash]) + str(obs_tracker_hash_table[obs_tracker_stock_hash])
            if obs_tracker_source_hash not in obs_tracker_source_hash_table:
                obs_tracker_source_hash_table[obs_tracker_source_hash] = obs_tracker_source_id
                obs_tracker_source_new[(obs_tracker_source_id, obs_tracker_hash_table[obs_tracker_exp_hash], obs_tracker_hash_table[obs_tracker_stock_hash])] = obs_tracker_source_id
                obs_tracker_source_id = obs_tracker_source_id + 1

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['stock_new'] = stock_new
    results_dict['passport_new'] = passport_new
    results_dict['collecting_new'] = collecting_new
    results_dict['people_new'] = people_new
    results_dict['taxonomy_new'] = taxonomy_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['obs_tracker_source_new'] = obs_tracker_source_new
    results_dict['plant_id_error'] = plant_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['field_name_error'] = field_name_error
    results_dict['collecting_hash_exists'] = collecting_hash_exists
    results_dict['people_hash_exists'] = people_hash_exists
    results_dict['taxonomy_hash_exists'] = taxonomy_hash_exists
    results_dict['passport_hash_exists'] = passport_hash_exists
    results_dict['stock_hash_exists'] = stock_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def seed_stock_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Stock Table'])
    writer.writerow(['stock_id', 'passport_id', 'seed_id', 'seed_name', 'cross_type', 'pedigree', 'stock_status', 'stock_date', 'inoculated', 'comments'])
    for key in results_dict['stock_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Collecting Table'])
    writer.writerow(['collecting_id', 'user_id', 'collection_date', 'collection_method', 'comments'])
    for key in results_dict['collecting_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New People Table'])
    writer.writerow(['people_id', 'first_name', 'last_name', 'organization', 'phone', 'email', 'comments'])
    for key in results_dict['people_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Taxonomy Table'])
    writer.writerow(['taxonomy_id', 'genus', 'species', 'population', 'common_name', 'alias', 'race', 'subtaxa'])
    for key in results_dict['taxonomy_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Passport Table'])
    writer.writerow(['passport_id', 'collecting_id', 'people_id', 'taxonomy_id'])
    for key in results_dict['passport_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTrackerSource Table'])
    writer.writerow(['obs_tracker_source_id', 'source_obs_id', 'targe_obs_id'])
    for key in results_dict['obs_tracker_source_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Plant ID Errors'])
    writer.writerow(['seed_id', 'seed_name', 'cross_type', 'pedigree', 'stock_status', 'stock_date', 'inoculated', 'stock_comments', 'genus', 'species', 'population', 'row_id', 'field_name', 'plant_id', 'collection_username', 'collection_date', 'collection_method', 'collection_comments', 'organization', 'first_name', 'last_name', 'phone', 'email', 'source_comments'])
    for key in results_dict['plant_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Field Name Errors'])
    writer.writerow(['seed_id', 'seed_name', 'cross_type', 'pedigree', 'stock_status', 'stock_date', 'inoculated', 'stock_comments', 'genus', 'species', 'population', 'row_id', 'field_name', 'plant_id', 'collection_username', 'collection_date', 'collection_method', 'collection_comments', 'organization', 'first_name', 'last_name', 'phone', 'email', 'source_comments'])
    for key in results_dict['field_name_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['seed_id', 'seed_name', 'cross_type', 'pedigree', 'stock_status', 'stock_date', 'inoculated', 'stock_comments', 'genus', 'species', 'population', 'row_id', 'field_name', 'plant_id', 'collection_username', 'collection_date', 'collection_method', 'collection_comments', 'organization', 'first_name', 'last_name', 'phone', 'email', 'source_comments'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Collecting Entries Already Exist'])
    for key in results_dict['collecting_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['People Entries Already Exist'])
    for key in results_dict['people_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Taxonomy Entries Already Exist'])
    for key in results_dict['taxonomy_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Passport Entries Already Exist'])
    for key in results_dict['passport_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Stock Entries Already Exist'])
    for key in results_dict['stock_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entries Already Exist'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)

    return response

@transaction.atomic
def seed_stock_loader(results_dict):
    try:
        for key in results_dict['collecting_new'].iterkeys():
            try:
                new_stock = Collecting.objects.create(id=key[0], user_id=key[1], collection_date=key[2], collection_method=key[3], comments=key[4])
            except Exception as e:
                print("Collecting Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['people_new'].iterkeys():
            try:
                new_stock = People.objects.create(id=key[0], first_name=key[1], last_name=key[2], organization=key[3], phone=key[4], email=key[5], comments=key[6])
            except Exception as e:
                print("People Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['taxonomy_new'].iterkeys():
            try:
                new_stock = Taxonomy.objects.create(id=key[0], genus=key[1], species=key[2], population=key[3], common_name=key[4], alias=key[5], race=key[6], subtaxa=key[7])
            except Exception as e:
                print("Taxonomy Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['passport_new'].iterkeys():
            try:
                new_stock = Passport.objects.create(id=key[0], collecting_id=key[1], people_id=key[2], taxonomy_id=key[3])
            except Exception as e:
                print("Passport Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['stock_new'].iterkeys():
            try:
                new_stock = Stock.objects.create(id=key[0], passport_id=key[1], seed_id=key[2], seed_name=key[3], cross_type=key[4], pedigree=key[5], stock_status=key[6], stock_date=key[7], inoculated=key[8], comments=key[9])
            except Exception as e:
                print("Stock Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_source_new'].iterkeys():
            try:
                new_stock = ObsTrackerSource.objects.create(id=key[0], source_obs_id=key[1], target_obs_id=key[2])
            except Exception as e:
                print("ObsTrackerSource Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def seed_packet_loader_prep(upload_file, user):
    start = time.clock()

    #-- These are the tables that will hold the curated data that is then written to csv files --
    stock_packet_new = OrderedDict({})
    #--- Key = (stock_id, passport_id, seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, comments)
    #--- Value = (stock_id)
    location_new = OrderedDict({})
    #--- Key = (location_name, building_name, room, shelf, column, box_name, comments)
    #--- Value = (location_id)
    locality_new = OrderedDict({})
    #--- Key = (city, state, country, zipcode)
    #--- Value = (locality_id)

    stock_packet_hash_table = loader_db_mirror.stock_packet_hash_mirror()
    stock_packet_id = loader_db_mirror.stock_packet_id_mirror()
    location_hash_table = loader_db_mirror.location_hash_mirror()
    location_id = loader_db_mirror.location_id_mirror()
    locality_hash_table = loader_db_mirror.locality_hash_mirror()
    locality_id = loader_db_mirror.locality_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    locality_hash_exists = OrderedDict({})
    location_hash_exists = OrderedDict({})
    stock_packet_hash_exists = OrderedDict({})

    stock_packet_file = csv.DictReader(upload_file)
    for row in stock_packet_file:
        seed_id = row["Seed ID"]
        weight = row["Weight"]
        num_seeds = row["Number of Seeds"]
        packet_comments = row["Seed Packet Comments"]
        location_name = row["Location Name"]
        building_name = row["Building Name"]
        room = row["Room"]
        shelf = row["Shelf"]
        column = row["Column"]
        box_name = row["Box Name"]
        city = row["City"]
        state = row["State"]
        country = row["Country"]
        zipcode = row["Zipcode"]
        location_comments = row["Location Comments"]

        if seed_id != '':
            seed_id_fix = row_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix]
            else:
                seed_id_error[(seed_id, weight, num_seeds, packet_comments, location_name, building_name, room, shelf, column, box_name, city, state, country, zipcode, location_comments)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            seed_id_error[(seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments, genus, species, population, row_id, field_name, plant_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments)] = error_count
            error_count = error_count + 1
            stock_id = 1

        locality_hash_fix = city + state + country + zipcode + '\r'
        locality_hash = city + state + country + zipcode
        if locality_hash not in locality_hash_table and locality_hash_fix not in locality_hash_table:
            locality_hash_table[locality_hash] = locality_id
            locality_new[(locality_id, city, state, country, zipcode)] = locality_id
            locality_id = locality_id + 1
        else:
            locality_hash_exists[(city, state, country, zipcode)] = locality_id

        location_hash_fix = location_name + building_name + room + shelf + column + box_name + location_comments + '\r'
        location_hash = location_name + building_name + room + shelf + column + box_name + location_comments
        if location_hash not in location_hash_table and location_hash_fix not in location_hash_table:
            location_hash_table[location_hash] = location_id
            location_new[(location_id, location_name, building_name, room, shelf, column, box_name, location_comments)] = location_id
            location_id = location_id + 1
        else:
            location_hash_exists[(location_name, building_name, room, shelf, column, box_name, location_comments)] = location_id

        if location_hash in location_hash_table:
            temp_location_id = location_hash_table[location_hash]
        elif location_hash_fix in location_hash_table:
            temp_location_id = location_hash_table[location_hash_fix]
        else:
            temp_location_id = 1
            error_count = error_count + 1

        stock_packet_hash_fix = str(stock_id) + str(location_id) + weight + num_seeds + packet_comments + '\r'
        stock_packet_hash = str(stock_id) + str(location_id) + weight + num_seeds + packet_comments
        if stock_packet_hash not in stock_packet_hash_table and stock_packet_hash_fix not in stock_packet_hash_table:
            stock_packet_hash_table[stock_packet_hash] = stock_packet_id
            stock_packet_new[(stock_packet_id, stock_id, location_id, weight, num_seeds, packet_comments)] = stock_packet_id
            stock_packet_id = stock_packet_id + 1
        else:
            stock_packet_hash_exists[(stock_id, location_id, weight, num_seeds, packet_comments)] = stock_packet_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['stock_packet_new'] = stock_packet_new
    results_dict['location_new'] = location_new
    results_dict['locality_new'] = locality_new
    results_dict['seed_id_error'] = seed_id_error
    results_dict['location_hash_exists'] = location_hash_exists
    results_dict['locality_hash_exists'] = locality_hash_exists
    results_dict['stock_packet_hash_exists'] = stock_packet_hash_exists
    results_dict['stats'] = stats
    return results_dict

def seed_packet_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Stock Packet Table'])
    writer.writerow(['stock_packet_id', 'stock_id', 'location_id', 'weight', 'num_seeds', 'comments'])
    for key in results_dict['stock_packet_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Location Table'])
    writer.writerow(['location_id', 'location_name', 'building_name', 'room', 'shelf', 'column', 'box_name', 'comments'])
    for key in results_dict['location_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Locality Table'])
    writer.writerow(['locality_id', 'city', 'state', 'country', 'zipcode'])
    for key in results_dict['locality_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['seed_id', 'weight', 'num_seeds', 'packet_comments', 'location_name', 'building_name', 'room', 'shelf', 'column', 'box_name', 'city', 'state', 'country', 'zipcode', 'location_comments'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Location Entries Already Exist'])
    for key in results_dict['location_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Locality Entries Already Exist'])
    for key in results_dict['locality_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Stock Packet Entries Already Exist'])
    for key in results_dict['stock_packet_hash_exists'].iterkeys():
        writer.writerow(key)

    return response

@transaction.atomic
def seed_packet_loader(results_dict):
    try:
        for key in results_dict['locality_new'].iterkeys():
            try:
                new_locality = Locality.objects.create(id=key[0], city=key[1], state=key[2], country=key[3], zipcode=key[4])
            except Exception as e:
                print("Locality Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['location_new'].iterkeys():
            try:
                new_location = Location.objects.create(id=key[0], locality_id=key[1], location_name=key[2], building_name=key[3], room=key[4], shelf=key[5], column=key[6], box_name=key[7], comments=key[8])
            except Exception as e:
                print("Location Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['stock_packet_new'].iterkeys():
            try:
                new_stock_packet = StockPacket.objects.create(id=key[0], stock_id=key[1], location_id=key[2], weight=key[3], num_seeds=key[4], comments=key[5])
            except Exception as e:
                print("StockPacket Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def row_loader_prep(upload_file, user):
    start = time.clock()

    obs_row_new = OrderedDict({})
    #--- Key = (obs_row_id, row_id, row_name, range_num, plot, block, rep, kernel_num, planting_date, harvest_date, comments)
    #--- Value = (obs_row_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_row_hash_table = loader_db_mirror.obs_row_hash_mirror()
    obs_row_id = loader_db_mirror.obs_row_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    field_name_table = loader_db_mirror.field_name_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    source_seed_id_error = OrderedDict({})
    field_name_error = OrderedDict({})
    row_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    row_file = csv.DictReader(upload_file)
    for row in row_file:
        row_id = row["Row ID"]
        experiment_name = row["Experiment Name"]
        source_seed_id = row["Source Seed ID"]
        field_name = row["Field Name"]
        row_name = row["Row Name"]
        row_range = row["Range"]
        plot = row["Plot"]
        block = row["Block"]
        rep = row["Rep"]
        kernel_num = row["Kernel Num"]
        planting_date = row["Planting Date"]
        harvest_date = row["Harvest Date"]
        comments = row["Row Comments"]

        if source_seed_id != '':
            source_seed_id_fix = source_seed_id + '\r'
            if source_seed_id in seed_id_table:
                stock_id = seed_id_table[source_seed_id][0]
            elif source_seed_id_fix in seed_id_table:
                stock_id = seed_id_table[source_seed_id_fix][0]
            else:
                source_seed_id_error[(row_id, source_seed_id, field_name, row_name, row_range, plot, block,rep, kernel_num, planting_date, harvest_date, comments)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            stock_id = 1

        if field_name != '':
            field_name_fix = field_name + '\r'
            if field_name in field_name_table:
                field_id = field_name_table[field_name][0]
            elif field_name_fix in field_name_table:
                field_id = field_name_table[field_name_fix][0]
            else:
                field_name_error[(row_id, source_seed_id, field_name, row_name, row_range, plot, block,rep, kernel_num, planting_date, harvest_date, comments)] = error_count
                error_count = error_count + 1
                field_id = 1
        else:
            field_id = 1

        row_hash = row_id + row_name + row_range + plot + block + rep + kernel_num + planting_date + harvest_date + comments
        row_hash_fix = row_id + row_name + row_range + plot + block + rep + kernel_num + planting_date + harvest_date + comments + '\r'
        if row_id not in row_id_table and row_id + '\r' not in row_id_table:
            if row_hash not in obs_row_hash_table and row_hash_fix not in obs_row_hash_table:
                obs_row_hash_table[row_hash] = obs_row_id
                obs_row_new[(obs_row_id, row_id, row_name, row_range, plot, block, rep, kernel_num, planting_date, harvest_date, comments)] = obs_row_id
                row_id_table[row_id] = (obs_row_id, row_id, row_name, row_range, plot, block, rep, kernel_num, planting_date, harvest_date, comments)
                obs_row_id = obs_row_id + 1
            else:
                row_hash_exists[(row_id, row_name, row_range, plot, block, rep, kernel_num, planting_date, harvest_date, comments)] = obs_row_id
        else:
            row_hash_exists[(row_id, row_name, row_range, plot, block, rep, kernel_num, planting_date, harvest_date, comments)] = obs_row_id

        if row_id in row_id_table:
            temp_obsrow_id = row_id[row_id][0]
        elif row_id + '\r' in row_id_table:
            temp_obsrow_id = row_id[row_id + '\r'][0]
        elif row_hash in obs_row_hash_table:
            temp_obsrow_id = obs_row_hash_table[row_hash]
        elif row_hash_fix in obs_row_hash_table:
            temp_obsrow_id = obs_row_hash_table[row_hash_fix]
        else:
            temp_obsrow_id = 1
            error_count = error_count + 1

        obs_tracker_row_hash = 'row' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsrow_id) + str(1) + str(1) + str(1) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_row_hash_fix = 'row' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsrow_id) + str(1) + str(1) + str(1) + str(stock_id) + str(user_hash_table[user.username]) + '\r'
        if obs_tracker_row_hash not in obs_tracker_hash_table and obs_tracker_row_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_row_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'row', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, temp_obsrow_id, 1, 1, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('row', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, temp_obsrow_id, 1, 1, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_row_new'] = obs_row_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['source_seed_id_error'] = source_seed_id_error
    results_dict['field_name_error'] = field_name_error
    results_dict['row_hash_exists'] = row_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def row_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Row Table'])
    writer.writerow(['obs_row_id', 'row_id', 'row_name', 'range_num', 'plot', 'block', 'rep', 'kernel_num', 'planting_date', 'harvest_date', 'comments'])
    for key in results_dict['obs_row_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Source Seed ID Errors'])
    writer.writerow(['row_id', 'source_seed_id', 'field_name', 'row_name', 'range', 'plot', 'block', 'rep', 'kernel_num', 'planting_date', 'harvest_date', 'comments'])
    for key in results_dict['source_seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Field Name Errors'])
    writer.writerow(['row_id', 'source_seed_id', 'field_name', 'row_name', 'range', 'plot', 'block', 'rep', 'kernel_num', 'planting_date', 'harvest_date', 'comments'])
    for key in results_dict['field_name_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row Entry Already Exists'])
    for key in results_dict['row_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

@transaction.atomic
def row_loader(results_dict):
    try:
        for key in results_dict['obs_row_new'].iterkeys():
            try:
                new_obsrow = ObsRow.objects.create(id=key[0], row_id=key[1], row_name=key[2], range_num=key[3], plot=key[4], block=key[5], rep=key[6], kernel_num=key[7], planting_date=key[8], harvest_date=key[9], comments=key[10])
            except Exception as e:
                print("ObsRow Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def measurement_loader_prep(upload_file, user):
    start = time.clock()

    #-- These are the tables that will hold the curated data that is then written to csv files --
    measurement_new = OrderedDict({})
    #--- Key = (measurement_id, obs_tracker_id, measurement_parameter_id, user_id, time_of_measurement, value, comments)
    #--- Value = (measurement_id)

    measurement_hash_table = loader_db_mirror.measurement_hash_mirror()
    measurement_id = loader_db_mirror.measurement_id_mirror()
    obs_tracker_row_id_table = loader_db_mirror.obs_tracker_row_id_mirror()
    obs_tracker_plant_id_table = loader_db_mirror.obs_tracker_plant_id_mirror()
    obs_tracker_env_id_table = loader_db_mirror.obs_tracker_env_id_mirror()
    obs_tracker_sample_id_table = loader_db_mirror.obs_tracker_sample_id_mirror()
    obs_tracker_microbe_id_table = loader_db_mirror.obs_tracker_microbe_id_mirror()
    obs_tracker_well_id_table = loader_db_mirror.obs_tracker_well_id_mirror()
    obs_tracker_plate_id_table = loader_db_mirror.obs_tracker_plate_id_mirror()
    obs_tracker_dna_id_table = loader_db_mirror.obs_tracker_dna_id_mirror()
    obs_tracker_tissue_id_table = loader_db_mirror.obs_tracker_tissue_id_mirror()
    obs_tracker_extract_id_table = loader_db_mirror.obs_tracker_extract_id_mirror()
    obs_tracker_culture_id_table = loader_db_mirror.obs_tracker_culture_id_mirror()
    user_hash_table = loader_db_mirror.user_hash_mirror()
    measurement_param_name_table = loader_db_mirror.measurement_parameter_name_mirror()

    error_count = 0
    obs_id_error = OrderedDict({})
    username_error = OrderedDict({})
    parameter_error = OrderedDict({})
    measurement_hash_exists = OrderedDict({})

    measurement_file = csv.DictReader(upload_file)
    for row in measurement_file:
        obs_id = row["Observation ID"]
        parameter = row["Parameter"]
        username = row["Username"]
        time_of_measurement = row["DateTime"]
        value = row["Value"]
        comments = row["Measurement Comments"]

        if obs_id in obs_tracker_row_id_table:
            obs_tracker_id = obs_tracker_row_id_table[obs_id][0]
        elif obs_id in obs_tracker_plant_id_table:
            obs_tracker_id = obs_tracker_plant_id_table[obs_id][0]
        elif obs_id in obs_tracker_env_id_table:
            obs_tracker_id = obs_tracker_env_id_table[obs_id][0]
        elif obs_id in obs_tracker_sample_id_table:
            obs_tracker_id = obs_tracker_sample_id_table[obs_id][0]
        elif obs_id in obs_tracker_microbe_id_table:
            obs_tracker_id = obs_tracker_microbe_id_table[obs_id][0]
        elif obs_id in obs_tracker_well_id_table:
            obs_tracker_id = obs_tracker_well_id_table[obs_id][0]
        elif obs_id in obs_tracker_plate_id_table:
            obs_tracker_id = obs_tracker_plate_id_table[obs_id][0]
        elif obs_id in obs_tracker_dna_id_table:
            obs_tracker_id = obs_tracker_dna_id_table[obs_id][0]
        elif obs_id in obs_tracker_tissue_id_table:
            obs_tracker_id = obs_tracker_tissue_id_table[obs_id][0]
        elif obs_id in obs_tracker_extract_id_table:
            obs_tracker_id = obs_tracker_extract_id_table[obs_id][0]
        elif obs_id in obs_tracker_culture_id_table:
            obs_tracker_id = obs_tracker_culture_id_table[obs_id][0]
        else:
            obs_tracker_id = 1
            obs_id_error[(obs_id, parameter, username, time_of_measurement, value, comments)] = obs_id
            error_count = error_count + 1

        if username in user_hash_table:
            user_id = user_hash_table[username]
        else:
            user_id = user_hash_table['unknown_person']
            username_error[(obs_id, parameter, username, time_of_measurement, value, comments)] = obs_id
            error_count = error_count + 1

        if parameter in measurement_param_name_table:
            parameter_id = measurement_param_name_table[parameter][0]
        else:
            parameter_id = 1
            parameter_error[(obs_id, parameter, username, time_of_measurement, value, comments)] = obs_id
            error_count = error_count + 1

        measurement_hash_fix = str(obs_tracker_id) + str(parameter_id) + str(user_id) + time_of_measurement + value + comments + '\r'
        measurement_hash = str(obs_tracker_id) + str(parameter_id) + str(user_id) + time_of_measurement + value + comments
        if measurement_hash not in measurement_hash_table and measurement_hash_fix not in measurement_hash_table:
            measurement_hash_table[measurement_hash] = measurement_id
            measurement_new[(measurement_id, obs_tracker_id, parameter_id, user_id, time_of_measurement, value, comments)] = measurement_id
            measurement_id = measurement_id + 1
        else:
            measurement_hash_exists[(measurement_id, obs_tracker_id, parameter_id, user_id, time_of_measurement, value, comments)] = measurement_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['measurement_new'] = measurement_new
    results_dict['obs_id_error'] = obs_id_error
    results_dict['username_error'] = username_error
    results_dict['parameter_error'] = parameter_error
    results_dict['measurement_hash_exists'] = measurement_hash_exists
    results_dict['stats'] = stats
    return results_dict

def measurement_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Measurement Table'])
    writer.writerow(['measurement_id', 'obs_tracker_id', 'measurement_parameter_id', 'user_id', 'time_of_measurement', 'value', 'comments'])
    for key in results_dict['measurement_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Observation ID Errors'])
    writer.writerow(['observation_id', 'parameter', 'username', 'time_of_measurement', 'value', 'comments'])
    for key in results_dict['obs_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Username Errors'])
    writer.writerow(['observation_id', 'parameter', 'username', 'time_of_measurement', 'value', 'comments'])
    for key in results_dict['username_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Parameter Errors'])
    writer.writerow(['observation_id', 'parameter', 'username', 'time_of_measurement', 'value', 'comments'])
    for key in results_dict['parameter_error'].iterkeys():
        writer.writerow([key])
    writer.writerow([''])
    writer.writerow(['Measurement Entry Already Exists'])
    for key in results_dict['measurement_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

@transaction.atomic
def measurement_loader(results_dict):
    try:
        for key in results_dict['measurement_new'].iterkeys():
            try:
                new_measurement = Measurement.objects.create(id=key[0], obs_tracker_id=key[1], measurement_parameter_id=key[2], user_id=key[3], time_of_measurement=key[4], value=key[5], comments=key[6])
            except Exception as e:
                print("Measurement Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True
