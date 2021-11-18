<title>Eletiva | Home</title>
<link rel="stylesheet" type="text/css" href="css/home_index.css">
<?php
require "dbconnect.php";
error_reporting(0);
include "header.php";
?>
<?php if(isset($_SESSION['status']) || empty($_SESSION['status'])): ?>
    <style>
    a.swPage {
    width: 100%;
    height: auto;
    background-color: wheat;
    color: black;
    font-weight: bold;
}

a.swPage:hover {
    text-decoration: none;
    color: red;
}

.swp {
    text-align: center;
}
</style>
<section>
    <?php if($_SESSION['status'] != 3): ?>
        <img class="banner" src="images/home.png" alt="Banner">
       <?php else: ?>
        <div style="padding: 10px;   padding-bottom: 1px;    width: 100%;    background: rgb(255, 231, 125);    margin-bottom: 30px">
            <a href="admin-home.php" class="swPage swp">
                <p class="swp">-- GO to Admin Page --</p>
            </a>
            </div>
        <?php endif ?>
    <!-- โพสล่าสุด -->
    <div class="inf">
     
    
        <!-- -ข้อมูล -->
        <?php              
        $query = "SELECT * FROM post WHERE type_post='3' ORDER BY time_post DESC";
        $result = mysqli_query($connect, $query);
        //"SELECT COUNT(ID_comment) FROM comment WHERE create_by = $";
    
            echo'<div class="posttext">';
            echo'<i class="fas fa-clock"></i>';
            echo'<p class="mainC">โพสจากอาจารย์</p>';
            echo'</div>';
            while($row =  mysqli_fetch_assoc($result)){
                $x = $row['ID_post'];
                $findCA = "SELECT COUNT(ID_comment) FROM comment WHERE from_post='$x'";
                $y = mysqli_query($connect, $findCA);
                $z = $row['create_by'];
                $queryU = "SELECT * FROM users WHERE ID = '$z'";
                $ua = mysqli_query($connect, $queryU);
                $rowUser = mysqli_fetch_assoc($ua);
                $name = (empty($rowUser['name'])) ? 'ไม่ระบุ' : $rowUser["name"];

                echo '<a href="post.php?id='.$row['ID_post'].'" class="Content">';
                echo '    <div class="post_btn">';
                echo '        <div class="A_left">';
                echo '            <i class="icon_next fas fa-chevron-circle-right"></i>';
                echo '            <h4 class="textC" name="Post">'.$row['title_post'].'</h4>';
                echo '            <h6 class="textS" name="subject">'.$row['Group_subject'].' : '.$row['ID_subject'].'</h6>';
                echo '            <br><p class="Timestamp">User:'.$name.' Time:'.$row['time_post'].'</p>';
                echo '        </div>';
                if($n =  mysqli_fetch_assoc($y)){
                echo '        <div  class="A_right">';
                echo '            <i class="iconcomment far fa-comment-dots"></i>';
                echo '            <h5 class="commentN">'.$n['COUNT(ID_comment)'].'</h5>';
                echo '        </div>';
                }
                echo '    </div>';
                echo '</a>';
        }
        ?>
    </div>

    <!-- โพสยอดนิยม -->
    <div class="inf">
        <!-- -ข้อมูล -->
        <?php              
        $query = "SELECT * FROM post WHERE type_post='1' ORDER BY time_post DESC";
        $result = mysqli_query($connect, $query);
 
            echo'<div class="posttext">';
            echo'<i class="fas fa-star"></i>';
            echo'<p class="mainC">โพสธรรมดา</p>';
            echo'</div>';
            while($row =  mysqli_fetch_assoc($result)){
                $x = $row['ID_post'];
                $findCB = "SELECT COUNT(ID_comment) FROM comment WHERE from_post='$x'";
                $y = mysqli_query($connect, $findCB);
                $z = $row['create_by'];
                $queryU = "SELECT * FROM users WHERE ID = '$z'";
                $ub = mysqli_query($connect, $queryU);
                $rowUser = mysqli_fetch_assoc($ub);
                $name = (empty($rowUser['name'])) ? 'ไม่ระบุ' : $rowUser["name"];
                
                echo '<a href="post.php?id='.$row['ID_post'].'" class="Content">';
                echo '    <div class="post_btn">';
                echo '        <div class="A_left">';
                echo '            <i class="icon_next fas fa-chevron-circle-right"></i>';
                echo '            <h4 class="textC" name="Post">'.$row['title_post'].'</h4>';
                echo '            <h6 class="textS" name="subject">'.$row['Group_subject'].' : '.$row['ID_subject'].'</h6>';
                echo '            <br><p class="Timestamp">User:'.$name.' Time:'.$row['time_post'].'</p>';
                echo '        </div>';
                if($n =  mysqli_fetch_assoc($y)){
                echo '        <div  class="A_right">';
                echo '            <i class="iconcomment far fa-comment-dots"></i>';
                echo '            <h5 class="commentN">'.$n['COUNT(ID_comment)'].'</h5>';
                echo '        </div>';
                }
                echo '    </div>';
                echo '</a>';
     
        }
        ?>
    </div>

    <!-- โพสแนะนำ -->
    <div class="inf">
        
        <!-- -ข้อมูล -->
        <?php              
        $query = "SELECT * FROM post WHERE type_post='2' ORDER BY time_post DESC";
        $result = mysqli_query($connect, $query);
            echo'<div class="posttext">';
            echo'<i class="fas fa-bookmark"></i>';
            echo'<p class="mainC">โพสรีวิว</p>';
            echo'</div>';
            while($row =  mysqli_fetch_assoc($result)){
                $x = $row['ID_post'];
                $findCC = "SELECT COUNT(ID_comment) FROM comment WHERE from_post='$x'";
                $y = mysqli_query($connect, $findCC);
                $z = $row['create_by'];
                $queryU = "SELECT * FROM users WHERE ID = '$z'";
                $uc = mysqli_query($connect, $queryU);
                $rowUser = mysqli_fetch_assoc($uc);
                $name = (empty($rowUser['name'])) ? 'ไม่ระบุ' : $rowUser["name"];

                echo '<a href="post.php?id='.$row['ID_post'].'" class="Content">';
                echo '    <div class="post_btn">';
                echo '        <div class="A_left">';
                echo '            <i class="icon_next fas fa-chevron-circle-right"></i>';
                echo '            <h4 class="textC" name="Post">'.$row['title_post'].'</h4>';
                echo '            <h6 class="textS" name="subject">'.$row['Group_subject'].' : '.$row['ID_subject'].'</h6>';
                echo '            <br><p class="Timestamp">User:'.$name;
                echo'  Time:'.$row['time_post'].'</p>';
                echo '        </div>';
                if($n = mysqli_fetch_assoc($y)){
                echo '        <div  class="A_right">';
                echo '            <i class="iconcomment far fa-comment-dots"></i>';
                echo '            <h5 class="commentN">'.$n['COUNT(ID_comment)'].'</h5>';
                echo '        </div>';
                }
                echo '    </div>';
                echo '</a>';
        }
        ?>
    </div>
</section>
<!--
<nav>
    <div class="footer">
        <p>Thank you to everyone who has used our website.</p>
    </div>    
</nav>
-->
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>