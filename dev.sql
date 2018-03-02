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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sentences`
--

LOCK TABLES `sentences` WRITE;
/*!40000 ALTER TABLE `sentences` DISABLE KEYS */;
INSERT INTO `sentences` VALUES (1,'Finance','show me my gpa this year.',1),(2,'ORM','asfds',7),(3,'Sales','show me the sale amount of iphoneX this year.',10),(4,'Sales','show me the sale amount of iphoneX this year.',10),(5,'CRM','asdfsafdsaf',10),(6,'Sales','dfafasfasfsdf',10),(7,'Sales','i love sandwiches',10),(8,'Sales','i love sandwiches',10),(9,'Sales','i love sandwiches',10),(10,'Sales','i love sandwiches',10),(11,'Sales','i love sandwiches',10),(12,'Sales','i love summer and wear my T-shirt.',7),(13,'CRM','asdfafsd',7),(14,'CRM','I am junyingzhou',7),(15,'OMS','asdfghj',7),(16,'Sales','how does the average fulfillment days change daily',7),(17,'CRM','I am Daran Kong',11),(18,'OMS','my name is daran.',12),(19,'Sales','efggfasgfksfgs',13),(20,'Sales','top sales employee',16),(21,'Sales','top sales employees',16),(22,'Sales','best product',16),(23,'Sales','best product',16),(24,'Sales','best product',16),(25,'Sales','best product',16),(26,'Sales','best product',16),(27,'Sales','who is the top sales employee this month?',17);
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'jyzhou77@gmail.com','junying zhou',20,2),(2,'young@qq.com','young',0,0),(3,'jun@qq.com','Catttt',0,0),(4,'jun@qqqq.com','junying',0,0),(5,'zhulin@hotmail.com','Lin',0,0),(6,'meaning@fudan.edu.cn','Wang lixia',0,0),(7,'jyzhou77@qq.com','Tangbohu',50,5),(8,'asdf@qqqqq.com','nkck',0,0),(9,'test@qqqq.com','testman',0,0),(10,'test@test.com','testman',50,6),(11,'daran@sap.comcom','Daran',10,1),(12,'daran@sap.com','Daran',10,1),(13,'zjh@qqq.com','zhoujun',10,1),(14,'interet@qq.vom','ini',0,0),(15,'','yuiyui',0,0),(16,'lin.zhu@sap.com','Lin',70,7),(17,'lisa.gao@sap.com','Lisa',10,1);
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

-- Dump completed on 2018-02-07 14:35:20
