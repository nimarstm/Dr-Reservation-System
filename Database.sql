-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: reservation_system
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `drinfo`
--

DROP TABLE IF EXISTS `drinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drinfo` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Expert` varchar(45) NOT NULL,
  `Date` varchar(45) NOT NULL,
  `Time` varchar(45) DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  PRIMARY KEY (`ID`,`Date`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drinfo`
--

LOCK TABLES `drinfo` WRITE;
/*!40000 ALTER TABLE `drinfo` DISABLE KEYS */;
INSERT INTO `drinfo` VALUES (1,'dr Ali','Dermotologist','2024-08-06','14:00',0),(2,'dr Ali','Dermotologist','2024-08-06','14:30',1),(3,'dr Ali','Dermotologist','2024-08-06','15:00',1),(4,'dr Ali','Dermotologist','2024-08-15','14:00',1),(5,'dr mahdi','Dermotologist','2024-08-28','14:30',1),(6,'dr mahdi','Dermotologist','2024-08-06','14:30',0),(7,'dr farhad','Cardiologist','2024-08-15','14:00',1),(8,'dr farhad','Cardiologist','2024-08-15','14:30',1),(9,'dr farhad','Cardiologist','2024-08-15','15:00',1),(10,'dr farhad','Cardiologist','2024-08-15','15:30',1),(11,'dr farhad','Cardiologist','2024-08-15','16:00',1),(12,'dr farhad','Cardiologist','2024-08-18','14:00',1),(13,'dr farhad','Cardiologist','2024-08-18','14:30',1),(14,'dr farhad','Cardiologist','2024-08-18','15:00',1),(15,'dr farhad','Cardiologist','2024-08-18','15:30',1),(16,'dr farhad','Cardiologist','2024-08-18','16:00',1),(17,'dr hasan','Cardiologist','2024-08-14','14:00',1),(18,'dr hasan','Cardiologist','2024-08-14','14:30',1),(19,'dr hasan','Cardiologist','2024-08-14','15:00',1),(20,'dr hasan','Cardiologist','2024-08-14','15:00',1),(21,'dr hasan','Cardiologist','2024-08-20','14:00',1),(22,'dr hasan','Cardiologist','2024-08-20','15:00',1),(23,'dr hasan','Cardiologist','2024-08-20','16:00',1),(24,'dr maryam','General Practitioner','2024-08-23','14:00',1),(25,'dr maryam','General Practitioner','2024-08-23','15:00',1),(26,'dr maryam','General Practitioner','2024-08-23','16:00',1),(27,'dr maryam','General Practitioner','2024-08-25','14:00',1),(28,'dr maryam','General Practitioner','2024-08-25','15:00',1),(29,'dr armin','General Practitioner','2024-08-27','14:00',1),(30,'dr armin','General Practitioner','2024-08-27','15:00',1),(31,'dr armin','General Practitioner','2024-08-27','16:00',1),(32,'dr armin','General Practitioner','2024-08-29','14:00',1),(33,'dr armin','General Practitioner','2024-08-29','15:00',1),(34,'dr armin','General Practitioner','2024-08-29','16:00',1),(35,'dr armin','General Practitioner','2024-08-29','17:00',1);
/*!40000 ALTER TABLE `drinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserve_info`
--

DROP TABLE IF EXISTS `reserve_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserve_info` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `drName` varchar(45) DEFAULT NULL,
  `userID` varchar(45) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Time` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserve_info`
--

LOCK TABLES `reserve_info` WRITE;
/*!40000 ALTER TABLE `reserve_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserve_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userinfo` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(45) NOT NULL,
  `PhoneNumber` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES (1,'Nima','09145660949','1234'),(2,'Armin0','09145663214','5858'),(4,'Saber','09143160949','9858');
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-07 11:20:54
