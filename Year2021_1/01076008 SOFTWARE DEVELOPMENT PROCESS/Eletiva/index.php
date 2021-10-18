
<?php
session_start();
require "dbconnect.php";
$email = $_SESSION['email'];
$password = $_SESSION['password'];
$status = $_SESSION['status'];
$check = "SELECT email,password,status FROM users WHERE email = '$email ' AND password = '$password' AND status = '$status'";
$result = mysqli_query($connect, $check);
if (mysqli_num_rows($result) != 1) {
    header('location: logout.php');
}

if (isset($_GET["logout"])) {
    session_destroy();
    unset($_SESSION["email"]);
    unset($_SESSION["status"]);
    header('location: login-user.php');
}

if($_SESSION["status"] == 0){
    echo '<p><h2>student page</h2></p>';
}

if($_SESSION["status"] == 1){
    echo '<p><h2>teacher page</h2></p>';
}

if($_SESSION["status"] == 2){
    echo '<p><h2>admin page</h2></p>';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="">

    <!-- add icon link -->
    <link rel="icon" href="images/icon.jpg" type="image/x-icon">
    <!-- specifying a webpage icon for web clip -->
    <link rel="apple-touch-icon" href="images/icon.jpg" />

</head>
<div>
    <!-- logged in user information -->
    <?php if (isset($_SESSION["email"])): ?>
        <p>Welcome <strong><?php echo $_SESSION["email"]; ?></strong></p>
        <p>status :
            <?php
if ($_SESSION["status"] == 0) {
    echo "student";
} else if ($_SESSION["status"] == 1) {
    echo "teacher";
} else if ($_SESSION["status"] == 2) {
    echo "admin";
}
?>
        <p><a href="logout.php">Logout</a></p>
        <p><a href="profile.php">Profile page</a></p>
    <?php endif?>

 <!--
    textarea {
  width: 100%;
  height: 150px;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #f8f8f8;
  resize: none;
}
    -->

</div>