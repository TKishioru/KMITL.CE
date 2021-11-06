<?php
session_start();
session_destroy();
//header("Location: login-user.php");	
header("location: index.php");	
?>