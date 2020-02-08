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

-- Dumping structure for table test.optdeflist
CREATE TABLE IF NOT EXISTS `optdeflist` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Underlying` varchar(10) DEFAULT NULL,
  `Level1` decimal(11,2) DEFAULT NULL,
  `Level2` decimal(11,2) DEFAULT NULL,
  `Level3` decimal(11,2) DEFAULT NULL,
  `Level4` decimal(11,2) DEFAULT NULL,
  `Level5` decimal(11,2) DEFAULT NULL,
  `NotAbove` decimal(11,2) DEFAULT NULL,
  `NotBelow` decimal(11,2) DEFAULT NULL,
  `IVTop` decimal(11,2) DEFAULT NULL,
  `IVBottom` decimal(11,2) DEFAULT NULL,
  `WeeklyExpiryTargetUp` decimal(11,2) DEFAULT NULL,
  `WeeklyExpiryTargetDown` decimal(11,2) DEFAULT NULL,
  `Trend15M` int DEFAULT NULL,
  `MaxPainDirection` int DEFAULT NULL,
  `MaxPainTarget` decimal(11,2) DEFAULT NULL,
  `PCRDirection` int DEFAULT NULL,
  `PCRUp` decimal(11,2) DEFAULT NULL,
  `PCRDown` decimal(11,2) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table test.optdeflist: ~7 rows (approximately)
/*!40000 ALTER TABLE `optdeflist` DISABLE KEYS */;
INSERT INTO `optdeflist` (`Id`, `Underlying`, `Level1`, `Level2`, `Level3`, `Level4`, `Level5`, `NotAbove`, `NotBelow`, `IVTop`, `IVBottom`, `WeeklyExpiryTargetUp`, `WeeklyExpiryTargetDown`, `Trend15M`, `MaxPainDirection`, `MaxPainTarget`, `PCRDirection`, `PCRUp`, `PCRDown`) VALUES
	(2, NULL, 12.00, 456.00, 100.00, 7.00, 89.00, 4.00, 7.00, 8.00, 8.00, 9.00, 4.00, 1, 1, 2.00, 1, 1.00, 9.00),
	(3, NULL, 3.00, 45.00, 7.00, 89.00, 990.00, 23.00, 76.00, 89.00, 45.00, 45.00, 23.00, 1, 2, 34.00, 3, 23.00, 67000.00),
	(4, NULL, 56.00, 78.00, 32900.67, 56400.00, 34000.00, 23000.00, 100000.67, 10000.00, 34000.00, 23000.00, 2300.99, 1, 1, 78000.00, 1, 2.00, 67000.00),
	(5, NULL, 32.00, 34.00, 78.00, 56400.00, 34000.00, 23000.00, 100000.67, 10000.00, 34000.00, 23000.00, 2300.99, 1, 1, 78000.00, 1, 2.00, 67000.00),
	(6, NULL, 4.00, 1.00, 5.00, 7.00, 9.00, 2.00, 6.00, 6.00, 2.00, 8.00, 9.00, 1, 1, 1.00, 1, 1.00, 1.00),
	(7, NULL, 9.00, 3.00, 5.00, 7.00, 9.00, 2.00, 6.00, 6.00, 2.00, 8.00, 9.00, 1, 1, 1.00, 3, 1.00, 1.00),
	(8, NULL, 67.00, 44.00, 5.00, 7.00, 9.00, 2.00, 6.00, 6.00, 2.00, 8.00, 9.00, 1, 1, 1.00, 2, 1.00, 1.00),
	(9, NULL, 67.00, 111.00, 5.00, 7.00, 9.00, 2.00, 6.00, 6.00, 2.00, 8.00, 9.00, 1, 1, 1.00, 2, 1.00, 1.00);
/*!40000 ALTER TABLE `optdeflist` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
