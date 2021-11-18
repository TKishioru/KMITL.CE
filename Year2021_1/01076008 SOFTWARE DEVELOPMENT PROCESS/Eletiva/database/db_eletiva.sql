-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 17, 2021 at 07:23 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_eletiva`
--

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `ID_comment` int(11) NOT NULL,
  `msg_comment` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `rate` int(5) DEFAULT NULL,
  `time_comment` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `create_by` bigint(20) UNSIGNED NOT NULL,
  `from_post` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`ID_comment`, `msg_comment`, `rate`, `time_comment`, `create_by`, `from_post`) VALUES
(1, 'fgfahafharthmdsdgasfag', NULL, '2021-11-15 05:12:36', 2, 1),
(2, 'dsafsdfsdf', NULL, '2021-11-17 03:01:58', 3, 2),
(3, 'fgfshfdjsewgb', NULL, '2021-11-17 03:02:25', 3, 1),
(4, 'dfgdfgdfgdfgdfg', NULL, '2021-11-17 03:02:21', 2, 2),
(6, 'dfgdfgsdfsdf', NULL, '2021-11-17 03:36:57', 2, 2),
(7, 'sdfsdfsd', NULL, '2021-11-17 03:37:04', 2, 2),
(8, 'SDFSDF', NULL, '2021-11-17 03:37:55', 2, 2),
(9, 'SDFSDFsdfsdf', NULL, '2021-11-17 03:38:06', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `education`
--

CREATE TABLE `education` (
  `faculty` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `major` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `education`
--

INSERT INTO `education` (`faculty`, `major`) VALUES
('﻿คณะ', 'ภาควิชา'),
('วิศวกรรมศาสตร์', 'วิศวกรรมการวัดและควบคุม'),
('วิศวกรรมศาสตร์', 'วิศวกรรมคอมพิวเตอร์'),
('วิศวกรรมศาสตร์', 'วิศวกรรมเครื่องกล'),
('วิศวกรรมศาสตร์', 'วิศวกรรมเคมี'),
('วิศวกรรมศาสตร์', 'วิศวกรรมไฟฟ้า'),
('วิศวกรรมศาสตร์', 'วิศวกรรมอุตสาหการ'),
('วิศวกรรมศาสตร์', 'วิศวกรรมอาหาร'),
('วิศวกรรมศาสตร์', 'วิศวกรรมอิเล็กทรอนิกส์'),
('วิศวกรรมศาสตร์', 'วิศวกรรมโทรคมนาคม'),
('วิศวกรรมศาสตร์', 'วิศวกรรมโยธา'),
('วิศวกรรมศาสตร์', 'วิศวกรรมชีวการแพทย์'),
('วิศวกรรมศาสตร์', 'วิศวกรรมเกษตร'),
('สถาปัตยกรรมศาสตร์', 'สถาปัตยกรรม'),
('สถาปัตยกรรมศาสตร์', 'สถาปัตยกรรมภายใน'),
('สถาปัตยกรรมศาสตร์', 'ศิลปอุตสาหกรรม'),
('สถาปัตยกรรมศาสตร์', 'นิเทศศิลป์'),
('สถาปัตยกรรมศาสตร์', 'วิจิตรศิลป์'),
('สถาปัตยกรรมศาสตร์', 'ศิลปกรรม'),
('ครุศาสตร์อุตสาหกรรมและเทคโนโลยี', 'ครุศาสตร์สถาปัตยกรรม'),
('ครุศาสตร์อุตสาหกรรมและเทคโนโลยี', 'ครุศาสตร์วิศวกรรม'),
('ครุศาสตร์อุตสาหกรรมและเทคโนโลยี', 'ครุศาสตร์เกษตร'),
('ครุศาสตร์อุตสาหกรรมและเทคโนโลยี', 'ภาษาและสังคม'),
('เทคโนโลยีการเกษตร', 'วิทยาศาสตร์การประมง'),
('เทคโนโลยีการเกษตร', 'เทคโนโลยีการผลิตพืช'),
('เทคโนโลยีการเกษตร', 'เทคโนโลยีการผลิตสัตว์'),
('เทคโนโลยีการเกษตร', 'เทคนิคเกษตร'),
('เทคโนโลยีการเกษตร', 'ปฐพีวิทยา'),
('เทคโนโลยีการเกษตร', 'เทคโนโลยีการจัดการศัตรูพืช'),
('เทคโนโลยีการเกษตร', 'นวัตกรรมการสื่อสารและพัฒนาการเกษตร'),
('วิทยาศาสตร์', 'คณิตศาสตร์'),
('วิทยาศาสตร์', 'วิทยาการคอมพิวเตอร์'),
('วิทยาศาสตร์', 'เคมี'),
('วิทยาศาสตร์', 'ชีววิทยา'),
('วิทยาศาสตร์', 'ฟิสิกส์'),
('วิทยาศาสตร์', 'สถิติ'),
('อุตสาหกรรมอาหาร', 'อุตสาหกรรมอาหาร'),
('เทคโนโลยีสารสนเทศ', 'เทคโนโลยีสารสนเทศ'),
('วิทยาลัยนานาชาติ', 'วิศวกรรมซอฟต์แวร์'),
('วิทยาลัยนานาชาติ', 'การจัดการวิศวกรรมและเทคโนโลยี'),
('วิทยาลัยนาโนเทคโนโลยีพระจอมเกล้าลาดกระบัง', 'นาโนวิทยาและนาโนเทคโนโลยี'),
('วิทยาลัยนวัตกรรมการผลิตขั้นสูง', 'วิศวกรรมระบบการผลิต'),
('การบริหารและจัดการ', 'บริหารธุรกิจเกษตร'),
('การบริหารและจัดการ', 'บริหารธุรกิจ'),
('การบริหารและจัดการ', 'เศรษฐศาสตร์ธุรกิจและการจัดการ'),
('วิทยาลัยอุตสาหกรรมการบินนานาชาติ', 'วิศวกรรมเครื่องกล'),
('วิทยาลัยอุตสาหกรรมการบินนานาชาติ', 'วิศวกรรมการบิน'),
('วิทยาลัยอุตสาหกรรมการบินนานาชาติ', 'นวัตกรรมการจัดการอุตสาหกรรมการบินและการบริการ'),
('ศิลปศาสตร์', 'ศิลปศาสตร์ประยุกต์'),
('ศิลปศาสตร์', 'ภาษา'),
('ศิลปศาสตร์', 'มนุษยศาสตร์และสังคมศาสตร์'),
('แพทยศาสตร์', 'แพทยศาสตร์นานาชาติ'),
('วิทยาลัยวิศวกรรมสังคีต', 'วิศวกรรมดนตรีและสื่อประสม'),
('วิทยาเขตชุมพรเขตรอุดมศักดิ์', 'เทคโนโลยีการเกษตร'),
('วิทยาเขตชุมพรเขตรอุดมศักดิ์', 'วิศวกรรมศาสตร์'),
('วิทยาเขตชุมพรเขตรอุดมศักดิ์', 'พื้นฐานทั่วไป'),
('ทันตแพทยศาสตร์', 'Dentistry');

-- --------------------------------------------------------

--
-- Table structure for table `interest`
--

CREATE TABLE `interest` (
  `Group_subject` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ID` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `interest`
--

INSERT INTO `interest` (`Group_subject`, `ID`) VALUES
('8', 2),
('9', 2);

-- --------------------------------------------------------

--
-- Table structure for table `notify`
--

CREATE TABLE `notify` (
  `ID_notify` int(11) NOT NULL,
  `msg_notify` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `create_by` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `from_post` int(11) NOT NULL,
  `status_notify` int(11) NOT NULL,
  `time_notify` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `to_ID` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `notify`
--

INSERT INTO `notify` (`ID_notify`, `msg_notify`, `create_by`, `from_post`, `status_notify`, `time_notify`, `to_ID`) VALUES
(1, 'กรุณาตรวจสอบข้อความในโพสของคุณด้วยว่าผิดกฎหรือไม่?', 'admin', 2, 1, '2021-11-17 06:23:02', 3),
(2, 'กรุณาตรวจสอบข้อความในโพสของคุณด้วยว่าผิดกฎหรือไม่?', 'admin', 3, 1, '2021-11-17 06:23:05', 1);

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `ID_post` int(11) UNSIGNED NOT NULL,
  `Group_subject` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ID_subject` int(8) NOT NULL,
  `name_subject` varchar(75) COLLATE utf8_unicode_ci NOT NULL,
  `type_post` int(2) NOT NULL,
  `title_post` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `msg_post` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `time_post` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `create_by` bigint(20) UNSIGNED NOT NULL,
  `report` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`ID_post`, `Group_subject`, `ID_subject`, `name_subject`, `type_post`, `title_post`, `msg_post`, `time_post`, `create_by`, `report`) VALUES
(1, 'กลุ่มภาษาและการสื่อสาร', 90201003, 'ENGLISH FOR ACADEMIC PURPOSES', 1, 'test1', 'qwertyuiopasdfghjklzxcvbnm', '2021-11-15 21:27:55', 2, 0),
(2, 'กลุ่มคุณค่าแห่งชีวิต', 90641001, 'CHARM SCHOOL', 1, 'test2', 'qwertyuiopasdfghjklzxcvbnm', '2021-11-17 04:10:26', 3, 1),
(3, 'กลุ่มภาษาและการสื่อสาร', 90106003, 'ARTS OF EMOTION DEVELOPMENT', 2, 'test', 'fd8oiawegfjiaslJFol', '2021-11-17 06:21:46', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `ID_subject` int(8) NOT NULL,
  `Name_subject` varchar(75) COLLATE utf8_unicode_ci NOT NULL,
  `Group_subject` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`ID_subject`, `Name_subject`, `Group_subject`) VALUES
(90101002, 'MATHEMATICS IN DAILY LIFE', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90101003, 'STATISTICS IN DAILY LIFE', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90101007, 'INTRODUCTION TO MATHEMATICAL ECONOMICS', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90101008, 'MATHEMATICS IN BUSINESS AND INDUSTRY', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90102005, 'INTRODUCTION TO INFORMATION SYSTEMS FOR MANAGEMENT', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90104003, 'HEALTH AND NUTRITION', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90104005, 'SCIENCE OF PHOTOGRAPHY', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90104007, 'FOOD SCIENCE IN DAILY LIFE', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90104009, 'ENVIRONMENT AND NATURAL RESOURCES CONSERVATION', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90104010, 'HOME GARDEN MANAGEMENT', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90104011, 'PET MANAGEMENT', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90106002, 'HUMAN AND ENERGY', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90106003, 'EARTH AND UNIVERSE', 'กลุ่มวิชาวิทยาศาสตร์และคณิตศาสตร์'),
(90201003, 'ENGLISH FOR ACADEMIC PURPOSES', 'กลุ่มวิชาภาษา'),
(90201012, 'DEVELOPMENT OF READING AND WRITING SKILLS IN ENGLISH', 'กลุ่มวิชาภาษา'),
(90201013, 'ENGLISH FOR MANAGEMENT', 'กลุ่มวิชาภาษา'),
(90201016, 'ENGLISH FOR PROFESSIONAL COMMUNICATION', 'กลุ่มวิชาภาษา'),
(90201017, 'ENGLISH FOR BUSINESS', 'กลุ่มวิชาภาษา'),
(90201020, 'ENGLISH FOR INDUSTRY', 'กลุ่มวิชาภาษา'),
(90201024, 'ENGLISH FOR PROFESSIONAL PURPOSES', 'กลุ่มวิชาภาษา'),
(90201029, 'ENGLISH FOR TOURISM AND TRAVELLING', 'กลุ่มวิชาภาษา'),
(90201035, 'WRITING AND SPEAKING IN THE PROFESSIONS', 'กลุ่มวิชาภาษา'),
(90201040, 'ORAL ENGLISH COMMUNICATION AT WORK', 'กลุ่มวิชาภาษา'),
(90302001, 'GENERAL PSYCHOLOGY', 'กลุ่มวิชามนุษยศาสตร์'),
(90302003, 'HUMAN RELATIONS', 'กลุ่มวิชามนุษยศาสตร์'),
(90302010, 'PSYCHOLOGY FOR SELF DEVELOPMENT', 'กลุ่มวิชามนุษยศาสตร์'),
(90302011, 'PSYCHOLOGY OF THINKING', 'กลุ่มวิชามนุษยศาสตร์'),
(90303005, 'INTRODUCTION TO PHYSICAL EDUCATION', 'กลุ่มวิชามนุษยศาสตร์'),
(90303011, 'ENHANCEMENT OF QUALITY OF LIFE', 'กลุ่มวิชามนุษยศาสตร์'),
(90304001, 'LIBRARY USAGE AND INFORMATION', 'กลุ่มวิชามนุษยศาสตร์'),
(90305005, 'HUMAN AND TOURIM', 'กลุ่มวิชามนุษยศาสตร์'),
(90306003, 'LIVING SKILLS', 'กลุ่มวิชามนุษยศาสตร์'),
(90306007, 'HAPPINESS SKILLS', 'กลุ่มวิชามนุษยศาสตร์'),
(90306008, 'MEDITATION FOR LIFE DEVELOPMENT', 'กลุ่มวิชามนุษยศาสตร์'),
(90307007, 'SPEECH COMMUNICATION', 'กลุ่มวิชามนุษยศาสตร์'),
(90401007, 'INTRODUCTION TO THAI ECONOMY', 'กลุ่มวิชาสังคมศาสตร์'),
(90401012, 'INTRODUCTION TO MARKETING', 'กลุ่มวิชาสังคมศาสตร์'),
(90401013, 'GENERAL BUSINESS', 'กลุ่มวิชาสังคมศาสตร์'),
(90402007, 'INTRODUCTION TO PRINCIPLES OF SOCIAL AND FAMILY RIGHTS', 'กลุ่มวิชาสังคมศาสตร์'),
(90402011, 'ENGINEERING AND TECHNOLOGY LAWS', 'กลุ่มวิชาสังคมศาสตร์'),
(90402012, 'INTRODUCTION TO ASEAN TRADE AND LABOR MARKET', 'กลุ่มวิชาสังคมศาสตร์'),
(90402013, 'THAI INTELLECTUAL PROPERTY', 'กลุ่มวิชาสังคมศาสตร์'),
(90403008, 'THAI SOCIETY AND CULTURE', 'กลุ่มวิชาสังคมศาสตร์'),
(90403010, 'PUBLIC MANAGEMENT', 'กลุ่มวิชาสังคมศาสตร์'),
(90591002, 'SPORTS AND RECREATIONAL ACTIVITIES', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591003, 'IMMUNITY OF MIND', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591004, 'ARTS OF EMOTION DEVELOPMENT', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591005, 'DESIGNING YOUR LIFE', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591006, 'POWER OF PERSONALITY', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591008, 'PHOTOGRAPHY APPRECIATION', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591009, 'MEDITATION FOR LIFE DEVELOPMENT', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591011, 'IMAGINATIVE ART', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591014, 'POWER OF CHANGE', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591015, 'JOY OF SHARING', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591016, 'HAPPINESS SKILLS', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591019, 'CHARM SCHOOL', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591024, 'FENG SHUI', 'กลุ่มคุณค่าแห่งชีวิต'),
(90591027, 'RAP APPRECIATION', 'กลุ่มคุณค่าแห่งชีวิต'),
(90592001, 'WORLD SOCIETY AWARENESS', 'กลุ่มวิถีแห่งสังคม'),
(90592002, 'LIVING IN DIGITAL SOCIETY', 'กลุ่มวิถีแห่งสังคม'),
(90592003, 'APPLIED THAI WISDOMS', 'กลุ่มวิถีแห่งสังคม'),
(90592004, 'CONTEMPORARY CULTURE', 'กลุ่มวิถีแห่งสังคม'),
(90592007, 'THE PHILOSOPHY OF SUFFICIENCY ECONOMY', 'กลุ่มวิถีแห่งสังคม'),
(90592008, 'TODAY\'S THAI SOCIETY', 'กลุ่มวิถีแห่งสังคม'),
(90592013, 'NATIONAL SECURITY DEVELOPMENT', 'กลุ่มวิถีแห่งสังคม'),
(90592016, 'THAI CULTURE AND TOURISM', 'กลุ่มวิถีแห่งสังคม'),
(90592017, 'SPORTS TOURISM', 'กลุ่มวิถีแห่งสังคม'),
(90592020, 'PATH TO CAREER', 'กลุ่มวิถีแห่งสังคม'),
(90592022, 'THAI ASTROLOGY', 'กลุ่มวิถีแห่งสังคม'),
(90592023, 'DYNAMICS OF THAI SOCIETY', 'กลุ่มวิถีแห่งสังคม'),
(90592028, 'TREE DOCTOR', 'กลุ่มวิถีแห่งสังคม'),
(90592029, 'GAMBLING LITERACY', 'กลุ่มวิถีแห่งสังคม'),
(90592033, 'ACTIVE AGING SOCIETY', 'กลุ่มวิถีแห่งสังคม'),
(90593001, 'INTEGRATED THINKING', 'กลุ่มศาสตร์แห่งการคิด'),
(90593002, 'THINK EARTH', 'กลุ่มศาสตร์แห่งการคิด'),
(90593003, 'SUSTAINABLE ENERGY', 'กลุ่มศาสตร์แห่งการคิด'),
(90593005, 'INNOVATION UNBOXED', 'กลุ่มศาสตร์แห่งการคิด'),
(90593007, 'SERIES IN DAILY LIFE', 'กลุ่มศาสตร์แห่งการคิด'),
(90593009, 'IMMUNITY THROUGH MEDIA', 'กลุ่มศาสตร์แห่งการคิด'),
(90593015, 'FUN WITH AI', 'กลุ่มศาสตร์แห่งการคิด'),
(90593016, 'INFOGRAPHIC DESIGN', 'กลุ่มศาสตร์แห่งการคิด'),
(90593017, 'FUN WITH DRUGS AND HERBS', 'กลุ่มศาสตร์แห่งการคิด'),
(90593019, 'DIGITAL STORY TELLING IN JOURNEY', 'กลุ่มศาสตร์แห่งการคิด'),
(90593021, 'BCG ECONOMY IN ACTION', 'กลุ่มศาสตร์แห่งการคิด'),
(90594001, 'MODERN ENTREPRENEURS', 'ศิลปแห่งการจัดการ'),
(90594002, 'SOCIAL ENTREPRENEURS', 'ศิลปแห่งการจัดการ'),
(90594003, 'MODERN MANAGEMENT AND LEADERSHIP', 'ศิลปแห่งการจัดการ'),
(90594004, 'INVESTMENT PLANNING', 'ศิลปแห่งการจัดการ'),
(90594006, 'LAW FOR NEW GENERATION', 'ศิลปแห่งการจัดการ'),
(90594009, 'KNOWLEDGE MANAGEMENT FOR INNOVATION DEVELOPMENT', 'ศิลปแห่งการจัดการ'),
(90594012, 'INNOVATIVE ENTREPRENEURS', 'ศิลปแห่งการจัดการ'),
(90594013, 'FUN WITH ONLINE BUSINESS', 'ศิลปแห่งการจัดการ'),
(90594015, 'CONTEMPORARY MARKETING', 'ศิลปแห่งการจัดการ'),
(90594016, 'SMART TIPS FOR BEGINNING INVESTERS', 'ศิลปแห่งการจัดการ'),
(90595004, 'DEVELOPMENT OF READING AND WRITING SKILLS IN ENGLISH', 'กลุ่มภาษาและการสื่อสาร'),
(90595012, 'ENGLISH FOR PROFESSIONAL COMMUNICATION', 'กลุ่มภาษาและการสื่อสาร'),
(90595014, 'ENGLISH FOR BUSINESS', 'กลุ่มภาษาและการสื่อสาร'),
(90595016, 'ENGLISH FOR INDUSTRY', 'กลุ่มภาษาและการสื่อสาร'),
(90595017, 'BASIC ENGLISH PRONUNCIATION', 'กลุ่มภาษาและการสื่อสาร'),
(90595022, 'LISTENING AND READING FOR IMPROVING LIFE QUALITY', 'กลุ่มภาษาและการสื่อสาร'),
(90595026, 'LANGUAGE IN THAI SOCIETY', 'กลุ่มภาษาและการสื่อสาร'),
(90595027, 'ENGLISH FOR PUBLIC RELATIONS', 'กลุ่มภาษาและการสื่อสาร'),
(90595029, 'ENGLISH FOR DESIGN', 'กลุ่มภาษาและการสื่อสาร'),
(90595033, 'CHINESE FOR TRAVEL', 'กลุ่มภาษาและการสื่อสาร'),
(90595037, 'FOUNDATION CHINESE', 'กลุ่มภาษาและการสื่อสาร'),
(90595039, 'CHINESE GRAMMAR AND IDIOMS AND PROVERBS', 'กลุ่มภาษาและการสื่อสาร'),
(90641001, 'CHARM SCHOOL', 'กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21 '),
(90641002, 'DIGITAL INTELLIGENCE QUOTIENT', 'กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21 '),
(90641003, 'SPORTS AND RECREATIONAL ACTIVITIES', 'กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21 '),
(90642012, 'DESIGN THINKING', 'กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ'),
(90642043, 'SCIENCE OF BURGER', 'กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ'),
(90642090, 'GLOBAL INSIDE', 'กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ'),
(90642108, 'DIGITAL PHOTOGRAPHY TECHNOLOGY', 'กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ'),
(90642116, 'SMART CITY AND CITY INNOVATION', 'กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ'),
(90642144, 'MAGIC MIRROR', 'กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ'),
(90643024, 'HAPPINESS FARMS', 'กลุ่มทักษะด้านการจัดการและภาวะความเป็นผู้นำ');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` bigint(20) UNSIGNED NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `code` mediumint(50) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `major` varchar(255) CHARACTER SET utf32 COLLATE utf32_unicode_ci DEFAULT NULL,
  `introduce` varchar(255) CHARACTER SET utf32 COLLATE utf32_unicode_ci DEFAULT NULL,
  `picture` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `email`, `password`, `code`, `status`, `name`, `major`, `introduce`, `picture`, `sex`) VALUES
(0, 'admin', '21232f297a57a5a743894a0e4a801fc3', NULL, 3, NULL, NULL, NULL, NULL, NULL),
(1, 'teacher', '8d788385431273d11e8b43bb78f3aa41', NULL, 2, NULL, NULL, NULL, NULL, NULL),
(2, 'student', 'cd73502828457d15655bbd7a63fb0bc8', NULL, 1, NULL, 'วิศวกรรมคอมพิวเตอร์', NULL, NULL, 'M'),
(3, 'student2', '213ee683360d88249109c2f92789dbc3', NULL, 1, NULL, NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`ID_comment`),
  ADD KEY `create_by` (`create_by`,`from_post`),
  ADD KEY `comment_2` (`from_post`);

--
-- Indexes for table `education`
--
ALTER TABLE `education`
  ADD KEY `major` (`major`);

--
-- Indexes for table `notify`
--
ALTER TABLE `notify`
  ADD PRIMARY KEY (`ID_notify`),
  ADD KEY `ID` (`to_ID`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`ID_post`),
  ADD UNIQUE KEY `ID_subject` (`ID_subject`),
  ADD KEY `post_2` (`name_subject`),
  ADD KEY `post_4` (`create_by`),
  ADD KEY `Group_subject` (`Group_subject`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`ID_subject`),
  ADD UNIQUE KEY `ID_subject_2` (`ID_subject`),
  ADD UNIQUE KEY `ID_subject_3` (`ID_subject`),
  ADD KEY `Group_subject` (`Group_subject`),
  ADD KEY `Name_subject_2` (`Name_subject`),
  ADD KEY `ID_subject` (`ID_subject`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `username` (`email`),
  ADD UNIQUE KEY `code` (`code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `ID_comment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `notify`
--
ALTER TABLE `notify`
  MODIFY `ID_notify` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `ID_post` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `notify`
--
ALTER TABLE `notify`
  ADD CONSTRAINT `n1` FOREIGN KEY (`to_ID`) REFERENCES `users` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_1` FOREIGN KEY (`ID_subject`) REFERENCES `subject` (`ID_subject`) ON UPDATE CASCADE,
  ADD CONSTRAINT `post_2` FOREIGN KEY (`name_subject`) REFERENCES `subject` (`Name_subject`) ON UPDATE CASCADE,
  ADD CONSTRAINT `post_3` FOREIGN KEY (`Group_subject`) REFERENCES `subject` (`Group_subject`) ON UPDATE CASCADE,
  ADD CONSTRAINT `post_4` FOREIGN KEY (`create_by`) REFERENCES `users` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
