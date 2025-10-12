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

 Date: 12/10/2025 11:17:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pwd` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'liming', '12345');
INSERT INTO `admin` VALUES (2, 'rose', '12345');
INSERT INTO `admin` VALUES (3, 'Jack', '12345');
INSERT INTO `admin` VALUES (4, 'pauline', '12345');
INSERT INTO `admin` VALUES (5, '李连杰', '12345');
INSERT INTO `admin` VALUES (6, '李丽珍', '12345');
INSERT INTO `admin` VALUES (7, '马云', '12345');
INSERT INTO `admin` VALUES (8, 'kenny', '123');
INSERT INTO `admin` VALUES (9, 'kenny', '123');

SET FOREIGN_KEY_CHECKS = 1;
