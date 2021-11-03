-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2021 at 10:49 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

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
  `code` mediumint(50) NOT NULL,
  `status` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `faculty` varchar(255) DEFAULT NULL,
  `major` varchar(255) DEFAULT NULL,
  `introduce` varchar(255) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `email`, `password`, `code`, `status`, `name`, `faculty`, `major`, `introduce`, `picture`) VALUES
(1, '1', '1', 0, 1, NULL, NULL, NULL, NULL, ''),
(2, '', 'e194ba46faf4ae67caa73ccfaa45e2c7', 0, 0, NULL, NULL, NULL, NULL, ''),
(4, '12', '12', 0, 0, NULL, NULL, NULL, NULL, ''),
(5, '62010090', 'dfg', 0, 0, NULL, NULL, NULL, NULL, ''),
(11, '11', '6512bd43d9caa6e02c990b0a82652dca', 0, 1, NULL, NULL, NULL, NULL, ''),
(12, '14', 'aab3238922bcc25a6f606eb525ffdc56', 0, 0, NULL, NULL, NULL, NULL, ''),
(13, '546456', 'c4ca4238a0b923820dcc509a6f75849b', 0, 0, NULL, NULL, NULL, NULL, ''),
(14, '16', '202cb962ac59075b964b07152d234b70', 0, 0, NULL, NULL, NULL, NULL, ''),
(15, 'zxc', 'a95aa44766a8e63c0db905f04d549ab7', 0, 0, NULL, NULL, NULL, NULL, ''),
(16, '456', 'a95aa44766a8e63c0db905f04d549ab7', 0, 0, NULL, NULL, NULL, NULL, ''),
(17, '62010090@kmitl.ac.th', '31316737269750506b1c0f186e4c4d0c', 0, 0, NULL, NULL, NULL, NULL, ''),
(18, 'khampeerada44@gmail.com', '167a79ea31910f5d5c62a8bd60dacf7b', 0, 1, NULL, NULL, NULL, NULL, ''),
(19, '123456789', '6652f1488aff7d45ce587ebf5d2c0efb', 0, 1, NULL, NULL, NULL, NULL, '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `username` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
