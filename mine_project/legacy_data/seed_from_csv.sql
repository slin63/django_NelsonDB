DROP TABLE IF EXISTS `legacy_legacy_seed`;

CREATE TABLE `legacy_legacy_seed` (
  `seed_id` varchar(100) DEFAULT NULL,
  `plant_id_origin` varchar(100) DEFAULT NULL,
  `row_id_origin` varchar(100) DEFAULT NULL,
  `experiment_id_origin` varchar(100) DEFAULT NULL,
  `plant_name` varchar(100) DEFAULT NULL,
  `row_name` varchar(100) DEFAULT NULL,
  `seed_name` varchar(100) DEFAULT NULL,
  `cross_type` varchar(100) DEFAULT NULL,
  `male_parent_id` varchar(100) DEFAULT NULL,
  `male_parent_name` varchar(100) DEFAULT NULL,
  `program_origin` varchar(100) DEFAULT NULL,
  `seed_pedigree` varchar(100) DEFAULT NULL,
  `line_num` varchar(100) DEFAULT NULL,
  `seed_person_id` varchar(100) DEFAULT NULL,
  `disease_info` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `accession` varchar(100) DEFAULT NULL,
  `lot` varchar(100) DEFAULT NULL
) ENGINE=InnoDB;

"""Could not add 10JH, 08SN, 12MY seeds due to Experiment FK"""
"""Could not add """


load data local infile 'C://Users/Nick/Documents/GitHub/mineproject/mine_project/legacy_data/nelson_lab_seed_table_c1.csv' 
into table legacy_legacy_seed fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(seed_id, plant_id_origin, row_id_origin, experiment_id_origin_id, plant_name, row_name, seed_name, cross_type, male_parent_id, male_parent_name, program_origin,
 seed_pedigree, line_num, seed_person_id, disease_info, notes, accession, lot)