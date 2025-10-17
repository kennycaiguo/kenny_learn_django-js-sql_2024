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
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

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

-- ----------------------------
-- Table structure for dept
-- ----------------------------
DROP TABLE IF EXISTS `dept`;
CREATE TABLE `dept`  (
  `deptId` int(11) NOT NULL AUTO_INCREMENT,
  `deptName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`deptId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of dept
-- ----------------------------
INSERT INTO `dept` VALUES (1, '应用开发部');
INSERT INTO `dept` VALUES (2, '行政部');
INSERT INTO `dept` VALUES (3, '软件测试部');
INSERT INTO `dept` VALUES (4, '销售部');
INSERT INTO `dept` VALUES (5, '后勤部');
INSERT INTO `dept` VALUES (6, '采购部');
INSERT INTO `dept` VALUES (7, '业务部');
INSERT INTO `dept` VALUES (8, '人事部');
INSERT INTO `dept` VALUES (9, '秘书部');
INSERT INTO `dept` VALUES (10, '财务部');
INSERT INTO `dept` VALUES (11, '保安部');
INSERT INTO `dept` VALUES (12, '培训部');
INSERT INTO `dept` VALUES (13, '质检部');

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee`  (
  `empId` int(11) NOT NULL AUTO_INCREMENT,
  `empName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salary` double(10, 2) NULL DEFAULT NULL,
  `dept_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`empId`) USING BTREE,
  INDEX `employee`(`dept_id`) USING BTREE,
  CONSTRAINT `employee` FOREIGN KEY (`dept_id`) REFERENCES `dept` (`deptId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES (1, 'Scott', 3000.00, 3);
INSERT INTO `employee` VALUES (2, 'Mary', 2000.00, 9);
INSERT INTO `employee` VALUES (3, 'Jackline', 1500.00, 5);
INSERT INTO `employee` VALUES (4, 'Stacey', 2000.00, 10);

-- ----------------------------
-- Table structure for log_
-- ----------------------------
DROP TABLE IF EXISTS `log_`;
CREATE TABLE `log_`  (
  `content` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of log_
-- ----------------------------
INSERT INTO `log_` VALUES ('在保存数据');
INSERT INTO `log_` VALUES ('在保存数据');

-- ----------------------------
-- Table structure for t_admin
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `adminName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pwd` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_admin
-- ----------------------------
INSERT INTO `t_admin` VALUES (1, 'liming', '12345');
INSERT INTO `t_admin` VALUES (2, 'rose', '12345');
INSERT INTO `t_admin` VALUES (3, 'Jack', '12345');
INSERT INTO `t_admin` VALUES (4, 'pauline', '12345');
INSERT INTO `t_admin` VALUES (5, '李连杰', '12345');
INSERT INTO `t_admin` VALUES (6, '李丽珍', '12345');
INSERT INTO `t_admin` VALUES (7, '马云', '12345');

-- ----------------------------
-- Table structure for t_dept
-- ----------------------------
DROP TABLE IF EXISTS `t_dept`;
CREATE TABLE `t_dept`  (
  `deptId` int(11) NOT NULL AUTO_INCREMENT,
  `deptName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`deptId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_dept
-- ----------------------------
INSERT INTO `t_dept` VALUES (1, '应用开发部');
INSERT INTO `t_dept` VALUES (2, '行政部');
INSERT INTO `t_dept` VALUES (3, '软件测试部');
INSERT INTO `t_dept` VALUES (4, '销售部');
INSERT INTO `t_dept` VALUES (5, '后勤部');
INSERT INTO `t_dept` VALUES (6, '采购部');
INSERT INTO `t_dept` VALUES (7, '业务部');
INSERT INTO `t_dept` VALUES (8, '人事部');
INSERT INTO `t_dept` VALUES (9, '秘书部');
INSERT INTO `t_dept` VALUES (10, '财务部');
INSERT INTO `t_dept` VALUES (11, '保安部');
INSERT INTO `t_dept` VALUES (12, '培训部');
INSERT INTO `t_dept` VALUES (13, '质检部');

-- ----------------------------
-- Table structure for t_employee
-- ----------------------------
DROP TABLE IF EXISTS `t_employee`;
CREATE TABLE `t_employee`  (
  `empId` int(11) NOT NULL AUTO_INCREMENT,
  `empName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `salary` double(10, 2) NULL DEFAULT NULL,
  `dept_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`empId`) USING BTREE,
  INDEX `employee`(`dept_id`) USING BTREE,
  INDEX `FKFDCF5A19856CCA6B`(`dept_id`) USING BTREE,
  CONSTRAINT `FKFDCF5A19856CCA6B` FOREIGN KEY (`dept_id`) REFERENCES `t_dept` (`deptId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `t_employee_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `dept` (`deptId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_employee
-- ----------------------------
INSERT INTO `t_employee` VALUES (1, 'Scott', 3000.00, 3);
INSERT INTO `t_employee` VALUES (2, 'Mary', 2000.00, 9);
INSERT INTO `t_employee` VALUES (3, 'Jackline', 800.00, 5);
INSERT INTO `t_employee` VALUES (4, 'Stacey', 2000.00, 10);
INSERT INTO `t_employee` VALUES (5, 'Lilian chan', 700.00, 5);
INSERT INTO `t_employee` VALUES (14, 'wangcai', 5000.00, 1);
INSERT INTO `t_employee` VALUES (15, 'pusky', 900.00, 9);

SET FOREIGN_KEY_CHECKS = 1;
