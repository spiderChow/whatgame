-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: whatgame
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `sentences`
--

DROP TABLE IF EXISTS `sentences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sentences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(20) NOT NULL DEFAULT '',
  `content` varchar(100) NOT NULL DEFAULT '',
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `sentences_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sentences`
--

LOCK TABLES `sentences` WRITE;
/*!40000 ALTER TABLE `sentences` DISABLE KEYS */;
INSERT INTO `sentences` VALUES (57,'Sales','how does the smart phone total order change',21),(58,'Sales','How possible will i3435leave',21),(59,'Sales','the best vendor code regarding the profit',21),(60,'Sales','show me the most beautiful woman',21),(65,'Sales','show me something',21),(66,'Sales','who owes Alibaba most',21),(67,'Sales','compare open number with last quarter',21),(68,'Sales','revenue this year',23),(69,'Sales','bp balance list',23),(70,'Sales','top sales person',23),(71,'Sales','what\'s best selling product',23),(72,'Sales','best branch',23),(73,'Sales','How does the best sale happen?',22),(74,'Sales','How does the best sale happen?',22),(75,'Sales','How does the best sale happen?',22),(76,'Sales','top 3 sales order',24),(77,'Sales','show me top 10 sales amount',24),(78,'CRM','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(79,'CRM','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(80,'CRM','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(81,'CRM','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(82,'Sales','I dont like working and living. I dont know what is the meaning of our lves.',21),(83,'Sales','I dont like working and living. I dont know what is the meaning of our lves.',21),(84,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(85,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(86,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(87,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(88,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(89,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(90,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(91,'Sales','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(92,'CRM','show me the most beautiful woman',21),(93,'CRM','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(94,'Topics','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(95,'Topics','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(96,'Topics','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(97,'Topics','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(98,'Topics','I dont like working and living. I dont know whsat is the meaning of our lves.',21),(99,'CRM','I dont like working and living. I dont know whsat is the meaning of our lves.',21);
/*!40000 ALTER TABLE `sentences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(32) NOT NULL DEFAULT '',
  `username` varchar(32) NOT NULL DEFAULT '',
  `score` int(11) NOT NULL DEFAULT '0',
  `questionamount` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  KEY `ix_users_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (21,'junying.zhou@sap.com','Junying',349,36),(22,'jyzhou77@gmail.com','zhou JY',39,3),(23,'lin.zhu@sap.com','Lin',89,5),(24,'eric.wang04@sap.com','Eric Wang',29,2),(25,'kongdaran@126.com','Daran',0,0),(26,'junjun@sap.com','junjun',0,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-09 14:24:55
