DROP TABLE IF EXISTS `legacy_legacy_experiment`;

CREATE TABLE `legacy_legacy_experiment` (
  `experiment_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `planting_date` varchar(100) DEFAULT NULL,
  `tissue_collection` varchar(100) DEFAULT NULL,
  `inoculations` varchar(100) DEFAULT NULL,
  `inoculation_date1` varchar(100) DEFAULT NULL,
  `inoculation_date2` varchar(100) DEFAULT NULL,
  `inoculation_date3` varchar(100) DEFAULT NULL,
  `pathogen_isolate` varchar(100) DEFAULT NULL,
  `harvest_date` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL
) ENGINE=InnoDB;

load data local infile 'C://Users/Nick/Documents/GitHub/mineproject/mine_project/legacy_data/nelson_lab_experiment_table.csv' 
into table legacy_legacy_experiment fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(experiment_id, location, planting_date, tissue_collection, inoculations, inoculation_date1, inoculation_date2, inoculation_date3, pathogen_isolate, harvest_date, description, notes)