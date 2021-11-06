<title>Eletiva | Home</title>
<?php
require "dbconnect.php";

include "header.php";
?>

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
