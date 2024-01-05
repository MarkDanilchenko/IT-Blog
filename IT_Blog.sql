-- MySQL dump 10.13  Distrib 8.0.33, for macos13.3 (arm64)
--
-- Host: localhost    Database: IT_Blog
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add User',6,'add_user'),(22,'Can change User',6,'change_user'),(23,'Can delete User',6,'delete_user'),(24,'Can view User',6,'view_user'),(25,'Can add Post',7,'add_post'),(26,'Can change Post',7,'change_post'),(27,'Can delete Post',7,'delete_post'),(28,'Can view Post',7,'view_post'),(29,'Can add tag',8,'add_tag'),(30,'Can change tag',8,'change_tag'),(31,'Can delete tag',8,'delete_tag'),(32,'Can view tag',8,'view_tag'),(33,'Can add tagged item',9,'add_taggeditem'),(34,'Can change tagged item',9,'change_taggeditem'),(35,'Can delete tagged item',9,'delete_taggeditem'),(36,'Can view tagged item',9,'view_taggeditem'),(37,'Can add Post_Comment',10,'add_post_comment'),(38,'Can change Post_Comment',10,'change_post_comment'),(39,'Can delete Post_Comment',10,'delete_post_comment'),(40,'Can view Post_Comment',10,'view_post_comment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Blog__main_post`
--

DROP TABLE IF EXISTS `Blog__main_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Blog__main_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `h1` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `url` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `content` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `author_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Blog__main_post_author_id_ee0b3476_fk_Blog__main_user_id` (`author_id`),
  KEY `Blog__main_post_url_f490c0e6` (`url`),
  CONSTRAINT `Blog__main_post_author_id_ee0b3476_fk_Blog__main_user_id` FOREIGN KEY (`author_id`) REFERENCES `Blog__main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Blog__main_post`
--

LOCK TABLES `Blog__main_post` WRITE;
/*!40000 ALTER TABLE `Blog__main_post` DISABLE KEYS */;
INSERT INTO `Blog__main_post` VALUES (5,'Python','About Python','about-python','<p>A few words about Python.</p>','<p>A high-level general-purpose programming language with dynamic strict typing and automatic memory management, aimed at improving developer productivity, code readability and quality, as well as ensuring the portability of programs written in it.</p>\r\n\r\n<p>The language is completely object-oriented in the sense that everything is objects.</p>\r\n\r\n<p>An unusual feature of the language is the indentation of code blocks.</p>\r\n\r\n<p>The syntax of the language core is minimalistic, due to which in practice there is rarely a need to refer to documentation.</p>','IMG/Python_logo.png','2024-01-05 11:12:03.816934',1),(6,'Webpack','About Webpack','about-webpack','<p>A few words about Webpack.</p>','<p>Webpack is a module bundler.</p>\r\n\r\n<p>Its main purpose is to bundle JavaScript files for usage in a browser, yet it is also capable of transforming, bundling, or packaging just about any resource or asset.</p>','IMG/Webpack_logo.png','2024-01-05 11:34:30.489872',1),(7,'JavaScript','About JavaScript','about-javascript','<p>A few words about JavaScript.</p>','<p>JavaScript is a multi&mdash;paradigm programming language. Supports object-oriented, imperative, and functional styles.</p>\r\n\r\n<p>A release using ECMAScript (ECMA-262 standard) is used. JavaScript is commonly used as an embedded language</p>\r\n\r\n<p>for software that is accessible to all users. It is most widely used in browsers as a scripting language for making web pages interactive.</p>','IMG/JavaScript_logo.png','2024-01-05 11:36:06.329121',1),(8,'MySQL','About MySQL','about-mysql','<p>A few words about MySQL.</p>','<p>A free relational database management system.</p>\r\n\r\n<p>MySQL is developed and supported by Oracle Corporation, which acquired the Swedish company MySQL AB.</p>\r\n\r\n<p>The product is distributed both under the GNU General Public License and under its own commercial license.</p>\r\n\r\n<p>MySQL is a solution for small and medium-sized applications. It is usually used as a server accessed by local or remote clients. However, the distribution package includes an internal server library that allows you to include MySQL in standalone programs.</p>','IMG/MySQL_logo.png','2024-01-05 11:37:30.172472',1),(9,'Bootstrap5','About Bootstrap5','about-bootstrap5','<p>A few words about Bootstrap5.</p>','<p>A free set of tools for creating websites and web applications.</p>\r\n\r\n<p>It includes HTML and CSS design templates for typography, web forms, buttons, labels, navigation blocks and other web interface components, including</p>\r\n\r\n<p>JavaScript extensions.</p>','IMG/Bootstrap_logo_PkWY837.png','2024-01-05 11:40:01.148184',1),(10,'NuxtJS','About NuxtJS','about-nuxtjs','<p>A few words about NuxtJS.</p>','<p>A high-level framework based on Vue.js, which allows you to develop isomorphic web applications out of the box, abstracting the details of the distribution of server and client code.</p>','IMG/NuxtJS_logo.png','2024-01-05 11:41:26.596245',1);
/*!40000 ALTER TABLE `Blog__main_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Blog__main_post_comment`
--

DROP TABLE IF EXISTS `Blog__main_post_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Blog__main_post_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `post_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Blog__main_post_comment_post_id_239c6280_fk_Blog__main_post_id` (`post_id`),
  KEY `Blog__main_post_comment_user_id_16ebdfcc_fk_Blog__main_user_id` (`user_id`),
  CONSTRAINT `Blog__main_post_comment_post_id_239c6280_fk_Blog__main_post_id` FOREIGN KEY (`post_id`) REFERENCES `Blog__main_post` (`id`),
  CONSTRAINT `Blog__main_post_comment_user_id_16ebdfcc_fk_Blog__main_user_id` FOREIGN KEY (`user_id`) REFERENCES `Blog__main_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Blog__main_post_comment`
--

LOCK TABLES `Blog__main_post_comment` WRITE;
/*!40000 ALTER TABLE `Blog__main_post_comment` DISABLE KEYS */;
INSERT INTO `Blog__main_post_comment` VALUES (73,'First comment...','2024-01-05 13:40:50.141301',9,1),(74,'Second comment...','2024-01-05 13:41:11.057439',9,1);
/*!40000 ALTER TABLE `Blog__main_post_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Blog__main_user`
--

DROP TABLE IF EXISTS `Blog__main_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Blog__main_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Blog__main_user`
--

LOCK TABLES `Blog__main_user` WRITE;
/*!40000 ALTER TABLE `Blog__main_user` DISABLE KEYS */;
INSERT INTO `Blog__main_user` VALUES (1,'pbkdf2_sha256$720000$ySAhlYtpuu3hCxshRAyb2t$IVBUUkMMqFkCVJ8UL+MQ5HOlsmbdqw/DDEerpulbkrw=','2024-01-07 14:56:30.024470',1,'admin','','','',1,1,'2023-12-28 14:04:07.573111',NULL);
/*!40000 ALTER TABLE `Blog__main_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Blog__main_user_groups`
--

DROP TABLE IF EXISTS `Blog__main_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Blog__main_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Blog__main_user_groups_user_id_group_id_743d6e6c_uniq` (`user_id`,`group_id`),
  KEY `Blog__main_user_groups_group_id_a0fabca8_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Blog__main_user_groups_group_id_a0fabca8_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `Blog__main_user_groups_user_id_96a331ad_fk_Blog__main_user_id` FOREIGN KEY (`user_id`) REFERENCES `Blog__main_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Blog__main_user_groups`
--

LOCK TABLES `Blog__main_user_groups` WRITE;
/*!40000 ALTER TABLE `Blog__main_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `Blog__main_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Blog__main_user_user_permissions`
--

DROP TABLE IF EXISTS `Blog__main_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Blog__main_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Blog__main_user_user_per_user_id_permission_id_05071a4a_uniq` (`user_id`,`permission_id`),
  KEY `Blog__main_user_user_permission_id_0c13f857_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Blog__main_user_user_permission_id_0c13f857_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `Blog__main_user_user_user_id_58d93831_fk_Blog__mai` FOREIGN KEY (`user_id`) REFERENCES `Blog__main_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Blog__main_user_user_permissions`
--

LOCK TABLES `Blog__main_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `Blog__main_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Blog__main_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Blog__main_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Blog__main_user_id` FOREIGN KEY (`user_id`) REFERENCES `Blog__main_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-28 21:00:48.634013','1','LoremPost',1,'[{\"added\": {}}]',7,1),(2,'2023-12-28 21:05:21.113107','2','testLorem2',1,'[{\"added\": {}}]',7,1),(3,'2023-12-28 21:06:02.364132','2','LoremPost2',2,'[{\"changed\": {\"fields\": [\"Title\"]}}]',7,1),(4,'2023-12-28 21:06:31.138373','2','LoremPost2',2,'[{\"changed\": {\"fields\": [\"URL\"]}}]',7,1),(5,'2023-12-29 15:36:16.705399','2','LoremPost2',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(6,'2023-12-29 16:09:37.068134','3','LoremPost3',1,'[{\"added\": {}}]',7,1),(7,'2023-12-29 16:10:24.455590','4','LoremPost4',1,'[{\"added\": {}}]',7,1),(8,'2023-12-29 16:11:46.608559','3','LoremPost3',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',7,1),(9,'2023-12-29 16:12:02.784448','4','LoremPost4',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',7,1),(10,'2023-12-29 16:12:22.343807','2','LoremPost2',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(11,'2023-12-30 21:16:21.310669','2','Mary, ID: (2)',3,'',6,1),(12,'2023-12-30 21:56:44.024738','3','Mary, ID: (3)',3,'',6,1),(13,'2024-01-02 22:29:05.238584','1','LoremPost',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',7,1),(14,'2024-01-02 22:37:18.249093','2','LoremPost2',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',7,1),(15,'2024-01-02 22:37:35.347777','3','LoremPost3',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',7,1),(16,'2024-01-02 22:37:47.796200','4','LoremPost4',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',7,1),(17,'2024-01-04 16:37:56.928902','11','Hello3...',3,'',10,1),(18,'2024-01-04 16:37:56.931857','10','Hello3...',3,'',10,1),(19,'2024-01-04 16:37:56.933603','9','Hello3...',3,'',10,1),(20,'2024-01-04 16:37:56.935220','8','Hello3...',3,'',10,1),(21,'2024-01-04 16:37:56.937126','7','Hello3...',3,'',10,1),(22,'2024-01-04 16:37:56.938976','6','Hello...',3,'',10,1),(23,'2024-01-04 16:37:56.941007','5','Hello...',3,'',10,1),(24,'2024-01-04 16:37:56.942650','4','Hello...',3,'',10,1),(25,'2024-01-04 16:37:56.943495','3','Hello...',3,'',10,1),(26,'2024-01-04 16:37:56.944146','2','Hello...',3,'',10,1),(27,'2024-01-04 16:37:56.944716','1','gc...',3,'',10,1),(28,'2024-01-04 16:41:40.998678','15','hgfknfd...',3,'',10,1),(29,'2024-01-04 16:41:41.001837','14','hgfknfd...',3,'',10,1),(30,'2024-01-04 16:41:41.003888','13','Hello3...',3,'',10,1),(31,'2024-01-04 16:41:41.005201','12','Hello3...',3,'',10,1),(32,'2024-01-04 16:56:36.615028','40','First comment...',3,'',10,1),(33,'2024-01-04 16:56:36.617317','39','First comment...',3,'',10,1),(34,'2024-01-04 16:56:36.618669','38','First comment...',3,'',10,1),(35,'2024-01-04 16:56:36.619908','37','First comment...',3,'',10,1),(36,'2024-01-04 16:56:36.621042','36','First comment...',3,'',10,1),(37,'2024-01-04 16:56:36.622558','35','First comment...',3,'',10,1),(38,'2024-01-04 16:56:36.623724','34','First comment...',3,'',10,1),(39,'2024-01-04 16:56:36.624705','33','First comment...',3,'',10,1),(40,'2024-01-04 16:56:36.625817','32','First comment...',3,'',10,1),(41,'2024-01-04 16:56:36.627139','31','First comment...',3,'',10,1),(42,'2024-01-04 16:56:36.628607','30','First comment...',3,'',10,1),(43,'2024-01-04 16:56:36.630359','29','First comment...',3,'',10,1),(44,'2024-01-04 16:56:36.631919','28','First comment...',3,'',10,1),(45,'2024-01-04 16:56:36.633915','27','First comment...',3,'',10,1),(46,'2024-01-04 16:56:36.634934','26','First comment...',3,'',10,1),(47,'2024-01-04 16:56:36.635815','25','First comment...',3,'',10,1),(48,'2024-01-04 16:56:36.637326','24','First comment...',3,'',10,1),(49,'2024-01-04 16:56:36.638568','23','First comment...',3,'',10,1),(50,'2024-01-04 16:56:36.639524','22','First comment...',3,'',10,1),(51,'2024-01-04 16:56:36.641097','21','First comment...',3,'',10,1),(52,'2024-01-04 16:56:36.642166','20','First comment...',3,'',10,1),(53,'2024-01-04 16:56:36.643461','19','First comment...',3,'',10,1),(54,'2024-01-04 16:56:36.644586','18','First comment...',3,'',10,1),(55,'2024-01-04 16:56:36.645512','17','First comment...',3,'',10,1),(56,'2024-01-04 16:56:36.646686','16','First comment...',3,'',10,1),(57,'2024-01-04 17:08:58.543164','57','fsjbdfhjdsc...',3,'',10,1),(58,'2024-01-04 17:08:58.545841','56','fsjbdfhjdsc...',3,'',10,1),(59,'2024-01-04 17:08:58.547206','55','fsjbdfhjdsc...',3,'',10,1),(60,'2024-01-04 17:08:58.548214','54','fsjbdfhjdsc...',3,'',10,1),(61,'2024-01-04 17:08:58.549186','53','ggg...',3,'',10,1),(62,'2024-01-04 17:08:58.550080','52','ggg...',3,'',10,1),(63,'2024-01-04 17:08:58.550765','51','ggg...',3,'',10,1),(64,'2024-01-04 17:08:58.551507','50','ggg...',3,'',10,1),(65,'2024-01-04 17:08:58.552448','49','ggg...',3,'',10,1),(66,'2024-01-04 17:08:58.553503','48','hghghff...',3,'',10,1),(67,'2024-01-04 17:08:58.554601','47','hghghff...',3,'',10,1),(68,'2024-01-04 17:08:58.555642','46','hghghff...',3,'',10,1),(69,'2024-01-04 17:08:58.556693','45','hghgh...',3,'',10,1),(70,'2024-01-04 17:08:58.558856','44','hghgh...',3,'',10,1),(71,'2024-01-04 17:08:58.561532','43','hghgh...',3,'',10,1),(72,'2024-01-04 17:08:58.562462','42','First comment here...',3,'',10,1),(73,'2024-01-04 17:08:58.563146','41','First comment here...',3,'',10,1),(74,'2024-01-04 17:21:03.798374','64','22222...',3,'',10,1),(75,'2024-01-04 17:21:03.800764','63','22222...',3,'',10,1),(76,'2024-01-04 17:21:03.802694','62','22222...',3,'',10,1),(77,'2024-01-04 17:21:03.804568','61','22222...',3,'',10,1),(78,'2024-01-04 17:21:03.809517','60','22222...',3,'',10,1),(79,'2024-01-04 17:21:03.811460','59','fsjbdfhjdsc...',3,'',10,1),(80,'2024-01-04 17:21:03.813092','58','fsjbdfhjdsc...',3,'',10,1),(81,'2024-01-04 19:56:45.186439','71','sjcsjdc scdl;smcdls...',3,'',10,1),(82,'2024-01-04 19:56:45.189784','70','sjcsjdc scdl;smcdls...',3,'',10,1),(83,'2024-01-04 19:56:45.190885','69','sjcsjdc scdl;smcdls...',3,'',10,1),(84,'2024-01-04 19:56:45.192054','68','hukil...',3,'',10,1),(85,'2024-01-04 19:56:45.193235','67','7777...',3,'',10,1),(86,'2024-01-04 19:56:45.194292','66','7777...',3,'',10,1),(87,'2024-01-04 19:56:45.195636','65','22222...',3,'',10,1),(88,'2024-01-05 10:11:14.054608','4','Mary, ID: (4)',3,'',6,1),(89,'2024-01-05 10:11:57.471197','4','Mary, ID: (4)',3,'',6,1),(90,'2024-01-05 10:17:11.158934','5','Mary, ID: (5)',3,'',6,1),(91,'2024-01-05 10:19:05.164724','6','Mary, ID: (6)',3,'',6,1),(92,'2024-01-05 10:30:48.337894','72','First comment here.....',3,'',10,1),(93,'2024-01-05 10:34:32.182886','4','LoremPost4',3,'',7,1),(94,'2024-01-05 10:34:32.186626','3','LoremPost3',3,'',7,1),(95,'2024-01-05 10:34:32.188037','2','LoremPost2',3,'',7,1),(96,'2024-01-05 10:34:32.189428','1','LoremPost',3,'',7,1),(97,'2024-01-05 11:12:03.827819','5','About Python',1,'[{\"added\": {}}]',7,1),(98,'2024-01-05 11:34:30.509102','6','About Webpack',1,'[{\"added\": {}}]',7,1),(99,'2024-01-05 11:36:06.338349','7','About JavaScript',1,'[{\"added\": {}}]',7,1),(100,'2024-01-05 11:37:30.181040','8','About MySQL',1,'[{\"added\": {}}]',7,1),(101,'2024-01-05 11:40:01.166284','9','About Bootstrap5',1,'[{\"added\": {}}]',7,1),(102,'2024-01-05 11:41:26.612556','10','About NuxtJS',1,'[{\"added\": {}}]',7,1),(103,'2024-01-05 11:44:44.663694','11','bhjb',1,'[{\"added\": {}}]',7,1),(104,'2024-01-05 11:52:56.935681','11','bhjb',3,'',7,1),(105,'2024-01-07 14:57:01.849942','13','nuxjs',3,'',8,1),(106,'2024-01-07 14:57:07.604638','5','bootstrap',3,'',8,1),(107,'2024-01-07 14:57:49.984014','73','First comment......',2,'[{\"changed\": {\"fields\": [\"Comment\"]}}]',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(7,'Blog__main','post'),(10,'Blog__main','post_comment'),(6,'Blog__main','user'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(8,'taggit','tag'),(9,'taggit','taggeditem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-28 14:03:34.949326'),(2,'contenttypes','0002_remove_content_type_name','2023-12-28 14:03:34.961105'),(3,'auth','0001_initial','2023-12-28 14:03:34.999374'),(4,'auth','0002_alter_permission_name_max_length','2023-12-28 14:03:35.014966'),(5,'auth','0003_alter_user_email_max_length','2023-12-28 14:03:35.017487'),(6,'auth','0004_alter_user_username_opts','2023-12-28 14:03:35.019701'),(7,'auth','0005_alter_user_last_login_null','2023-12-28 14:03:35.021574'),(8,'auth','0006_require_contenttypes_0002','2023-12-28 14:03:35.021958'),(9,'auth','0007_alter_validators_add_error_messages','2023-12-28 14:03:35.023753'),(10,'auth','0008_alter_user_username_max_length','2023-12-28 14:03:35.025517'),(11,'auth','0009_alter_user_last_name_max_length','2023-12-28 14:03:35.027296'),(12,'auth','0010_alter_group_name_max_length','2023-12-28 14:03:35.033659'),(13,'auth','0011_update_proxy_permissions','2023-12-28 14:03:35.036073'),(14,'auth','0012_alter_user_first_name_max_length','2023-12-28 14:03:35.037850'),(15,'Blog__main','0001_initial','2023-12-28 14:03:35.083327'),(16,'admin','0001_initial','2023-12-28 14:03:35.108058'),(17,'admin','0002_logentry_remove_auto_add','2023-12-28 14:03:35.111198'),(18,'admin','0003_logentry_add_action_flag_choices','2023-12-28 14:03:35.113753'),(19,'sessions','0001_initial','2023-12-28 14:03:35.118815'),(20,'Blog__main','0002_post','2023-12-28 20:01:37.731192'),(21,'Blog__main','0003_alter_post_image_alter_post_url','2023-12-28 21:00:29.038890'),(22,'Blog__main','0004_alter_user_phone_alter_user_username','2023-12-30 20:42:04.459767'),(23,'Blog__main','0005_alter_user_phone','2023-12-30 20:59:26.953542'),(24,'taggit','0001_initial','2024-01-02 22:23:31.283171'),(25,'taggit','0002_auto_20150616_2121','2024-01-02 22:23:31.288803'),(26,'taggit','0003_taggeditem_add_unique_index','2024-01-02 22:23:31.296409'),(27,'taggit','0004_alter_taggeditem_content_type_alter_taggeditem_tag','2024-01-02 22:23:31.304221'),(28,'taggit','0005_auto_20220424_2025','2024-01-02 22:23:31.305539'),(29,'taggit','0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx','2024-01-02 22:23:31.316389'),(30,'Blog__main','0006_remove_post_tag_post_tag','2024-01-02 22:23:31.327562'),(31,'Blog__main','0007_post_comment','2024-01-03 20:31:11.385221'),(32,'Blog__main','0008_alter_post_comment_text_alter_post_comment_user','2024-01-04 14:27:33.703841');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2loukadp9xfepj65uze2etkz26iik7tw','.eJxVjDsOwjAQBe_iGln-rT-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWHkFlCtoboZID60GY5IhqcATeBEkKCC0kicG7pEWtxWoJVVsMqIm9P8saN4Y:1rLPNQ:tA1LumiXVDgNi9wTLKwz3I6Pq-Lsfauf5Ff-Pyf629o','2024-01-18 15:11:20.876102'),('4tvamnoejzj6ysr49fyesb9h7qzlkwub','.eJxVjDsOwyAQBe9CHSEvHxtSpvcZ0MIuwUmEJWNXUe4eIblI2jcz7y0CHnsJR-MtLCSuQovL7xYxPbl2QA-s91Wmte7bEmVX5EmbnFfi1-10_w4KttLrbKzznAwhMaoImLRP4E3EOI1msOQgASoGGsGwz2iV1npwFCE7nsTnCwyDOIY:1rJgiu:ga9mAtfj2gZmj1EhUrZyBr0bpWVz6HHJRK2vC5se79s','2024-01-13 21:18:24.140577'),('atgeh3d6dkf2ivbacn0d7tjwujwcn0jn','.eJxVjDsOwjAQBe_iGln-rT-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWHkFlCtoboZID60GY5IhqcATeBEkKCC0kicG7pEWtxWoJVVsMqIm9P8saN4Y:1rJhmL:I4RIyg33YjoFqd0TuL1exXdjO7-zoed53LMXpQ8atbA','2024-01-13 22:26:01.729792'),('f4e1a02qjrir8zaenc37eip09u1xrgba','.eJxVjDsOwjAQBe_iGln-rT-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWHkFlCtoboZID60GY5IhqcATeBEkKCC0kicG7pEWtxWoJVVsMqIm9P8saN4Y:1rLhI3:h8zPlolrVye61tYsO57hCPC3aGP_XRl29MjLKFoak9M','2024-01-19 10:18:59.320681'),('hv0d8iev61snacwhv3vyk7w5fq436ktm','.eJxVjMsOwiAQRf-FtSHlDS7d-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7Mw0O_1uCfKD2g7wDu3Wee5tXebEd4UfdPBrR3peDvfvoMKo3zpPydtiUKigtHOS_JQkyBSMEhl0kMUHtFpoB84XkhaF08l5D0RoArL3B8ztN48:1rJhKS:Sgzt4wLCZbJ73TGV65kJTTXxnkvzTxvMNPE7KvoYz2E','2024-01-13 21:57:12.289395'),('wqkpdmt9e53tekg22jr0frrcniwjok3o','e30:1rJgeh:UT0RJSSYTQ-9ilxNOIjjbV30DKWuZ8iKsJczTbi-A1Q','2024-01-13 21:14:03.747234');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taggit_tag`
--

DROP TABLE IF EXISTS `taggit_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taggit_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taggit_tag`
--

LOCK TABLES `taggit_tag` WRITE;
/*!40000 ALTER TABLE `taggit_tag` DISABLE KEYS */;
INSERT INTO `taggit_tag` VALUES (1,'css','css'),(2,'drf','drf'),(3,'django','django'),(4,'scss','scss'),(6,'nuxtjs','nuxtjs'),(7,'webpack','webpack'),(8,'python','python'),(9,'js','js'),(10,'mysql','mysql'),(11,'html','html'),(12,'bootstrap5','bootstrap5');
/*!40000 ALTER TABLE `taggit_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taggit_taggeditem`
--

DROP TABLE IF EXISTS `taggit_taggeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taggit_taggeditem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `object_id` int NOT NULL,
  `content_type_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uniq` (`content_type_id`,`object_id`,`tag_id`),
  KEY `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` (`tag_id`),
  KEY `taggit_taggeditem_object_id_e2d7d1df` (`object_id`),
  KEY `taggit_tagg_content_8fc721_idx` (`content_type_id`,`object_id`),
  CONSTRAINT `taggit_taggeditem_content_type_id_9957a03c_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `taggit_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taggit_taggeditem`
--

LOCK TABLES `taggit_taggeditem` WRITE;
/*!40000 ALTER TABLE `taggit_taggeditem` DISABLE KEYS */;
INSERT INTO `taggit_taggeditem` VALUES (12,5,7,2),(13,5,7,3),(11,5,7,8),(14,6,7,1),(16,6,7,7),(15,6,7,9),(17,7,7,9),(18,8,7,10),(19,9,7,1),(21,9,7,4),(20,9,7,11),(22,9,7,12),(23,10,7,9);
/*!40000 ALTER TABLE `taggit_taggeditem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-07 18:14:25
