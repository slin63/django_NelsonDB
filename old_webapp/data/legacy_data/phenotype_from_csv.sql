load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_phenotype_table.csv' 
into table legacy_legacy_phenotype fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(phenotype_id, entity_id, entity_type, entity_name, experiment_id, trait_id, phenotype_value, phenotype_date, plate_id, phenotype_person_id, scoring_order, notes, changed, technical_rep, biological_rep, trait_id_buckler
)