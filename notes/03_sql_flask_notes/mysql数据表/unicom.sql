/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 50647
 Source Host           : localhost:3306
 Source Schema         : unicom

 Target Server Type    : MySQL
 Target Server Version : 50647
 File Encoding         : 65001

 Date: 13/10/2025 11:57:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` char(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `mobile` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'Jackma', '123', '13532619997');
INSERT INTO `admin` VALUES (2, 'Mahuateng', '1223', '123456789');
INSERT INTO `admin` VALUES (3, 'Benny', '12345', '13566677889');
INSERT INTO `admin` VALUES (4, 'Guo', '123456', '12345678900');
INSERT INTO `admin` VALUES (6, '刘德华', '234', '13566677889');
INSERT INTO `admin` VALUES (7, '赵丽颖', '223344', '15166678987');

SET FOREIGN_KEY_CHECKS = 1;
