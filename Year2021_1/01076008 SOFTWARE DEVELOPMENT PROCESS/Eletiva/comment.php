<title>Eletiva | </title>
<?php
require "dbconnect.php";

include "header.php";
?>
<?php if((isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] != 3) || empty($_SESSION['status'])) : ?>

    
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>