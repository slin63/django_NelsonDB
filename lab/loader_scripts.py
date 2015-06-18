
import csv
from collections import OrderedDict
import time
import loader_db_mirror
from django.http import HttpResponseRedirect, HttpResponse
from lab.models import UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, People, Collecting, Field, Locality, Location, ObsRow, ObsPlant, ObsSample, ObsEnv, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, ObsMicrobe, ObsExtract, ObsTracker, ObsTrackerSource, Isolate, DiseaseInfo, Measurement, MeasurementParameter, Treatment, UploadQueue, Medium, Citation, Publication, MaizeSample, Separation, GlycerolStock

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

    user_hash_table = loader_db_mirror.user_hash_mirror()
    stock_hash_table = loader_db_mirror.stock_hash_mirror()
    stock_id = loader_db_mirror.stock_id_mirror()
    obs_tracker_row_id_table = loader_db_mirror.obs_tracker_row_id_mirror()
    obs_tracker_plant_id_table = loader_db_mirror.obs_tracker_plant_id_mirror()
    obs_tracker_seed_id_table = loader_db_mirror.obs_tracker_seed_id_mirror()
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
            if row_id in obs_tracker_row_id_table:
                obs_row_id = obs_tracker_row_id_table[row_id][15]
            elif row_id_fix in obs_tracker_row_id_table:
                obs_row_id = obs_tracker_row_id_table[row_id_fix][15]
            else:
                row_id_error[(seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, inoculated, stock_comments, genus, species, population, row_id, field_name, plant_id, collection_username, collection_date, collection_method, collection_comments, organization, first_name, last_name, phone, email, source_comments)] = error_count
                error_count = error_count + 1
                obs_row_id = 1
        else:
            obs_row_id = 1

        if plant_id != '':
            plant_id_fix = plant_id + '\r'
            if plant_id in obs_tracker_plant_id_table:
                obs_plant_id = obs_tracker_plant_id_table[plant_id][13]
            elif plant_id_fix in obs_tracker_plant_id_table:
                obs_plant_id = obs_tracker_plant_id_table[plant_id_fix][13]
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

        obs_tracker_stock_hash_fix = 'stock' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(temp_stock_id) + str(user_hash_table[user.username]) + '\r'
        obs_tracker_stock_hash = 'stock' + str(experiment_name_table[experiment_name][0]) + str(field_id) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(1) + str(obs_plant_id) + str(1) + str(obs_row_id) + str(1) + str(1) + str(1) + str(temp_stock_id) + str(user_hash_table[user.username])
        if obs_tracker_stock_hash not in obs_tracker_hash_table and obs_tracker_stock_hash_fix not in obs_tracker_hash_table:
            obs_tracker_hash_table[obs_tracker_stock_hash] = obs_tracker_id
            obs_tracker_new[(obs_tracker_id, 'stock', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, 1, 1, temp_stock_id, user_hash_table[user.username])] = obs_tracker_id
            obs_tracker_id = obs_tracker_id + 1
        else:
            obs_tracker_hash_exists[('stock', experiment_name_table[experiment_name][0], field_id, 1, 1, 1, 1, 1, 1, 1, 1, 1, obs_plant_id, 1, obs_row_id, 1, 1, 1, temp_stock_id, user_hash_table[user.username])] = obs_tracker_id

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
    return True
