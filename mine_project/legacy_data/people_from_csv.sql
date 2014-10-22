DROP TABLE IF EXISTS `legacy_legacy_people`;

CREATE TABLE `legacy_legacy_people` (
  `person_id` varchar(100) DEFAULT NULL,
  `person_name` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `fax` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `URL` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  `peopleorg_id` varchar(100) DEFAULT NULL
) ENGINE=InnoDB;

load data local infile 'C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/legacy_data/nelson_lab_people_table.csv' 
into table legacy_legacy_people fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(person_id, person_name, first_name, last_name, title, address, phone, fax, email, URL, notes, peopleorg_id)