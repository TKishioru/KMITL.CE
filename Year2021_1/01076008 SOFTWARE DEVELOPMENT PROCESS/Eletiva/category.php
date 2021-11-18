<title>Eletiva | Category</title>
<link rel="stylesheet" type="text/css" href="css/home_index.css">
<link rel="stylesheet" type="text/css" href="css/category.css">

<?php
require "dbconnect.php";

include "header.php";
?>
<?php if((isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] != 3) || empty($_SESSION['status'])) : ?>
<div class="inf ">
    <div id="myBtnContainer">
        <br>
        <form method="POST">
     <button class="btn active" value="" name="E00"><i class="fas fa-book"></i>ทุกหมวด</button>
     <button class="btn" value="กลุ่มวิชาภาษา" name="E01"><i class="fas fa-language"></i>หมวดภาษา</button>
     <button class="btn" value="กลุ่มวิชามนุษย์ศาสตร์" name="E02"><i class="fas fa-users"></i>หมวดมนุษย์ศาสตร์</button>
     <button class="btn" value="กลุ่มวิชาสังคมศาสตร์" name="E03"><i class="fas fa-globe"></i>หมวดสังคมศาสตร์</button>
     <button class="btn" value="กลุ่มวิชาวิทยาศาสตร์กับคณิตศาสตร์" name="E04"><i class="fas fa-atom"></i>หมวดวิทยาศาสตร์ฯ</button>
     <button class="btn" value="วิชาเลือกเสรี" name="E05"> <i class="fas fa-dove"></i>หมวดวิชาเลือกเสรี</button>
     <button class="btn" value="กลุ่มคุณค่าแห่งชีวิต" name="E06"><i class="fas fa-hand-holding-heart"></i>หมวดคุณค่าแห่งชีวิต</button>
     <button class="btn" value="กลุ่มวิถีแห่งสังคม" name="E07"><i class="fas fa-icons"></i>หมวดวิถีแห่งสังคม</button>
     <button class="btn" value="กลุ่มศาสตร์แห่งการคิด" name="E08"><i class="fas fa-brain"></i>ศาสตร์แห่งการคิด</button>
     <button class="btn" value="กลุ่มศิลปแห่งการจัดการ" name="E09"><i class="fas fa-chart-line"></i>ศิลปแห่งการจัดการ</button>
     <button class="btn" value="กลุ่มภาษาและการสื่อสาร" name="E10"><i class="fas fa-comments"></i>ภาษาและการสื่อสาร</button>
     <button class="btn btn_L" value="กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21" name="E11"><i class="fas fa-vr-cardboard"></i>หมวดทักษะที่จำเป็นในศตวรรษที่ 21</button>
     <button class="btn btn_L" value="กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ" name="E12"><i class="fas fa-user-tie"></i>ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</button>
     <button class="btn btn_L" value="กลุ่มทักษะด้านการจัดการและภาวะความเป็นผู้นำ" name="E13"><i class="fas fa-book-reader"></i>ทักษะด้านการจัดการและภาวะความเป็นผู้นำ</button>
     <button class="btn btn_L" value="กลุ่มทักษะด้านภาษาและการสื่อสาร" name="E14"><i class="fas fa-globe-americas"></i>หมวดทักษะด้านภาษาและการสื่อสาร</button>
     </form>
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
    if(isset($_POST["E01"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มวิชาภาษา'";
    }
    elseif(isset($_POST["E02"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มวิชามนุษย์ศาสตร์'";
    }
    elseif(isset($_POST["E03"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มวิชาสังคมศาสตร์'";
    }
    elseif(isset($_POST["E04"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มวิชาวิทยาศาสตร์กับคณิตศาสตร์'";
    }
    elseif(isset($_POST["E05"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'วิชาเลือกเสรี'";
    }
    elseif(isset($_POST["E06"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มคุณค่าแห่งชีวิต'";
    }
    elseif(isset($_POST["E07"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มวิถีแห่งสังคม'";
    }
    elseif(isset($_POST["E08"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มศาสตร์แห่งการคิด'";
    }
    elseif(isset($_POST["E09"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มศิลปแห่งการจัดการ'";
    }
    elseif(isset($_POST["E10"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มภาษาและการสื่อสาร'";
    }
    elseif(isset($_POST["E11"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21'";
    }
    elseif(isset($_POST["E12"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ'";
    }
    elseif(isset($_POST["E13"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มทักษะด้านการจัดการและภาวะความเป็นผู้นำ'";
    }
    elseif(isset($_POST["E14"])){
        $query = "SELECT * FROM post WHERE Group_subject = 'กลุ่มทักษะด้านภาษาและการสื่อสาร'";
    }
    else{
        $query = "SELECT * FROM post";
    }
    
    $result = mysqli_query($connect, $query);
    while($row =  mysqli_fetch_assoc($result)){
        $x = $row['ID_post'];
		$findCA = "SELECT COUNT(ID_comment) FROM comment WHERE from_post='$x'";
		$y = mysqli_query($connect, $findCA);
        $z = $row['create_by'];
        $queryU = "SELECT * FROM users WHERE ID = '$z'";
        $ua = mysqli_query($connect, $queryU);
        $rowUser = mysqli_fetch_assoc($ua);
        $name = (empty($rowUser['name'])) ? 'ไม่ระบุ' : $rowUser["name"];
        
		if($n =  mysqli_fetch_assoc($y)){
            echo '<a href="post.php?id='.$row['ID_post'].'" class="Content">';
            echo '    <div class="post_btn">';
            echo '        <div class="A_left">';
            echo '            <i class="icon_next fas fa-chevron-circle-right"></i>';
            echo '            <h4 class="textC" name="Post">'.$row['title_post'].'</h4>';
            echo '            <h6 class="textS" name="subject">'.$row['Group_subject'].' : '.$row['ID_subject'].'</h6>';
            echo '            <br><p class="Timestamp">User:'.$name.' Time:'.$row['time_post'].'</p>';
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
    </div>
</section>
<script>
function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
</script>
<script src="javascript/category.js"></script>
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>