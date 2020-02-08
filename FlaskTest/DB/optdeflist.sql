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
  `idno` int DEFAULT NULL,
  `atdate` datetime DEFAULT NULL,
  `strike` decimal(11,2) DEFAULT NULL,
  `entry` decimal(11,2) DEFAULT NULL,
  `stoploss` decimal(11,2) DEFAULT NULL,
  `target` decimal(11,2) DEFAULT NULL,
  `risk` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table test.optdeflist: ~2 rows (approximately)
/*!40000 ALTER TABLE `optdeflist` DISABLE KEYS */;
INSERT INTO `optdeflist` (`idno`, `atdate`, `strike`, `entry`, `stoploss`, `target`, `risk`) VALUES
	(1, '2019-08-20 12:05:01', 11545554.00, 48545554.00, 55455554.00, 4444444.00, 'loss'),
	(2, '2019-08-22 12:05:11', 115455554.00, 68545554.00, 5545584.00, 65561564.00, 'profit'),
	(3, '2019-10-22 12:10:11', 233455554.00, 68566554.00, 55444484.00, 88161564.00, 'profit');
/*!40000 ALTER TABLE `optdeflist` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
