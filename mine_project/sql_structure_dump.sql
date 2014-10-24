-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 24, 2014 at 11:22 AM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `nelson_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=115 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(75) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=73 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=39 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) COLLATE utf8_bin NOT NULL,
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_collecting`
--

CREATE TABLE IF NOT EXISTS `lab_collecting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obs_selector_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL,
  `collection_date` varchar(200) COLLATE utf8_bin NOT NULL,
  `collection_method` varchar(1000) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_collecting_59bde93e` (`obs_selector_id`),
  KEY `lab_collecting_6340c63c` (`user_id`),
  KEY `lab_collecting_aeee0ce4` (`field_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=703 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_diseaseinfo`
--

CREATE TABLE IF NOT EXISTS `lab_diseaseinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `common_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `abbrev` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=12 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_experiment`
--

CREATE TABLE IF NOT EXISTS `lab_experiment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL,
  `name` varchar(200) COLLATE utf8_bin NOT NULL,
  `start_date` varchar(200) COLLATE utf8_bin NOT NULL,
  `purpose` varchar(1000) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `lab_experiment_6340c63c` (`user_id`),
  KEY `lab_experiment_aeee0ce4` (`field_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=156 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_field`
--

CREATE TABLE IF NOT EXISTS `lab_field` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `locality_id` int(11) NOT NULL,
  `field_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `field_num` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_field_0f50bb3a` (`locality_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=40 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_isolate`
--

CREATE TABLE IF NOT EXISTS `lab_isolate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `passport_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `disease_info_id` int(11) NOT NULL,
  `isolate_id` varchar(200) COLLATE utf8_bin NOT NULL,
  `isolate_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `plant_organ` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_isolate_69d1a3d5` (`passport_id`),
  KEY `lab_isolate_afbb987d` (`location_id`),
  KEY `lab_isolate_1e93574a` (`disease_info_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=309 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_locality`
--

CREATE TABLE IF NOT EXISTS `lab_locality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(200) COLLATE utf8_bin NOT NULL,
  `state` varchar(200) COLLATE utf8_bin NOT NULL,
  `country` varchar(200) COLLATE utf8_bin NOT NULL,
  `zipcode` varchar(30) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=27 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_location`
--

CREATE TABLE IF NOT EXISTS `lab_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `locality_id` int(11) NOT NULL,
  `building_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `location_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `room` varchar(200) COLLATE utf8_bin NOT NULL,
  `shelf` varchar(200) COLLATE utf8_bin NOT NULL,
  `column` varchar(200) COLLATE utf8_bin NOT NULL,
  `box_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_location_0f50bb3a` (`locality_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=29 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_obsplant`
--

CREATE TABLE IF NOT EXISTS `lab_obsplant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obs_selector_id` int(11) NOT NULL,
  `obs_row_id` int(11) NOT NULL,
  `plant_id` varchar(200) COLLATE utf8_bin NOT NULL,
  `plant_num` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_obsplant_59bde93e` (`obs_selector_id`),
  KEY `lab_obsplant_6336f924` (`obs_row_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_obsrow`
--

CREATE TABLE IF NOT EXISTS `lab_obsrow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obs_selector_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL,
  `stock_id` int(11) NOT NULL,
  `row_id` varchar(200) COLLATE utf8_bin NOT NULL,
  `row_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `range_num` varchar(200) COLLATE utf8_bin NOT NULL,
  `plot` varchar(200) COLLATE utf8_bin NOT NULL,
  `block` varchar(200) COLLATE utf8_bin NOT NULL,
  `rep` varchar(200) COLLATE utf8_bin NOT NULL,
  `kernel_num` varchar(200) COLLATE utf8_bin NOT NULL,
  `planting_date` varchar(200) COLLATE utf8_bin NOT NULL,
  `harvest_date` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_obsrow_59bde93e` (`obs_selector_id`),
  KEY `lab_obsrow_aeee0ce4` (`field_id`),
  KEY `lab_obsrow_80945c99` (`stock_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=668 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_obsselector`
--

CREATE TABLE IF NOT EXISTS `lab_obsselector` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `experiment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_obsselector_3e8130cb` (`experiment_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=670 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_obstissue`
--

CREATE TABLE IF NOT EXISTS `lab_obstissue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obs_selector_id` int(11) NOT NULL,
  `obs_row_id` int(11) NOT NULL,
  `tissue_type` varchar(200) COLLATE utf8_bin NOT NULL,
  `plant` varchar(200) COLLATE utf8_bin NOT NULL,
  `well` varchar(200) COLLATE utf8_bin NOT NULL,
  `plate_id` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_obstissue_59bde93e` (`obs_selector_id`),
  KEY `lab_obstissue_6336f924` (`obs_row_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_passport`
--

CREATE TABLE IF NOT EXISTS `lab_passport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collecting_id` int(11) NOT NULL,
  `people_id` int(11) NOT NULL,
  `taxonomy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_passport_4fdd4318` (`collecting_id`),
  KEY `lab_passport_3cff102f` (`people_id`),
  KEY `lab_passport_1b516ba0` (`taxonomy_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=719 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_people`
--

CREATE TABLE IF NOT EXISTS `lab_people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `organization` varchar(200) COLLATE utf8_bin NOT NULL,
  `phone` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_publication`
--

CREATE TABLE IF NOT EXISTS `lab_publication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `publisher` varchar(200) COLLATE utf8_bin NOT NULL,
  `name_of_paper` varchar(200) COLLATE utf8_bin NOT NULL,
  `publish_date` date NOT NULL,
  `publication_info` varchar(200) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_publication_6340c63c` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_stock`
--

CREATE TABLE IF NOT EXISTS `lab_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `passport_id` int(11) NOT NULL,
  `seed_id` varchar(200) COLLATE utf8_bin NOT NULL,
  `seed_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `cross_type` varchar(200) COLLATE utf8_bin NOT NULL,
  `pedigree` varchar(200) COLLATE utf8_bin NOT NULL,
  `stock_status` varchar(200) COLLATE utf8_bin NOT NULL,
  `stock_date` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_stock_69d1a3d5` (`passport_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=669 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_stockpacket`
--

CREATE TABLE IF NOT EXISTS `lab_stockpacket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `weight` varchar(200) COLLATE utf8_bin NOT NULL,
  `num_seeds` varchar(200) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_stockpacket_80945c99` (`stock_id`),
  KEY `lab_stockpacket_afbb987d` (`location_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=364 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_taxonomy`
--

CREATE TABLE IF NOT EXISTS `lab_taxonomy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `genus` varchar(200) COLLATE utf8_bin NOT NULL,
  `species` varchar(200) COLLATE utf8_bin NOT NULL,
  `population` varchar(200) COLLATE utf8_bin NOT NULL,
  `common_name` varchar(200) COLLATE utf8_bin NOT NULL,
  `alias` varchar(200) COLLATE utf8_bin NOT NULL,
  `race` varchar(200) COLLATE utf8_bin NOT NULL,
  `subtaxa` varchar(200) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=30 ;

-- --------------------------------------------------------

--
-- Table structure for table `lab_userprofile`
--

CREATE TABLE IF NOT EXISTS `lab_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `website` varchar(250) COLLATE utf8_bin NOT NULL,
  `picture` varchar(100) COLLATE utf8_bin NOT NULL,
  `phone` varchar(30) COLLATE utf8_bin NOT NULL,
  `organization` varchar(200) COLLATE utf8_bin NOT NULL,
  `notes` varchar(1000) COLLATE utf8_bin NOT NULL,
  `job_title` varchar(200) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=73 ;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_diseaseinfo`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_diseaseinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trait` varchar(100) COLLATE utf8_bin NOT NULL,
  `disease_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `abbreviation` varchar(100) COLLATE utf8_bin NOT NULL,
  `topic` varchar(100) COLLATE utf8_bin NOT NULL,
  `disease_info` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=31 ;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_experiment`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_experiment` (
  `experiment_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `location` varchar(100) COLLATE utf8_bin NOT NULL,
  `planting_date` varchar(100) COLLATE utf8_bin NOT NULL,
  `tissue_collection` varchar(100) COLLATE utf8_bin NOT NULL,
  `inoculations` varchar(100) COLLATE utf8_bin NOT NULL,
  `inoculation_date1` varchar(100) COLLATE utf8_bin NOT NULL,
  `inoculation_date2` varchar(100) COLLATE utf8_bin NOT NULL,
  `inoculation_date3` varchar(100) COLLATE utf8_bin NOT NULL,
  `pathogen_isolate` varchar(100) COLLATE utf8_bin NOT NULL,
  `harvest_date` varchar(100) COLLATE utf8_bin NOT NULL,
  `description` varchar(1000) COLLATE utf8_bin NOT NULL,
  `notes` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`experiment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_genotype`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_genotype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `genotype_plate_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `genotype_well_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `genotype_plate_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `well_A01` varchar(100) COLLATE utf8_bin NOT NULL,
  `well_01A` varchar(100) COLLATE utf8_bin NOT NULL,
  `plate_size` varchar(100) COLLATE utf8_bin NOT NULL,
  `dna_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `sample_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `locus_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `marker_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `marker_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `marker_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `f_primer_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `r_primer_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `f2_primer_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `r2_primer_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `label_color` varchar(100) COLLATE utf8_bin NOT NULL,
  `value1` varchar(100) COLLATE utf8_bin NOT NULL,
  `value2` varchar(100) COLLATE utf8_bin NOT NULL,
  `value3` varchar(100) COLLATE utf8_bin NOT NULL,
  `value4` varchar(100) COLLATE utf8_bin NOT NULL,
  `passive_ref` varchar(100) COLLATE utf8_bin NOT NULL,
  `quality_value` varchar(100) COLLATE utf8_bin NOT NULL,
  `call_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `call_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `genotype` varchar(100) COLLATE utf8_bin NOT NULL,
  `brc_plate_num` varchar(100) COLLATE utf8_bin NOT NULL,
  `brc_sample_num` varchar(100) COLLATE utf8_bin NOT NULL,
  `genotype_file` varchar(100) COLLATE utf8_bin NOT NULL,
  `run_date` varchar(100) COLLATE utf8_bin NOT NULL,
  `genotype_person_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=25110 ;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_isolate`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_isolate` (
  `ID` varchar(100) COLLATE utf8_bin NOT NULL,
  `isolate_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `isolate_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `scientific_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `other_sname` varchar(100) COLLATE utf8_bin NOT NULL,
  `pathotype_race` varchar(100) COLLATE utf8_bin NOT NULL,
  `mating_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `disease_common_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `collection_site` varchar(100) COLLATE utf8_bin NOT NULL,
  `collection_date` varchar(100) COLLATE utf8_bin NOT NULL,
  `plant_organ` varchar(100) COLLATE utf8_bin NOT NULL,
  `collector` varchar(100) COLLATE utf8_bin NOT NULL,
  `provider` varchar(100) COLLATE utf8_bin NOT NULL,
  `glycerol_stock_n80c` varchar(100) COLLATE utf8_bin NOT NULL,
  `mycelium_4c` varchar(100) COLLATE utf8_bin NOT NULL,
  `cite` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_markers`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_markers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_placeholder` varchar(100) COLLATE utf8_bin NOT NULL,
  `marker_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `locus_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `chromosome` varchar(100) COLLATE utf8_bin NOT NULL,
  `maize_bin` varchar(100) COLLATE utf8_bin NOT NULL,
  `map_physical` varchar(100) COLLATE utf8_bin NOT NULL,
  `map_physical_refgen_v1` varchar(100) COLLATE utf8_bin NOT NULL,
  `map_physical_refgen_v2` varchar(100) COLLATE utf8_bin NOT NULL,
  `map_physical_refgen_v3` varchar(100) COLLATE utf8_bin NOT NULL,
  `bac` varchar(100) COLLATE utf8_bin NOT NULL,
  `nam_marker` varchar(100) COLLATE utf8_bin NOT NULL,
  `map_IBM2n_cM` varchar(100) COLLATE utf8_bin NOT NULL,
  `polymorphism_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `snp_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `sequence_f1` varchar(100) COLLATE utf8_bin NOT NULL,
  `sequence_f2` varchar(100) COLLATE utf8_bin NOT NULL,
  `sequence_r1` varchar(100) COLLATE utf8_bin NOT NULL,
  `sequence_r2` varchar(100) COLLATE utf8_bin NOT NULL,
  `primer_name_f1` varchar(100) COLLATE utf8_bin NOT NULL,
  `primer_name_f2` varchar(100) COLLATE utf8_bin NOT NULL,
  `primer_name_r1` varchar(100) COLLATE utf8_bin NOT NULL,
  `primer_name_r2` varchar(100) COLLATE utf8_bin NOT NULL,
  `primer_tail` varchar(100) COLLATE utf8_bin NOT NULL,
  `size_range` varchar(100) COLLATE utf8_bin NOT NULL,
  `Tm_min` varchar(100) COLLATE utf8_bin NOT NULL,
  `Tm_max` varchar(100) COLLATE utf8_bin NOT NULL,
  `chemestry` varchar(100) COLLATE utf8_bin NOT NULL,
  `primer_person` varchar(100) COLLATE utf8_bin NOT NULL,
  `order_date` varchar(100) COLLATE utf8_bin NOT NULL,
  `consense_sequence` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference_B73` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference_Mo17` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference_CML52` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference_DK888` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference_S11` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference_XL380` varchar(100) COLLATE utf8_bin NOT NULL,
  `reference_Tx303` varchar(100) COLLATE utf8_bin NOT NULL,
  `MaizeGDBLink` varchar(100) COLLATE utf8_bin NOT NULL,
  `MaizeSeqLink` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_people`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_people` (
  `person_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `person_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `title` varchar(100) COLLATE utf8_bin NOT NULL,
  `address` varchar(100) COLLATE utf8_bin NOT NULL,
  `phone` varchar(100) COLLATE utf8_bin NOT NULL,
  `fax` varchar(100) COLLATE utf8_bin NOT NULL,
  `email` varchar(100) COLLATE utf8_bin NOT NULL,
  `URL` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  `peopleorg_id` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_phenotype`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_phenotype` (
  `phenotype_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `entity_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `entity_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `entity_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `experiment_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `phenotype_value` varchar(100) COLLATE utf8_bin NOT NULL,
  `phenotype_date` varchar(100) COLLATE utf8_bin NOT NULL,
  `plate_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `phenotype_person_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `scoring_order` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  `changed` varchar(100) COLLATE utf8_bin NOT NULL,
  `technical_rep` varchar(100) COLLATE utf8_bin NOT NULL,
  `biological_rep` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_id_buckler` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`phenotype_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_plant`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_plant` (
  `plant_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `row_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `plant_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`plant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_row`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_row` (
  `row_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `row_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `experiment_id_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `pedigree` varchar(100) COLLATE utf8_bin NOT NULL,
  `line_num` varchar(100) COLLATE utf8_bin NOT NULL,
  `source_seed_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `source_seed_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `range_num` varchar(100) COLLATE utf8_bin NOT NULL,
  `plot` varchar(100) COLLATE utf8_bin NOT NULL,
  `block` varchar(100) COLLATE utf8_bin NOT NULL,
  `rep_num` varchar(100) COLLATE utf8_bin NOT NULL,
  `kernel_num` varchar(100) COLLATE utf8_bin NOT NULL,
  `pop` varchar(100) COLLATE utf8_bin NOT NULL,
  `delay` varchar(100) COLLATE utf8_bin NOT NULL,
  `purpose` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  `row_person` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`row_id`),
  KEY `legacy_legacy_row_908130ae` (`experiment_id_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_seed`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_seed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seed_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `plant_id_origin` varchar(100) COLLATE utf8_bin NOT NULL,
  `row_id_origin` varchar(100) COLLATE utf8_bin NOT NULL,
  `experiment_id_origin_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `plant_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `row_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `seed_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `cross_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `male_parent_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `male_parent_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `program_origin` varchar(100) COLLATE utf8_bin NOT NULL,
  `seed_pedigree` varchar(100) COLLATE utf8_bin NOT NULL,
  `line_num` varchar(100) COLLATE utf8_bin NOT NULL,
  `seed_person_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `disease_info` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  `accession` varchar(100) COLLATE utf8_bin NOT NULL,
  `lot` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `seed_id` (`seed_id`),
  KEY `legacy_legacy_seed_6583ac3e` (`experiment_id_origin_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=42846 ;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_seed_inventory`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_seed_inventory` (
  `ID` varchar(100) COLLATE utf8_bin NOT NULL,
  `seed_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `seed_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `inventory_date` varchar(100) COLLATE utf8_bin NOT NULL,
  `inventory_person` varchar(100) COLLATE utf8_bin NOT NULL,
  `seed_person_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `location` varchar(100) COLLATE utf8_bin NOT NULL,
  `notes` varchar(100) COLLATE utf8_bin NOT NULL,
  `weight_g` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_tissue`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_tissue` (
  `ID` varchar(100) COLLATE utf8_bin NOT NULL,
  `experiment_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `entity_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `entity_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `pedigree` varchar(100) COLLATE utf8_bin NOT NULL,
  `row_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `plant` varchar(100) COLLATE utf8_bin NOT NULL,
  `tissue_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `well` varchar(100) COLLATE utf8_bin NOT NULL,
  `tissue_plate_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `comments` varchar(1000) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `legacy_legacy_trait_info`
--

CREATE TABLE IF NOT EXISTS `legacy_legacy_trait_info` (
  `trait_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_grp` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_grp_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_name_id` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_basis` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_id_buckler` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_min` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_max` varchar(100) COLLATE utf8_bin NOT NULL,
  `data_type` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_howto` varchar(100) COLLATE utf8_bin NOT NULL,
  `trait_when` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`trait_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `lab_collecting`
--
ALTER TABLE `lab_collecting`
  ADD CONSTRAINT `user_id_refs_id_d3b81eae` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `field_id_refs_id_d6182808` FOREIGN KEY (`field_id`) REFERENCES `lab_field` (`id`),
  ADD CONSTRAINT `obs_selector_id_refs_id_1e1b8ab4` FOREIGN KEY (`obs_selector_id`) REFERENCES `lab_obsselector` (`id`);

--
-- Constraints for table `lab_experiment`
--
ALTER TABLE `lab_experiment`
  ADD CONSTRAINT `user_id_refs_id_ad023396` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `field_id_refs_id_b0352b61` FOREIGN KEY (`field_id`) REFERENCES `lab_field` (`id`);

--
-- Constraints for table `lab_field`
--
ALTER TABLE `lab_field`
  ADD CONSTRAINT `locality_id_refs_id_754060c8` FOREIGN KEY (`locality_id`) REFERENCES `lab_locality` (`id`);

--
-- Constraints for table `lab_isolate`
--
ALTER TABLE `lab_isolate`
  ADD CONSTRAINT `passport_id_refs_id_fa1ff11a` FOREIGN KEY (`passport_id`) REFERENCES `lab_passport` (`id`),
  ADD CONSTRAINT `disease_info_id_refs_id_5541a93a` FOREIGN KEY (`disease_info_id`) REFERENCES `lab_diseaseinfo` (`id`),
  ADD CONSTRAINT `location_id_refs_id_83518ed9` FOREIGN KEY (`location_id`) REFERENCES `lab_location` (`id`);

--
-- Constraints for table `lab_location`
--
ALTER TABLE `lab_location`
  ADD CONSTRAINT `locality_id_refs_id_598c62cf` FOREIGN KEY (`locality_id`) REFERENCES `lab_locality` (`id`);

--
-- Constraints for table `lab_obsplant`
--
ALTER TABLE `lab_obsplant`
  ADD CONSTRAINT `obs_row_id_refs_id_4bccc216` FOREIGN KEY (`obs_row_id`) REFERENCES `lab_obsrow` (`id`),
  ADD CONSTRAINT `obs_selector_id_refs_id_70b01467` FOREIGN KEY (`obs_selector_id`) REFERENCES `lab_obsselector` (`id`);

--
-- Constraints for table `lab_obsrow`
--
ALTER TABLE `lab_obsrow`
  ADD CONSTRAINT `field_id_refs_id_8e287639` FOREIGN KEY (`field_id`) REFERENCES `lab_field` (`id`),
  ADD CONSTRAINT `obs_selector_id_refs_id_dd6cf36f` FOREIGN KEY (`obs_selector_id`) REFERENCES `lab_obsselector` (`id`),
  ADD CONSTRAINT `stock_id_refs_id_257a2602` FOREIGN KEY (`stock_id`) REFERENCES `lab_stock` (`id`);

--
-- Constraints for table `lab_obsselector`
--
ALTER TABLE `lab_obsselector`
  ADD CONSTRAINT `experiment_id_refs_id_4ae581aa` FOREIGN KEY (`experiment_id`) REFERENCES `lab_experiment` (`id`);

--
-- Constraints for table `lab_obstissue`
--
ALTER TABLE `lab_obstissue`
  ADD CONSTRAINT `obs_row_id_refs_id_9e8e07b3` FOREIGN KEY (`obs_row_id`) REFERENCES `lab_obsrow` (`id`),
  ADD CONSTRAINT `obs_selector_id_refs_id_ab4df3eb` FOREIGN KEY (`obs_selector_id`) REFERENCES `lab_obsselector` (`id`);

--
-- Constraints for table `lab_passport`
--
ALTER TABLE `lab_passport`
  ADD CONSTRAINT `taxonomy_id_refs_id_cf0e987b` FOREIGN KEY (`taxonomy_id`) REFERENCES `lab_taxonomy` (`id`),
  ADD CONSTRAINT `collecting_id_refs_id_9cafd6c6` FOREIGN KEY (`collecting_id`) REFERENCES `lab_collecting` (`id`),
  ADD CONSTRAINT `people_id_refs_id_48339a9e` FOREIGN KEY (`people_id`) REFERENCES `lab_people` (`id`);

--
-- Constraints for table `lab_publication`
--
ALTER TABLE `lab_publication`
  ADD CONSTRAINT `user_id_refs_id_217a1b50` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `lab_stock`
--
ALTER TABLE `lab_stock`
  ADD CONSTRAINT `passport_id_refs_id_2124c94d` FOREIGN KEY (`passport_id`) REFERENCES `lab_passport` (`id`);

--
-- Constraints for table `lab_stockpacket`
--
ALTER TABLE `lab_stockpacket`
  ADD CONSTRAINT `stock_id_refs_id_358085eb` FOREIGN KEY (`stock_id`) REFERENCES `lab_stock` (`id`),
  ADD CONSTRAINT `location_id_refs_id_744dc085` FOREIGN KEY (`location_id`) REFERENCES `lab_location` (`id`);

--
-- Constraints for table `lab_userprofile`
--
ALTER TABLE `lab_userprofile`
  ADD CONSTRAINT `user_id_refs_id_bc0fef46` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `legacy_legacy_row`
--
ALTER TABLE `legacy_legacy_row`
  ADD CONSTRAINT `experiment_id_id_refs_experiment_id_24ea129c` FOREIGN KEY (`experiment_id_id`) REFERENCES `legacy_legacy_experiment` (`experiment_id`);

--
-- Constraints for table `legacy_legacy_seed`
--
ALTER TABLE `legacy_legacy_seed`
  ADD CONSTRAINT `experiment_id_origin_id_refs_experiment_id_9f87a8ef` FOREIGN KEY (`experiment_id_origin_id`) REFERENCES `legacy_legacy_experiment` (`experiment_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
