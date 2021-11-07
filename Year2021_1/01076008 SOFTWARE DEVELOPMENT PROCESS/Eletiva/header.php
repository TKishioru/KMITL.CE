<?php
    session_start();
    require "dbconnect.php";
?>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script crossorigin="anonymous" src="https://kit.fontawesome.com/c8e4d183c2.js"></script>
    <link rel="stylesheet" type="text/css" href="css/navbar.css">

    <?php if($_SESSION['status'] == 2) : ?>
        <link rel="stylesheet" href="css/admin-home.css">
        <link rel="stylesheet" href="css/admin-post.css">
        <link rel="stylesheet" href="css/pop-up.css">
    <?php elseif (isset($_SESSION['status']) && !empty($_SESSION['status']) || $_SESSION['status'] != 2) : ?>
        <link rel="stylesheet" type="text/css" href="css/home_index.css">
        <link rel="stylesheet" type="text/css" href="css/category.css">
    <?php endif ?>
    
    <!-- add icon link -->
    <link rel="icon" href="images/icon.jpg" type="image/x-icon">
    <!-- specifying a webpage icon for web clip -->
    <link rel="apple-touch-icon" href="images/icon.jpg" />

</head>
<?php

if(isset($_GET["logout"])){
    session_destroy();
    unset($_SESSION["email"]);
    unset($_SESSION["status"]);
    header('location: index.php');
  }

if(isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] == 3) {
   //echo 'Guest Mode!';
    echo'<nav>';
    echo'<ul class="menu">';
    echo'<li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>';
    echo'<li class="item"><a href="search.php" title="Search"><i class="iconnav fas fa-search"><span class="navTitle">Search</span></i></a></li>';
    echo'<li class="item"><a href="category.php" title="Category"><i class="iconnav fas fa-th-large"><span class="navTitle">Category</span></i></a></li>';
    echo'<li class="item button"><a class="loginnav" href="login-user.php">Log In</a></li>';
    echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
    echo'</ul>';
    echo'</nav>';
}
else{
    //echo 'User Mode!';
    $email = $_SESSION['email'];
    $password = $_SESSION['password'];
    $status = $_SESSION['status'];
    $check = "SELECT email,password,status FROM users WHERE email = '$email ' AND password = '$password' AND status = '$status'";
    $result = mysqli_query($connect, $check);

    if(mysqli_num_rows($result) != 1){
        $_SESSION['status'] = 3;
        //echo 'Guest Mode!';
        header("location: index.php");
    }
    

    if($status == 0){
        //student
        echo'<nav>';
        echo'<ul class="menu">';
        echo'<li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>';
        echo'<li class="item"><a href="creatpost.php" title="Creat Post"><i class="iconnav fas fa-edit"><span class="navTitle">Creat Post</span></i></a></i></li>';
        echo'<li class="item"><a href="notify.php" title="Notification"><i class="iconnav fas fa-bell"><span class="navTitle">Notification</span><div class = "number">num</div></i></a></li>';
        echo'<li class="item"><a href="search.php" title="Search"><i class="iconnav fas fa-search"><span class="navTitle">Search</span></i></a></li>';
        echo'<li class="item"><a href="category.php" title="Category"><i class="iconnav fas fa-th-large"><span class="navTitle">Category</span></i></a></li>';
        echo'<li class="item has-submenu">';
        echo'<a class="usernav" tabindex="0">My User</a>';
        echo'<ul class="submenu userlink">';
        echo'<li class="subitem"><a href="profile.php"><span class="Texthide">---</span>My Page<span class="Texthide">---</span></a></li>';
        echo'<li class="subitem"><a href="post_poll.php">My Post</a></li>';
        echo'<li class="subitem"><a href="setting.php">Setting</a></li>';
        echo'<li class="subitem logoutnav"><a href="logout.php" onclick="myFunction()">Log Out</a></li>';
        echo'</ul>';
        echo'</li>';
        echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
        echo'</ul>';
        echo'</nav>';
    }
    else if ($status == 1){
        //teacher
        echo'<nav id="navbar">';
        echo'<ul class="menu">';
        echo'<li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>';
        echo'<li class="item"><a href="creatpoll.php" title="Creat Poll"><i class="iconnav fas fa-edit"><span class="navTitle">Creat Poll</span></i></a></li>';
        echo'<li class="item"><a href="notify.php" title="Notification"><i class="iconnav fas fa-bell"><span class="navTitle">Notification</span><div class = "number">num</div></i></a></li>';
        echo'<li class="item"><a href="search.php" title="Search"><i class="iconnav fas fa-search"><span class="navTitle">Search</span></i></a></li>';
        echo'<li class="item"><a href="category.php" title="Category"><i class="iconnav fas fa-th-large"><span class="navTitle">Category</span></i></a></li>';
        echo'<li class="item has-submenu">';
        echo'<a class="usernav" tabindex="0">My User</a>';
        echo'<ul class="submenu userlink">';
        echo'<li class="subitem"><a href="profile.php"><span class="Texthide">---</span>My Page<span class="Texthide">---</span></a></li>';
        echo'<li class="subitem"><a href="post_poll.php">My Poll</a></li>';
        echo'<li class="subitem"><a href="setting.php">Setting</a></li>';
        echo'<li class="subitem logoutnav"><a href="logout.php" onclick="myFunction()">Log Out</a></li>';
        echo'</ul>';
        echo'</li>';
        echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
        echo'</ul>';
        echo'</nav>';
    }
    else if($status == 2){
        //Admin
        echo'<nav>';
        echo'<ul class="menu">';
        echo'<li class="logo"><a class="logonav" href="admin-home.php">ELETIVA</a></li>';
        echo'<li class="item"><a href="logout.php" onclick="myFunction()" title="Logout"><i class="iconnav fas fa-sign-out-alt"><span class="navTitle">Log Out</span></i></a></li>';
        echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
        echo'</ul>';
        echo'</nav>';
    }
}
?>
<script type="text/javascript" src="javascript/Jquery.js"></script>
<script src="javascript/navbar.js"></script>
<script>
    function myFunction() {
    //alert("You have already logged out.!");
    }
</script>