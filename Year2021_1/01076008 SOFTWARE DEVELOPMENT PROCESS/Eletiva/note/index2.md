<?php
session_start();
require "dbconnect.php";

$email = $_SESSION['email'];
$password = $_SESSION['password'];
$status = $_SESSION['status'];
$check = "SELECT email,password,status FROM users WHERE email = '$email ' AND password = '$password' AND status = '$status'";
$result = mysqli_query($connect, $check);
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eletiva | Home</title>
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
    <?php
    if($result){
        if($_SESSION["status"] == 0){
            //echo "student"; 
        echo'<ul class="menu">';
        echo'<li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>';
        echo'<li class="item"><a href="#" title="Creat Post"><i class="iconnav fas fa-edit"><span class="navTitle">Creat Post</span></i></a></i></li>';
        echo'<li class="item"><a href="#" title="Notification"><i class="iconnav fas fa-bell"><span class="navTitle">Notification</span><div class = "number">num</div></i></a></li>';
        echo'<li class="item"><a href="search.php" title="Search"><i class="iconnav fas fa-search"><span class="navTitle">Search</span></i></a></li>';
        echo'<li class="item"><a href="#" title="Category"><i class="iconnav fas fa-th-large"><span class="navTitle">Category</span></i></a></li>';
        echo'<li class="item has-submenu">';
        echo'<a class="usernav" tabindex="0">My User</a>';
        echo'<ul class="submenu userlink">';
        echo'<li class="subitem"><a href="#"><span class="Texthide">---</span>My Page<span class="Texthide">---</span></a></li>';
        echo'<li class="subitem"><a href="#">My Post</a></li>';
        echo'<li class="subitem"><a href="#">Setting</a></li>';
        echo'<li class="subitem logoutnav"><a href="logout.php">Log Out</a></li>';
        echo'</ul>';
        echo'</li>';
        echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
        echo'</ul>';
        }
        else if ($_SESSION["status"] == 1){
            //echo "teacher";
        echo'<ul class="menu">';
        echo'<li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>';
        echo'<li class="item"><a href="#" title="Creat Post"><i class="iconnav fas fa-edit"><span class="navTitle">Creat Post</span></i></a></i></li>';
        echo'<li class="item"><a href="#" title="Notification"><i class="iconnav fas fa-bell"><span class="navTitle">Notification</span><div class = "number">num</div></i></a></li>';
        echo'<li class="item"><a href="search.php" title="Search"><i class="iconnav fas fa-search"><span class="navTitle">Search</span></i></a></li>';
        echo'<li class="item"><a href="#" title="Category"><i class="iconnav fas fa-th-large"><span class="navTitle">Category</span></i></a></li>';
        echo'<li class="item has-submenu">';
        echo'<a class="usernav" tabindex="0">My User</a>';
        echo'<ul class="submenu userlink">';
        echo'<li class="subitem"><a href="#"><span class="Texthide">---</span>My Page<span class="Texthide">---</span></a></li>';
        echo'<li class="subitem"><a href="#">My Post</a></li>';
        echo'<li class="subitem"><a href="#">Setting</a></li>';
        echo'<li class="subitem logoutnav"><a href="logout.php">Log Out</a></li>';
        echo'</ul>';
        echo'</li>';
        echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
        echo'</ul>';
        }
        else if ($_SESSION["status"] == 2){
            //echo "admin";
            //echo '<p><a href="admin.php">admin page</a></p>';
        echo'<ul class="menu">';
        echo'<li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>';
        echo'<li class="item"><a href="logout.php title="Logout"><i class="iconnav fas fa-sign-out-alt"><span class="navTitle">Log Out</span></i></a></li>';
        echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
        echo'</ul>';
        }
    }
    else{
        // Guest
        echo'<ul class="menu">';
        echo'<li class="logo"><a class="logonav" href="index.php">ELETIVA</a></li>';
        echo'<li class="item"><a href="search.php" title="Search"><i class="iconnav fas fa-search"><span class="navTitle">Search</span></i></a></li>';
        echo'<li class="item"><a href="#" title="Category"><i class="iconnav fas fa-th-large"><span class="navTitle">Category</span></i></a></li>';
        echo'<li class="item button"><a class="loginnav" href="login-user.php">Log In</a></li>';
        echo'<li class="toggle"><a class="icontog" href="#"><i class="icontog fas fa-bars"></i></a></li>';
        echo'</ul>';
    }
    ?>

</nav>
<section>
    <img class="banner" src="images/home.png" alt="Banner">
    <!-- โพสล่าสุด -->
    <div class="inf">
        <div class="posttext">
            <i class="fas fa-clock"></i>
            <p class="mainC">โพสล่าสุด</p>
        </div>
        <!-- -ข้อมูล -->
        <?php              
        echo '<a href="#Test1" class="Content">';
        echo '    <div class="post_btn">';
        echo '        <div class="A_left">';
        echo '            <i class="icon_next fas fa-chevron-circle-right"></i>';
        echo '            <h4 class="textC" name="Post">Post1โพส</h4>';
        echo '            <h6 class="textS" name="subject">วิชาเลือกกลุ่ม....</h6>';
        echo '            <br><p class="Timestamp">User:??? Time:???</p>';
        echo '        </div>';
        echo '        <div  class="A_right">';
        echo '            <i class="iconcomment far fa-comment-dots"></i>';
        echo '            <h5 class="commentN">num</h5>';
        echo '        </div>';
        echo '    </div>';
        echo '</a>';
        ?>
    </div>

    <!-- โพสยอดนิยม -->
    <div class="inf">
        <div class="posttext">
            <i class="fas fa-star"></i>
            <p class="mainC">โพสยอดนิยม</p>
        </div>
        <!-- -ข้อมูล -->
        <a href="#Test1" class="Content">
            <div class="post_btn">
                <div class="A_left">
                    <i class="icon_next fas fa-chevron-circle-right"></i>
                    <h4 class="textC" name="Post">Post1โพส</h4>
                    <h6 class="textS" name="subject">วิชาเลือกกลุ่ม....</h6>
                    <br><p class="Timestamp">User:??? Time:???</p>
                </div>
                <div  class="A_right">
                    <i class="iconcomment far fa-comment-dots"></i>
                    <h5 class="commentN">num</h5>
                </div>
            </div>
        </a>
    </div>

    <!-- โพสแนะนำ -->
    <div class="inf">
        <div class="posttext">
            <i class="fas fa-bookmark"></i>
            <p class="mainC">โพสแนะนำ</p>
        </div>
        <!-- -ข้อมูล -->
        <a href="#Test1" class="Content">
            <div class="post_btn">
                <div class="A_left">
                    <i class="icon_next fas fa-chevron-circle-right"></i>
                    <h4 class="textC" name="Post">Post1โพส</h4>
                    <h6 class="textS" name="subject">วิชาเลือกกลุ่ม....</h6>
                    <br><p class="Timestamp">User:??? Time:???</p>
                </div>
                <div  class="A_right">
                    <i class="iconcomment far fa-comment-dots"></i>
                    <h5 class="commentN">num</h5>
                </div>
            </div>
        </a>
    </div>
</section>
<nav>
    <div class="footer">
        <p>Thank you to everyone who has used our website.</p>
    </div>    
</nav>
<script src="javascript/navbar.js"></script>