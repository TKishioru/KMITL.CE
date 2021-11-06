<title>Eletiva | Notification</title>
<?php
require "dbconnect.php";

include "header.php";
?>
<section>
    <!-- โพสล่าสุด -->
    <div class="inf">
        <br>
        <div class="posttext">
            <i class="fas fa-bell"></i>
            <p class="mainC">การแจ้งเตือน</p>
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
</section>