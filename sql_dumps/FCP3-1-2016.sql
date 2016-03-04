-- MySQL dump 10.14  Distrib 5.5.44-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: FCPDB
-- ------------------------------------------------------
-- Server version	5.5.44-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user profile',7,'add_userprofile'),(20,'Can change user profile',7,'change_userprofile'),(21,'Can delete user profile',7,'delete_userprofile'),(22,'Can add locality',8,'add_locality'),(23,'Can change locality',8,'change_locality'),(24,'Can delete locality',8,'delete_locality'),(25,'Can add field',9,'add_field'),(26,'Can change field',9,'change_field'),(27,'Can delete field',9,'delete_field'),(28,'Can add experiment',10,'add_experiment'),(29,'Can change experiment',10,'change_experiment'),(30,'Can delete experiment',10,'delete_experiment'),(31,'Can add file dump',11,'add_filedump'),(32,'Can change file dump',11,'change_filedump'),(33,'Can delete file dump',11,'delete_filedump'),(34,'Can add publication',12,'add_publication'),(35,'Can change publication',12,'change_publication'),(36,'Can delete publication',12,'delete_publication'),(37,'Can add taxonomy',13,'add_taxonomy'),(38,'Can change taxonomy',13,'change_taxonomy'),(39,'Can delete taxonomy',13,'delete_taxonomy'),(40,'Can add people',14,'add_people'),(41,'Can change people',14,'change_people'),(42,'Can delete people',14,'delete_people'),(43,'Can add citation',15,'add_citation'),(44,'Can change citation',15,'change_citation'),(45,'Can delete citation',15,'delete_citation'),(46,'Can add medium',16,'add_medium'),(47,'Can change medium',16,'change_medium'),(48,'Can delete medium',16,'delete_medium'),(49,'Can add obs row',17,'add_obsrow'),(50,'Can change obs row',17,'change_obsrow'),(51,'Can delete obs row',17,'delete_obsrow'),(52,'Can add obs plant',18,'add_obsplant'),(53,'Can change obs plant',18,'change_obsplant'),(54,'Can delete obs plant',18,'delete_obsplant'),(55,'Can add obs sample',19,'add_obssample'),(56,'Can change obs sample',19,'change_obssample'),(57,'Can delete obs sample',19,'delete_obssample'),(58,'Can add separation',20,'add_separation'),(59,'Can change separation',20,'change_separation'),(60,'Can delete separation',20,'delete_separation'),(61,'Can add obs extract',21,'add_obsextract'),(62,'Can change obs extract',21,'change_obsextract'),(63,'Can delete obs extract',21,'delete_obsextract'),(64,'Can add obs env',22,'add_obsenv'),(65,'Can change obs env',22,'change_obsenv'),(66,'Can delete obs env',22,'delete_obsenv'),(67,'Can add obs dna',23,'add_obsdna'),(68,'Can change obs dna',23,'change_obsdna'),(69,'Can delete obs dna',23,'delete_obsdna'),(70,'Can add obs tissue',24,'add_obstissue'),(71,'Can change obs tissue',24,'change_obstissue'),(72,'Can delete obs tissue',24,'delete_obstissue'),(73,'Can add obs plate',25,'add_obsplate'),(74,'Can change obs plate',25,'change_obsplate'),(75,'Can delete obs plate',25,'delete_obsplate'),(76,'Can add obs well',26,'add_obswell'),(77,'Can change obs well',26,'change_obswell'),(78,'Can delete obs well',26,'delete_obswell'),(79,'Can add obs culture',27,'add_obsculture'),(80,'Can change obs culture',27,'change_obsculture'),(81,'Can delete obs culture',27,'delete_obsculture'),(82,'Can add obs microbe',28,'add_obsmicrobe'),(83,'Can change obs microbe',28,'change_obsmicrobe'),(84,'Can delete obs microbe',28,'delete_obsmicrobe'),(85,'Can add location',29,'add_location'),(86,'Can change location',29,'change_location'),(87,'Can delete location',29,'delete_location'),(88,'Can add collecting',30,'add_collecting'),(89,'Can change collecting',30,'change_collecting'),(90,'Can delete collecting',30,'delete_collecting'),(91,'Can add passport',31,'add_passport'),(92,'Can change passport',31,'change_passport'),(93,'Can delete passport',31,'delete_passport'),(94,'Can add stock',32,'add_stock'),(95,'Can change stock',32,'change_stock'),(96,'Can delete stock',32,'delete_stock'),(97,'Can add maize sample',33,'add_maizesample'),(98,'Can change maize sample',33,'change_maizesample'),(99,'Can delete maize sample',33,'delete_maizesample'),(100,'Can add disease info',34,'add_diseaseinfo'),(101,'Can change disease info',34,'change_diseaseinfo'),(102,'Can delete disease info',34,'delete_diseaseinfo'),(103,'Can add isolate stock',35,'add_isolatestock'),(104,'Can change isolate stock',35,'change_isolatestock'),(105,'Can delete isolate stock',35,'delete_isolatestock'),(106,'Can add isolate',36,'add_isolate'),(107,'Can change isolate',36,'change_isolate'),(108,'Can delete isolate',36,'delete_isolate'),(109,'Can add stock packet',37,'add_stockpacket'),(110,'Can change stock packet',37,'change_stockpacket'),(111,'Can delete stock packet',37,'delete_stockpacket'),(112,'Can add treatment',38,'add_treatment'),(113,'Can change treatment',38,'change_treatment'),(114,'Can delete treatment',38,'delete_treatment'),(115,'Can add upload queue',39,'add_uploadqueue'),(116,'Can change upload queue',39,'change_uploadqueue'),(117,'Can delete upload queue',39,'delete_uploadqueue'),(118,'Can add obs tracker',40,'add_obstracker'),(119,'Can change obs tracker',40,'change_obstracker'),(120,'Can delete obs tracker',40,'delete_obstracker'),(121,'Can add obs tracker source',41,'add_obstrackersource'),(122,'Can change obs tracker source',41,'change_obstrackersource'),(123,'Can delete obs tracker source',41,'delete_obstrackersource'),(124,'Can add primer',42,'add_primer'),(125,'Can change primer',42,'change_primer'),(126,'Can delete primer',42,'delete_primer'),(127,'Can add map feature',43,'add_mapfeature'),(128,'Can change map feature',43,'change_mapfeature'),(129,'Can delete map feature',43,'delete_mapfeature'),(130,'Can add map feature annotation',44,'add_mapfeatureannotation'),(131,'Can change map feature annotation',44,'change_mapfeatureannotation'),(132,'Can delete map feature annotation',44,'delete_mapfeatureannotation'),(133,'Can add map feature interval',45,'add_mapfeatureinterval'),(134,'Can change map feature interval',45,'change_mapfeatureinterval'),(135,'Can delete map feature interval',45,'delete_mapfeatureinterval'),(136,'Can add marker',46,'add_marker'),(137,'Can change marker',46,'change_marker'),(138,'Can delete marker',46,'delete_marker'),(139,'Can add measurement parameter',47,'add_measurementparameter'),(140,'Can change measurement parameter',47,'change_measurementparameter'),(141,'Can delete measurement parameter',47,'delete_measurementparameter'),(142,'Can add qtl',48,'add_qtl'),(143,'Can change qtl',48,'change_qtl'),(144,'Can delete qtl',48,'delete_qtl'),(145,'Can add map feature expression',49,'add_mapfeatureexpression'),(146,'Can change map feature expression',49,'change_mapfeatureexpression'),(147,'Can delete map feature expression',49,'delete_mapfeatureexpression'),(148,'Can add genotype results',50,'add_genotyperesults'),(149,'Can change genotype results',50,'change_genotyperesults'),(150,'Can delete genotype results',50,'delete_genotyperesults'),(151,'Can add gwas results',51,'add_gwasresults'),(152,'Can change gwas results',51,'change_gwasresults'),(153,'Can delete gwas results',51,'delete_gwasresults'),(154,'Can add gwas experiment set',52,'add_gwasexperimentset'),(155,'Can change gwas experiment set',52,'change_gwasexperimentset'),(156,'Can delete gwas experiment set',52,'delete_gwasexperimentset'),(157,'Can add measurement',53,'add_measurement'),(158,'Can change measurement',53,'change_measurement'),(159,'Can delete measurement',53,'delete_measurement');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (3,'pbkdf2_sha256$12000$gqCrGR6WKKt3$7g1GMJGId0d6cjQ2jLgBK5XPSEm8hcTSXwWq6Gobni0=','2016-02-26 20:40:54',1,'slin63','Shean','Lin','slin63@illinois.edu',1,1,'2016-02-23 03:20:25'),(4,'pbkdf2_sha256$12000$xSZSMdujlaLh$PXNd/yHfiopbbuaynRGWcNbPFnfBPLzGETnKWAUzf9Q=','2016-02-23 17:24:56',0,'mehl1','Kelsey','Mehl','mehl1@illinois.edu',0,1,'2016-02-23 17:24:47'),(5,'pbkdf2_sha256$12000$MWUAEjnBOMmM$yB5waGoqqa4ObxludPDvuLqwsP33i5iS8oMTl9KmCHw=','2016-02-26 20:46:49',1,'smideros','Santiago','Mideros','smideros@illinois.edu',0,1,'2016-02-24 19:46:35'),(6,'pbkdf2_sha256$12000$rQklQzR56rog$Cehj8wHWal//m7WzIq7kUvk+Lc00ptTQhXfW83Mj4AM=','2016-02-26 19:23:13',0,'tjamann','Tiffany','Jamann','tjamann@illinois.edu',0,1,'2016-02-26 19:23:05'),(7,'pbkdf2_sha256$12000$ABUFtkLbKJIj$y7kfxVtQZG3+4q95P534xpV1O5Fq1HdY544sm6eFfQU=','2016-02-28 16:28:27',0,'clin88','Chen','Lin','chenmonitor@gmail.com',0,1,'2016-02-28 16:28:21');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-02-23 03:23:23','3','slin63',1,'',7,3),(2,'2016-02-24 00:02:37','3','DemoIso2',3,'',36,3),(3,'2016-02-26 20:41:33','5','smideros',2,'Changed is_superuser.',4,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'user profile','lab','userprofile'),(8,'locality','lab','locality'),(9,'field','lab','field'),(10,'experiment','lab','experiment'),(11,'file dump','lab','filedump'),(12,'publication','lab','publication'),(13,'taxonomy','lab','taxonomy'),(14,'people','lab','people'),(15,'citation','lab','citation'),(16,'medium','lab','medium'),(17,'obs row','lab','obsrow'),(18,'obs plant','lab','obsplant'),(19,'obs sample','lab','obssample'),(20,'separation','lab','separation'),(21,'obs extract','lab','obsextract'),(22,'obs env','lab','obsenv'),(23,'obs dna','lab','obsdna'),(24,'obs tissue','lab','obstissue'),(25,'obs plate','lab','obsplate'),(26,'obs well','lab','obswell'),(27,'obs culture','lab','obsculture'),(28,'obs microbe','lab','obsmicrobe'),(29,'location','lab','location'),(30,'collecting','lab','collecting'),(31,'passport','lab','passport'),(32,'stock','lab','stock'),(33,'maize sample','lab','maizesample'),(34,'disease info','lab','diseaseinfo'),(35,'isolate stock','lab','isolatestock'),(36,'isolate','lab','isolate'),(37,'stock packet','lab','stockpacket'),(38,'treatment','lab','treatment'),(39,'upload queue','lab','uploadqueue'),(40,'obs tracker','lab','obstracker'),(41,'obs tracker source','lab','obstrackersource'),(42,'primer','lab','primer'),(43,'map feature','lab','mapfeature'),(44,'map feature annotation','lab','mapfeatureannotation'),(45,'map feature interval','lab','mapfeatureinterval'),(46,'marker','lab','marker'),(47,'measurement parameter','lab','measurementparameter'),(48,'qtl','lab','qtl'),(49,'map feature expression','lab','mapfeatureexpression'),(50,'genotype results','lab','genotyperesults'),(51,'gwas results','lab','gwasresults'),(52,'gwas experiment set','lab','gwasexperimentset'),(53,'measurement','lab','measurement');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-02-23 02:55:33'),(2,'auth','0001_initial','2016-02-23 02:55:33'),(3,'admin','0001_initial','2016-02-23 02:55:33'),(4,'lab','0001_initial','2016-02-23 02:55:41'),(5,'sessions','0001_initial','2016-02-23 02:55:41');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('02rffh5bmvpydslfa45xd5n4komtt3k3','MzljYTI0YTU0YTRkZmNjZmRjNTc4YzY4ZWJmMzViMzkwZjRiMTFjZjp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjMgMTI6MTk6NDUuNTQ0NzU5In0=','2016-03-08 17:19:45'),('0uv45kz1z7rm1svw6qks7v7g5vrq91os','NjIzNTE3ODYxMGU4OGFmNzc0YzA1NGVhYzI4ZmNlNGJiN2EzMWM4Yzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjkgMTQ6NTY6NTAuODA4ODUzIn0=','2016-03-14 19:56:50'),('1an9rchfmwawkftyxdfdki4we2i1qwkn','MGU1MWQ1NjU5MmY0NmI1M2E4OGE4ZWY4N2JhNzA1NjEyYzZmMjJlNzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjkgMTQ6NTY6NDguMTU0OTkxIn0=','2016-03-14 19:56:48'),('1oukwbptsjup2ok8sxhoaoug4qe7rr3k','NGMxZjYwZGFjZDgzZmUwYmRlM2RjN2QyZDUxYmM5NDk4M2Q2ZjgxNzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MywiX2F1dGhfdXNlcl9oYXNoIjoiMmUwOTAxNzI5YjU3YWExY2M0OGU1NmIwN2M5MWVhMWYxNWQzMTk1NCIsImxhc3RfdmlzaXQiOiIyMDE2LTAyLTI1IDE4OjU1OjE5LjAwMjY4MyIsInZpc2l0cyI6MX0=','2016-03-10 23:55:32'),('2bvqgpl1zhp384r3uas5ufs2i0frryue','YTgxYTVkNDcxNGMwZDVmNDdhYzIwYWFmZTQ5MWU1NWRlYWFmMzU3Yjp7Il9hdXRoX3VzZXJfaWQiOjYsImxhc3RfdmlzaXQiOiIyMDE2LTAzLTAxIDEyOjEyOjU4LjczODkxOCIsImNoZWNrYm94X3N0b2NrIjpbIjIiLCI0IiwiNSJdLCJ2aXNpdHMiOjQsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMjE3ZjQ4MDM2M2ZhZDkwZDdmNmIzYmI2OWE4NmE4MDdjOTcwNTM5OSJ9','2016-03-15 17:17:27'),('2ompwwpw53uaprx4ahf831hr890yjiwk','ODhhOGZlNGM0YTY0ZWQwYWY4NzlmNGJhOTFjODU2N2I3ODBjZDQ0ZDp7Il9hdXRoX3VzZXJfaWQiOjMsImNoZWNrYm94X2lzb2xhdGVzdG9ja3MiOlsiMiJdLCJsYXN0X3Zpc2l0IjoiMjAxNi0wMi0yOCAyMzowMzoxOS40NzQ3MjUiLCJ2aXNpdHMiOjQsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmUwOTAxNzI5YjU3YWExY2M0OGU1NmIwN2M5MWVhMWYxNWQzMTk1NCJ9','2016-03-14 04:03:19'),('33lbsqqnf67sq2clynmqn84y399kkruj','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 03:03:00'),('3brvy64lkv65awn0juy9ogi6hqi0qwo3','NDU0MjdiZmFiZTlhZmYwMzQ2OTg3NjRiZjdiY2VjNTc1OTI1NmFjODp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDMtMDEgMDY6MjY6MzkuNTk3MjkwIn0=','2016-03-15 11:26:39'),('4eucm6cu4ijtyhihqfqskiivnguj89ck','NTgwZGMwODQ2M2RkNDY1OTA0NTExYWEwYzZkM2I0MWQxNmIxOTg3ZDp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjggMjM6NDk6NTQuMDA0OTE2In0=','2016-03-14 04:49:54'),('4ppth8z0jcq9kv9bx1nu2ajqnhmkkn22','NDcyYmNjNGIxOWEyN2I0ODBlZWY1N2Y3OTAyYTI1M2MwMTE0ZDUzNTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjMgMTE6Mjk6MDMuNjY3NzgxIn0=','2016-03-08 16:29:03'),('573vrm0yoiv60b2inf4q8al39skqgt7g','NjI1Y2FmMTM5NzYxZmFkMDIyMTgwYWQxNGQ4OTFmZjdlYzY4OGU5Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NSwiX2F1dGhfdXNlcl9oYXNoIjoiODcyZjBjOTNiYmQ4Y2I0YjEwZTJlY2E5YWFmMjBiYjg0YzNjNWU3MiIsImxhc3RfdmlzaXQiOiIyMDE2LTAyLTI2IDE1OjQzOjQ4LjczMzczOSIsInZpc2l0cyI6MX0=','2016-03-11 20:46:49'),('5jfv7ny8g5qs420lvufik9tp19kk7hko','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 02:56:25'),('an2cyztgojsa2kha8fx16u9tt01x5k83','MTBmNzMxYjBkMzU5ZWQxMTE2ZTc2MjE3ZDRhNWVkYzcwZjRkMGMwNzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjMgMTE6Mjk6NDcuNjg5NDU1In0=','2016-03-08 16:29:47'),('au7sqtl5e4ilw3j76yp1ds3aqq5xvu6v','OTNkYTFmNzgzM2JjNDgxYWRmOTg4MzVmNzM0NDQwM2Y2Zjc5ZmFjMTp7InZpc2l0cyI6MiwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMTQ6MjE6MDYuODQ5NjA5IiwiX2F1dGhfdXNlcl9oYXNoIjoiMmUwOTAxNzI5YjU3YWExY2M0OGU1NmIwN2M5MWVhMWYxNWQzMTk1NCIsIl9hdXRoX3VzZXJfaWQiOjMsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-03-11 19:21:06'),('bcl70hkq3oeggk9l0lebmvz96e7q0770','OTkyODdmYjljNDdkMTZiM2JhYTMwMmU1MDZlMzZmNjdkZjMzNmY5YTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjUgMjA6MjU6MzIuNjYxNjg4In0=','2016-03-11 01:25:32'),('bktsocytnmy91m91c5519a6i514xzblj','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 02:56:56'),('e11axg5d0gjw1n5pi3lpa7fbr3rbcty7','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 03:01:11'),('eemqeichsa5iqyqzicga02g9xha8f3ko','ZTk3MmRkYmQ0ODc3Y2Q4MmJkOGEzOGFjMjliMjcyNjJhNzYzNjVhMTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMTQ6MjI6MTMuMTMzMDI1In0=','2016-03-11 19:22:13'),('ezwxkowx7nyjrbhiuytpic0a8ljp97sl','OTg2NmMxMjcwNDU0ZTVjNWNhZTIxMDEzM2UwNWJlNmI1NTg2N2Y5MTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjQgMDA6MDY6MDUuMjMzODY3In0=','2016-03-09 05:06:05'),('glewwafutg8gn4ilozhqb2y0y04qnacm','NTU2ZjA3ZjM2ZjUzN2IzZGVkNjFlYWFmOGU4MTZkOGIxNjViNDk0Yzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjkgMTc6MzA6MzMuMTgyMzk0In0=','2016-03-14 22:30:33'),('hehtp4sku2fmyl16tmp7t5j7o9sw9lg0','NzJmM2VkNjA3NTg3YTk2OWExZDEwZWExODNlMzBmOTVmMTcyYTdmZDp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMjI6Mjk6MTcuODU0MzE0In0=','2016-03-12 03:29:17'),('hr5t6qhyjll0jt5nszsmrpvncx2xrv2l','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 02:57:09'),('kdlpqzvnegcf5r9r8qi4vj7oqu9knchm','Nzc5N2NmMTU2ZGRmZmIyMmQ0MmMwZDk2MDJiYTI2M2RmY2ZhY2E1Yzp7InZpc2l0cyI6MiwibGFzdF92aXNpdCI6IjIwMTYtMDItMjkgMTQ6NTY6MTkuNjE3MjQzIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTExMThjNzFmNmE4ZWJhN2Q3OWFkNDM3MjMxOTE4MTFhODJkMzIzOSIsIl9hdXRoX3VzZXJfaWQiOjQsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-03-14 19:56:19'),('kme7gnamhfmpb05wfy8ff3gtczb8a93u','NzE3MjhlYzAzMzMzMTM2NWFiM2FjNjk0ZjgzYTIxMzFkMmUxYTQxMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MywiX2F1dGhfdXNlcl9oYXNoIjoiMmUwOTAxNzI5YjU3YWExY2M0OGU1NmIwN2M5MWVhMWYxNWQzMTk1NCIsImxhc3RfdmlzaXQiOiIyMDE2LTAyLTIzIDE4OjM5OjQ2LjQyNTcxMyIsInZpc2l0cyI6MX0=','2016-03-08 23:40:06'),('m271qy3g184n7yvmrw1f9w4haz0bguuc','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 02:56:57'),('mttzj9hqaqm1cr8oe00mbmpho8wtaq15','OTVmZmVjYjc4YWNlYTg4MzgwYmJhOTk3ODBhNTgxYzU2NTE2ZTMwNTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMTQ6MjE6NTguMTYyOTcwIn0=','2016-03-11 19:21:58'),('nn7s8dy6uhxm7kdfnjalr3extdzin2de','ZmEyMjlkNjZkYWRlODYxZjBiMjNjNmUyZjc1MDFkMjRkNTIyMmNmMzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDMtMDEgMTQ6MzU6MTUuNjcwMDY2In0=','2016-03-15 19:35:15'),('nq5r9pfyslyp7w7nk4mjp25bfvjz1grx','ZDFjYjcyY2YyYmM1NDRjYWZmYWZhN2M0YjI4MTZlZWYyMGFkNjcxNjp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDMtMDEgMTQ6MzU6MTUuNjAxOTUxIn0=','2016-03-15 19:35:15'),('op82tn9km0wzx1ru0vl1ofrcs8s26l42','NDYxNTIyMDZjM2Q3MzgzODU3YjNhMzk3N2YzN2UxNjc3MGMwNWZjNTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMDk6Mjc6MDIuMTIxNTcwIn0=','2016-03-11 14:27:02'),('q4c4s5hq259a2d3z2z1uyztkaxif3k19','ZjBmMTFmMDhlNGRlYjJkYjQxZDMwNzc4NTE5MDVlZmZhMjNjY2Y2Nzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjMgMTI6MTk6NDIuNzYzMjU4In0=','2016-03-08 17:19:42'),('rklilrmpm2bqh12mgxh4ip9rj70d67h2','OGNhOTRiZGU0Nzc5YmQxMmEwZWQ1YmVjN2YzZGJhM2MzZDNiZjFmZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NywiX2F1dGhfdXNlcl9oYXNoIjoiNWNkYjFiZTExNGQzYzFhZmRmYWRmZmM3Y2RkM2YzYzc5NjhjYzFlMyIsImxhc3RfdmlzaXQiOiIyMDE2LTAyLTI4IDExOjI3OjU2LjQ2NjY1MyIsInZpc2l0cyI6MX0=','2016-03-13 16:28:27'),('smoq7up48bn045j2ro961xmbcanf23xq','NzdkMzRmMDE3ZWI1N2M4ZDFhMTM1YmM0ODNjMDE3YjJmODc5NmRhYTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjMgMTE6Mjk6NDMuNDg3Mjk3In0=','2016-03-08 16:29:43'),('sxol99lsn4fok0qg6h8gsmjvw62guwra','YjU4OWQzOGY1MmFiYjQ5MGEyMmJlMjY3YjI4M2U5MjVlNjY3ZWZhMjp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMTQ6MjE6NTUuNDkyOTE1In0=','2016-03-11 19:21:55'),('uhrofqj08qxztdy6krc45tr7lq2h7tjs','YWRlODJhYjZmODM3MjM5OGVhNmNmYTFlMmVjYTc2NGE4ZGVkNTkyMzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMTQ6MjI6MTAuMzI1NTI3In0=','2016-03-11 19:22:10'),('x0y1kt9klo45hh4g7jpcwa42j79nmvla','ZDgxMzVmNDc2MmU5N2IyYWZmNzY2OWQ3MTlmNGQ2MDEzMGQ0ZmJlMTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMTQ6MjE6NTUuNTc3NDYyIn0=','2016-03-11 19:21:55'),('x14b37v20nqiespx5o5hc1t4kunaud15','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 03:13:23'),('xbyxiq2g2d7yqsmirsnm7m6utx2reztf','ZjU0ODIxYmU4MjQ3ZDViNTk2M2ExMzY2Nzk3NGFiOTc4OWZiOWQ1OTp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjkgMTQ6NTY6MzUuNzM1MDE3In0=','2016-03-14 19:56:35'),('ykby06q3fjf4vb6y1dd7xnjvri77tst7','ZThkNjJlMzllNmZhYjcwODJlOTgzMzAwOGFjMjQzNTYwNmRiOTVmNjp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjYgMjM6MTY6MzQuMjY1Nzg0In0=','2016-03-12 04:16:34'),('yucvci1rombry33su1bvcnxik87jk40h','M2YzNThlYWVmYTJlYjE0MWRmZjA2OTY4NTA2NTE3NjU4NTk5ZTc3Mzp7InZpc2l0cyI6MSwibGFzdF92aXNpdCI6IjIwMTYtMDItMjcgMTA6MTc6MjUuNzY4NDg4In0=','2016-03-12 15:17:25'),('z12x84klzrkrxrsvcygmazyhxijl77vv','OTkxNmIyOTFjNDRiODM4ZWQ2ZDAzNzlmZjgzNDhhYTc3NmJkZjM5OTp7fQ==','2016-03-08 02:57:05');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_citation`
--

DROP TABLE IF EXISTS `lab_citation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_citation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `citation_type` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `url` varchar(300) NOT NULL,
  `pubmed_id` varchar(300) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_citation`
--

LOCK TABLES `lab_citation` WRITE;
/*!40000 ALTER TABLE `lab_citation` DISABLE KEYS */;
INSERT INTO `lab_citation` VALUES (1,'No Citation','No Citation','No Citation','No Citation','');
/*!40000 ALTER TABLE `lab_citation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_collecting`
--

DROP TABLE IF EXISTS `lab_collecting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_collecting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collection_date` varchar(200) NOT NULL,
  `collection_method` varchar(1000) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_collecting_e8701ad4` (`user_id`),
  CONSTRAINT `lab_collecting_user_id_7143567fc1de02a3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_collecting`
--

LOCK TABLES `lab_collecting` WRITE;
/*!40000 ALTER TABLE `lab_collecting` DISABLE KEYS */;
INSERT INTO `lab_collecting` VALUES (2,'','','test',5),(3,'','','',2),(4,'','','Don White Collection',6),(5,'','','',6),(6,'03/01/2016','','',6),(7,'','','',1);
/*!40000 ALTER TABLE `lab_collecting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_diseaseinfo`
--

DROP TABLE IF EXISTS `lab_diseaseinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_diseaseinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `common_name` varchar(200) NOT NULL,
  `abbrev` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `common_name` (`common_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_diseaseinfo`
--

LOCK TABLES `lab_diseaseinfo` WRITE;
/*!40000 ALTER TABLE `lab_diseaseinfo` DISABLE KEYS */;
INSERT INTO `lab_diseaseinfo` VALUES (1,'No Disease','',''),(2,'Sorghum Leaf Blight','SB','');
/*!40000 ALTER TABLE `lab_diseaseinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_experiment`
--

DROP TABLE IF EXISTS `lab_experiment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_experiment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `start_date` varchar(200) NOT NULL,
  `purpose` varchar(1000) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `field_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `lab_experiment_3aabf39f` (`field_id`),
  KEY `lab_experiment_e8701ad4` (`user_id`),
  CONSTRAINT `lab_experiment_user_id_96122507feea308_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `lab_experiment_field_id_411dd7acfa9ce010_fk_lab_field_id` FOREIGN KEY (`field_id`) REFERENCES `lab_field` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_experiment`
--

LOCK TABLES `lab_experiment` WRITE;
/*!40000 ALTER TABLE `lab_experiment` DISABLE KEYS */;
INSERT INTO `lab_experiment` VALUES (2,'15IS','2015-08-15','Collection of Isolates','',1,5),(3,'00DI','2016-02-29','Germination tests','test seed viability',1,6);
/*!40000 ALTER TABLE `lab_experiment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_field`
--

DROP TABLE IF EXISTS `lab_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_field` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `field_name` varchar(200) NOT NULL,
  `field_num` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `locality_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `field_name` (`field_name`),
  KEY `lab_field_7e3ea948` (`locality_id`),
  CONSTRAINT `lab_field_locality_id_51c97e78387aa804_fk_lab_locality_id` FOREIGN KEY (`locality_id`) REFERENCES `lab_locality` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_field`
--

LOCK TABLES `lab_field` WRITE;
/*!40000 ALTER TABLE `lab_field` DISABLE KEYS */;
INSERT INTO `lab_field` VALUES (1,'No Field','','',1);
/*!40000 ALTER TABLE `lab_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_filedump`
--

DROP TABLE IF EXISTS `lab_filedump`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_filedump` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(250) NOT NULL,
  `file` varchar(100) NOT NULL,
  `date` datetime NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `experiment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_filedump_abd1812d` (`experiment_id`),
  KEY `lab_filedump_e8701ad4` (`user_id`),
  CONSTRAINT `lab_filedump_user_id_30684f0b91f73d61_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `lab_filedump_experiment_id_14c03ed4d7858c9_fk_lab_experiment_id` FOREIGN KEY (`experiment_id`) REFERENCES `lab_experiment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_filedump`
--

LOCK TABLES `lab_filedump` WRITE;
/*!40000 ALTER TABLE `lab_filedump` DISABLE KEYS */;
/*!40000 ALTER TABLE `lab_filedump` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_genotyperesults`
--

DROP TABLE IF EXISTS `lab_genotyperesults`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_genotyperesults` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sequence` longtext NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `fasta_file` varchar(100) NOT NULL,
  `chromatogram_file` varchar(100) NOT NULL,
  `marker_id` int(11) NOT NULL,
  `parameter_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_genotyperesults_945c7b03` (`marker_id`),
  KEY `lab_genotyperesults_80740216` (`parameter_id`),
  CONSTRAINT `lab_parameter_id_143837b053c727e0_fk_lab_measurementparameter_id` FOREIGN KEY (`parameter_id`) REFERENCES `lab_measurementparameter` (`id`),
  CONSTRAINT `lab_genotyperesults_marker_id_3fb98718d738b294_fk_lab_marker_id` FOREIGN KEY (`marker_id`) REFERENCES `lab_marker` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_genotyperesults`
--

LOCK TABLES `lab_genotyperesults` WRITE;
/*!40000 ALTER TABLE `lab_genotyperesults` DISABLE KEYS */;
/*!40000 ALTER TABLE `lab_genotyperesults` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_gwasexperimentset`
--

DROP TABLE IF EXISTS `lab_gwasexperimentset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_gwasexperimentset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `experiment_id` int(11) NOT NULL,
  `gwas_results_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_gwasexperimentset_abd1812d` (`experiment_id`),
  KEY `lab_gwasexperimentset_83a5e0ca` (`gwas_results_id`),
  CONSTRAINT `lab_gwasex_gwas_results_id_947c66d0b486431_fk_lab_gwasresults_id` FOREIGN KEY (`gwas_results_id`) REFERENCES `lab_gwasresults` (`id`),
  CONSTRAINT `lab_gwasexpe_experiment_id_6968507ecb26d96d_fk_lab_experiment_id` FOREIGN KEY (`experiment_id`) REFERENCES `lab_experiment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_gwasexperimentset`
--

LOCK TABLES `lab_gwasexperimentset` WRITE;
/*!40000 ALTER TABLE `lab_gwasexperimentset` DISABLE KEYS */;
INSERT INTO `lab_gwasexperimentset` VALUES (1,1,1);
/*!40000 ALTER TABLE `lab_gwasexperimentset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_gwasresults`
--

DROP TABLE IF EXISTS `lab_gwasresults`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_gwasresults` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_value` varchar(200) NOT NULL,
  `strand` varchar(200) NOT NULL,
  `relationship_to_hit` varchar(200) NOT NULL,
  `interpro_domain` varchar(200) NOT NULL,
  `distance_from_gene` varchar(200) NOT NULL,
  `f_value` varchar(200) NOT NULL,
  `perm_p_value` varchar(200) NOT NULL,
  `r2` varchar(200) NOT NULL,
  `alleles` varchar(200) NOT NULL,
  `bpp` varchar(200) NOT NULL,
  `effect` varchar(200) NOT NULL,
  `cM` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `parameter_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_gwasresults_80740216` (`parameter_id`),
  CONSTRAINT `lab_parameter_id_4772d31198cf2677_fk_lab_measurementparameter_id` FOREIGN KEY (`parameter_id`) REFERENCES `lab_measurementparameter` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_gwasresults`
--

LOCK TABLES `lab_gwasresults` WRITE;
/*!40000 ALTER TABLE `lab_gwasresults` DISABLE KEYS */;
INSERT INTO `lab_gwasresults` VALUES (1,'No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','No GWAS Result','',1);
/*!40000 ALTER TABLE `lab_gwasresults` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_isolate`
--

DROP TABLE IF EXISTS `lab_isolate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_isolate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `isolate_id` varchar(200) NOT NULL,
  `stock_date` varchar(200) NOT NULL,
  `extract_color` varchar(200) NOT NULL,
  `organism` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isolate_id` (`isolate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_isolate`
--

LOCK TABLES `lab_isolate` WRITE;
/*!40000 ALTER TABLE `lab_isolate` DISABLE KEYS */;
INSERT INTO `lab_isolate` VALUES (1,'No Isolate','No Isolate','','',''),(7,'test','','','','');
/*!40000 ALTER TABLE `lab_isolate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_isolatestock`
--

DROP TABLE IF EXISTS `lab_isolatestock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_isolatestock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `isolatestock_id` varchar(200) NOT NULL,
  `isolatestock_name` varchar(200) NOT NULL,
  `plant_organ` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `disease_info_id` int(11) NOT NULL,
  `locality_id` int(11) NOT NULL,
  `passport_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isolatestock_id` (`isolatestock_id`),
  KEY `lab_isolatestock_d766bd11` (`disease_info_id`),
  KEY `lab_isolatestock_7e3ea948` (`locality_id`),
  KEY `lab_isolatestock_71116643` (`passport_id`),
  CONSTRAINT `lab_isolatestock_passport_id_3c760bae6702681_fk_lab_passport_id` FOREIGN KEY (`passport_id`) REFERENCES `lab_passport` (`id`),
  CONSTRAINT `lab_isolatestock_locality_id_6e031954e90e5176_fk_lab_locality_id` FOREIGN KEY (`locality_id`) REFERENCES `lab_locality` (`id`),
  CONSTRAINT `lab_isola_disease_info_id_540a1340e78ac168_fk_lab_diseaseinfo_id` FOREIGN KEY (`disease_info_id`) REFERENCES `lab_diseaseinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_isolatestock`
--

LOCK TABLES `lab_isolatestock` WRITE;
/*!40000 ALTER TABLE `lab_isolatestock` DISABLE KEYS */;
INSERT INTO `lab_isolatestock` VALUES (3,'15st002','','Leaf','',1,4,3),(4,'TestStock ID','ISO NAME','ORGAN','COM',1,2,5);
/*!40000 ALTER TABLE `lab_isolatestock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_locality`
--

DROP TABLE IF EXISTS `lab_locality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_locality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(200) NOT NULL,
  `county` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `country` varchar(200) NOT NULL,
  `zipcode` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_locality`
--

LOCK TABLES `lab_locality` WRITE;
/*!40000 ALTER TABLE `lab_locality` DISABLE KEYS */;
INSERT INTO `lab_locality` VALUES (1,'No Locality','','No Locality','No Locality','No Locality'),(2,'Urbana','','IL','USA','61801'),(3,'South Farms','','IL','USA',''),(4,'Energy Farm','','IL','USA',''),(5,'Auburn','','IL','USA',''),(6,'DeKalb','','IL','USA','');
/*!40000 ALTER TABLE `lab_locality` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_location`
--

DROP TABLE IF EXISTS `lab_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `building_name` varchar(200) NOT NULL,
  `location_name` varchar(200) NOT NULL,
  `room` varchar(200) NOT NULL,
  `shelf` varchar(200) NOT NULL,
  `column` varchar(200) NOT NULL,
  `box_name` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `locality_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `location_name` (`location_name`),
  KEY `lab_location_7e3ea948` (`locality_id`),
  CONSTRAINT `lab_location_locality_id_226528f634d79ab8_fk_lab_locality_id` FOREIGN KEY (`locality_id`) REFERENCES `lab_locality` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_location`
--

LOCK TABLES `lab_location` WRITE;
/*!40000 ALTER TABLE `lab_location` DISABLE KEYS */;
INSERT INTO `lab_location` VALUES (2,'Turner Hall','Chest Freezer','N-520','','','','',2),(3,'','Turner Hall','','','','','',6),(4,'','Urbana','','','','','',2),(5,'Turner','Turner Cold Storage','C427','35','F','B73-B104','drawer stuck',2),(6,'Turner','Turner Cold Room','C427','4','K','B73-B104','shelf bent',2),(10,'','Tuerner','','','','','',2);
/*!40000 ALTER TABLE `lab_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_maizesample`
--

DROP TABLE IF EXISTS `lab_maizesample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_maizesample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `maize_id` varchar(200) NOT NULL,
  `county` varchar(200) NOT NULL,
  `sub_location` varchar(200) NOT NULL,
  `village` varchar(200) NOT NULL,
  `weight` varchar(200) NOT NULL,
  `harvest_date` varchar(200) NOT NULL,
  `storage_months` varchar(200) NOT NULL,
  `storage_conditions` varchar(200) NOT NULL,
  `maize_variety` varchar(200) NOT NULL,
  `seed_source` varchar(200) NOT NULL,
  `moisture_content` varchar(200) NOT NULL,
  `source_type` varchar(200) NOT NULL,
  `appearance` varchar(200) NOT NULL,
  `gps_latitude` varchar(200) NOT NULL,
  `gps_longitude` varchar(200) NOT NULL,
  `gps_altitude` varchar(200) NOT NULL,
  `gps_accuracy` varchar(200) NOT NULL,
  `photo` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `maize_id` (`maize_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_maizesample`
--

LOCK TABLES `lab_maizesample` WRITE;
/*!40000 ALTER TABLE `lab_maizesample` DISABLE KEYS */;
INSERT INTO `lab_maizesample` VALUES (1,'No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','No Maize Sample','');
/*!40000 ALTER TABLE `lab_maizesample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_mapfeature`
--

DROP TABLE IF EXISTS `lab_mapfeature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_mapfeature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `map_feature_id` varchar(200) NOT NULL,
  `chromosome` varchar(200) NOT NULL,
  `genetic_bin` varchar(200) NOT NULL,
  `physical_map` varchar(200) NOT NULL,
  `genetic_position` varchar(200) NOT NULL,
  `physical_position` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `map_feature_id` (`map_feature_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_mapfeature`
--

LOCK TABLES `lab_mapfeature` WRITE;
/*!40000 ALTER TABLE `lab_mapfeature` DISABLE KEYS */;
INSERT INTO `lab_mapfeature` VALUES (1,'No Map Feature','No Map Feature','No Map Feature','No Map Feature','No Map Feature','No Map Feature','');
/*!40000 ALTER TABLE `lab_mapfeature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_mapfeatureannotation`
--

DROP TABLE IF EXISTS `lab_mapfeatureannotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_mapfeatureannotation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `annotation_type` varchar(200) NOT NULL,
  `annotation_value` varchar(200) NOT NULL,
  `map_feature_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_mapfeatureannotation_bb611cd7` (`map_feature_id`),
  CONSTRAINT `lab_mapfeat_map_feature_id_4a0f52051f6605e1_fk_lab_mapfeature_id` FOREIGN KEY (`map_feature_id`) REFERENCES `lab_mapfeature` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_mapfeatureannotation`
--

LOCK TABLES `lab_mapfeatureannotation` WRITE;
/*!40000 ALTER TABLE `lab_mapfeatureannotation` DISABLE KEYS */;
INSERT INTO `lab_mapfeatureannotation` VALUES (1,'No Annotation','No Annotation',1);
/*!40000 ALTER TABLE `lab_mapfeatureannotation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_mapfeatureexpression`
--

DROP TABLE IF EXISTS `lab_mapfeatureexpression`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_mapfeatureexpression` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `map_feature_interval_id` int(11) NOT NULL,
  `parameter_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_mapfeatureexpression_d251f6f3` (`map_feature_interval_id`),
  KEY `lab_mapfeatureexpression_80740216` (`parameter_id`),
  CONSTRAINT `lab_parameter_id_6ba4d50ff37617e8_fk_lab_measurementparameter_id` FOREIGN KEY (`parameter_id`) REFERENCES `lab_measurementparameter` (`id`),
  CONSTRAINT `D9d2f257f69c205f617816df1c2d4c62` FOREIGN KEY (`map_feature_interval_id`) REFERENCES `lab_mapfeatureinterval` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_mapfeatureexpression`
--

LOCK TABLES `lab_mapfeatureexpression` WRITE;
/*!40000 ALTER TABLE `lab_mapfeatureexpression` DISABLE KEYS */;
INSERT INTO `lab_mapfeatureexpression` VALUES (1,'No Expression','',1,1);
/*!40000 ALTER TABLE `lab_mapfeatureexpression` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_mapfeatureinterval`
--

DROP TABLE IF EXISTS `lab_mapfeatureinterval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_mapfeatureinterval` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `interval_type` varchar(200) NOT NULL,
  `interval_name` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `map_feature_end_id` int(11) NOT NULL,
  `map_feature_start_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_mapfeatureinterval_f0d44331` (`map_feature_end_id`),
  KEY `lab_mapfeatureinterval_c6452281` (`map_feature_start_id`),
  CONSTRAINT `lab_m_map_feature_start_id_681e3442823924b6_fk_lab_mapfeature_id` FOREIGN KEY (`map_feature_start_id`) REFERENCES `lab_mapfeature` (`id`),
  CONSTRAINT `lab_map_map_feature_end_id_311e5f7f19ca5c7f_fk_lab_mapfeature_id` FOREIGN KEY (`map_feature_end_id`) REFERENCES `lab_mapfeature` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_mapfeatureinterval`
--

LOCK TABLES `lab_mapfeatureinterval` WRITE;
/*!40000 ALTER TABLE `lab_mapfeatureinterval` DISABLE KEYS */;
INSERT INTO `lab_mapfeatureinterval` VALUES (1,'No Map Feature Interval','No Map Feature Interval','',1,1);
/*!40000 ALTER TABLE `lab_mapfeatureinterval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_marker`
--

DROP TABLE IF EXISTS `lab_marker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_marker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marker_id` varchar(200) NOT NULL,
  `marker_name` varchar(200) NOT NULL,
  `length` varchar(200) NOT NULL,
  `bac` varchar(200) NOT NULL,
  `nam_marker` varchar(200) NOT NULL,
  `poly_type` varchar(200) NOT NULL,
  `ref_seq` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `strand` varchar(200) NOT NULL,
  `allele` varchar(200) NOT NULL,
  `map_feature_interval_id` int(11) NOT NULL,
  `marker_map_feature_id` int(11) NOT NULL,
  `primer_f_id` int(11),
  `primer_r_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `marker_id` (`marker_id`),
  KEY `lab_marker_d251f6f3` (`map_feature_interval_id`),
  KEY `lab_marker_77376227` (`marker_map_feature_id`),
  KEY `lab_marker_957ba6cd` (`primer_f_id`),
  KEY `lab_marker_6cf2ff0c` (`primer_r_id`),
  CONSTRAINT `lab_marker_primer_r_id_3f07f2cebf20ad1c_fk_lab_primer_id` FOREIGN KEY (`primer_r_id`) REFERENCES `lab_primer` (`id`),
  CONSTRAINT `ec7c42431dd1ae0851e4619dfacf7b48` FOREIGN KEY (`map_feature_interval_id`) REFERENCES `lab_mapfeatureinterval` (`id`),
  CONSTRAINT `lab_marker_primer_f_id_3ccdcc0a1df73048_fk_lab_primer_id` FOREIGN KEY (`primer_f_id`) REFERENCES `lab_primer` (`id`),
  CONSTRAINT `lab__marker_map_feature_id_6053e02576330542_fk_lab_mapfeature_id` FOREIGN KEY (`marker_map_feature_id`) REFERENCES `lab_mapfeature` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_marker`
--

LOCK TABLES `lab_marker` WRITE;
/*!40000 ALTER TABLE `lab_marker` DISABLE KEYS */;
INSERT INTO `lab_marker` VALUES (1,'No Marker','','No Marker','No Marker','No Marker','No Marker','','','','',1,1,1,1);
/*!40000 ALTER TABLE `lab_marker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_measurement`
--

DROP TABLE IF EXISTS `lab_measurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_measurement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_of_measurement` varchar(200) NOT NULL,
  `value` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `measurement_parameter_id` int(11) NOT NULL,
  `obs_tracker_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_measurement_53d07fdc` (`measurement_parameter_id`),
  KEY `lab_measurement_38a17e37` (`obs_tracker_id`),
  KEY `lab_measurement_e8701ad4` (`user_id`),
  CONSTRAINT `lab_measurement_user_id_5833a7aad4b03854_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `D81683983a926190955e52a105acc509` FOREIGN KEY (`measurement_parameter_id`) REFERENCES `lab_measurementparameter` (`id`),
  CONSTRAINT `lab_measure_obs_tracker_id_6840205f62fa5dfb_fk_lab_obstracker_id` FOREIGN KEY (`obs_tracker_id`) REFERENCES `lab_obstracker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_measurement`
--

LOCK TABLES `lab_measurement` WRITE;
/*!40000 ALTER TABLE `lab_measurement` DISABLE KEYS */;
INSERT INTO `lab_measurement` VALUES (1,'No Measurement','No Measurement','',1,1,1);
/*!40000 ALTER TABLE `lab_measurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_measurementparameter`
--

DROP TABLE IF EXISTS `lab_measurementparameter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_measurementparameter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parameter` varchar(200) NOT NULL,
  `parameter_type` varchar(200) NOT NULL,
  `unit_of_measure` varchar(200) NOT NULL,
  `protocol` varchar(1000) NOT NULL,
  `trait_id_buckler` varchar(200) NOT NULL,
  `marker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `parameter` (`parameter`),
  KEY `lab_measurementparameter_945c7b03` (`marker_id`),
  CONSTRAINT `lab_measurementparame_marker_id_83c841bc618b997_fk_lab_marker_id` FOREIGN KEY (`marker_id`) REFERENCES `lab_marker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_measurementparameter`
--

LOCK TABLES `lab_measurementparameter` WRITE;
/*!40000 ALTER TABLE `lab_measurementparameter` DISABLE KEYS */;
INSERT INTO `lab_measurementparameter` VALUES (1,'No Parameter','No Parameter','No Parameter','No Parameter','No Parameter',1),(2,'Germination','Seed','%','/JamannLab/protocols/Germination.txt','',NULL);
/*!40000 ALTER TABLE `lab_measurementparameter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_medium`
--

DROP TABLE IF EXISTS `lab_medium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_medium` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `media_name` varchar(200) NOT NULL,
  `media_type` varchar(200) NOT NULL,
  `media_description` varchar(200) NOT NULL,
  `media_preparation` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `citation_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `media_name` (`media_name`),
  KEY `lab_medium_5710fff7` (`citation_id`),
  CONSTRAINT `lab_medium_citation_id_50b57418e7c9882_fk_lab_citation_id` FOREIGN KEY (`citation_id`) REFERENCES `lab_citation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_medium`
--

LOCK TABLES `lab_medium` WRITE;
/*!40000 ALTER TABLE `lab_medium` DISABLE KEYS */;
INSERT INTO `lab_medium` VALUES (1,'No Medium','No Medium','No Medium','No Medium','',1);
/*!40000 ALTER TABLE `lab_medium` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsculture`
--

DROP TABLE IF EXISTS `lab_obsculture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsculture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `culture_id` varchar(200) NOT NULL,
  `culture_name` varchar(200) NOT NULL,
  `microbe_type` varchar(200) NOT NULL,
  `plating_cycle` varchar(200) NOT NULL,
  `dilution` varchar(200) NOT NULL,
  `image_filename` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  `num_colonies` varchar(200) NOT NULL,
  `num_microbes` varchar(200) NOT NULL,
  `medium_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `culture_id` (`culture_id`),
  KEY `lab_obsculture_c20e5590` (`medium_id`),
  CONSTRAINT `lab_obsculture_medium_id_57b9f479efccff57_fk_lab_medium_id` FOREIGN KEY (`medium_id`) REFERENCES `lab_medium` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsculture`
--

LOCK TABLES `lab_obsculture` WRITE;
/*!40000 ALTER TABLE `lab_obsculture` DISABLE KEYS */;
INSERT INTO `lab_obsculture` VALUES (1,'No Culture','No Culture','No Culture','','','','','','',1);
/*!40000 ALTER TABLE `lab_obsculture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsdna`
--

DROP TABLE IF EXISTS `lab_obsdna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsdna` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dna_id` varchar(200) NOT NULL,
  `extraction_method` varchar(500) NOT NULL,
  `date` varchar(200) NOT NULL,
  `tube_id` varchar(200) NOT NULL,
  `tube_type` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dna_id` (`dna_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsdna`
--

LOCK TABLES `lab_obsdna` WRITE;
/*!40000 ALTER TABLE `lab_obsdna` DISABLE KEYS */;
INSERT INTO `lab_obsdna` VALUES (1,'No DNA','No DNA','No DNA','No DNA','No DNA','');
/*!40000 ALTER TABLE `lab_obsdna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsenv`
--

DROP TABLE IF EXISTS `lab_obsenv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsenv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `environment_id` varchar(200) NOT NULL,
  `longitude` varchar(200) NOT NULL,
  `latitude` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `environment_id` (`environment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsenv`
--

LOCK TABLES `lab_obsenv` WRITE;
/*!40000 ALTER TABLE `lab_obsenv` DISABLE KEYS */;
INSERT INTO `lab_obsenv` VALUES (1,'No Environment','No Environment','No Environment','');
/*!40000 ALTER TABLE `lab_obsenv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsextract`
--

DROP TABLE IF EXISTS `lab_obsextract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsextract` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `extract_id` varchar(200) NOT NULL,
  `weight` varchar(200) NOT NULL,
  `rep` varchar(200) NOT NULL,
  `grind_method` varchar(200) NOT NULL,
  `solvent` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `extract_id` (`extract_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsextract`
--

LOCK TABLES `lab_obsextract` WRITE;
/*!40000 ALTER TABLE `lab_obsextract` DISABLE KEYS */;
INSERT INTO `lab_obsextract` VALUES (1,'No Extract','No Extract','No Extract','No Extract','No Extract','');
/*!40000 ALTER TABLE `lab_obsextract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsmicrobe`
--

DROP TABLE IF EXISTS `lab_obsmicrobe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsmicrobe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `microbe_id` varchar(200) NOT NULL,
  `microbe_type` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `microbe_id` (`microbe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsmicrobe`
--

LOCK TABLES `lab_obsmicrobe` WRITE;
/*!40000 ALTER TABLE `lab_obsmicrobe` DISABLE KEYS */;
INSERT INTO `lab_obsmicrobe` VALUES (1,'No Microbe','No Microbe','');
/*!40000 ALTER TABLE `lab_obsmicrobe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsplant`
--

DROP TABLE IF EXISTS `lab_obsplant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsplant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plant_id` varchar(200) NOT NULL,
  `plant_num` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `plant_id` (`plant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsplant`
--

LOCK TABLES `lab_obsplant` WRITE;
/*!40000 ALTER TABLE `lab_obsplant` DISABLE KEYS */;
INSERT INTO `lab_obsplant` VALUES (1,'No Plant','No Plant','');
/*!40000 ALTER TABLE `lab_obsplant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsplate`
--

DROP TABLE IF EXISTS `lab_obsplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plate_id` varchar(200) NOT NULL,
  `plate_name` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `contents` varchar(200) NOT NULL,
  `rep` varchar(200) NOT NULL,
  `plate_type` varchar(200) NOT NULL,
  `plate_status` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `plate_id` (`plate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsplate`
--

LOCK TABLES `lab_obsplate` WRITE;
/*!40000 ALTER TABLE `lab_obsplate` DISABLE KEYS */;
INSERT INTO `lab_obsplate` VALUES (1,'No Plate','No Plate','No Plate','No Plate','No Plate','No Plate','No Plate','');
/*!40000 ALTER TABLE `lab_obsplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obsrow`
--

DROP TABLE IF EXISTS `lab_obsrow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obsrow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `row_id` varchar(200) NOT NULL,
  `row_name` varchar(200) NOT NULL,
  `range_num` varchar(200) NOT NULL,
  `plot` varchar(200) NOT NULL,
  `block` varchar(200) NOT NULL,
  `rep` varchar(200) NOT NULL,
  `kernel_num` varchar(200) NOT NULL,
  `planting_date` varchar(200) NOT NULL,
  `harvest_date` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `row_id` (`row_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obsrow`
--

LOCK TABLES `lab_obsrow` WRITE;
/*!40000 ALTER TABLE `lab_obsrow` DISABLE KEYS */;
INSERT INTO `lab_obsrow` VALUES (1,'No Row','No Row','No Row','No Row','No Row','No Row','No Row','No Row','No Row','');
/*!40000 ALTER TABLE `lab_obsrow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obssample`
--

DROP TABLE IF EXISTS `lab_obssample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obssample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sample_id` varchar(200) NOT NULL,
  `sample_type` varchar(200) NOT NULL,
  `sample_name` varchar(200) NOT NULL,
  `weight` varchar(200) NOT NULL,
  `volume` varchar(200) NOT NULL,
  `density` varchar(200) NOT NULL,
  `kernel_num` varchar(200) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_id` (`sample_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obssample`
--

LOCK TABLES `lab_obssample` WRITE;
/*!40000 ALTER TABLE `lab_obssample` DISABLE KEYS */;
INSERT INTO `lab_obssample` VALUES (1,'No Sample','No Sample','No Sample','No Sample','No Sample','No Sample','No Sample','No Sample','');
/*!40000 ALTER TABLE `lab_obssample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obstissue`
--

DROP TABLE IF EXISTS `lab_obstissue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obstissue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tissue_id` varchar(200) NOT NULL,
  `tissue_type` varchar(200) NOT NULL,
  `tissue_name` varchar(200) NOT NULL,
  `date_ground` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tissue_id` (`tissue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obstissue`
--

LOCK TABLES `lab_obstissue` WRITE;
/*!40000 ALTER TABLE `lab_obstissue` DISABLE KEYS */;
INSERT INTO `lab_obstissue` VALUES (1,'No Tissue','No Tissue','No Tissue','No Tissue','');
/*!40000 ALTER TABLE `lab_obstissue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obstracker`
--

DROP TABLE IF EXISTS `lab_obstracker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obstracker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `obs_entity_type` varchar(200) NOT NULL,
  `experiment_id` int(11) DEFAULT NULL,
  `field_id` int(11) DEFAULT NULL,
  `isolate_id` int(11) DEFAULT NULL,
  `isolatestock_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `maize_sample_id` int(11) DEFAULT NULL,
  `obs_culture_id` int(11) DEFAULT NULL,
  `obs_dna_id` int(11) DEFAULT NULL,
  `obs_env_id` int(11) DEFAULT NULL,
  `obs_extract_id` int(11) DEFAULT NULL,
  `obs_microbe_id` int(11) DEFAULT NULL,
  `obs_plant_id` int(11) DEFAULT NULL,
  `obs_plate_id` int(11) DEFAULT NULL,
  `obs_row_id` int(11) DEFAULT NULL,
  `obs_sample_id` int(11) DEFAULT NULL,
  `obs_tissue_id` int(11) DEFAULT NULL,
  `obs_well_id` int(11),
  `stock_id` int(11),
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_obstracker_abd1812d` (`experiment_id`),
  KEY `lab_obstracker_3aabf39f` (`field_id`),
  KEY `lab_obstracker_0bcc6cf1` (`isolate_id`),
  KEY `lab_obstracker_f488af03` (`isolatestock_id`),
  KEY `lab_obstracker_e274a5da` (`location_id`),
  KEY `lab_obstracker_c6c49225` (`maize_sample_id`),
  KEY `lab_obstracker_e657b43a` (`obs_culture_id`),
  KEY `lab_obstracker_b5ab3033` (`obs_dna_id`),
  KEY `lab_obstracker_f88a56ec` (`obs_env_id`),
  KEY `lab_obstracker_fc2cb91f` (`obs_extract_id`),
  KEY `lab_obstracker_c8f8c520` (`obs_microbe_id`),
  KEY `lab_obstracker_14a9700c` (`obs_plant_id`),
  KEY `lab_obstracker_f7d618bc` (`obs_plate_id`),
  KEY `lab_obstracker_98bde180` (`obs_row_id`),
  KEY `lab_obstracker_b4a416ac` (`obs_sample_id`),
  KEY `lab_obstracker_6f42fc6b` (`obs_tissue_id`),
  KEY `lab_obstracker_c8760344` (`obs_well_id`),
  KEY `lab_obstracker_aff86b81` (`stock_id`),
  KEY `lab_obstracker_e8701ad4` (`user_id`),
  CONSTRAINT `lab_obstracker_user_id_1d4ef4e7847cc8c9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `lab_obstracker_field_id_3a779c5b37751c11_fk_lab_field_id` FOREIGN KEY (`field_id`) REFERENCES `lab_field` (`id`),
  CONSTRAINT `lab_obstracker_isolate_id_6eff9974ed33b922_fk_lab_isolate_id` FOREIGN KEY (`isolate_id`) REFERENCES `lab_isolate` (`id`),
  CONSTRAINT `lab_obstracker_location_id_178e71b08f730301_fk_lab_location_id` FOREIGN KEY (`location_id`) REFERENCES `lab_location` (`id`),
  CONSTRAINT `lab_obstracker_obs_dna_id_7cd2c0deab68228f_fk_lab_obsdna_id` FOREIGN KEY (`obs_dna_id`) REFERENCES `lab_obsdna` (`id`),
  CONSTRAINT `lab_obstracker_obs_env_id_6b49e5a20968a649_fk_lab_obsenv_id` FOREIGN KEY (`obs_env_id`) REFERENCES `lab_obsenv` (`id`),
  CONSTRAINT `lab_obstracker_obs_plant_id_6be749b0f10b48ad_fk_lab_obsplant_id` FOREIGN KEY (`obs_plant_id`) REFERENCES `lab_obsplant` (`id`),
  CONSTRAINT `lab_obstracker_obs_plate_id_2e0ff1a6308c58c8_fk_lab_obsplate_id` FOREIGN KEY (`obs_plate_id`) REFERENCES `lab_obsplate` (`id`),
  CONSTRAINT `lab_obstracker_obs_row_id_3f6a6e0bef4452a6_fk_lab_obsrow_id` FOREIGN KEY (`obs_row_id`) REFERENCES `lab_obsrow` (`id`),
  CONSTRAINT `lab_obstracker_obs_well_id_5c277f9ab028f32f_fk_lab_obswell_id` FOREIGN KEY (`obs_well_id`) REFERENCES `lab_obswell` (`id`),
  CONSTRAINT `lab_obstracker_stock_id_5301987d47bf9f23_fk_lab_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `lab_stock` (`id`),
  CONSTRAINT `lab_obstracke_obs_sample_id_5e836d6a6acacde9_fk_lab_obssample_id` FOREIGN KEY (`obs_sample_id`) REFERENCES `lab_obssample` (`id`),
  CONSTRAINT `lab_obstracke_obs_tissue_id_69072b052562da70_fk_lab_obstissue_id` FOREIGN KEY (`obs_tissue_id`) REFERENCES `lab_obstissue` (`id`),
  CONSTRAINT `lab_obstrack_experiment_id_1c1534ee29b49eff_fk_lab_experiment_id` FOREIGN KEY (`experiment_id`) REFERENCES `lab_experiment` (`id`),
  CONSTRAINT `lab_obstrac_obs_culture_id_420c318a816bcdd8_fk_lab_obsculture_id` FOREIGN KEY (`obs_culture_id`) REFERENCES `lab_obsculture` (`id`),
  CONSTRAINT `lab_obstrac_obs_extract_id_47f647eefe02de6b_fk_lab_obsextract_id` FOREIGN KEY (`obs_extract_id`) REFERENCES `lab_obsextract` (`id`),
  CONSTRAINT `lab_obstrac_obs_microbe_id_4e00ee0892087d01_fk_lab_obsmicrobe_id` FOREIGN KEY (`obs_microbe_id`) REFERENCES `lab_obsmicrobe` (`id`),
  CONSTRAINT `lab_obstra_maize_sample_id_88e2e3323a29dc1_fk_lab_maizesample_id` FOREIGN KEY (`maize_sample_id`) REFERENCES `lab_maizesample` (`id`),
  CONSTRAINT `lab_obst_isolatestock_id_1b6a1b81f41b03eb_fk_lab_isolatestock_id` FOREIGN KEY (`isolatestock_id`) REFERENCES `lab_isolatestock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obstracker`
--

LOCK TABLES `lab_obstracker` WRITE;
/*!40000 ALTER TABLE `lab_obstracker` DISABLE KEYS */;
INSERT INTO `lab_obstracker` VALUES (7,'isolatestock',2,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5),(9,'stock',2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,5),(10,'experiment',2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5),(11,'isolatestock',1,1,1,4,1,1,NULL,NULL,1,1,NULL,1,NULL,1,1,1,NULL,1,3),(13,'experiment',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3),(14,'stock',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,6),(15,'experiment',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6),(16,'stock',3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,6),(17,'experiment',3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6),(18,'stock',3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6),(19,'stock',3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7,6),(20,'stock',3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,6),(21,'stock',3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,6);
/*!40000 ALTER TABLE `lab_obstracker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obstrackersource`
--

DROP TABLE IF EXISTS `lab_obstrackersource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obstrackersource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relationship` varchar(200) DEFAULT NULL,
  `source_obs_id` int(11) NOT NULL,
  `target_obs_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_obstrackersource_9da38ad3` (`source_obs_id`),
  KEY `lab_obstrackersource_e8a17766` (`target_obs_id`),
  CONSTRAINT `lab_obstrack_target_obs_id_5bae4e59b307074b_fk_lab_obstracker_id` FOREIGN KEY (`target_obs_id`) REFERENCES `lab_obstracker` (`id`),
  CONSTRAINT `lab_obstrack_source_obs_id_7eac41af8eb43b47_fk_lab_obstracker_id` FOREIGN KEY (`source_obs_id`) REFERENCES `lab_obstracker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obstrackersource`
--

LOCK TABLES `lab_obstrackersource` WRITE;
/*!40000 ALTER TABLE `lab_obstrackersource` DISABLE KEYS */;
INSERT INTO `lab_obstrackersource` VALUES (1,NULL,1,1),(6,'isolatestock_stock_from_isolatestock',7,8),(7,'stock_from_experiment',10,9),(9,'stock_from_experiment',15,14),(10,'stock_from_experiment',17,16),(11,'stock_from_experiment',17,18),(12,'stock_from_experiment',17,19),(13,'stock_from_experiment',17,20),(14,'stock_from_experiment',17,21);
/*!40000 ALTER TABLE `lab_obstrackersource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_obswell`
--

DROP TABLE IF EXISTS `lab_obswell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_obswell` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `well_id` varchar(200) NOT NULL,
  `well` varchar(200) NOT NULL,
  `well_inventory` varchar(200) NOT NULL,
  `tube_label` varchar(200) NOT NULL,
  `comments` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `well_id` (`well_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_obswell`
--

LOCK TABLES `lab_obswell` WRITE;
/*!40000 ALTER TABLE `lab_obswell` DISABLE KEYS */;
INSERT INTO `lab_obswell` VALUES (1,'No Well','No Well','No Well','No Well','');
/*!40000 ALTER TABLE `lab_obswell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_passport`
--

DROP TABLE IF EXISTS `lab_passport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_passport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collecting_id` int(11) NOT NULL,
  `people_id` int(11) NOT NULL,
  `taxonomy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_passport_6ed98fb8` (`collecting_id`),
  KEY `lab_passport_a42854b3` (`people_id`),
  KEY `lab_passport_e7be5c2c` (`taxonomy_id`),
  CONSTRAINT `lab_passport_taxonomy_id_21587207e2ced08f_fk_lab_taxonomy_id` FOREIGN KEY (`taxonomy_id`) REFERENCES `lab_taxonomy` (`id`),
  CONSTRAINT `lab_passport_collecting_id_18195ed6ec7e76c8_fk_lab_collecting_id` FOREIGN KEY (`collecting_id`) REFERENCES `lab_collecting` (`id`),
  CONSTRAINT `lab_passport_people_id_3f96ad5b90249eb7_fk_lab_people_id` FOREIGN KEY (`people_id`) REFERENCES `lab_people` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_passport`
--

LOCK TABLES `lab_passport` WRITE;
/*!40000 ALTER TABLE `lab_passport` DISABLE KEYS */;
INSERT INTO `lab_passport` VALUES (2,1,1,2),(3,1,1,3),(4,2,2,4),(5,1,3,5),(6,3,2,6),(7,4,2,6),(8,5,4,7),(9,6,5,6),(10,7,2,6);
/*!40000 ALTER TABLE `lab_passport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_people`
--

DROP TABLE IF EXISTS `lab_people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `organization` varchar(200) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `email` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_people`
--

LOCK TABLES `lab_people` WRITE;
/*!40000 ALTER TABLE `lab_people` DISABLE KEYS */;
INSERT INTO `lab_people` VALUES (2,'','','','','',''),(3,'SHEAN','LIN','UIUC','33333333','3@GMAIL.COM','COM'),(4,'Don','White','UIUC','','','0026:565_01s'),(5,'Don','White','UIUC','','','');
/*!40000 ALTER TABLE `lab_people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_primer`
--

DROP TABLE IF EXISTS `lab_primer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_primer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `primer_id` varchar(200) NOT NULL,
  `primer_name` varchar(200) NOT NULL,
  `primer_tail` varchar(200) NOT NULL,
  `size_range` varchar(200) NOT NULL,
  `temp_min` varchar(200) NOT NULL,
  `temp_max` varchar(200) NOT NULL,
  `order_date` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `primer_id` (`primer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_primer`
--

LOCK TABLES `lab_primer` WRITE;
/*!40000 ALTER TABLE `lab_primer` DISABLE KEYS */;
INSERT INTO `lab_primer` VALUES (1,'No Primer','No Primer','','','','','','');
/*!40000 ALTER TABLE `lab_primer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_publication`
--

DROP TABLE IF EXISTS `lab_publication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_publication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publisher` varchar(200) NOT NULL,
  `name_of_paper` varchar(200) NOT NULL,
  `publish_date` date NOT NULL,
  `publication_info` varchar(200) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_of_paper` (`name_of_paper`),
  KEY `lab_publication_e8701ad4` (`user_id`),
  CONSTRAINT `lab_publication_user_id_1aae846eac8609b6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_publication`
--

LOCK TABLES `lab_publication` WRITE;
/*!40000 ALTER TABLE `lab_publication` DISABLE KEYS */;
INSERT INTO `lab_publication` VALUES (1,'No Publication','No Publication','0000-00-00','',1);
/*!40000 ALTER TABLE `lab_publication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_qtl`
--

DROP TABLE IF EXISTS `lab_qtl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_qtl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comments` varchar(1000) NOT NULL,
  `map_feature_interval_id` int(11) NOT NULL,
  `parameter_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_qtl_d251f6f3` (`map_feature_interval_id`),
  KEY `lab_qtl_80740216` (`parameter_id`),
  CONSTRAINT `lab_parameter_id_4e4a2f1a185b61b0_fk_lab_measurementparameter_id` FOREIGN KEY (`parameter_id`) REFERENCES `lab_measurementparameter` (`id`),
  CONSTRAINT `ea213a2a7f2d89a020e434115b09b016` FOREIGN KEY (`map_feature_interval_id`) REFERENCES `lab_mapfeatureinterval` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_qtl`
--

LOCK TABLES `lab_qtl` WRITE;
/*!40000 ALTER TABLE `lab_qtl` DISABLE KEYS */;
INSERT INTO `lab_qtl` VALUES (1,'No QTL',1,1);
/*!40000 ALTER TABLE `lab_qtl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_separation`
--

DROP TABLE IF EXISTS `lab_separation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_separation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `separation_type` varchar(200) NOT NULL,
  `apparatus` varchar(200) NOT NULL,
  `SG` varchar(200) NOT NULL,
  `light_weight` varchar(200) NOT NULL,
  `intermediate_weight` varchar(200) NOT NULL,
  `heavy_weight` varchar(200) NOT NULL,
  `light_percent` varchar(200) NOT NULL,
  `intermediate_percent` varchar(200) NOT NULL,
  `heavy_percent` varchar(200) NOT NULL,
  `operating_factor` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `obs_sample_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_separation_b4a416ac` (`obs_sample_id`),
  CONSTRAINT `lab_separatio_obs_sample_id_50780f2b9eaebe25_fk_lab_obssample_id` FOREIGN KEY (`obs_sample_id`) REFERENCES `lab_obssample` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_separation`
--

LOCK TABLES `lab_separation` WRITE;
/*!40000 ALTER TABLE `lab_separation` DISABLE KEYS */;
INSERT INTO `lab_separation` VALUES (1,'No Separation','No Separation','No Separation','No Separation','No Separation','No Separation','No Separation','No Separation','No Separation','No Separation','',1);
/*!40000 ALTER TABLE `lab_separation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_stock`
--

DROP TABLE IF EXISTS `lab_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seed_id` varchar(200) NOT NULL,
  `seed_name` varchar(200) NOT NULL,
  `cross_type` varchar(200) NOT NULL,
  `pedigree` varchar(200) NOT NULL,
  `stock_status` varchar(200) NOT NULL,
  `stock_date` varchar(200) NOT NULL,
  `inoculated` tinyint(1) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `passport_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `seed_id` (`seed_id`),
  KEY `lab_stock_71116643` (`passport_id`),
  CONSTRAINT `lab_stock_passport_id_12dc2e4e982ebdcf_fk_lab_passport_id` FOREIGN KEY (`passport_id`) REFERENCES `lab_passport` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_stock`
--

LOCK TABLES `lab_stock` WRITE;
/*!40000 ALTER TABLE `lab_stock` DISABLE KEYS */;
INSERT INTO `lab_stock` VALUES (2,'15XX001','B666','self','B73 x 666','','',0,'',4),(4,'00DI001_001b','B73','bulk','?','','',0,'',7),(5,'00DI0002_002s','','Self','?','','',0,'',8),(6,'002:565_01s','b73','self','?','','',0,'',9),(7,'002:565_02s','b73','SELF','?','','',0,'',10),(8,'002:565_03s','b73','self','?','','',0,'',10),(9,'002:565_00b','b73','bulk','?','','',0,'',10);
/*!40000 ALTER TABLE `lab_stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_stockpacket`
--

DROP TABLE IF EXISTS `lab_stockpacket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_stockpacket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weight` varchar(200) NOT NULL,
  `num_seeds` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `location_id` int(11) NOT NULL,
  `stock_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_stockpacket_e274a5da` (`location_id`),
  KEY `lab_stockpacket_aff86b81` (`stock_id`),
  CONSTRAINT `lab_stockpacket_stock_id_328c21605d036254_fk_lab_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `lab_stock` (`id`),
  CONSTRAINT `lab_stockpacket_location_id_6da26476fa72152a_fk_lab_location_id` FOREIGN KEY (`location_id`) REFERENCES `lab_location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_stockpacket`
--

LOCK TABLES `lab_stockpacket` WRITE;
/*!40000 ALTER TABLE `lab_stockpacket` DISABLE KEYS */;
INSERT INTO `lab_stockpacket` VALUES (2,'','100','',3,2),(6,'','','',6,4),(7,'','','',10,6);
/*!40000 ALTER TABLE `lab_stockpacket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_taxonomy`
--

DROP TABLE IF EXISTS `lab_taxonomy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_taxonomy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `binomial` varchar(200) NOT NULL,
  `population` varchar(200) NOT NULL,
  `common_name` varchar(200) NOT NULL,
  `alias` varchar(200) NOT NULL,
  `race` varchar(200) NOT NULL,
  `subtaxa` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_taxonomy`
--

LOCK TABLES `lab_taxonomy` WRITE;
/*!40000 ALTER TABLE `lab_taxonomy` DISABLE KEYS */;
INSERT INTO `lab_taxonomy` VALUES (2,'','','IsolateStock','','',''),(3,'Setosphaeria turcica','','IsolateStock','Exerohilum turcicum','',''),(4,'Zea','','Maize','NULL','NULL','NULL'),(5,'GENUS','','IsolateStock','ALIAS','RACE','SUB'),(6,'','','Maize','NULL','NULL','NULL'),(7,'Zea / Mays','Illinois Pathology Panel','Maize','NULL','NULL','NULL');
/*!40000 ALTER TABLE `lab_taxonomy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_treatment`
--

DROP TABLE IF EXISTS `lab_treatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_treatment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `treatment_id` varchar(200) NOT NULL,
  `treatment_type` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `experiment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `treatment_id` (`treatment_id`),
  KEY `lab_treatment_abd1812d` (`experiment_id`),
  CONSTRAINT `lab_treatment_experiment_id_db1ccff1aaf1d34_fk_lab_experiment_id` FOREIGN KEY (`experiment_id`) REFERENCES `lab_experiment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_treatment`
--

LOCK TABLES `lab_treatment` WRITE;
/*!40000 ALTER TABLE `lab_treatment` DISABLE KEYS */;
INSERT INTO `lab_treatment` VALUES (1,'No Treatment','No Treatment','No Treatment','',1);
/*!40000 ALTER TABLE `lab_treatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_uploadqueue`
--

DROP TABLE IF EXISTS `lab_uploadqueue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_uploadqueue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(100) NOT NULL,
  `upload_type` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `completed` tinyint(1) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `comments` varchar(1000) NOT NULL,
  `experiment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_uploadqueue_abd1812d` (`experiment_id`),
  KEY `lab_uploadqueue_e8701ad4` (`user_id`),
  CONSTRAINT `lab_uploadqueue_user_id_1086a8f9b27eca9c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `lab_uploadque_experiment_id_9dc776a75b6ecc6_fk_lab_experiment_id` FOREIGN KEY (`experiment_id`) REFERENCES `lab_experiment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_uploadqueue`
--

LOCK TABLES `lab_uploadqueue` WRITE;
/*!40000 ALTER TABLE `lab_uploadqueue` DISABLE KEYS */;
/*!40000 ALTER TABLE `lab_uploadqueue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_userprofile`
--

DROP TABLE IF EXISTS `lab_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `website` varchar(250) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `organization` varchar(200) NOT NULL,
  `notes` varchar(1000) NOT NULL,
  `job_title` varchar(200) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `lab_userprofile_user_id_180e14b8e1cf2164_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_userprofile`
--

LOCK TABLES `lab_userprofile` WRITE;
/*!40000 ALTER TABLE `lab_userprofile` DISABLE KEYS */;
INSERT INTO `lab_userprofile` VALUES (3,'https://github.com/slin63','profile_images/512aTeupRIL._SL500_AA280__5bhR9UK.jpg','510-495-7455','UIUC','','Site Admin',3),(4,'','profile_images/underwater.jpg','8472801592','University of Illinois','','',4),(5,'','profile_images/underwater.jpg','2172654526','University of Illinois','','',5),(6,'','profile_images/underwater.jpg','999999999','UIUC','','',6),(7,'','profile_images/underwater.jpg','16262151307','meh','','',7);
/*!40000 ALTER TABLE `lab_userprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-01 21:31:46
