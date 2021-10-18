-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 16, 2021 at 08:18 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

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
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` bigint(20) UNSIGNED NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `code` mediumint(50) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `faculty` varchar(255) DEFAULT NULL,
  `major` varchar(255) DEFAULT NULL,
  `introduce` varchar(255) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `interest` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `email`, `password`, `code`, `status`, `name`, `faculty`, `major`, `introduce`, `picture`, `interest`) VALUES
(0, 'admin', '21232f297a57a5a743894a0e4a801fc3', NULL, 2, NULL, NULL, NULL, NULL, NULL, '{\"elective_eng1\":\"0\",\"elective_hu\":\"0\",\"elective_so1\":\"0\",\"elective_sci\":\"0\",\"elective_free\":\"0\",\"elective_life\":\"0\",\"elective_so2\":\"0\",\"elective_think\":\"0\",\"elective_manage\":\"0\",\"elective_eng2\":\"0\",\"elective_21\":\"0\",\"elective_carrer\":\"0\",\"elective_eng3\":\"0\"}'),
(1, 'teacher', '8d788385431273d11e8b43bb78f3aa41', NULL, 1, NULL, NULL, NULL, NULL, NULL, '{\"name\":\"John\",\"age\":30,\"city\":\"New York\"}'),
(2, 'student', 'cd73502828457d15655bbd7a63fb0bc8', NULL, 0, NULL, NULL, NULL, NULL, NULL, '{\"elective_eng1\":\"0\",\"elective_hu\":\"0\",\"elective_so1\":\"0\",\"elective_sci\":\"0\",\"elective_free\":\"0\",\"elective_life\":\"0\",\"elective_so2\":\"0\",\"elective_think\":\"0\",\"elective_manage\":\"0\",\"elective_eng2\":\"0\",\"elective_21\":\"0\",\"elective_carrer\":\"0\",\"elective_eng3\":\"0\"}');

--
-- Indexes for dumped tables
--

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
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
