DROP TABLE IF EXISTS `legacy_legacy_row`;

CREATE TABLE `legacy_legacy_row` (
  `row_id` varchar(100) DEFAULT NULL,
  `row_name` varchar(100) DEFAULT NULL,
  `experiment_id_id` varchar(100) DEFAULT NULL,
  `pedigree` varchar(100) DEFAULT NULL,
  `line_num` varchar(100) DEFAULT NULL,
  `source_seed_id` varchar(100) DEFAULT NULL,
  `source_seed_name` varchar(100) DEFAULT NULL,
  `range_num` varchar(100) DEFAULT NULL,
  `plot` varchar(100) DEFAULT NULL,
  `block` varchar(100) DEFAULT NULL,
  `rep_num` varchar(100) DEFAULT NULL,
  `kernel_num` varchar(100) DEFAULT NULL,
  `pop` varchar(100) DEFAULT NULL,
  `delay` varchar(100) DEFAULT NULL,
  `purpose` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `row_personSeed` varchar(100) DEFAULT NULL
) ENGINE=InnoDB;

"""Could not add 08SN, 09NC, 09PM, 09PX, 10GT, 12MY, 10JH """

load data local infile 'C://Users/Nick/Documents/GitHub/mineproject/mine_project/legacy_data/nelson_lab_row_table_c1.csv' 
into table legacy_legacy_row fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(row_id, row_name, experiment_id_id, pedigree, line_num, source_seed_id, source_seed_name, range_num, plot, block, rep_num,
 kernel_num, pop, delay, purpose, notes, row_person)