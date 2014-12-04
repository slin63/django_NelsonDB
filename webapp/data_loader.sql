--
-- SET FOREIGN_KEY_CHECKS = 0;
--

--
-- IMPORTANT: Run the user_loader.py script BEFORE running this
--

-- /srv/nelsondb/app/webapp/data/csv_from_script/

-- Load Lab Data--


load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/locality.csv' 
into table lab_locality fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, city, state, country, zipcode);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/field.csv' 
into table lab_field fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, locality_id, field_name);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/experiment.csv' 
into table lab_experiment fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, user_id, field_id, name, start_date, purpose, comments);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/taxonomy.csv' 
into table lab_taxonomy fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, genus, species, population, common_name, alias, race, subtaxa);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/people.csv' 
into table lab_people fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, organization);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/obs_selector.csv' 
into table lab_obsselector fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, experiment_id);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/collecting.csv' 
into table lab_collecting fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, obs_selector_id, user_id, field_id, collection_date, collection_method, comments);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/passport.csv' 
into table lab_passport fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, collecting_id, people_id, taxonomy_id);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/stock.csv' 
into table lab_stock fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, passport_id, seed_id, seed_name, cross_type, pedigree, stock_status, stock_date, comments);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/disease_info.csv' 
into table lab_diseaseinfo fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, common_name);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/obs_row.csv' 
into table lab_obsrow fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, obs_selector_id, field_id, stock_id, row_id, row_name, range_num, plot, block, rep, kernel_num, planting_date, harvest_date, comments);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/obs_plant.csv' 
into table lab_obsplant fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, obs_selector_id, obs_row_id, plant_id, plant_num, comments);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/location.csv' 
into table lab_location fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, locality_id, building_name, location_name, box_name);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/isolate.csv' 
into table lab_isolate fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, passport_id, location_id, disease_info_id, isolate_id, isolate_name, plant_organ, comments);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/stock_packet.csv' 
into table lab_stockpacket fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, stock_id, location_id, weight, comments);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/measurement_parameter.csv' 
into table lab_measurementparameter fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, parameter, parameter_type, unit_of_measure, protocol, trait_id_buckler);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/csv_from_script/measurement.csv' 
into table lab_measurement fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(id, obs_selector_id, user_id, measurement_parameter_id, time_of_measurement, value, comments);

--
-- Load Legacy Data
--

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_diseaseinfo_table.csv' 
into table legacy_legacy_diseaseinfo fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(trait, disease_name, abbreviation, topic, disease_info);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_experiment_table.csv' 
into table legacy_legacy_experiment fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(experiment_id, location, planting_date, tissue_collection, inoculations, inoculation_date1, inoculation_date2, inoculation_date3, pathogen_isolate, harvest_date, description, notes);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_genotype_table.csv' 
into table legacy_legacy_genotype fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(genotype_plate_id, genotype_well_id, genotype_plate_name, well_A01, well_01A, plate_size, dna_id, sample_id, locus_name, marker_id, marker_name, marker_type, f_primer_id, r_primer_id, f2_primer_id, r2_primer_id, label_color, value1, value2, value3, value4, passive_ref, quality_value, call_type, call_name, genotype, brc_plate_num, brc_sample_num, genotype_file, run_date, genotype_person_id, notes);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_isolate_table.csv' 
into table legacy_legacy_isolate fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(ID, isolate_id, isolate_name, scientific_name, other_sname, pathotype_race, mating_type, disease_common_name, collection_site, collection_date, plant_organ, collector, provider, glycerol_stock_n80c, mycelium_4c, cite, notes);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_people_table.csv' 
into table legacy_legacy_people fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(person_id, person_name, first_name, last_name, title, address, phone, fax, email, URL, notes, peopleorg_id);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_phenotype_table.csv' 
into table legacy_legacy_phenotype fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(phenotype_id, entity_id, entity_type, entity_name, experiment_id, trait_id, phenotype_value, phenotype_date, plate_id, phenotype_person_id, scoring_order, notes, changed, technical_rep, biological_rep, trait_id_buckler);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_plant_table.csv' 
into table legacy_legacy_plant fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(plant_id, row_id, plant_name, notes);

load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_row_table_c1.1.csv' 
into table legacy_legacy_row fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(row_id, row_name, experiment_id_id, pedigree, line_num, source_seed_id, source_seed_name, range_num, plot, block, rep_num,
 kernel_num, pop, delay, purpose, notes, row_person);
 
load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_seed_table_c1.2.csv' 
into table legacy_legacy_seed fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(seed_id, plant_id_origin, row_id_origin, experiment_id_origin_id, plant_name, row_name, seed_name, cross_type, male_parent_id, male_parent_name, program_origin,
 seed_pedigree, line_num, seed_person_id, disease_info, notes, accession, lot);
 
load data local infile 'C://Users/Nicolas/Documents/GitHub/django_NelsonDB/webapp/data/legacy_data/nelson_lab_seedinv_table.csv' 
into table legacy_legacy_seed_inventory fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(ID, seed_id, seed_name, inventory_date, inventory_person, seed_person_id, location, notes, weight_g);

--
-- SET FOREIGN_KEY_CHECKS = 1;
--