-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.19 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table test.bank1
CREATE TABLE IF NOT EXISTS OptDefPlan (
  Id int not null AUTO_INCREMENT,
  Underlying varchar(10) DEFAULT NULL,
  Level1 decimal(11,2) DEFAULT NULL,
  Level2 decimal(11,2) DEFAULT NULL,
  Level3 decimal(11,2) DEFAULT NULL,
  Level4 decimal(11,2) DEFAULT NULL,
  Level5 decimal(11,2) DEFAULT NULL,
  NotAbove decimal(11,2) DEFAULT NULL,
  NotBelow decimal(11,2) DEFAULT NULL,
  IVTop decimal(11,2) DEFAULT NULL,
  IVBottom decimal(11,2) DEFAULT NULL,
  WeeklyExpiryTargetUp decimal(11,2) DEFAULT NULL,
  WeeklyExpiryTargetDown decimal(11,2) DEFAULT NULL,
  Trend15M int DEFAULT NULL,
  MaxPainDirection int DEFAULT NULL,
  MaxPainTarget decimal(11,2) DEFAULT NULL,
  PCRDirection int DEFAULT NULL,
  PCRUp decimal(11,2) DEFAULT NULL,
  PCRDown decimal(11,2) DEFAULT NULL
);

