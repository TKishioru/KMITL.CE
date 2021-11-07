<title>Eletiva | Category</title>
<?php
require "dbconnect.php";

include "header.php";
?>
<div class="inf ">
    <div id="myBtnContainer">
        <br>
        <button class="btn active" name="show_all"><i class="fas fa-book"></i>ทุกหมวด</button>
      <button class="btn" name="show_eng1"><i class="fas fa-language"></i>หมวดภาษา</button>
      <button class="btn" name="show_hu"><i class="fas fa-users"></i>หมวดมนุษย์ศาสตร์</button>
      <button class="btn" name="show_so1"><i class="fas fa-globe"></i>หมวดสังคมศาสตร์</button>
      <button class="btn" name="show_sci"><i class="fas fa-atom"></i>หมวดวิทยาศาสตร์ฯ</button>
      <button class="btn" name="show_free"> <i class="fas fa-dove"></i>หมวดวิชาเลือกเสรี</button>
      <button class="btn" name="show_life"><i class="fas fa-hand-holding-heart"></i>หมวดคุณค่าแห่งชีวิต</button>
      <button class="btn" name="show_so2"><i class="fas fa-icons"></i>หมวดวิถีแห่งสังคม</button>
      <button class="btn" name="show_think"><i class="fas fa-brain"></i>ศาสตร์แห่งการคิด</button>
      <button class="btn" name="elective_manage"><i class="fas fa-chart-line"></i>ศิลปแห่งการจัดการ</button>
      <button class="btn" name="elective_eng2"><i class="fas fa-comments"></i>ภาษาและการสื่อสาร</button>
      <button class="btn btn_L" name="elective_21"><i class="fas fa-vr-cardboard"></i>หมวดทักษะที่จำเป็นในศตวรรษที่ 21</button>
      <button class="btn btn_L" name="elective_carrer"><i class="fas fa-user-tie"></i>ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</button>
      <button class="btn btn_L" name="elective_leader"><i class="fas fa-book-reader"></i>ทักษะด้านการจัดการและภาวะความเป็นผู้นำ</button>
      <button class="btn btn_L" name="elective_eng3"><i class="fas fa-globe-americas"></i>หมวดทักษะด้านภาษาและการสื่อสาร</button>
      </div>
    </div>
<section>
    <!-- โพสล่าสุด -->
    <div class="inf ">
        <div class="posttext">
            <i class="fas fa-bookmark"></i>
            <p class="mainC">ผลการค้นหา</p>
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
<script src="javascript/category.js"></script>