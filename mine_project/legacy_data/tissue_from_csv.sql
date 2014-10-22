load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_tissue_table.csv'
into table legacy_legacy_tissue fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(ID, experiment_id, entity_id, entity_name, pedigree, row_name, plant, tissue_type, well, tissue_plate_id, comments)