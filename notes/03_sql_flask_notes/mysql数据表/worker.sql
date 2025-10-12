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

 Date: 12/10/2025 12:01:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for worker
-- ----------------------------
DROP TABLE IF EXISTS `worker`;
CREATE TABLE `worker`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` tinyint(4) NULL DEFAULT NULL,
  `salary` decimal(10, 2) NULL DEFAULT NULL,
  `created` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of worker
-- ----------------------------
INSERT INTO `worker` VALUES (1, 'Jackline', '123', 'female', 'jl123@gmail.com', 18, 2000.50, '2022-09-30 08:12:30');
INSERT INTO `worker` VALUES (2, 'Denny', '123', 'male', 'dy123bb@hotmail.com', 18, 2100.50, '2023-03-30 08:12:30');
INSERT INTO `worker` VALUES (3, 'Miky', '123', 'male', 'mky123456@hotmail.com', 18, 4000.50, '2022-09-30 08:12:30');
INSERT INTO `worker` VALUES (4, 'Marycake', '123', 'female', 'mcake123@gmail.com', 18, 2200.50, '2024-08-30 08:24:30');
INSERT INTO `worker` VALUES (5, 'Ashley', '123', 'female', 'ash123bb@hotmail.com', 18, 3100.50, '2024-10-30 09:12:30');
INSERT INTO `worker` VALUES (6, 'Mandy', '123', 'female', 'mky123456@hotmail.com', 18, 1900.50, '2024-11-03 07:12:30');

SET FOREIGN_KEY_CHECKS = 1;
