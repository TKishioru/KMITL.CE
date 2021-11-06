<?php
require "dbconnect.php";

session_start();

if(!isset($_SESSION["email"])){
    //$_SESSION['msg'] = "You must log in first";
    header('location: index.php');
}

if($_SESSION["status"] != 2){
    header('location: index.php');
}

if(isset($_GET["logout"])){
    session_destroy();
    unset($_SESSION["email"]);
    unset($_SESSION["status"]);
    header('location: index.php');
  }
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eletiva | Admin</title>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script crossorigin="anonymous" src="https://kit.fontawesome.com/c8e4d183c2.js"></script>
    <link rel="stylesheet" type="text/css" href="css/home_index.css">
    <link rel="stylesheet" type="text/css" href="css/navbar.css">

    <!-- add icon link -->
    <link rel="icon" href="images/icon.jpg" type="image/x-icon">
    <!-- specifying a webpage icon for web clip -->
    <link rel="apple-touch-icon" href="images/icon.jpg" />

</head>
<nav> <!--id="navbar"-->
    <ul class="menu">
    <li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>
    <li class="item"><a href="logout.php" title="Logout"><i class="iconnav fas fa-sign-out-alt"><span class="navTitle">Log Out</span></i></a></li>
    <li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>
    </ul>
</nav>
ADmin Page

<script src="javascript/navbar.js"></script>