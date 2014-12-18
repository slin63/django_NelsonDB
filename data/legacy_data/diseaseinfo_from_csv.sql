load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_diseaseinfo_table.csv' 
into table legacy_legacy_diseaseinfo fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(trait, disease_name, abbreviation, topic, disease_info)
