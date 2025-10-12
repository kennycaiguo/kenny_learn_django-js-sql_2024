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

 Date: 12/10/2025 11:17:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for log
-- ----------------------------
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `datime` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 51 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of log
-- ----------------------------
INSERT INTO `log` VALUES (1, 'new record added', NULL);
INSERT INTO `log` VALUES (2, 'new record added', NULL);
INSERT INTO `log` VALUES (3, 'new record added', NULL);
INSERT INTO `log` VALUES (4, 'new record added', NULL);
INSERT INTO `log` VALUES (5, 'new record added', NULL);
INSERT INTO `log` VALUES (6, 'new record added', NULL);
INSERT INTO `log` VALUES (7, 'new record added', NULL);
INSERT INTO `log` VALUES (8, 'new record added', NULL);
INSERT INTO `log` VALUES (9, 'new record added', NULL);
INSERT INTO `log` VALUES (10, 'new record added', NULL);
INSERT INTO `log` VALUES (11, 'new record added', NULL);
INSERT INTO `log` VALUES (12, 'new record added', NULL);
INSERT INTO `log` VALUES (13, 'new record added', NULL);
INSERT INTO `log` VALUES (14, 'new record added', NULL);
INSERT INTO `log` VALUES (15, 'new record added', NULL);
INSERT INTO `log` VALUES (16, 'new record added', NULL);
INSERT INTO `log` VALUES (17, 'new record added', NULL);
INSERT INTO `log` VALUES (18, 'new record added', NULL);
INSERT INTO `log` VALUES (19, 'new record added', NULL);
INSERT INTO `log` VALUES (20, 'new record added', NULL);
INSERT INTO `log` VALUES (21, 'new record added', NULL);
INSERT INTO `log` VALUES (22, 'new record added', NULL);
INSERT INTO `log` VALUES (23, 'new record added', NULL);
INSERT INTO `log` VALUES (24, 'new record added', NULL);
INSERT INTO `log` VALUES (25, 'new record added', NULL);
INSERT INTO `log` VALUES (26, 'new record added', NULL);
INSERT INTO `log` VALUES (27, 'new record added', NULL);
INSERT INTO `log` VALUES (28, 'new record added', NULL);
INSERT INTO `log` VALUES (29, 'new record added', NULL);
INSERT INTO `log` VALUES (30, 'new record added', NULL);
INSERT INTO `log` VALUES (31, 'new record added', NULL);
INSERT INTO `log` VALUES (32, 'new record added', NULL);
INSERT INTO `log` VALUES (33, 'new record added', NULL);
INSERT INTO `log` VALUES (34, 'new record added', NULL);
INSERT INTO `log` VALUES (35, 'new record added', NULL);
INSERT INTO `log` VALUES (36, 'new record added', NULL);
INSERT INTO `log` VALUES (37, 'new record added', NULL);
INSERT INTO `log` VALUES (38, 'new record added', NULL);
INSERT INTO `log` VALUES (39, 'new record added', NULL);
INSERT INTO `log` VALUES (40, 'new record added', NULL);
INSERT INTO `log` VALUES (41, 'new record added', NULL);
INSERT INTO `log` VALUES (42, 'new record added', NULL);
INSERT INTO `log` VALUES (43, 'new record added', NULL);
INSERT INTO `log` VALUES (44, 'new record added', NULL);
INSERT INTO `log` VALUES (45, 'new record added', NULL);
INSERT INTO `log` VALUES (46, 'new record added', NULL);
INSERT INTO `log` VALUES (47, 'new record added', NULL);
INSERT INTO `log` VALUES (48, 'new record added', NULL);
INSERT INTO `log` VALUES (49, 'new record added', NULL);
INSERT INTO `log` VALUES (50, 'new record added', NULL);

SET FOREIGN_KEY_CHECKS = 1;
