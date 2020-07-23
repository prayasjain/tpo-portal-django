-- MySQL dump 10.13  Distrib 5.5.50, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: TPO
-- ------------------------------------------------------
-- Server version	5.5.50-0ubuntu0.14.04.1

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
-- Table structure for table `TPR`
--

DROP TABLE IF EXISTS `TPR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TPR` (
  `roll_number` varchar(20) NOT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`roll_number`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `TPR_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `TPR_ibfk_2` FOREIGN KEY (`roll_number`) REFERENCES `student` (`roll_number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TPR`
--

LOCK TABLES `TPR` WRITE;
/*!40000 ALTER TABLE `TPR` DISABLE KEYS */;
INSERT INTO `TPR` VALUES ('14075008',1),('14075043',1),('14034008',2),('14065008',3),('14024008',4);
/*!40000 ALTER TABLE `TPR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `Admin_ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `EMail` varchar(40) DEFAULT NULL,
  `type` varchar(40) NOT NULL,
  PRIMARY KEY (`Admin_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Prayas','prayas.jain.cse14@iitbhu.ac.in','student'),(2,'Bharat','bharat.khanna.cse14@iitbhu.ac.in','student'),(3,'Akash','akash.gupta.cse14@iitbhu.ac.in','TPR'),(4,'Naveen','naveen.sysanalyst@iitbhu.ac.in','System Analyst'),(5,'Prayas2','prayasjain1996@gmail.com','Student'),(6,'Rishabh','rishabh.jain.cse14@itbhu.ac.in','student'),(7,'qwert','qwert@qwe.com','qwer');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cgpa`
--

DROP TABLE IF EXISTS `cgpa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cgpa` (
  `semester` int(11) NOT NULL DEFAULT '0',
  `roll_number` varchar(20) NOT NULL DEFAULT '',
  `spi` varchar(5) NOT NULL,
  PRIMARY KEY (`semester`,`roll_number`),
  KEY `roll_number` (`roll_number`),
  CONSTRAINT `cgpa_ibfk_1` FOREIGN KEY (`roll_number`) REFERENCES `student` (`roll_number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cgpa`
--

LOCK TABLES `cgpa` WRITE;
/*!40000 ALTER TABLE `cgpa` DISABLE KEYS */;
INSERT INTO `cgpa` VALUES (0,'14024008','8.87'),(0,'14025008','8.92'),(0,'14075043','7.00'),(0,'14075044','9.37'),(1,'14075044','9.50'),(2,'14075043','6.23'),(2,'14075044','9.25'),(3,'14075044','9.85'),(4,'14075044','9.50');
/*!40000 ALTER TABLE `cgpa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `class_NAME` varchar(40) NOT NULL,
  `year` int(11) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,'B.Tech',2018),(2,'IDD',2019),(3,'IMD',2019),(4,'B.Sc',2018),(5,'M.Sc',2019);
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `name` varchar(40) NOT NULL,
  `type` varchar(20) NOT NULL,
  `description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`comp_id`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `company_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`Admin_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,3,'Goldman Sachs','Internship','2 months. 60k pm. All expenses covered. Profile machine learning, databases'),(2,3,'Goldman Sachs','Placement','CTC 28lpa  Stock options availables. Profile machine learning, databases'),(3,4,'Accenture','Placement','CTC 14lpa Skill Set required databases, data structures , algorithms'),(4,4,'Accenture','Internship','2 months intern 30k per months  Skill Set required databases, data structures , algorithms'),(5,3,'Wipro','Internship','2 months intern 30k per month  Skill Set required  data structures , algorithms'),(6,3,'MyKarma','Internship','2 months research  intern 25k per month  Candidates with good coding skills will be preferred'),(7,1,'Random Comp','Internship','just adding something');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_NAME` varchar(40) NOT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `Contact` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Computer Science and Engg.','Dept. of CSE IIT BHU','22341234'),(2,'Mathematical','Dept. of MnC  IIT BHU','2223434'),(3,'Mechanical Engineering','Mech Dept.  IIT BHU','22312312'),(4,'Applied Physics','Physics Dept.  IIT BHU','21312312');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept_class`
--

DROP TABLE IF EXISTS `dept_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dept_class` (
  `dept_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  KEY `dept_id` (`dept_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `dept_class_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dept_class_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept_class`
--

LOCK TABLES `dept_class` WRITE;
/*!40000 ALTER TABLE `dept_class` DISABLE KEYS */;
INSERT INTO `dept_class` VALUES (1,1),(1,2),(2,3),(3,1),(4,4),(4,5);
/*!40000 ALTER TABLE `dept_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `help`
--

DROP TABLE IF EXISTS `help`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `help` (
  `help_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `name` varchar(40) NOT NULL,
  `contact` varchar(20) DEFAULT NULL,
  `EMAil` varchar(40) NOT NULL,
  `Designation` varchar(40) NOT NULL,
  PRIMARY KEY (`help_id`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `help_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`Admin_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `help`
--

LOCK TABLES `help` WRITE;
/*!40000 ALTER TABLE `help` DISABLE KEYS */;
INSERT INTO `help` VALUES (1,4,'Ramesh','9764675356','ramesh.mishra13@gmail.com','System Analyst'),(2,4,'Rajesh','9764676756','rajesh.gupta13@gmail.com','System Analyst'),(3,1,'Pranav','9764779756','pranav.goel.cse14@iitbhu.ac.in','Student'),(4,3,'Amrinder','9764779716','amrinder.dhaliwal.cse14@iitbhu.ac.in','TPR');
/*!40000 ALTER TABLE `help` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `Date` date NOT NULL,
  `content` varchar(4000) NOT NULL,
  PRIMARY KEY (`post_id`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`Admin_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,1,'2016-07-23',' Beta version of the portal launched for testing. Upload your profiles '),(2,2,'2016-07-24',' Site temporaily down for maintence. Profile wont be updated for another 23 hrs '),(3,3,'2016-07-28','Resume Tips: Please avoid unnecessary details on your resume. Keep it precise '),(4,3,'2016-07-29','Goldman Sachs is open for willingness. All brances are open for internship. '),(5,4,'2016-08-02','1 hour maintence break. Sorry for inconvience'),(9,1,'2016-05-28','Today\'s my birthday'),(10,6,'2016-07-07','shahshs');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruitment`
--

DROP TABLE IF EXISTS `recruitment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recruitment` (
  `comp_id` int(11) NOT NULL DEFAULT '0',
  `dept_id` int(11) NOT NULL DEFAULT '0',
  `class_id` int(11) NOT NULL DEFAULT '0',
  `CGPA` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`comp_id`,`dept_id`,`class_id`),
  KEY `dept_id` (`dept_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `recruitment_ibfk_1` FOREIGN KEY (`comp_id`) REFERENCES `company` (`comp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `recruitment_ibfk_2` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `recruitment_ibfk_3` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruitment`
--

LOCK TABLES `recruitment` WRITE;
/*!40000 ALTER TABLE `recruitment` DISABLE KEYS */;
INSERT INTO `recruitment` VALUES (1,1,1,'6.000'),(1,2,3,'8.50'),(1,3,1,'9.000'),(1,4,1,'9.50'),(2,1,1,'8.00'),(2,1,2,'8.50'),(2,2,3,'8.50'),(3,1,1,'8.00'),(3,1,2,'8.00'),(3,2,3,'7.00'),(4,1,1,'7.00'),(4,2,3,'7.00'),(5,1,1,'7.00'),(5,1,2,'7.50'),(5,2,3,'8.00'),(5,3,1,'8.00'),(5,4,4,'8.00'),(5,4,5,'8.00'),(6,1,1,'0.00'),(6,1,2,'0.00'),(6,2,3,'0.00'),(6,3,1,'0.00'),(6,4,4,'0.00'),(6,4,5,'0.00'),(7,4,4,'0.00');
/*!40000 ALTER TABLE `recruitment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `roll_number` varchar(20) NOT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  `first_name` varchar(30) NOT NULL,
  `middle_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) NOT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `EMail` varchar(40) NOT NULL,
  `Mother_Tongue` varchar(40) DEFAULT NULL,
  `Address_temp` varchar(200) DEFAULT NULL,
  `Address_perm` varchar(200) DEFAULT NULL,
  `contact` varchar(20) DEFAULT NULL,
  `resume` varchar(10) DEFAULT NULL,
  `backlogs` varchar(100) DEFAULT NULL,
  `interests` varchar(200) DEFAULT NULL,
  `profile_picture` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`roll_number`),
  KEY `dept_id` (`dept_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `student_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('14024008',4,5,'Rohit','Kumar','Bansal','M','rohit.bansal.phy14@iitbhu.ac.in','Hindi','23 Aryabhatta  Hostel','124 bhera enclave indore','923422312','N','NA','','NA'),('14025008',4,4,'Rajat','Kumar','Meena','M','rajat.meena.phy14@iitbhu.ac.in','Hindi','25 Aryabhatta  Hostel','120 bhera enclave indore','923422385','N','NA','','NA'),('14034008',2,3,'Gaurav','','Somani','M','gaurav.somani.mat14@iitbhu.ac.in','Hindi','45 Vishvakarma Hostel','120 symphony enclave meerut','919242385','N','NA','','NA'),('14065008',3,1,'Arihant','','Jain','M','arihant.jain.mec14@iitbhu.ac.in','Hindi','45 Aryabhatta  Hostel','120 army compartments meerut','919442385','N','NA','','NA'),('14074008',1,2,'Ishank','','Arora','M','ishank.arora.cse14@iitbhu.ac.in','Hindi','45 Ramanujan Hostel','120 krishna enclave agra','989242385','N','NA','','NA'),('14075005',1,1,'Akash','','Gupta','M','akash.gupta.cse14@iitbhu.ac.in','Hindi','15 Ramanujan Hostel','130 Civil Lines Kota','912245685','N','NA','','NA'),('14075008',1,1,'Amrinder','Singh','Dhaliwal','M','amrinder.dhaliwal.cse14@iitbhu.ac.in','Punjabi','15 Ramanujan Hostel','130 Harmony Appts Ludhiana','989245685','N','NA','','NA'),('14075015',1,1,'Bharat','','Khanna','M','bharat.khanna.cse14@iitbhu.ac.in','Hindi','25 Ramanujan Hostel','430 Civil Lines Delhi','912245455','N','NA','','NA'),('14075043',1,1,'Rishabh','','Jain','','rishabh.jain.cse14@itbhu.ac.in','','','','','Y','','','Y'),('14075044',1,1,'Prayas','','Jain','M','prayas.jain.cse14@iitbhu.ac.in','Hindi','23 Ramanujan Hostel','430 Laxmi Nagar Delhi','912345455','Y','NA','','Y');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `willingness`
--

DROP TABLE IF EXISTS `willingness`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `willingness` (
  `comp_id` int(11) NOT NULL DEFAULT '0',
  `roll_number` varchar(20) NOT NULL DEFAULT '',
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`comp_id`,`roll_number`),
  KEY `roll_number` (`roll_number`),
  CONSTRAINT `willingness_ibfk_1` FOREIGN KEY (`comp_id`) REFERENCES `company` (`comp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `willingness_ibfk_2` FOREIGN KEY (`roll_number`) REFERENCES `student` (`roll_number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `willingness`
--

LOCK TABLES `willingness` WRITE;
/*!40000 ALTER TABLE `willingness` DISABLE KEYS */;
INSERT INTO `willingness` VALUES (1,'14075043','willing_sent'),(1,'14075044','willing_sent'),(4,'14075043','willing_sent'),(4,'14075044','willing_sent'),(5,'14075044','willing_sent'),(6,'14024008','willing_approved'),(6,'14025008','willing_approved'),(6,'14075044','willing_sent');
/*!40000 ALTER TABLE `willingness` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-22 13:45:12
