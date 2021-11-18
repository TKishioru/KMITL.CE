<title>Eletiva | Admin Page</title>
<link rel="stylesheet" type="text/css" href="css/home_index.css">
<?php
require "dbconnect.php";

include "header.php";
?>
<?php if(isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] == 3) : ?>
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
     <div style="padding: 10px;   padding-bottom: 1px;    width: 100%;    background: rgb(255, 231, 125);    margin-bottom: 30px">
            <a href="index.php" class="swPage swp">
                <p class="swp">-- GO to User Page --</p>
            </a>
            </div>     
        <!-- โพสล่าสุด -->
        <div class="inf">
            
            
        <div class="posttext">
            <i class="fas fa-file-alt"></i>
            <p class="mainC">รายงาน</p>
        </div>
        <!-- -ข้อมูล -->
        <?php              
        $query = "SELECT * FROM post WHERE report='1'";
        $result = mysqli_query($connect, $query);

        while($row =  mysqli_fetch_assoc($result)){
            $x = $row['ID_post'];
            $findCA = "SELECT COUNT(ID_comment) FROM comment WHERE from_post='$x'";
            $y = mysqli_query($connect, $findCA);

            if($n =  mysqli_fetch_assoc($y)){
                echo '<a href="admin-post.php?id='.$row['ID_post'].'" class="Content">';
                echo '    <div class="post_btn">';
                echo '        <div class="A_left">';
                echo '            <i class="icon_next fas fa-chevron-circle-right"></i>';
                echo '            <h4 class="textC" name="Post">'.$row['title_post'].'</h4>';
                echo '            <h6 class="textS" name="subject">'.$row['Group_subject'].' : '.$row['ID_subject'].'</h6>';
                echo '            <br><p class="Timestamp">User:'.$row['create_by'].' Time:'.$row['time_post'].'</p>';
                echo '        </div>';
                echo '        <div  class="A_right">';
                echo '            <i class="iconcomment far fa-comment-dots"></i>';
                echo '            <h5 class="commentN">'.$n['COUNT(ID_comment)'].'</h5>';
                echo '        </div>';
                echo '    </div>';
                echo '</a>';
            }
        }
        ?>
</section>

<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>