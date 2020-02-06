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
CREATE TABLE IF NOT EXISTS `bank1` (
  `underlying` varchar(50) DEFAULT NULL,
  `underlyinglevel1` decimal(11,2) DEFAULT NULL,
  `underlyinglevel2` decimal(11,2) DEFAULT NULL,
  `underlyinglevel3` decimal(11,2) DEFAULT NULL,
  `underlyinglevel4` decimal(11,2) DEFAULT NULL,
  `underlyinglevel5` decimal(11,2) DEFAULT NULL,
  `notabove` decimal(11,2) DEFAULT NULL,
  `notbelow` decimal(11,2) DEFAULT NULL,
  `ivtop` decimal(11,2) DEFAULT NULL,
  `ivbottom` decimal(11,2) DEFAULT NULL,
  `weeklyexpirypriceup` decimal(11,2) DEFAULT NULL,
  `weeklyexpirypricedown` decimal(11,2) DEFAULT NULL,
  `15mtrend` int DEFAULT NULL,
  `maxpaindirection` int DEFAULT NULL,
  `maxpaintarget` decimal(11,2) DEFAULT NULL,
  `pcrdirection` int DEFAULT NULL,
  `pcrto` decimal(11,2) DEFAULT NULL,
  `pcrotherside` decimal(11,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
