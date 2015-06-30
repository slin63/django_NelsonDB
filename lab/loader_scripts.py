
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

def seed_stock_loader(results_dict):
    try:
        for key in results_dict['collecting_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = Collecting.objects.create(id=key[0], user_id=key[1], collection_date=key[2], collection_method=key[3], comments=key[4])
            except Exception as e:
                print("Collecting Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['people_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = People.objects.create(id=key[0], first_name=key[1], last_name=key[2], organization=key[3], phone=key[4], email=key[5], comments=key[6])
            except Exception as e:
                print("People Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['taxonomy_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = Taxonomy.objects.create(id=key[0], genus=key[1], species=key[2], population=key[3], common_name=key[4], alias=key[5], race=key[6], subtaxa=key[7])
            except Exception as e:
                print("Taxonomy Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['passport_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = Passport.objects.create(id=key[0], collecting_id=key[1], people_id=key[2], taxonomy_id=key[3])
            except Exception as e:
                print("Passport Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['stock_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = Stock.objects.create(id=key[0], passport_id=key[1], seed_id=key[2], seed_name=key[3], cross_type=key[4], pedigree=key[5], stock_status=key[6], stock_date=key[7], inoculated=key[8], comments=key[9])
            except Exception as e:
                print("Stock Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_source_new'].iterkeys():
            try:
                with transaction.atomic():
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
    #--- Key = (location_id, location_name, building_name, room, shelf, column, box_name, comments)
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

def seed_packet_loader(results_dict):
    try:
        for key in results_dict['locality_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_locality = Locality.objects.create(id=key[0], city=key[1], state=key[2], country=key[3], zipcode=key[4])
            except Exception as e:
                print("Locality Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['location_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_location = Location.objects.create(id=key[0], locality_id=key[1], location_name=key[2], building_name=key[3], room=key[4], shelf=key[5], column=key[6], box_name=key[7], comments=key[8])
            except Exception as e:
                print("Location Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['stock_packet_new'].iterkeys():
            try:
                with transaction.atomic():
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
            temp_obsrow_id = row_id_table[row_id][0]
        elif row_id + '\r' in row_id_table:
            temp_obsrow_id = row_id_table[row_id + '\r'][0]
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

def row_loader(results_dict):
    try:
        for key in results_dict['obs_row_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obsrow = ObsRow.objects.create(id=key[0], row_id=key[1], row_name=key[2], range_num=key[3], plot=key[4], block=key[5], rep=key[6], kernel_num=key[7], planting_date=key[8], harvest_date=key[9], comments=key[10])
            except Exception as e:
                print("ObsRow Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def plant_loader_prep(upload_file, user):
    start = time.clock()

    obs_plant_new = OrderedDict({})
    #--- Key = (obs_plant_id, plant_id, plant_num, comments)
    #--- Value = (obs_plant_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_plant_hash_table = loader_db_mirror.obs_plant_hash_mirror()
    obs_plant_id = loader_db_mirror.obs_plant_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    row_id_error = OrderedDict({})
    plant_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    plant_file = csv.DictReader(upload_file)
    for row in plant_file:
        plant_id = row["Plant ID"]
        experiment_name = row["Experiment Name"]
        row_id = row["Row ID"]
        seed_id = row["Seed ID"]
        plant_num = row["Plant Number"]
        comments = row["Plant Comments"]
        user = request.user

        if seed_id != '':
            seed_id_fix = seed_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id][0]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix][0]
            else:
                seed_id_error[(plant_id, experiment_name, row_id, seed_id, plant_num, comments)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            stock_id = 1

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(plant_id, experiment_name, row_id, seed_id, plant_num, comments)] = error_count
                error_count = error_count + 1
                obs_row_id = 1
        else:
            obs_row_id = 1

        plant_hash = plant_id + plant_num + comments
        plant_hash_fix = plant_id + plant_num + comments + '\r'
        if plant_id not in plant_id_table and plant_id + '\r' not in plant_id_table:
            if plant_hash not in obs_plant_hash_table and plant_hash_fix not in obs_plant_hash_table:
                obs_row_hash_table[plant_hash] = obs_plant_id
                obs_plant_new[(obs_plant_id, plant_id, plant_num, comments)] = obs_plant_id
                plant_id_table[plant_id] = (obs_plant_id, plant_id, plant_num, comments)
                obs_plant_id = obs_plant_id + 1
            else:
                plant_hash_exists[(plant_id, plant_num, comments)] = obs_plant_id
        else:
            plant_hash_exists[(plant_id, plant_num, comments)] = obs_plant_id

        if plant_id in plant_id_table:
            temp_obsplant_id = plant_id_table[plant_id][0]
        elif plant_id + '\r' in plant_id_table:
            temp_obsplant_id = plant_id_table[plant_id + '\r'][0]
        elif plant_hash in obs_plant_hash_table:
            temp_obsplant_id = obs_plant_hash_table[plant_hash]
        elif plant_hash_fix in obs_plant_hash_table:
            temp_obsplant_id = obs_plant_hash_table[plant_hash_fix]
        else:
            temp_obsplant_id = 1
            error_count = error_count + 1

        obs_tracker_plant_hash = 'plant' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsplant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_plant_hash_fix = 'plant' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsplant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(stock_id) + str(user_hash_table[user.username]) + '\r'
        if obs_tracker_plant_hash not in obs_tracker_hash_table and obs_tracker_plant_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_plant_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'plant', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, temp_obsplant_id, 1, obs_row_id, 1, 1, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('plant', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, temp_obsplant_id, 1, obs_row_id, 1, 1, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_plant_new'] = obs_plant_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['seed_id_error'] = seed_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['plant_hash_exists'] = plant_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def plant_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Plant Table'])
    writer.writerow(['obs_plant_id', 'plant_id', 'plant_num', 'comments'])
    for key in results_dict['obs_plant_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['plant_id', 'experiment_name', 'row_id', 'seed_id', 'plant_num', 'comments'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['plant_id', 'experiment_name', 'row_id', 'seed_id', 'plant_num', 'comments'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plant Entry Already Exists'])
    for key in results_dict['plant_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def plant_loader(results_dict):
    try:
        for key in results_dict['obs_plant_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obsrow = ObsPlant.objects.create(id=key[0], plant_id=key[1], plant_num=key[2], comments=key[3])
            except Exception as e:
                print("ObsPlant Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def tissue_loader_prep(upload_file, user):
    start = time.clock()

    obs_tissue_new = OrderedDict({})
    #--- Key = (obs_tissue_id, tissue_id, tissue_type, tissue_name, date_ground, comments)
    #--- Value = (obs_tissue_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_tissue_hash_table = loader_db_mirror.obs_tissue_hash_mirror()
    obs_tissue_id = loader_db_mirror.obs_tissue_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    culture_id_table = loader_db_mirror.culture_id_mirror()
    tissue_id_table = loader_db_mirror.tissue_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    row_id_error = OrderedDict({})
    plant_id_error = OrderedDict({})
    culture_id_error = OrderedDict({})
    tissue_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    tissue_file = csv.DictReader(upload_file)
    for row in tissue_file:
        tissue_id = row["Tissue ID"]
        experiment_name = row["Experiment Name"]
        tissue_name = row["Tissue Name"]
        tissue_type = row["Tissue Type"]
        date_ground = row["Date Ground"]
        tissue_comments = row["Tissue Comments"]
        row_id = row["Source Row ID"]
        seed_id = row["Source Seed ID"]
        plant_id = row["Source Plant ID"]
        culture_id = row["Source Culture ID"]
        user = request.user

        if seed_id != '':
            seed_id_fix = seed_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id][0]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix][0]
            else:
                seed_id_error[(tissue_id, experiment_name, tissue_name, tissue_type, date_ground, row_id, seed_id, plant_id, culture_id, tissue_comments)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            stock_id = 1

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(tissue_id, experiment_name, tissue_name, tissue_type, date_ground, row_id, seed_id, plant_id, culture_id, tissue_comments)] = error_count
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
                plant_id_error[(tissue_id, experiment_name, tissue_name, tissue_type, date_ground, row_id, seed_id, plant_id, culture_id, tissue_comments)] = error_count
                error_count = error_count + 1
                obs_plant_id = 1
        else:
            obs_plant_id = 1

        if culture_id != '':
            culture_id_fix = culture_id + '\r'
            if culture_id in culture_id_table:
                obs_culture_id = culture_id_table[culture_id][0]
            elif culture_id_fix in culture_id_table:
                obs_culture_id = culture_id_table[culture_id_fix][0]
            else:
                culture_id_error[(tissue_id, experiment_name, tissue_name, tissue_type, date_ground, row_id, seed_id, plant_id, culture_id, tissue_comments)] = error_count
                error_count = error_count + 1
                obs_culture_id = 1
        else:
            obs_culture_id = 1

        tissue_hash = tissue_id + tissue_type + tissue_name + date_ground + tissue_comments
        tissue_hash_fix = tissue_id + tissue_type + tissue_name + date_ground + tissue_comments + '\r'
        if tissue_id not in tissue_id_table and tissue_id + '\r' not in tissue_id_table:
            if tissue_hash not in obs_tissue_hash_table and tissue_hash_fix not in obs_tissue_hash_table:
                obs_tissue_hash_table[tissue_hash] = obs_tissue_id
                obs_tissue_new[(obs_tissue_id, tissue_id, tissue_type, tissue_name, date_ground, tissue_comments)] = obs_tissue_id
                tissue_id_table[tissue_id] = (obs_tissue_id, tissue_id, tissue_type, tissue_name, date_ground, tissue_comments)
                obs_tissue_id = obs_tissue_id + 1
            else:
                tissue_hash_exists[(tissue_id, tissue_type, tissue_name, date_ground, tissue_comments)] = obs_tissue_id
        else:
            tissue_hash_exists[(tissue_id, tissue_type, tissue_name, date_ground, tissue_comments)] = obs_tissue_id

        if tissue_id in tissue_id_table:
            temp_obstissue_id = tissue_id_table[tissue_id][0]
        elif tissue_id + '\r' in tissue_id_table:
            temp_obstissue_id = tissue_id_table[tissue_id + '\r'][0]
        elif tissue_hash in obs_tissue_hash_table:
            temp_obstissue_id = obs_tissue_hash_table[tissue_hash]
        elif tissue_hash_fix in obs_tissue_hash_table:
            temp_obstissue_id = obs_tissue_hash_table[tissue_hash_fix]
        else:
            temp_obstissue_id = 1
            error_count = error_count + 1

        obs_tracker_tissue_hash = 'tissue' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_culture_id) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(temp_obstissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_tissue_hash_fix = 'tissue' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_culture_id) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(temp_obstissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username]) + '\r'
        if obs_tracker_tissue_hash not in obs_tracker_hash_table and obs_tracker_tissue_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_tissue_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'tissue', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, temp_obstissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('tissue', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, temp_obstissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_tissue_new'] = obs_tissue_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['seed_id_error'] = seed_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['plant_id_error'] = plant_id_error
    results_dict['culture_id_error'] = culture_id_error
    results_dict['tissue_hash_exists'] = tissue_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def tissue_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Tissue Table'])
    writer.writerow(['obs_tissue_id', 'tissue_id', 'tissue_type', 'tissue_name', 'date_ground', 'comments'])
    for key in results_dict['obs_tissue_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['tissue_id', 'experiment_name', 'tissue_name', 'tissue_type', 'date_ground', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_culture_id', 'tissue_comments'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['tissue_id', 'experiment_name', 'tissue_name', 'tissue_type', 'date_ground', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_culture_id', 'tissue_comments'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plant ID Errors'])
    writer.writerow(['tissue_id', 'experiment_name', 'tissue_name', 'tissue_type', 'date_ground', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_culture_id', 'tissue_comments'])
    for key in results_dict['plant_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Culture ID Errors'])
    writer.writerow(['tissue_id', 'experiment_name', 'tissue_name', 'tissue_type', 'date_ground', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_culture_id', 'tissue_comments'])
    for key in results_dict['culture_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Tissue Entry Already Exists'])
    for key in results_dict['tissue_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def tissue_loader(results_dict):
    try:
        for key in results_dict['obs_tissue_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obstissue = ObsTissue.objects.create(id=key[0], tissue_id=key[1], tissue_type=key[2], tissue_name=key[3], date_ground=key[4], comments=key[5])
            except Exception as e:
                print("ObsTissue Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def culture_loader_prep(upload_file, user):
    start = time.clock()

    obs_culture_new = OrderedDict({})
    #--- Key = (obs_culture_id, medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, comments, num_colonies, num_microbes)
    #--- Value = (obs_culture_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_culture_hash_table = loader_db_mirror.obs_culture_hash_mirror()
    obs_culture_id = loader_db_mirror.obs_culture_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    tissue_id_table = loader_db_mirror.tissue_id_mirror()
    microbe_id_table = loader_db_mirror.microbe_id_mirror()
    culture_id_table = loader_db_mirror.culture_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()
    media_name_table = loader_db_mirror.media_name_mirror()
    location_name_table = loader_db_mirror.location_name_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    row_id_error = OrderedDict({})
    plant_id_error = OrderedDict({})
    tissue_id_error = OrderedDict({})
    microbe_id_error = OrderedDict({})
    media_name_error = OrderedDict({})
    location_name_error = OrderedDict({})
    culture_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    culture_file = csv.DictReader(upload_file)
    for row in culture_file:
        culture_id = row["Culture ID"]
        experiment_name = row["Experiment Name"]
        media_name = row["Media Name"]
        location_name = row["Location Name"]
        culture_name = row["Culture Name"]
        microbe_type = row["Microbe Type"]
        plating_cycle = row["Plating Cycle"]
        dilution = row["Dilution"]
        image_filename = row["Image File"]
        culture_comments = row["Culture Comments"]
        num_colonies = row["Num Colonies"]
        num_microbes = row["Num Microbes"]
        row_id = row["Source Row ID"]
        seed_id = row["Source Seed ID"]
        plant_id = row["Source Plant ID"]
        tissue_id = row["Source Tissue ID"]
        microbe_id = row["Source Microbe ID"]
        user = request.user

        if seed_id != '':
            seed_id_fix = seed_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id][0]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix][0]
            else:
                seed_id_error[(culture_id, experiment_name, media_name, location_name, culture_name, microbe_type, plating_cycle, dilution, image_filename, culture_comments, row_id, seed_id, plant_id, tissue_id, microbe_id)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            stock_id = 1

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(culture_id, experiment_name, media_name, location_name, culture_name, microbe_type, plating_cycle, dilution, image_filename, culture_comments, row_id, seed_id, plant_id, tissue_id, microbe_id)] = error_count
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
                plant_id_error[(culture_id, experiment_name, media_name, location_name, culture_name, microbe_type, plating_cycle, dilution, image_filename, culture_comments, row_id, seed_id, plant_id, tissue_id, microbe_id)] = error_count
                error_count = error_count + 1
                obs_plant_id = 1
        else:
            obs_plant_id = 1

        if tissue_id != '':
            tissue_id_fix = tissue_id + '\r'
            if tissue_id in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id][0]
            elif tissue_id_fix in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id_fix][0]
            else:
                tissue_id_error[(culture_id, experiment_name, media_name, location_name, culture_name, microbe_type, plating_cycle, dilution, image_filename, culture_comments, row_id, seed_id, plant_id, tissue_id, microbe_id)] = error_count
                error_count = error_count + 1
                obs_tissue_id = 1
        else:
            obs_tissue_id = 1

        if microbe_id != '':
            microbe_id_fix = microbe_id + '\r'
            if microbe_id in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id][0]
            elif microbe_id_fix in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id_fix][0]
            else:
                microbe_id_error[(culture_id, experiment_name, media_name, location_name, culture_name, microbe_type, plating_cycle, dilution, image_filename, culture_comments, row_id, seed_id, plant_id, tissue_id, microbe_id)] = error_count
                error_count = error_count + 1
                obs_microbe_id = 1
        else:
            obs_microbe_id = 1

        if media_name != '':
            media_name_fix = media_name + '\r'
            if media_name in media_name_table:
                medium_id = media_name_table[media_name][0]
            elif media_name_fix in media_name_table:
                medium_id = media_name_table[media_name_fix][0]
            else:
                media_name_error[(culture_id, experiment_name, media_name, location_name, culture_name, microbe_type, plating_cycle, dilution, image_filename, culture_comments, row_id, seed_id, plant_id, tissue_id, microbe_id)] = error_count
                error_count = error_count + 1
                medium_id = 1
        else:
            medium_id = 1

        if location_name != '':
            location_name_fix = location_name + '\r'
            if location_name in location_name_table:
                location_id = location_name_table[location_name][0]
            elif location_name_fix in location_name_table:
                location_id = location_name_table[location_name_fix][0]
            else:
                location_name_error[(culture_id, experiment_name, media_name, location_name, culture_name, microbe_type, plating_cycle, dilution, image_filename, culture_comments, row_id, seed_id, plant_id, tissue_id, microbe_id)] = error_count
                error_count = error_count + 1
                location_id = 1
        else:
            location_id = 1

        culture_hash = str(medium_id) + culture_id + culture_name + microbe_type + plating_cycle + dilution + image_filename + tissue_comments + num_colonies + num_microbes
        culture_hash_fix = str(medium_id) + culture_id + culture_name + microbe_type + plating_cycle + dilution + image_filename + tissue_comments + num_colonies + num_microbes + '\r'
        if culture_id not in culture_id_table and culture_id + '\r' not in culture_id_table:
            if culture_hash not in obs_culture_hash_table and culture_hash_fix not in obs_culture_hash_table:
                obs_culture_hash_table[culture_hash] = obs_culture_id
                obs_culture_new[(obs_culture_id, medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, tissue_comments, num_colonies, num_microbes)] = obs_culture_id
                culture_id_table[culture_id] = (obs_culture_id, medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, tissue_comments, num_colonies, num_microbes)
                obs_culture_id = obs_culture_id + 1
            else:
                culture_hash_exists[(medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, tissue_comments, num_colonies, num_microbes)] = obs_culture_id
        else:
            culture_hash_exists[(medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, tissue_comments, num_colonies, num_microbes)] = obs_culture_id

        if culture_id in culture_id_table:
            temp_obsculture_id = culture_id_table[culture_id][0]
        elif culture_id + '\r' in culture_id_table:
            temp_obsculture_id = culture_id_table[culture_id + '\r'][0]
        elif culture_hash in obs_culture_hash_table:
            temp_obsculture_id = obs_culture_hash_table[culture_hash]
        elif culture_hash_fix in obs_culture_hash_table:
            temp_obsculture_id = obs_culture_hash_table[culture_hash_fix]
        else:
            temp_obsculture_id = 1
            error_count = error_count + 1

        obs_tracker_culture_hash = 'culture' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsculture_id) + str(1) + str(1) + str(1) + str(obs_microbe_id) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_culture_hash_fix = 'culture' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsculture_id) + str(1) + str(1) + str(1) + str(obs_microbe_id) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username]) + '\r'
        if obs_tracker_culture_hash not in obs_tracker_hash_table and obs_tracker_culture_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_culture_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'culture', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, temp_obsculture_id, 1, 1, 1, obs_microbe_id, obs_plant_id, 1, obs_row_id, 1, obs_tissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('culture', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, temp_obsculture_id, 1, 1, 1, obs_microbe_id, obs_plant_id, 1, obs_row_id, 1, obs_tissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_culture_new'] = obs_culture_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['seed_id_error'] = seed_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['plant_id_error'] = plant_id_error
    results_dict['tissue_id_error'] = tissue_id_error
    results_dict['microbe_id_error'] = microbe_id_error
    results_dict['media_name_error'] = media_name_error
    results_dict['location_name_error'] = location_name_error
    results_dict['culture_hash_exists'] = culture_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def culture_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Culture Table'])
    writer.writerow(['obs_culture_id', 'medium_id', 'culture_id', 'culture_name', 'microbe_type', 'plating_cycle', 'dilution', 'image_filename', 'tissue_comments', 'num_colonies', 'num_microbes'])
    for key in results_dict['obs_culture_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['culture_id', 'experiment_name', 'media_name', 'location_name', 'culture_name', 'microbe_type', 'plating_cycle', 'dilution', 'image_filename', 'culture_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['culture_id', 'experiment_name', 'media_name', 'location_name', 'culture_name', 'microbe_type', 'plating_cycle', 'dilution', 'image_filename', 'culture_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plant ID Errors'])
    writer.writerow(['culture_id', 'experiment_name', 'media_name', 'location_name', 'culture_name', 'microbe_type', 'plating_cycle', 'dilution', 'image_filename', 'culture_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id'])
    for key in results_dict['plant_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Tissue ID Errors'])
    writer.writerow(['culture_id', 'experiment_name', 'media_name', 'location_name', 'culture_name', 'microbe_type', 'plating_cycle', 'dilution', 'image_filename', 'culture_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id'])
    for key in results_dict['tissue_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Microbe ID Errors'])
    writer.writerow(['culture_id', 'experiment_name', 'media_name', 'location_name', 'culture_name', 'microbe_type', 'plating_cycle', 'dilution', 'image_filename', 'culture_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id'])
    for key in results_dict['microbe_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Culture Entry Already Exists'])
    for key in results_dict['culture_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def culture_loader(results_dict):
    try:
        for key in results_dict['obs_culture_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obsculture = ObsCulture.objects.create(id=key[0], medium_id=key[1], culture_id=key[2], culture_name=key[3], microbe_type=key[4], plating_cycle=key[5], dilution=key[6], image_filename=key[7], comments=key[8], num_colonies=key[9], num_microbes=key[10])
            except Exception as e:
                print("ObsCulture Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def dna_loader_prep(upload_file, user):
    start = time.clock()

    obs_dna_new = OrderedDict({})
    #--- Key = (obs_dna_id, dna_id, extraction_method, date, tube_id, tube_type, comments)
    #--- Value = (obs_dna_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_dna_hash_table = loader_db_mirror.obs_dna_hash_mirror()
    obs_dna_id = loader_db_mirror.obs_dna_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    tissue_id_table = loader_db_mirror.tissue_id_mirror()
    microbe_id_table = loader_db_mirror.microbe_id_mirror()
    culture_id_table = loader_db_mirror.culture_id_mirror()
    well_id_table = loader_db_mirror.well_id_mirror()
    dna_id_table = loader_db_mirror.dna_id_mirror()
    plate_id_table = loader_db_mirror.plate_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    row_id_error = OrderedDict({})
    plant_id_error = OrderedDict({})
    tissue_id_error = OrderedDict({})
    microbe_id_error = OrderedDict({})
    culture_id_error = OrderedDict({})
    well_id_error = OrderedDict({})
    plate_id_error = OrderedDict({})
    dna_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    dna_file = csv.DictReader(upload_file)
    for row in dna_file:
        dna_id = row["DNA ID"]
        experiment_name = row["Experiment Name"]
        extraction = row["Extraction Method"]
        date = row["Date"]
        tube_id = row["Tube ID"]
        tube_type = row["Tube Type"]
        dna_comments = row["DNA Comments"]
        row_id = row["Source Row ID"]
        seed_id = row["Source Seed ID"]
        plant_id = row["Source Plant ID"]
        tissue_id = row["Source Tissue ID"]
        microbe_id = row["Source Microbe ID"]
        well_id = row["Source Well ID"]
        culture_id = row["Source Culture ID"]
        plate_id = row["Source Plate ID"]
        user = request.user

        if seed_id != '':
            seed_id_fix = seed_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id][0]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix][0]
            else:
                seed_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            stock_id = 1

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
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
                plant_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_plant_id = 1
        else:
            obs_plant_id = 1

        if tissue_id != '':
            tissue_id_fix = tissue_id + '\r'
            if tissue_id in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id][0]
            elif tissue_id_fix in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id_fix][0]
            else:
                tissue_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_tissue_id = 1
        else:
            obs_tissue_id = 1

        if microbe_id != '':
            microbe_id_fix = microbe_id + '\r'
            if microbe_id in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id][0]
            elif microbe_id_fix in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id_fix][0]
            else:
                microbe_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_microbe_id = 1
        else:
            obs_microbe_id = 1

        if well_id != '':
            well_id_fix = well_id + '\r'
            if well_id in well_id_table:
                obs_well_id = well_id_table[well_id][0]
            elif well_id_fix in well_id_table:
                obs_well_id = well_id_table[well_id_fix][0]
            else:
                well_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_well_id = 1
        else:
            obs_well_id = 1

        if culture_id != '':
            culture_id_fix = culture_id + '\r'
            if culture_id in culture_id_table:
                obs_culture_id = culture_id_table[culture_id][0]
            elif culture_id_fix in culture_id_table:
                obs_culture_id = culture_id_table[culture_id_fix][0]
            else:
                culture_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_culture_id = 1
        else:
            obs_culture_id = 1

        if plate_id != '':
            plate_id_fix = plate_id + '\r'
            if plate_id in plate_id_table:
                obs_plate_id = plate_id_table[plate_id][0]
            elif plate_id_fix in plate_id_table:
                obs_plate_id = plate_id_table[plate_id_fix][0]
            else:
                plate_id_error[(dna_id, experiment_name, extraction, date, tube_id, tube_type, dna_comments, row_id, seed_id, plant_id, tissue_id, microbe_id, well_id, culture_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_plate_id = 1
        else:
            obs_plate_id = 1

        dna_hash = dna_id + extraction + date + tube_id + tube_type + dna_comments
        dna_hash_fix = dna_id + extraction + date + tube_id + tube_type + dna_comments + '\r'
        if dna_id not in dna_id_table and dna_id + '\r' not in dna_id_table:
            if dna_hash not in obs_dna_hash_table and dna_hash_fix not in obs_dna_hash_table:
                obs_dna_hash_table[dna_hash] = obs_dna_id
                obs_dna_new[(obs_dna_id, dna_id, extraction, date, tube_id, tube_type, dna_comments)] = obs_dna_id
                dna_id_table[dna_id] = (obs_dna_id, dna_id, extraction, date, tube_id, tube_type, dna_comments)
                obs_dna_id = obs_dna_id + 1
            else:
                dna_hash_exists[(dna_id, extraction, date, tube_id, tube_type, dna_comments)] = obs_dna_id
        else:
            dna_hash_exists[(dna_id, extraction, date, tube_id, tube_type, dna_comments)] = obs_dna_id

        if dna_id in dna_id_table:
            temp_obsdna_id = dna_id_table[dna_id][0]
        elif dna_id + '\r' in dna_id_table:
            temp_obsdna_id = dna_id_table[dna_id + '\r'][0]
        elif dna_hash in obs_dna_hash_table:
            temp_obsdna_id = obs_dna_hash_table[dna_hash]
        elif dna_hash_fix in obs_dna_hash_table:
            temp_obsdna_id = obs_dna_hash_table[dna_hash_fix]
        else:
            temp_obsdna_id = 1
            error_count = error_count + 1

        obs_tracker_dna_hash = 'dna' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_culture_id) + str(temp_obsdna_id) + str(1) + str(1) + str(obs_microbe_id) + str(obs_plant_id) + str(obs_plate_id) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_dna_hash_fix = 'dna' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_culture_id) + str(temp_obsdna_id) + str(1) + str(1) + str(obs_microbe_id) + str(obs_plant_id) + str(obs_plate_id) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username]) + '\r'
        if obs_tracker_dna_hash not in obs_tracker_hash_table and obs_tracker_dna_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_dna_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'dna', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, temp_obsdna_id, 1, 1, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, 1, obs_tissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('dna', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, temp_obsdna_id, 1, 1, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, 1, obs_tissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_dna_new'] = obs_culture_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['seed_id_error'] = seed_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['plant_id_error'] = plant_id_error
    results_dict['tissue_id_error'] = tissue_id_error
    results_dict['microbe_id_error'] = microbe_id_error
    results_dict['culture_id_error'] = culture_id_error
    results_dict['plate_id_error'] = plate_id_error
    results_dict['well_id_error'] = well_id_error
    results_dict['dna_hash_exists'] = dna_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def dna_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New DNA Table'])
    writer.writerow(['obs_dna_id', 'dna_id', 'extraction_method', 'date', 'tube_id', 'tube_type', 'comments'])
    for key in results_dict['obs_dna_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plant ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['plant_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Tissue ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['tissue_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Microbe ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['microbe_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Culture ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['culture_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plate ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['plate_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Well ID Errors'])
    writer.writerow(['dna_id', 'experiment_name', 'extraction', 'date', 'tube_id', 'tube_type', 'dna_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_microbe_id', 'source_well_id', 'source_culture_id', 'source_plate_id'])
    for key in results_dict['well_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['DNA Entry Already Exists'])
    for key in results_dict['dna_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def dna_loader(results_dict):
    try:
        for key in results_dict['obs_dna_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obsdna = ObsDNA.objects.create(id=key[0], dna_id=key[1], extraction_method=key[2], date=key[3], tube_id=key[4], tube_type=key[5], comments=key[6])
            except Exception as e:
                print("ObsDNA Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def microbe_loader_prep(upload_file, user):
    start = time.clock()

    obs_microbe_new = OrderedDict({})
    #--- Key = (obs_microbe_id, microbe_id, microbe_type, comments)
    #--- Value = (obs_microbe_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_microbe_hash_table = loader_db_mirror.obs_microbe_hash_mirror()
    obs_microbe_id = loader_db_mirror.obs_microbe_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    tissue_id_table = loader_db_mirror.tissue_id_mirror()
    microbe_id_table = loader_db_mirror.microbe_id_mirror()
    culture_id_table = loader_db_mirror.culture_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    row_id_error = OrderedDict({})
    plant_id_error = OrderedDict({})
    tissue_id_error = OrderedDict({})
    culture_id_error = OrderedDict({})
    microbe_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    microbe_file = csv.DictReader(upload_file)
    for row in microbe_file:
        microbe_id = row["Microbe ID"]
        experiment_name = row["Experiment Name"]
        microbe_type = row["Microbe Type"]
        microbe_comments = row["Microbe Comments"]
        row_id = row["Source Row ID"]
        seed_id = row["Source Seed ID"]
        plant_id = row["Source Plant ID"]
        tissue_id = row["Source Tissue ID"]
        culture_id = row["Source Culture ID"]
        user = request.user

        if seed_id != '':
            seed_id_fix = seed_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id][0]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix][0]
            else:
                seed_id_error[(microbe_id, experiment_name, microbe_type, microbe_comments, row_id, seed_id, plant_id, tissue_id, culture_id)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            stock_id = 1

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(microbe_id, experiment_name, microbe_type, microbe_comments, row_id, seed_id, plant_id, tissue_id, culture_id)] = error_count
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
                plant_id_error[(microbe_id, experiment_name, microbe_type, microbe_comments, row_id, seed_id, plant_id, tissue_id, culture_id)] = error_count
                error_count = error_count + 1
                obs_plant_id = 1
        else:
            obs_plant_id = 1

        if tissue_id != '':
            tissue_id_fix = tissue_id + '\r'
            if tissue_id in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id][0]
            elif tissue_id_fix in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id_fix][0]
            else:
                tissue_id_error[(microbe_id, experiment_name, microbe_type, microbe_comments, row_id, seed_id, plant_id, tissue_id, culture_id)] = error_count
                error_count = error_count + 1
                obs_tissue_id = 1
        else:
            obs_tissue_id = 1

        if culture_id != '':
            culture_id_fix = culture_id + '\r'
            if culture_id in culture_id_table:
                obs_culture_id = culture_id_table[culture_id][0]
            elif culture_id_fix in culture_id_table:
                obs_culture_id = culture_id_table[culture_id_fix][0]
            else:
                culture_id_error[(microbe_id, experiment_name, microbe_type, microbe_comments, row_id, seed_id, plant_id, tissue_id, culture_id)] = error_count
                error_count = error_count + 1
                obs_culture_id = 1
        else:
            obs_culture_id = 1

        microbe_hash = microbe_id + microbe_type + microbe_comments
        microbe_hash_fix = microbe_id + microbe_type + microbe_comments + '\r'
        if microbe_id not in microbe_id_table and microbe_id + '\r' not in microbe_id_table:
            if microbe_hash not in obs_microbe_hash_table and microbe_hash_fix not in obs_microbe_hash_table:
                obs_microbe_hash_table[microbe_hash] = obs_microbe_id
                obs_microbe_new[(obs_microbe_id, microbe_id, microbe_type, microbe_comments)] = obs_microbe_id
                microbe_id_table[microbe_id] = (obs_microbe_id, microbe_id, microbe_type, microbe_comments)
                obs_microbe_id = obs_microbe_id + 1
            else:
                microbe_hash_exists[(medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, tissue_comments, num_colonies, num_microbes)] = obs_microbe_id
        else:
            microbe_hash_exists[(medium_id, culture_id, culture_name, microbe_type, plating_cycle, dilution, image_filename, tissue_comments, num_colonies, num_microbes)] = obs_microbe_id

        if microbe_id in microbe_id_table:
            temp_obsmicrobe_id = microbe_id_table[microbe_id][0]
        elif microbe_id + '\r' in microbe_id_table:
            temp_obsmicrobe_id = microbe_id_table[microbe_id + '\r'][0]
        elif microbe_hash in obs_microbe_hash_table:
            temp_obsmicrobe_id = obs_microbe_hash_table[microbe_hash]
        elif microbe_hash_fix in obs_microbe_hash_table:
            temp_obsmicrobe_id = obs_microbe_hash_table[microbe_hash_fix]
        else:
            temp_obsmicrobe_id = 1
            error_count = error_count + 1

        obs_tracker_microbe_hash = 'microbe' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_culture_id) + str(1) + str(1) + str(1) + str(temp_obsmicrobe_id) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_microbe_hash_fix = 'microbe' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_culture_id) + str(1) + str(1) + str(1) + str(temp_obsmicrobe_id) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(1) + str(stock_id) + str(user_hash_table[user.username]) + '\r'
        if obs_tracker_microbe_hash not in obs_tracker_hash_table and obs_tracker_microbe_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_microbe_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'microbe', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, 1, 1, 1, temp_obsmicrobe_id, obs_plant_id, 1, obs_row_id, 1, obs_tissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('microbe', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, 1, 1, 1, temp_obsmicrobe_id, obs_plant_id, 1, obs_row_id, 1, obs_tissue_id, 1, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_culture_new'] = obs_culture_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['seed_id_error'] = seed_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['plant_id_error'] = plant_id_error
    results_dict['tissue_id_error'] = tissue_id_error
    results_dict['culture_id_error'] = culture_id_error
    results_dict['culture_hash_exists'] = culture_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def microbe_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Microbe Table'])
    writer.writerow(['obs_microbe_id', 'microbe_id', 'microbe_type', 'comments'])
    for key in results_dict['obs_microbe_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['microbe_id', 'experiment_name', 'microbe_type', 'microbe_comments','source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['microbe_id', 'experiment_name', 'microbe_type', 'microbe_comments','source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plant ID Errors'])
    writer.writerow(['microbe_id', 'experiment_name', 'microbe_type', 'microbe_comments','source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id'])
    for key in results_dict['plant_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Tissue ID Errors'])
    writer.writerow(['microbe_id', 'experiment_name', 'microbe_type', 'microbe_comments','source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id'])
    for key in results_dict['tissue_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Culture ID Errors'])
    writer.writerow(['microbe_id', 'experiment_name', 'microbe_type', 'microbe_comments','source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id'])
    for key in results_dict['culture_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Microbe Entry Already Exists'])
    for key in results_dict['microbe_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def microbe_loader(results_dict):
    try:
        for key in results_dict['obs_microbe_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obsmicrobe = ObsMicrobe.objects.create(id=key[0], microbe_id=key[1], microbe_type=key[2], comments=key[3])
            except Exception as e:
                print("ObsMicrobe Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def plate_loader_prep(upload_file, user):
    start = time.clock()

    obs_plate_new = OrderedDict({})
    #--- Key = (obs_plate_id, plate_id, plate_name, date, contents, rep, plate_type, plate_status, comments)
    #--- Value = (obs_plate_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_plate_hash_table = loader_db_mirror.obs_plate_hash_mirror()
    obs_plate_id = loader_db_mirror.obs_plate_id_mirror()
    plate_id_table = loader_db_mirror.plate_id_mirror()
    location_name_table = loader_db_mirror.location_name_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    location_name_error = OrderedDict({})
    plate_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    plate_file = csv.DictReader(upload_file)
    for row in plate_file:
        plate_id = row["Plate ID"]
        experiment_name = row["Experiment Name"]
        location_name = row["Location Name"]
        plate_name = row["Plate Name"]
        date = row["Date Plated"]
        contents = row["Plate Contents"]
        rep = row["Plate Rep"]
        plate_type = row["Plate Type"]
        plate_status = row["Plate Status"]
        plate_comments = row["Plate Comments"]
        user = request.user

        if location_name != '':
            location_name_fix = location_name + '\r'
            if location_name in location_name_table:
                location_id = location_name_table[location_name][0]
            elif location_name_fix in location_name_table:
                location_id = location_name_table[location_name_fix][0]
            else:
                location_name_error[(plate_id, experiment_name, location_name, plate_name, date, contents, rep, plate_type, plate_status, plate_comments)] = error_count
                error_count = error_count + 1
                location_id = 1
        else:
            location_id = 1

        plate_hash = plate_id + plate_name + date + contents + rep + plate_type + plate_status + plate_comments
        plate_hash_fix = plate_id + plate_name + date + contents + rep + plate_type + plate_status + plate_comments + '\r'
        if plate_id not in plate_id_table and plate_id + '\r' not in plate_id_table:
            if plate_hash not in obs_plate_hash_table and plate_hash_fix not in obs_plate_hash_table:
                obs_plate_hash_table[plate_hash] = obs_plate_id
                obs_plate_new[(obs_plate_id, plate_id, plate_name, date, contents, rep, plate_type, plate_status, plate_comments)] = obs_plate_id
                plate_id_table[plate_id] = (obs_plate_id, plate_id, plate_name, date, contents, rep, plate_type, plate_status, plate_comments)
                obs_plate_id = obs_plate_id + 1
            else:
                plate_hash_exists[(plate_id, plate_name, date, contents, rep, plate_type, plate_status, plate_comments)] = obs_plate_id
        else:
            plate_hash_exists[(plate_id, plate_name, date, contents, rep, plate_type, plate_status, plate_comments)] = obs_plate_id

        if plate_id in plate_id_table:
            temp_obsplate_id = plate_id_table[plate_id][0]
        elif plate_id + '\r' in plate_id_table:
            temp_obsplate_id = plate_id_table[plate_id + '\r'][0]
        elif plate_hash in obs_plate_hash_table:
            temp_obsplate_id = obs_plate_hash_table[plate_hash]
        elif plate_hash_fix in obs_plate_hash_table:
            temp_obsplate_id = obs_plate_hash_table[plate_hash_fix]
        else:
            temp_obsplate_id = 1
            error_count = error_count + 1

        obs_tracker_plate_hash = 'plate' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(location_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsplate_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(user_hash_table[user.username])
        obs_tracker_plate_hash_fix = 'plate' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(location_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsplate_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(user_hash_table[user.username]) + '\r'
        if obs_tracker_plate_hash not in obs_tracker_hash_table and obs_tracker_plate_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_plate_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'plate', experiment_name_table[experiment_name][0], 1, 1, 1, location_id, 1, 1, 1, 1, 1, 1, 1, temp_obsplate_id, 1, 1, 1, 1, 1, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('plate', experiment_name_table[experiment_name][0], 1, 1, 1, location_id, 1, 1, 1, 1, 1, 1, 1, temp_obsplate_id, 1, 1, 1, 1, 1, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_plate_new'] = obs_plate_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['location_name_error'] = location_name_error
    results_dict['plate_hash_exists'] = plate_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def plate_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Plate Table'])
    writer.writerow(['obs_plate_id', 'plate_id', 'plate_name', 'date', 'contents', 'rep', 'plate_type', 'plate_status', 'comments'])
    for key in results_dict['obs_plate_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Location Name Errors'])
    writer.writerow(['plate_id', 'experiment_name', 'location_name', 'plate_name', 'date', 'contents', 'rep', 'plate_type', 'plate_status', 'plate_comments'])
    for key in results_dict['location_name_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plate Entry Already Exists'])
    for key in results_dict['plate_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def plate_loader(results_dict):
    try:
        for key in results_dict['obs_plate_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obsplate = ObsPlate.objects.create(id=key[0], plate_id=key[1], plate_name=key[2], date=key[3], contents=key[4], rep=key[5], plate_type=key[6], plate_status=key[7], comments=key[8])
            except Exception as e:
                print("ObsPlate Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def env_loader_prep(upload_file, user):
    start = time.clock()

    obs_env_new = OrderedDict({})
    #--- Key = (obs_env_id, environment_id, longitude, latitude, comments)
    #--- Value = (obs_env_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_env_hash_table = loader_db_mirror.obs_env_hash_mirror()
    obs_env_id = loader_db_mirror.obs_env_id_mirror()
    field_name_table = loader_db_mirror.field_name_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    field_name_error = OrderedDict({})
    env_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    env_file = csv.DictReader(upload_file)
    for row in env_file:
        environment_id = row["Environment ID"]
        experiment_name = row["Experiment Name"]
        field_name = row["Field Name"]
        longitude = row["Longitude"]
        latitude = row["Latitude"]
        env_comments = row["Environment Comments"]
        user = request.user

        if field_name != '':
            field_name_fix = field_name + '\r'
            if field_name in field_name_table:
                field_id = field_name_table[field_name][0]
            elif field_name_fix in field_name_table:
                field_id = field_name_table[field_name_fix][0]
            else:
                field_name_error[(environment_id, experiment_name, field_name, longitude, latitude, env_comments)] = error_count
                error_count = error_count + 1
                field_id = 1
        else:
            field_id = 1

        env_hash = environment_id + longitude + latitude + env_comments
        env_hash_fix = env_hash + '\r'
        if environment_id not in env_id_table and environment_id + '\r' not in env_id_table:
            if env_hash not in obs_env_hash_table and env_hash_fix not in obs_env_hash_table:
                obs_env_hash_table[env_hash] = obs_env_id
                obs_env_new[(obs_env_id, environment_id, longitude, latitude, env_comments)] = obs_env_id
                env_id_table[environment_id] = (obs_env_id, environment_id, longitude, latitude, env_comments)
                obs_env_id = obs_env_id + 1
            else:
                env_hash_exists[(environment_id, longitude, latitude, env_comments)] = obs_env_id
        else:
            env_hash_exists[(environment_id, longitude, latitude, env_comments)] = obs_env_id

        if environment_id in env_id_table:
            temp_obsenv_id = env_id_table[environment_id][0]
        elif environment_id + '\r' in env_id_table:
            temp_obsenv_id = env_id_table[environment_id + '\r'][0]
        elif env_hash in obs_env_hash_table:
            temp_obsenv_id = obs_env_hash_table[env_hash]
        elif env_hash_fix in obs_env_hash_table:
            temp_obsenv_id = obs_env_hash_table[env_hash_fix]
        else:
            temp_obsenv_id = 1
            error_count = error_count + 1

        obs_tracker_env_hash = 'environment' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(temp_obsenv_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(user_hash_table[user.username])
        obs_tracker_env_hash_fix = obs_tracker_env_hash + '\r'
        if obs_tracker_env_hash not in obs_tracker_hash_table and obs_tracker_env_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_env_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'environment', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, temp_obsenv_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('environment', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, temp_obsenv_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_env_new'] = obs_env_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['field_name_error'] = field_name_error
    results_dict['env_hash_exists'] = env_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def env_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Environment Table'])
    writer.writerow(['obs_env_id', 'environment_id', 'longitude', 'latitude', 'comments'])
    for key in results_dict['obs_env_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Field Name Errors'])
    writer.writerow(['environment_id', 'experiment_name', 'field_name', 'longitude', 'latitude', 'env_comments'])
    for key in results_dict['field_name_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Environment Entry Already Exists'])
    for key in results_dict['env_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def env_loader(results_dict):
    try:
        for key in results_dict['obs_env_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obsenv = ObsEnv.objects.create(id=key[0], environment_id=key[1], longitude=key[2], latitude=key[3], comments=key[4])
            except Exception as e:
                print("ObsEnv Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def well_loader_prep(upload_file, user):
    start = time.clock()

    obs_well_new = OrderedDict({})
    #--- Key = (obs_well_id, well_id, well, well_inventory, tube_label, comments)
    #--- Value = (obs_well_id)
    obs_tracker_new = OrderedDict({})
    #--- Key = (obs_tracker_id, obs_entity_type, experiment_id, field_id, glycerol_stock_id, isolate_id, location_id, maize_sample_id, obs_culture_id, obs_dna_id, obs_env_id, obs_extract_id, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, obs_sample_id, obs_tissue_id, obs_well_id, stock_id, user_id)
    #--- Value = (obs_tracker_id)

    user_hash_table = loader_db_mirror.user_hash_mirror()
    obs_well_hash_table = loader_db_mirror.obs_well_hash_mirror()
    obs_well_id = loader_db_mirror.obs_well_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    tissue_id_table = loader_db_mirror.tissue_id_mirror()
    microbe_id_table = loader_db_mirror.microbe_id_mirror()
    culture_id_table = loader_db_mirror.culture_id_mirror()
    plate_id_table = loader_db_mirror.plate_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    row_id_error = OrderedDict({})
    plant_id_error = OrderedDict({})
    tissue_id_error = OrderedDict({})
    culture_id_error = OrderedDict({})
    plate_id_error = OrderedDict({})
    microbe_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    well_file = csv.DictReader(upload_file)
    for row in well_file:
        well_id = row["Well ID"]
        experiment_name = row["Experiment Name"]
        well = row["Well"]
        inventory = row["Inventory"]
        tube_label = row["Tube Label"]
        well_comments = row["Well Comments"]
        row_id = row["Source Row ID"]
        seed_id = row["Source Seed ID"]
        plant_id = row["Source Plant ID"]
        tissue_id = row["Source Tissue ID"]
        culture_id = row["Source Culture ID"]
        microbe_id = row["Source Microbe ID"]
        plate_id = row["Source Plate ID"]
        user = request.user

        if seed_id != '':
            seed_id_fix = seed_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id][0]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix][0]
            else:
                seed_id_error[(well_id, experiment_name, well, inventory, tube_label, well_comments, row_id, seed_id, plant_id, tissue_id, culture_id, microbe_id, plate_id)] = error_count
                error_count = error_count + 1
                stock_id = 1
        else:
            stock_id = 1

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(well_id, experiment_name, well, inventory, tube_label, well_comments, row_id, seed_id, plant_id, tissue_id, culture_id, microbe_id, plate_id)] = error_count
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
                plant_id_error[(well_id, experiment_name, well, inventory, tube_label, well_comments, row_id, seed_id, plant_id, tissue_id, culture_id, microbe_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_plant_id = 1
        else:
            obs_plant_id = 1

        if tissue_id != '':
            tissue_id_fix = tissue_id + '\r'
            if tissue_id in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id][0]
            elif tissue_id_fix in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id_fix][0]
            else:
                tissue_id_error[(well_id, experiment_name, well, inventory, tube_label, well_comments, row_id, seed_id, plant_id, tissue_id, culture_id, microbe_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_tissue_id = 1
        else:
            obs_tissue_id = 1

        if culture_id != '':
            culture_id_fix = culture_id + '\r'
            if culture_id in culture_id_table:
                obs_culture_id = culture_id_table[culture_id][0]
            elif culture_id_fix in culture_id_table:
                obs_culture_id = culture_id_table[culture_id_fix][0]
            else:
                culture_id_error[(well_id, experiment_name, well, inventory, tube_label, well_comments, row_id, seed_id, plant_id, tissue_id, culture_id, microbe_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_culture_id = 1
        else:
            obs_culture_id = 1

        if plate_id != '':
            plate_id_fix = plate_id + '\r'
            if plate_id in plate_id_table:
                obs_plate_id = plate_id_table[plate_id][0]
            elif plate_id_fix in plate_id_table:
                obs_plate_id = plate_id_table[plate_id_fix][0]
            else:
                plate_id_error[(well_id, experiment_name, well, inventory, tube_label, well_comments, row_id, seed_id, plant_id, tissue_id, culture_id, microbe_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_plate_id = 1
        else:
            obs_plate_id = 1

        if microbe_id != '':
            microbe_id_fix = microbe_id + '\r'
            if microbe_id in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id][0]
            elif microbe_id_fix in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id_fix][0]
            else:
                microbe_id_error[(well_id, experiment_name, well, inventory, tube_label, well_comments, row_id, seed_id, plant_id, tissue_id, culture_id, microbe_id, plate_id)] = error_count
                error_count = error_count + 1
                obs_microbe_id = 1
        else:
            obs_microbe_id = 1

        well_hash = well_id + well + inventory + tube_label + well_comments
        well_hash_fix = well_id + well + inventory + tube_label + well_comments + '\r'
        if well_id not in well_id_table and well_id + '\r' not in well_id_table:
            if well_hash not in obs_well_hash_table and well_hash_fix not in obs_well_hash_table:
                obs_well_hash_table[well_hash] = obs_well_id
                obs_well_new[(obs_well_id, well_id, well, inventory, tube_label, well_comments)] = obs_well_id
                well_id_table[well_id] = (obs_well_id, well_id, well, inventory, tube_label, well_comments)
                obs_well_id = obs_well_id + 1
            else:
                well_hash_exists[(well_id, well, inventory, tube_label, well_comments)] = obs_well_id
        else:
            well_hash_exists[(well_id, well, inventory, tube_label, well_comments)] = obs_well_id

        if well_id in well_id_table:
            temp_obswell_id = well_id_table[well_id][0]
        elif well_id + '\r' in well_id_table:
            temp_obswell_id = well_id_table[well_id + '\r'][0]
        elif well_hash in obs_well_hash_table:
            temp_obswell_id = obs_well_hash_table[well_hash]
        elif well_hash_fix in obs_well_hash_table:
            temp_obswell_id = obs_well_hash_table[well_hash_fix]
        else:
            temp_obswell_id = 1
            error_count = error_count + 1

        obs_tracker_well_hash = 'well' + str(experiment_name_table[experiment_name][0]) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_culture_id) + str(1) + str(1) + str(1) + str(obs_microbe_id) + str(obs_plant_id) + str(obs_plate_id) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(temp_obswell_id) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_well_hash_fix = obs_tracker_well_hash + '\r'
        if obs_tracker_microbe_hash not in obs_tracker_hash_table and obs_tracker_microbe_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_microbe_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'well', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, 1, 1, 1, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, 1, obs_tissue_id, temp_obswell_id, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('well', experiment_name_table[experiment_name][0], 1, 1, 1, 1, 1, obs_culture_id, 1, 1, 1, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, 1, obs_tissue_id, temp_obswell_id, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['obs_well_new'] = obs_well_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['seed_id_error'] = seed_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['plant_id_error'] = plant_id_error
    results_dict['tissue_id_error'] = tissue_id_error
    results_dict['culture_id_error'] = culture_id_error
    results_dict['plate_id_error'] = plate_id_error
    results_dict['microbe_id_error'] = microbe_id_error
    results_dict['well_hash_exists'] = well_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def well_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Well Table'])
    writer.writerow(['obs_well_id', 'well_id', 'well', 'well_inventory', 'tube_label', 'comments'])
    for key in results_dict['obs_well_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plant ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['plant_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Tissue ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['tissue_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Culture ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['culture_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Microbe ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['microbe_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plate ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['plate_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Well Entry Already Exists'])
    for key in results_dict['well_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def well_loader(results_dict):
    try:
        for key in results_dict['obs_well_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_obswell = ObsWell.objects.create(id=key[0], well_id=key[1], well=key[2], well_inventory=key[3], tube_label=key[4], comments=key[5])
            except Exception as e:
                print("ObsWell Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_stock = ObsTracker.objects.create(id=key[0], obs_entity_type=key[1], experiment_id=key[2], field_id=key[3], glycerol_stock_id=key[4], isolate_id=key[5], location_id=key[6], maize_sample_id=key[7], obs_culture_id=key[8], obs_dna_id=key[9], obs_env_id=key[10], obs_extract_id=key[11], obs_microbe_id=key[12], obs_plant_id=key[13], obs_plate_id=key[14], obs_row_id=key[15], obs_sample_id=key[16], obs_tissue_id=key[17], obs_well_id=key[18], stock_id=key[19], user_id=key[20])
            except Exception as e:
                print("ObsTracker Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True

def isolate_loader_prep(upload_file, user):
    start = time.clock()

    isolate_new = OrderedDict({})
    #--- Key = (isolate_table_id, passport_id, location_id, disease_info_id, isolate_id, isolate_name, plant_organ, comments)
    #--- Value = (isolate_table_id)
    location_new = OrderedDict({})
    #--- Key = (location_id, locality_id, building_name, location_name, room, shelf, column, box_name, comments)
    #--- Value = (location_id)
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

    user_hash_table = loader_db_mirror.user_hash_mirror()
    location_hash_table = loader_db_mirror.location_hash_mirror()
    location_id = loader_db_mirror.location_id_mirror()
    passport_hash_table = loader_db_mirror.passport_hash_mirror()
    passport_id = loader_db_mirror.passport_id_mirror()
    collecting_hash_table = loader_db_mirror.collecting_hash_mirror()
    collecting_id = loader_db_mirror.collecting_id_mirror()
    taxonomy_hash_table = loader_db_mirror.taxonomy_hash_mirror()
    taxonomy_id = loader_db_mirror.taxonomy_id_mirror()
    people_hash_table = loader_db_mirror.people_hash_mirror()
    people_id = loader_db_mirror.people_id_mirror()
    isolate_hash_table = loader_db_mirror.obs_well_hash_mirror()
    isolate_table_id = loader_db_mirror.isolate_table_id_mirror()
    row_id_table = loader_db_mirror.row_id_mirror()
    seed_id_table = loader_db_mirror.seed_id_mirror()
    plant_id_table = loader_db_mirror.plant_id_mirror()
    tissue_id_table = loader_db_mirror.tissue_id_mirror()
    microbe_id_table = loader_db_mirror.microbe_id_mirror()
    culture_id_table = loader_db_mirror.culture_id_mirror()
    plate_id_table = loader_db_mirror.plate_id_mirror()
    dna_id_table = loader_db_mirror.dna_id_mirror()
    well_id_table = loader_db_mirror.well_id_mirror()
    isolate_id_table = loader_db_mirror.isolate_id_mirror()
    obs_tracker_hash_table = loader_db_mirror.obs_tracker_hash_mirror()
    obs_tracker_id = loader_db_mirror.obs_tracker_id_mirror()
    experiment_name_table = loader_db_mirror.experiment_name_mirror()
    field_name_table = loader_db_mirror.field_name_mirror()
    disease_name_table = loader_db_mirror.disease_name_mirror()

    error_count = 0
    seed_id_error = OrderedDict({})
    row_id_error = OrderedDict({})
    plant_id_error = OrderedDict({})
    tissue_id_error = OrderedDict({})
    culture_id_error = OrderedDict({})
    plate_id_error = OrderedDict({})
    well_id_error = OrderedDict({})
    dna_id_error = OrderedDict({})
    microbe_id_error = OrderedDict({})
    disease_common_name_error = OrderedDict({})
    field_name_error = OrderedDict({})
    isolate_hash_exists = OrderedDict({})
    obs_tracker_hash_exists = OrderedDict({})

    isolate_file = csv.DictReader(upload_file)
    for row in isolate_file:
        isolate_id = row["Isolate ID"]
        experiment_name = row["Experiment Name"]
        isolate_name = row["Isolate Name"]
        plant_organ = row["Plant Organ"]
        isolate_comments = row["Isolate Comments"]
        genus = row["Genus"]
        species = row["Species"]
        population = row["Population"]
        alias = row["Alias"]
        race = row["Race"]
        subtaxa = row["Subtaxa"]
        disease_common_name = row["Disease Common Name"]
        row_id = row["Source Row ID"]
        field_name = row["Source Field Name"]
        seed_id = row["Source Seed ID"]
        plant_id = row["Source Plant ID"]
        tissue_id = row["Source Tissue ID"]
        culture_id = row["Source Culture ID"]
        microbe_id = row["Source Microbe ID"]
        plate_id = row["Source Plate ID"]
        well_id = row["Source Well ID"]
        dna_id = row["Source DNA ID"]
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
        location_name = row["Location Name"]
        locality = row["Locality"]
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
        user = request.user

        if seed_id != '':
            seed_id_fix = seed_id + '\r'
            if seed_id in seed_id_table:
                stock_id = seed_id_table[seed_id][0]
            elif seed_id_fix in seed_id_table:
                stock_id = seed_id_table[seed_id_fix][0]
            else:
                seed_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
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
                field_name_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                field_id = 1
        else:
            field_id = 1

        if row_id != '':
            row_id_fix = row_id + '\r'
            if row_id in row_id_table:
                obs_row_id = row_id_table[row_id][0]
            elif row_id_fix in row_id_table:
                obs_row_id = row_id_table[row_id_fix][0]
            else:
                row_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
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
                plant_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                obs_plant_id = 1
        else:
            obs_plant_id = 1

        if tissue_id != '':
            tissue_id_fix = tissue_id + '\r'
            if tissue_id in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id][0]
            elif tissue_id_fix in tissue_id_table:
                obs_tissue_id = tissue_id_table[tissue_id_fix][0]
            else:
                tissue_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                obs_tissue_id = 1
        else:
            obs_tissue_id = 1

        if culture_id != '':
            culture_id_fix = culture_id + '\r'
            if culture_id in culture_id_table:
                obs_culture_id = culture_id_table[culture_id][0]
            elif culture_id_fix in culture_id_table:
                obs_culture_id = culture_id_table[culture_id_fix][0]
            else:
                culture_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                obs_culture_id = 1
        else:
            obs_culture_id = 1

        if plate_id != '':
            plate_id_fix = plate_id + '\r'
            if plate_id in plate_id_table:
                obs_plate_id = plate_id_table[plate_id][0]
            elif plate_id_fix in plate_id_table:
                obs_plate_id = plate_id_table[plate_id_fix][0]
            else:
                plate_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                obs_plate_id = 1
        else:
            obs_plate_id = 1

        if microbe_id != '':
            microbe_id_fix = microbe_id + '\r'
            if microbe_id in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id][0]
            elif microbe_id_fix in microbe_id_table:
                obs_microbe_id = microbe_id_table[microbe_id_fix][0]
            else:
                microbe_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                obs_microbe_id = 1
        else:
            obs_microbe_id = 1

        if well_id != '':
            well_id_fix = well_id + '\r'
            if well_id in well_id_table:
                obs_well_id = well_id_table[well_id][0]
            elif well_id_fix in well_id_table:
                obs_well_id = well_id_table[well_id_fix][0]
            else:
                well_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                obs_well_id = 1
        else:
            obs_well_id = 1

        if dna_id != '':
            dna_id_fix = dna_id + '\r'
            if dna_id in dna_id_table:
                obs_dna_id = dna_id_table[dna_id][0]
            elif dna_id_fix in dna_id_table:
                obs_dna_id = dna_id_table[dna_id_fix][0]
            else:
                dna_id_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                obs_dna_id = 1
        else:
            obs_dna_id = 1

        if disease_common_name != '':
            disease_common_name_fix = disease_common_name + '\r'
            if disease_common_name in disease_name_table:
                disease_info_id = disease_name_table[disease_common_name][0]
            elif disease_common_name_fix in disease_name_table:
                disease_info_id = disease_name_table[disease_common_name_fix][0]
            else:
                disease_common_name_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                disease_info_id = 1
        else:
            disease_info_id = 1

        if collection_user == '':
            collection_user_id = user_hash_table['unknown_person']
        else:
            try:
                collection_user_id = user_hash_table[collection_user]
            except KeyError:
                collection_user_error[(isolate_id, experiment_name, isolate_name, plant_organ, isolate_comments, genus, species, population, alias, race, subtaxa, row_id, field_name, plant_id, seed_id, tissue_id, microbe_id, well_id, plate_id, dna_id, culture_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments, location_name, building_name, room, shelf, column, box_name, location_comments)] = error_count
                error_count = error_count + 1
                collection_user_id = user_hash_table['unknown_person']

        collecting_hash = str(collection_user_id) + collection_date + collection_method + collection_comments
        collecting_hash_fix = collecting_hash + '\r'
        if collecting_hash not in collecting_hash_table and collecting_hash_fix not in collecting_hash_table:
            collecting_hash_table[collecting_hash] = collecting_id
            collecting_new[(collecting_id, collection_user_id, collection_date, collection_method, collection_comments)] = collecting_id
            collecting_id = collecting_id + 1
        else:
            collecting_hash_exists[(collection_user_id, collection_date, collection_method, collection_comments)] = collecting_id

        if collecting_hash in collecting_hash_table:
            temp_collecting_id = collecting_hash_table[collecting_hash]
        elif collecting_hash_fix in collecting_hash_table:
            temp_collecting_id = collecting_hash_table[collecting_hash_fix]
        else:
            temp_collecting_id = 1
            error_count = error_count + 1

        taxonomy_hash = genus + species + population + 'Isolate' + alias + race + subtaxa
        taxonomy_hash_fix = taxonomy_hash + '\r'
        if taxonomy_hash not in taxonomy_hash_table and taxonomy_hash_fix not in taxonomy_hash_table:
            taxonomy_hash_table[taxonomy_hash] = taxonomy_id
            taxonomy_new[(taxonomy_id, genus, species, population, 'Isolate', alias, race, subtaxa)] = taxonomy_id
            taxonomy_id = taxonomy_id + 1
        else:
            taxonomy_hash_exists[(genus, species, population, 'Isolate', alias, race, subtaxa)] = taxonomy_id

        if taxonomy_hash in taxonomy_hash_table:
            temp_taxonomy_id = taxonomy_hash_table[taxonomy_hash]
        elif taxonomy_hash_fix in taxonomy_hash_table:
            temp_taxonomy_id = taxonomy_hash_table[taxonomy_hash_fix]
        else:
            temp_taxonomy_id = 1
            error_count = error_count + 1

        people_hash = first_name + last_name + organization + phone + email + source_comments
        people_hash_fix = people_hash + '\r'
        if people_hash not in people_hash_table and people_hash_fix not in people_hash_table:
            people_hash_table[people_hash] = people_id
            people_new[(people_id, first_name, last_name, organization, phone, email, source_comments)] = people_id
            people_id = people_id + 1
        else:
            people_hash_exists[(first_name, last_name, organization, phone, email, source_comments)] = people_id

        if people_hash in people_hash_table:
            temp_people_id = people_hash_table[people_hash]
        elif people_hash_fix in people_hash_table:
            temp_people_id = people_hash_table[people_hash_fix]
        else:
            temp_people_id = 1
            error_count = error_count + 1

        passport_hash = str(temp_collecting_id) + str(temp_people_id) + str(temp_taxonomy_id)
        passport_hash_fix = passport_hash + '\r'
        if passport_hash not in passport_hash_table and passport_hash_fix not in passport_hash_table:
            passport_hash_table[passport_hash] = passport_id
            passport_new[(passport_id, temp_collecting_id, temp_people_id, temp_taxonomy_id)] = passport_id
            passport_id = passport_id + 1
        else:
            passport_hash_exists[(temp_collecting_id, temp_people_id, temp_taxonomy_id)] = passport_id

        if passport_hash in passport_hash_table:
            temp_passport_id = passport_hash_table[passport_hash]
        elif passport_hash_fix in passport_hash_table:
            temp_passport_id = passport_hash_table[passport_hash_fix]
        else:
            temp_passport_id = 1
            error_count = error_count + 1

        location_hash = str(locality.id) + building_name + location_name + room + shelf + column + box_name + location_comments
        location_hash_fix = location_hash + '\r'
        if location_hash not in location_hash_table and location_hash_fix not in location_hash_table:
            location_hash_table[location_hash] = location_id
            location_new[(location_id, locality.id, building_name, location_name, room, shelf, column, box_name, location_comments)] = location_id
            location_id = location_id + 1
        else:
            location_hash_exists[(locality.id, building_name, location_name, room, shelf, column, box_name, location_comments)] = location_id

        if location_hash in location_hash_table:
            temp_location_id = location_hash_table[location_hash]
        elif location_hash_fix in location_hash_table:
            temp_location_id = location_hash_table[location_hash_fix]
        else:
            temp_location_id = 1
            error_count = error_count + 1

        isolate_hash = str(temp_passport_id) + str(temp_location_id) + str(disease_info_id) + isolate_id + isolate_name + plant_organ + isolate_comments
        isolate_hash_fix = isolate_hash + '\r'
        if isolate_id not in isolate_id_table and isolate_id + '\r' not in isolate_id_table:
            if isolate_hash not in isolate_hash_table and isolate_hash_fix not in isolate_hash_table:
                isolate_hash_table[isolate_hash] = isolate_table_id
                isolate_new[(isolate_table_id, temp_passport_id, temp_location_id, disease_info_id, isolate_id, isolate_name, plant_organ, isolate_comments)] = isolate_table_id
                isolate_id_table[isolate_id] = (isolate_table_id, temp_passport_id, temp_location_id, disease_info_id, isolate_id, isolate_name, plant_organ, isolate_comments)
                isolate_table_id = isolate_table_id + 1
            else:
                isolate_hash_exists[(temp_passport_id, temp_location_id, disease_info_id, isolate_id, isolate_name, plant_organ, isolate_comments)] = isolate_table_id
        else:
            isolate_hash_exists[(temp_passport_id, temp_location_id, disease_info_id, isolate_id, isolate_name, plant_organ, isolate_comments)] = isolate_table_id

        if isolate_id in isolate_id_table:
            temp_isolate_id = isolate_id_table[isolate_id][0]
        elif isolate_id + '\r' in isolate_id_table:
            temp_isolate_id = isolate_id_table[isolate_id + '\r'][0]
        elif isolate_hash in isolate_hash_table:
            temp_isolate_id = isolate_hash_table[isolate_hash]
        elif isolate_hash_fix in isolate_hash_table:
            temp_isolate_id = isolate_hash_table[isolate_hash_fix]
        else:
            temp_isolate_id = 1
            error_count = error_count + 1

        obs_tracker_isolate_hash = 'isolate' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(temp_isolate_id) + str(temp_location_id) + str(1) + str(obs_culture_id) + str(obs_dna_id) + str(1) + str(1) + str(obs_microbe_id) + str(obs_plant_id) + str(obs_plate_id) + str(obs_row_id) + str(1) + str(obs_tissue_id) + str(obs_well_id) + str(stock_id) + str(user_hash_table[user.username])
        obs_tracker_isolate_hash_fix = obs_tracker_well_hash + '\r'
        if obs_tracker_isolate_hash not in obs_tracker_hash_table and obs_tracker_isolate_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_isolate_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'isolate', experiment_name_table[experiment_name][0], field_id, 1, temp_isolate_id, temp_location_id, 1, obs_culture_id, obs_dna_id, 1, 1, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, 1, obs_tissue_id, obs_well_id, stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('isolate', experiment_name_table[experiment_name][0], field_id, 1, temp_isolate_id, temp_location_id, 1, obs_culture_id, obs_dna_id, 1, 1, obs_microbe_id, obs_plant_id, obs_plate_id, obs_row_id, 1, obs_tissue_id, obs_well_id, stock_id, user_hash_table[user.username])] = obs_tracker_id

    end = time.clock()
    stats = {}
    stats[("Time: %s" % (end-start), "Errors: %s" % (error_count))] = error_count

    results_dict = {}
    results_dict['isolate_new'] = isolate_new
    results_dict['location_new'] = location_new
    results_dict['passport_new'] = passport_new
    results_dict['collecting_new'] = collecting_new
    results_dict['people_new'] = people_new
    results_dict['taxonomy_new'] = taxonomy_new
    results_dict['obs_tracker_new'] = obs_tracker_new
    results_dict['field_name_error'] = field_name_error
    results_dict['disease_common_name_error'] = disease_common_name_error
    results_dict['seed_id_error'] = seed_id_error
    results_dict['row_id_error'] = row_id_error
    results_dict['plant_id_error'] = plant_id_error
    results_dict['tissue_id_error'] = tissue_id_error
    results_dict['culture_id_error'] = culture_id_error
    results_dict['plate_id_error'] = plate_id_error
    results_dict['microbe_id_error'] = microbe_id_error
    results_dict['dna_id_error'] = dna_id_error
    results_dict['well_id_error'] = well_id_error
    results_dict['isolate_hash_exists'] = well_hash_exists
    results_dict['obs_tracker_hash_exists'] = obs_tracker_hash_exists
    results_dict['stats'] = stats
    return results_dict

def isolate_loader_prep_output(results_dict, new_upload_exp, template_type):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s_%s_prep.csv"' % (new_upload_exp, template_type)
    writer = csv.writer(response)
    writer.writerow(['Stats'])
    writer.writerow([''])
    for key in results_dict['stats'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New Isolate Table'])
    writer.writerow(['isolate_table_id', 'passport_id', 'location_id', 'disease_info_id', 'isolate_id', 'isolate_name', 'plant_organ', 'comments'])
    for key in results_dict['isolate_new'].iterkeys():
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
    writer.writerow(['New Location Table'])
    writer.writerow(['location_id', 'location_name', 'building_name', 'room', 'shelf', 'column', 'box_name', 'comments'])
    for key in results_dict['location_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['New ObsTracker Table'])
    writer.writerow(['obs_tracker_id', 'obs_entity_type', 'experiment_id', 'field_id', 'glycerol_stock_id', 'isolate_id', 'location_id', 'maize_sample_id', 'obs_culture_id', 'obs_dna_id', 'obs_env_id', 'obs_extract_id', 'obs_microbe_id', 'obs_plant_id', 'obs_plate_id', 'obs_row_id', 'obs_sample_id', 'obs_tissue_id', 'obs_well_id', 'stock_id', 'user_id'])
    for key in results_dict['obs_tracker_new'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['---------------------------------------------------------------------------------------------------'])
    writer.writerow([''])
    writer.writerow(['Seed ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['seed_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Row ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['row_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plant ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['plant_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Tissue ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['tissue_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Culture ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['culture_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Microbe ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['microbe_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Plate ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['plate_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Well ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['well_id_error'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['DNA ID Errors'])
    writer.writerow(['well_id', 'experiment_name', 'well', 'inventory', 'tube_label', 'well_comments', 'source_row_id', 'source_seed_id', 'source_plant_id', 'source_tissue_id', 'source_culture_id', 'source_microbe_id', 'source_plate_id'])
    for key in results_dict['dna_id_error'].iterkeys():
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
    writer.writerow(['Isolate Entry Already Exists'])
    for key in results_dict['isolate_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['Location Entry Already Exists'])
    for key in results_dict['location_hash_exists'].iterkeys():
        writer.writerow(key)
    writer.writerow([''])
    writer.writerow(['ObsTracker Entry Already Exists'])
    for key in results_dict['obs_tracker_hash_exists'].iterkeys():
        writer.writerow(key)
    return response

def isolate_loader(results_dict):
    try:
        for key in results_dict['isolate_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_isolate = Isolate.objects.create(id=key[0], passport_id=key[1], location_id=key[2], disease_info_id=key[3], isolate_id=key[4], isolate_name=key[5], plant_organ=key[6], comments=key[7])
            except Exception as e:
                print("Isolate Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['passport_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_isolate = Passport.objects.create(id=key[0], passport_id=key[1], collecting_id=key[2], people_id=key[3], taxonomy_id=key[4])
            except Exception as e:
                print("Passport Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['collecting_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_isolate = Collecting.objects.create(id=key[0], user_id=key[1], collection_date=key[2], collection_method=key[3], comments=key[4])
            except Exception as e:
                print("Collecting Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['people_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_isolate = People.objects.create(id=key[0], first_name=key[1], last_name=key[2], organization=key[3], phone=key[4], email=key[5], comments=key[6])
            except Exception as e:
                print("People Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['taxonomy_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_isolate = Taxonomy.objects.create(id=key[0], genus=key[1], species=key[2], population=key[3], common_name=key[4], alias=key[5], race=key[6], subtaxa=key[7])
            except Exception as e:
                print("Taxonomy Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['location_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_isolate = Location.objects.create(id=key[0], locality_id=key[1], building_name=key[2], location_name=key[3], room=key[4], shelf=key[5], column=key[6], box_name=key[7], comments=key[8])
            except Exception as e:
                print("Location Error: %s %s" % (e.message, e.args))
                return False
        for key in results_dict['obs_tracker_new'].iterkeys():
            try:
                with transaction.atomic():
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

def measurement_loader(results_dict):
    try:
        for key in results_dict['measurement_new'].iterkeys():
            try:
                with transaction.atomic():
                    new_measurement = Measurement.objects.create(id=key[0], obs_tracker_id=key[1], measurement_parameter_id=key[2], user_id=key[3], time_of_measurement=key[4], value=key[5], comments=key[6])
            except Exception as e:
                print("Measurement Error: %s %s" % (e.message, e.args))
                return False
    except Exception as e:
        print("Error: %s %s" % (e.message, e.args))
        return False
    return True
