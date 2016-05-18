-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 09, 2015 at 06:02 PM
-- Server version: 5.6.21
-- PHP Version: 5.5.19

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `db_test`
--

--
-- Truncate table before insert `auth_user`
--

TRUNCATE TABLE `auth_user`;
--
-- Dumping data for table `auth_user`
-- !! Do not use null '0000-00-00 00:00:00' in datetime fields! Throws error if accessed !!

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, '', '1990-12-25 00:00:00', 0, 'unknown_person', 'Unknown', 'Person', '', 0, 0, '1990-12-25 00:00:00'),
(2, 'pbkdf2_sha256$12000$Rjx9Y2539UK6$LPk6T47VPLFgNeaMYnwPljlB96Jqvd3QsCelWOkVHrA=', '2015-10-09 15:29:42', 1, 'nick_morales', 'Nicolas', 'Morales', 'nm529@cornell.edu', 1, 1, '2015-10-09 15:27:50');

--
-- Truncate table before insert `lab_citation`
--

TRUNCATE TABLE `lab_citation`;
--
-- Dumping data for table `lab_citation`
--

INSERT INTO `lab_citation` (`id`, `citation_type`, `title`, `url`, `pubmed_id`, `comments`) VALUES
(1, 'No Citation', 'No Citation', 'No Citation', 'No Citation', '');

--
-- Truncate table before insert `lab_collecting`
--

TRUNCATE TABLE `lab_collecting`;
--
-- Dumping data for table `lab_collecting`
--

INSERT INTO `lab_collecting` (`id`, `collection_date`, `collection_method`, `comments`, `user_id`) VALUES
(1, 'No Collection', 'No Collection', 'No Collection', 1);

--
-- Truncate table before insert `lab_diseaseinfo`
--

TRUNCATE TABLE `lab_diseaseinfo`;
--
-- Dumping data for table `lab_diseaseinfo`
--

INSERT INTO `lab_diseaseinfo` (`id`, `common_name`, `abbrev`, `comments`) VALUES
(1, 'No Disease', '', '');

--
-- Truncate table before insert `lab_experiment`
--

TRUNCATE TABLE `lab_experiment`;
--
-- Dumping data for table `lab_experiment`
--

INSERT INTO `lab_experiment` (`id`, `name`, `start_date`, `purpose`, `comments`, `field_id`, `user_id`) VALUES
(1, 'No_Experiment', '', '', '', 1, 1);

--
-- Truncate table before insert `lab_field`
--

TRUNCATE TABLE `lab_field`;
--
-- Dumping data for table `lab_field`
--

INSERT INTO `lab_field` (`id`, `field_name`, `field_num`, `comments`, `locality_id`) VALUES
(1, 'No Field', '', '', 1);

--
-- Truncate table before insert `lab_filedump`
--

TRUNCATE TABLE `lab_filedump`;
--
-- Truncate table before insert `lab_isolate`
--

TRUNCATE TABLE `lab_isolate`;
--
-- Dumping data for table `lab_isolate`
--

INSERT INTO `lab_isolate` (`id`, `isolate_id`, `isolatestock_id`, `location_id`, `stock_date`, `extract_color`, `organism`, `comments`, `locality_id`, `user_id`) VALUES
(1, 'No Isolate', 1, 1, 'No Isolate', '', '', '', 1, 1);

--
-- Truncate table before insert `lab_gwasexperimentset`
--

TRUNCATE TABLE `lab_gwasexperimentset`;
--
-- Dumping data for table `lab_gwasexperimentset`
--

INSERT INTO `lab_gwasexperimentset` (`id`, `experiment_id`, `gwas_results_id`) VALUES
(1, 1, 1);

--
-- Truncate table before insert `lab_gwasresults`
--

TRUNCATE TABLE `lab_gwasresults`;
--
-- Dumping data for table `lab_gwasresults`
--

INSERT INTO `lab_gwasresults` (`id`, `p_value`, `strand`, `relationship_to_hit`, `interpro_domain`, `distance_from_gene`, `f_value`, `perm_p_value`, `r2`, `alleles`, `bpp`, `effect`, `cM`, `comments`, `parameter_id`) VALUES
(1, 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', 'No GWAS Result', '', 1);

--
-- Truncate table before insert `lab_isolate`
--

TRUNCATE TABLE `lab_isolatestock`;
--
-- Dumping data for table `lab_isolate`
--

INSERT INTO `lab_isolatestock` (`id`, `isolatestock_id`, `isolatestock_name`, `plant_organ`, `comments`, `disease_info_id`, `locality_id`, `passport_id`) VALUES
(1, 'No Isolate', 'No Isolate', 'No Isolate', '', 1, 1, 1);

--
-- Truncate table before insert `lab_locality`
--

TRUNCATE TABLE `lab_locality`;
--
-- Dumping data for table `lab_locality`
--

INSERT INTO `lab_locality` (`id`, `city`, `state`, `country`, `zipcode`) VALUES
(1, 'No Locality', 'No Locality', 'No Locality', 'No Locality');

--
-- Truncate table before insert `lab_location`
--

TRUNCATE TABLE `lab_location`;
--
-- Dumping data for table `lab_location`
--

INSERT INTO `lab_location` (`id`, `building_name`, `location_name`, `room`, `shelf`, `column`, `box_name`, `comments`, `locality_id`) VALUES
(1, 'No Location', 'No Location', 'No Location', 'No Location', 'No Location', 'No Location', '', 1);

--
-- Truncate table before insert `lab_maizesample`
--

TRUNCATE TABLE `lab_maizesample`;
--
-- Dumping data for table `lab_maizesample`
--

INSERT INTO `lab_maizesample` (`id`, `maize_id`, `county`, `sub_location`, `village`, `weight`, `harvest_date`, `storage_months`, `storage_conditions`, `maize_variety`, `seed_source`, `moisture_content`, `source_type`, `appearance`, `gps_latitude`, `gps_longitude`, `gps_altitude`, `gps_accuracy`, `photo`) VALUES
(1, 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', 'No Maize Sample', '');

--
-- Truncate table before insert `lab_mapfeature`
--

TRUNCATE TABLE `lab_mapfeature`;
--
-- Dumping data for table `lab_mapfeature`
--

INSERT INTO `lab_mapfeature` (`id`, `map_feature_id`, `chromosome`, `genetic_bin`, `physical_map`, `genetic_position`, `physical_position`, `comments`) VALUES
(1, 'No Map Feature', 'No Map Feature', 'No Map Feature', 'No Map Feature', 'No Map Feature', 'No Map Feature', '');

--
-- Truncate table before insert `lab_mapfeatureannotation`
--

TRUNCATE TABLE `lab_mapfeatureannotation`;
--
-- Dumping data for table `lab_mapfeatureannotation`
--

INSERT INTO `lab_mapfeatureannotation` (`id`, `annotation_type`, `annotation_value`, `map_feature_id`) VALUES
(1, 'No Annotation', 'No Annotation', 1);

--
-- Truncate table before insert `lab_mapfeatureexpression`
--

TRUNCATE TABLE `lab_mapfeatureexpression`;
--
-- Dumping data for table `lab_mapfeatureexpression`
--

INSERT INTO `lab_mapfeatureexpression` (`id`, `value`, `comments`, `map_feature_interval_id`, `parameter_id`) VALUES
(1, 'No Expression', '', 1, 1);

--
-- Truncate table before insert `lab_mapfeatureinterval`
--

TRUNCATE TABLE `lab_mapfeatureinterval`;
--
-- Dumping data for table `lab_mapfeatureinterval`
--

INSERT INTO `lab_mapfeatureinterval` (`id`, `interval_type`, `interval_name`, `comments`, `map_feature_end_id`, `map_feature_start_id`) VALUES
(1, 'No Map Feature Interval', 'No Map Feature Interval', '', 1, 1);

--
-- Truncate table before insert `lab_marker`
--

TRUNCATE TABLE `lab_marker`;
--
-- Dumping data for table `lab_marker`
--

INSERT INTO `lab_marker` (`id`, `marker_id`, `length`, `bac`, `nam_marker`, `poly_type`, `ref_seq`, `comments`, `strand`, `allele`, `map_feature_interval_id`, `marker_map_feature_id`, `primer_f_id`, `primer_r_id`) VALUES
(1, 'No Marker', 'No Marker', 'No Marker', 'No Marker', 'No Marker', '', '', '', '', 1, 1, 1, 1);

--
-- Truncate table before insert `lab_measurement`
--

TRUNCATE TABLE `lab_measurement`;
--
-- Dumping data for table `lab_measurement`
--

INSERT INTO `lab_measurement` (`id`, `time_of_measurement`, `value`, `comments`, `measurement_parameter_id`, `obs_tracker_id`, `user_id`, `experiment_id`) VALUES
(1, 'No Measurement', 'No Measurement', '', 1, 1, 1, 1);

--
-- Truncate table before insert `lab_measurementparameter`
--

TRUNCATE TABLE `lab_measurementparameter`;
--
-- Dumping data for table `lab_measurementparameter`
--

INSERT INTO `lab_measurementparameter` (`id`, `parameter`, `parameter_type`, `unit_of_measure`, `protocol`, `trait_id_buckler`, `description`, `marker_id`) VALUES
(1, 'No Parameter', 'No Parameter', 'No Parameter', 'No Parameter', 'No Parameter', 'No Parameter', 1);

--
-- Truncate table before insert `lab_medium`
--

TRUNCATE TABLE `lab_medium`;
--
-- Dumping data for table `lab_medium`
--

INSERT INTO `lab_medium` (`id`, `media_name`, `media_type`, `media_description`, `media_preparation`, `comments`, `citation_id`) VALUES
(1, 'No Medium', 'No Medium', 'No Medium', 'No Medium', '', 1);

--
-- Truncate table before insert `lab_obsculture`
--

TRUNCATE TABLE `lab_obsculture`;
--
-- Dumping data for table `lab_obsculture`
--

INSERT INTO `lab_obsculture` (`id`, `culture_id`, `culture_name`, `microbe_type`, `plating_cycle`, `dilution`, `image_filename`, `comments`, `num_colonies`, `num_microbes`, `medium_id`) VALUES
(1, 'No Culture', 'No Culture', 'No Culture', '', '', '', '', '', '', 1);

--
-- Truncate table before insert `lab_obsdna`
--

TRUNCATE TABLE `lab_obsdna`;
--
-- Dumping data for table `lab_obsdna`
--

INSERT INTO `lab_obsdna` (`id`, `dna_id`, `extraction_method`, `date`, `tube_id`, `tube_type`, `comments`) VALUES
(1, 'No DNA', 'No DNA', 'No DNA', 'No DNA', 'No DNA', '');

--
-- Truncate table before insert `lab_obsenv`
--

TRUNCATE TABLE `lab_obsenv`;
--
-- Dumping data for table `lab_obsenv`
--

INSERT INTO `lab_obsenv` (`id`, `environment_id`, `longitude`, `latitude`, `comments`) VALUES
(1, 'No Environment', 'No Environment', 'No Environment', '');

--
-- Truncate table before insert `lab_obsextract`
--

TRUNCATE TABLE `lab_obsextract`;
--
-- Dumping data for table `lab_obsextract`
--

INSERT INTO `lab_obsextract` (`id`, `extract_id`, `weight`, `rep`, `grind_method`, `solvent`, `comments`) VALUES
(1, 'No Extract', 'No Extract', 'No Extract', 'No Extract', 'No Extract', '');

--
-- Truncate table before insert `lab_obsmicrobe`
--

TRUNCATE TABLE `lab_obsmicrobe`;
--
-- Dumping data for table `lab_obsmicrobe`
--

INSERT INTO `lab_obsmicrobe` (`id`, `microbe_id`, `microbe_type`, `comments`) VALUES
(1, 'No Microbe', 'No Microbe', '');

--
-- Truncate table before insert `lab_obsplant`
--

TRUNCATE TABLE `lab_obsplant`;
--
-- Dumping data for table `lab_obsplant`
--

INSERT INTO `lab_obsplant` (`id`, `plant_id`, `plant_num`, `comments`) VALUES
(1, 'No Plant', 'No Plant', '');

--
-- Truncate table before insert `lab_obsplate`
--

TRUNCATE TABLE `lab_obsplate`;
--
-- Dumping data for table `lab_obsplate`
--

INSERT INTO `lab_obsplate` (`id`, `plate_id`, `plate_name`, `date`, `contents`, `rep`, `plate_type`, `plate_status`, `comments`) VALUES
(1, 'No Plate', 'No Plate', 'No Plate', 'No Plate', 'No Plate', 'No Plate', 'No Plate', '');

--
-- Truncate table before insert `lab_obsplot`
--

TRUNCATE TABLE `lab_obsplot`;
--
-- Dumping data for table `lab_obsplot`
--

INSERT INTO `lab_obsplot` (`id`, `row_id`, `row_name`, `range_num`, `plot`, `block`, `rep`, `kernel_num`, `planting_date`, `harvest_date`, `comments`) VALUES
(1, 'No Plot', 'No Plot', 'No Plot', 'No Plot', 'No Plot', 'No Plot', 'No Plot', 'No Plot', 'No Plot', '');

--
-- Truncate table before insert `lab_obssample`
--

TRUNCATE TABLE `lab_obssample`;
--
-- Dumping data for table `lab_obssample`
--

INSERT INTO `lab_obssample` (`id`, `sample_id`, `sample_type`, `sample_name`, `weight`, `volume`, `density`, `kernel_num`, `photo`, `comments`) VALUES
(1, 'No Sample', 'No Sample', 'No Sample', 'No Sample', 'No Sample', 'No Sample', 'No Sample', 'No Sample', '');

--
-- Truncate table before insert `lab_obstissue`
--

TRUNCATE TABLE `lab_obstissue`;
--
-- Dumping data for table `lab_obstissue`
--

INSERT INTO `lab_obstissue` (`id`, `tissue_id`, `tissue_type`, `tissue_name`, `date_ground`, `comments`) VALUES
(1, 'No Tissue', 'No Tissue', 'No Tissue', 'No Tissue', '');

--
-- Truncate table before insert `lab_obstracker`
--

TRUNCATE TABLE `lab_obstracker`;
--
-- Dumping data for table `lab_obstracker`
--

INSERT INTO `lab_obstracker` (`id`, `obs_entity_type`, `experiment_id`, `field_id`, `isolate_id`, `isolatestock_id`, `location_id`, `maize_sample_id`, `obs_culture_id`, `obs_dna_id`, `obs_env_id`, `obs_extract_id`, `obs_microbe_id`, `obs_plant_id`, `obs_plate_id`, `obs_plot_id`, `obs_sample_id`, `obs_tissue_id`, `obs_well_id`, `stock_id`, `user_id`) VALUES
(1, 'No Type', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

--
-- Truncate table before insert `lab_obstrackersource`
--

TRUNCATE TABLE `lab_obstrackersource`;
--
-- Dumping data for table `lab_obstrackersource`
--

INSERT INTO `lab_obstrackersource` (`id`, `source_obs_id`, `target_obs_id`) VALUES
(1, 1, 1);

--
-- Truncate table before insert `lab_obswell`
--

TRUNCATE TABLE `lab_obswell`;
--
-- Dumping data for table `lab_obswell`
--

INSERT INTO `lab_obswell` (`id`, `well_id`, `well`, `well_inventory`, `tube_label`, `comments`) VALUES
(1, 'No Well', 'No Well', 'No Well', 'No Well', '');

--
-- Truncate table before insert `lab_passport`
--

TRUNCATE TABLE `lab_passport`;
--
-- Dumping data for table `lab_passport`
--

INSERT INTO `lab_passport` (`id`, `collecting_id`, `people_id`, `taxonomy_id`) VALUES
(1, 1, 1, 1);

--
-- Truncate table before insert `lab_people`
--

TRUNCATE TABLE `lab_people`;
--
-- Dumping data for table `lab_people`
--

INSERT INTO `lab_people` (`id`, `first_name`, `last_name`, `organization`, `phone`, `email`, `comments`) VALUES
(1, 'No Source', 'No Source', 'No Source', 'No Source', 'No Source', '');

--
-- Truncate table before insert `lab_primer`
--

TRUNCATE TABLE `lab_primer`;
--
-- Dumping data for table `lab_primer`
--

INSERT INTO `lab_primer` (`id`, `primer_id`, `primer_name`, `primer_tail`, `size_range`, `temp_min`, `temp_max`, `order_date`, `comments`) VALUES
(1, 'No Primer', 'No Primer', '', '', '', '', '', '');

--
-- Truncate table before insert `lab_publication`
--

TRUNCATE TABLE `lab_publication`;
--
-- Dumping data for table `lab_publication`
--

INSERT INTO `lab_publication` (`id`, `publisher`, `name_of_paper`, `publish_date`, `publication_info`, `user_id`) VALUES
(1, 'No Publication', 'No Publication', '0000-00-00', '', 1);

--
-- Truncate table before insert `lab_qtl`
--

TRUNCATE TABLE `lab_qtl`;
--
-- Dumping data for table `lab_qtl`
--

INSERT INTO `lab_qtl` (`id`, `comments`, `map_feature_interval_id`, `parameter_id`) VALUES
(1, 'No QTL', 1, 1);

--
-- Truncate table before insert `lab_separation`
--

TRUNCATE TABLE `lab_separation`;
--
-- Dumping data for table `lab_separation`
--

INSERT INTO `lab_separation` (`id`, `separation_type`, `apparatus`, `SG`, `light_weight`, `intermediate_weight`, `heavy_weight`, `light_percent`, `intermediate_percent`, `heavy_percent`, `operating_factor`, `comments`, `obs_sample_id`) VALUES
(1, 'No Separation', 'No Separation', 'No Separation', 'No Separation', 'No Separation', 'No Separation', 'No Separation', 'No Separation', 'No Separation', 'No Separation', '', 1);

--
-- Truncate table before insert `lab_stock`
--

TRUNCATE TABLE `lab_stock`;
--
-- Dumping data for table `lab_stock`
--

INSERT INTO `lab_stock` (`id`, `seed_id`, `seed_name`, `cross_type`, `pedigree`, `stock_status`, `stock_date`, `inoculated`, `comments`, `passport_id`) VALUES
(1, 'No Stock', 'No Stock', 'No Stock', 'No Stock', 'No Stock', '', 0, '', 1);

--
-- Truncate table before insert `lab_stockpacket`
--

TRUNCATE TABLE `lab_stockpacket`;
--
-- Dumping data for table `lab_stockpacket`
--

INSERT INTO `lab_stockpacket` (`id`, `weight`, `num_seeds`, `comments`, `location_id`, `stock_id`) VALUES
(1, 'No Stock Packet', 'No Stock Packet', '', 1, 1);

--
-- Truncate table before insert `lab_taxonomy`
--

TRUNCATE TABLE `lab_taxonomy`;
--
-- Dumping data for table `lab_taxonomy`
--

INSERT INTO `lab_taxonomy` (`id`, `binomial`, `population`, `common_name`, `alias`, `race`, `subtaxa`) VALUES
(1, 'No Taxonomy', 'No Taxonomy', 'No Taxonomy', 'No Taxonomy', 'No Taxonomy', 'No Taxonomy');

--
-- Truncate table before insert `lab_treatment`
--

TRUNCATE TABLE `lab_treatment`;
--
-- Dumping data for table `lab_treatment`
--

INSERT INTO `lab_treatment` (`id`, `treatment_id`, `treatment_type`, `date`, `comments`, `experiment_id`) VALUES
(1, 'No Treatment', 'No Treatment', 'No Treatment', '', 1);

--
-- Truncate table before insert `lab_uploadqueue`
--

TRUNCATE TABLE `lab_uploadqueue`;
--
-- Truncate table before insert `lab_userprofile`
--

TRUNCATE TABLE `lab_userprofile`;
--
-- Dumping data for table `lab_userprofile`
--

INSERT INTO `lab_userprofile` (`id`, `website`, `picture`, `phone`, `organization`, `notes`, `job_title`, `user_id`) VALUES
(1, 'No Profile', 'profile_images/underwater.jpg', 'No Profile', 'No Profile', 'No Profile', 'No Profile', 1),
(2, '', 'profile_images/underwater.jpg', '321-695-9465', 'BTI Cornell', '', 'Database', 2);
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
