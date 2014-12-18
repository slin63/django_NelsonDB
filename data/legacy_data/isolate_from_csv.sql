load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_isolate_table.csv' 
into table legacy_legacy_isolate fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(ID, isolate_id, isolate_name, scientific_name, other_sname, pathotype_race, mating_type, disease_common_name, collection_site, collection_date, plant_organ, collector, provider, glycerol_stock_n80c, mycelium_4c, cite, notes)
