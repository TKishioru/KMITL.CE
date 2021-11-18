<title>Eletiva | Creat Poll</title>
<?php
//For Teacher
require "dbconnect.php";

include "header.php";
?>
<?php if(isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] == 2) : ?>
poll
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>