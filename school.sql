

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for school
-- ----------------------------
DROP TABLE IF EXISTS `school`;
CREATE TABLE `school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `un_id` int(11) DEFAULT NULL,
  `url` varchar(1000) DEFAULT NULL,
  `title` varchar(1000) DEFAULT NULL,
  `contents` text,
  `last_scan_time` datetime DEFAULT NULL,
  `parent_url` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;
