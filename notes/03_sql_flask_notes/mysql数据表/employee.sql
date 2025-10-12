/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 50647
 Source Host           : localhost:3306
 Source Schema         : company

 Target Server Type    : MySQL
 Target Server Version : 50647
 File Encoding         : 65001

 Date: 12/10/2025 11:17:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `depId` int(11) NULL DEFAULT NULL,
  `gender` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salary` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `employee_dept_fk`(`depId`) USING BTREE,
  CONSTRAINT `employee_dept_fk` FOREIGN KEY (`depId`) REFERENCES `dept` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 58 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES (1, 'PaulinE', 1, 'female', 2500);
INSERT INTO `employee` VALUES (2, 'Nancy', 3, 'female', 3500);
INSERT INTO `employee` VALUES (3, 'john', 3, 'male', 5000);
INSERT INTO `employee` VALUES (4, 'johnny', 3, 'male', 5000);
INSERT INTO `employee` VALUES (5, 'Ricky Rojas', 1, 'male', 2000);
INSERT INTO `employee` VALUES (52, 'Kelly chen', 1, 'female', 3000);
INSERT INTO `employee` VALUES (53, 'Paula fernandez', 1, 'female', 3000);
INSERT INTO `employee` VALUES (55, 'Jacklou', 5, 'male', 5000);
INSERT INTO `employee` VALUES (56, 'Andylou', 5, 'male', 4000);

-- ----------------------------
-- Triggers structure for table employee
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_add`;
delimiter ;;
CREATE TRIGGER `trg_add` AFTER INSERT ON `employee` FOR EACH ROW INSERT INTO log(content) values("new record added")
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
