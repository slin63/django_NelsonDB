load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_diseaseinfo_table.csv' 
into table legacy_legacy_diseaseinfo fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(trait, disease_name, abbreviation, topic, disease_info)

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_experiment_table.csv' 
into table legacy_legacy_experiment fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(experiment_id, location, planting_date, tissue_collection, inoculations, inoculation_date1, inoculation_date2, inoculation_date3, pathogen_isolate, harvest_date, description, notes)

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_genotype_table.csv' 
into table legacy_legacy_genotype fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(genotype_plate_id, genotype_well_id, genotype_plate_name, well_A01, well_01A, plate_size, dna_id, sample_id, locus_name, marker_id, marker_name, marker_type, f_primer_id, r_primer_id, f2_primer_id, r2_primer_id, label_color, value1, value2, value3, value4, passive_ref, quality_value, call_type, call_name, genotype, brc_plate_num, brc_sample_num, genotype_file, run_date, genotype_person_id, notes)

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_isolate_table.csv' 
into table legacy_legacy_isolate fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(ID, isolate_id, isolate_name, scientific_name, other_sname, pathotype_race, mating_type, disease_common_name, collection_site, collection_date, plant_organ, collector, provider, glycerol_stock_n80c, mycelium_4c, cite, notes)

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_people_table.csv' 
into table legacy_legacy_people fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(person_id, person_name, first_name, last_name, title, address, phone, fax, email, URL, notes, peopleorg_id)

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_phenotype_table.csv' 
into table legacy_legacy_phenotype fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(phenotype_id, entity_id, entity_type, entity_name, experiment_id, trait_id, phenotype_value, phenotype_date, plate_id, phenotype_person_id, scoring_order, notes, changed, technical_rep, biological_rep, trait_id_buckler
)

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_plant_table.csv' 
into table legacy_legacy_plant fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(plant_id, row_id, plant_name, notes)

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_row_table_c1.1.csv' 
into table legacy_legacy_row fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(row_id, row_name, experiment_id_id, pedigree, line_num, source_seed_id, source_seed_name, range_num, plot, block, rep_num,
 kernel_num, pop, delay, purpose, notes, row_person)
 
load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_seed_table_c1.2.csv' 
into table legacy_legacy_seed fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(seed_id, plant_id_origin, row_id_origin, experiment_id_origin_id, plant_name, row_name, seed_name, cross_type, male_parent_id, male_parent_name, program_origin,
 seed_pedigree, line_num, seed_person_id, disease_info, notes, accession, lot)
 
load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_seedinv_table.csv' 
into table legacy_legacy_seed_inventory fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(ID, seed_id, seed_name, inventory_date, inventory_person, seed_person_id, location, notes, weight_g)