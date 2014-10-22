load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_genotype_table.csv' 
into table legacy_legacy_genotype fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(genotype_plate_id, genotype_well_id, genotype_plate_name, well_A01, well_01A, plate_size, dna_id, sample_id, locus_name, marker_id, marker_name, marker_type, f_primer_id, r_primer_id, f2_primer_id, r2_primer_id, label_color, value1, value2, value3, value4, passive_ref, quality_value, call_type, call_name, genotype, brc_plate_num, brc_sample_num, genotype_file, run_date, genotype_person_id, notes)