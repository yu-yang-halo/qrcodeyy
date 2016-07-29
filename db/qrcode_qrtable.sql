-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: qrcode
-- ------------------------------------------------------
-- Server version	5.6.31

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
-- Table structure for table `qrtable`
--

DROP TABLE IF EXISTS `qrtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qrtable` (
  `qrid` int(11) NOT NULL AUTO_INCREMENT,
  `qrindex` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `qrcontent` longtext COLLATE utf8_unicode_ci,
  `objectid` int(11) DEFAULT NULL,
  PRIMARY KEY (`qrid`),
  UNIQUE KEY `objectid_UNIQUE` (`objectid`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qrtable`
--

LOCK TABLES `qrtable` WRITE;
/*!40000 ALTER TABLE `qrtable` DISABLE KEYS */;
INSERT INTO `qrtable` VALUES (76,'1469688223','		<A><h>0F02333</h><p><n>3213213</n> <r>13Y000送风机状态</r><r>24Y001抽风机状态</r><r>35Y002冷却风机状态</r><r>46Y003冷却风泵状态</r><r>57Y004循环水泵状态</r> </p><p><n>5实时数据</n> <r>11D212顺序启动延时</r><r>22D1FE变频器频率</r><r>31D212顺序启动延时</r><r>42D1FE变频器频率</r><r>51D212顺序启动延</r></p></A>\n		',1223),(77,'1469689714','<A><h>0F02333</h><p><n>3213213</n> <r>13Y000送风机状态</r><r>24Y001抽风机状态</r><r>35Y002冷却风机状态</r><r>46Y003冷却风泵状态</r><r>57Y004循环水泵状态</r> </p><p><n>5实时数据</n> <r>11D212顺序启动延时</r><r>22D1FE变频器频率</r><r>31D212顺序启动延时</r><r>42D1FE变频器频率</r><r>51D212顺序启动延</r></p></A>',3123);
/*!40000 ALTER TABLE `qrtable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-29  9:39:57
