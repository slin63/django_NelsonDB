
DROP TABLE IF EXISTS `legacy_legacy_seed_inventory`;

CREATE TABLE `legacy_legacy_seed_inventory` (
  `ID` varchar(100) DEFAULT NULL,
  `seed_id` varchar(100) DEFAULT NULL,
  `seed_name` varchar(100) DEFAULT NULL,
  `inventory_date` varchar(100) DEFAULT NULL,
  `inventory_person` varchar(100) DEFAULT NULL,
  `seed_person_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `weight_g` varchar(100) DEFAULT NULL
) ENGINE=InnoDB;

load data local infile 'C://Users/Nick/Documents/GitHub/mineproject/mine_project/legacy_data/nelson_lab_seedinv_table.csv' 
into table legacy_legacy_seed_inventory fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(ID, seed_id, seed_name, inventory_date, inventory_person, seed_person_id, location, notes, weight_g)
