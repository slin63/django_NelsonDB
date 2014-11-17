load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_plant_table.csv' 
into table legacy_legacy_plant fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(plant_id, row_id, plant_name, notes)