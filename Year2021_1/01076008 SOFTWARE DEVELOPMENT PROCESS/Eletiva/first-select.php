<?php
session_start();
/*
if(!isset($_SESSION["email"])){
  $_SESSION['msg'] = "You must log in first";
  header('location: login-user.php');
}

if(isset($_GET["logout"])){
    session_destroy();
    unset($_SESSION["email"]);
    unset($_SESSION["status"]);
    header('location: login-user.php');
  }
*/
?>
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eletiva | Choose Your Subject of Interest</title>
    <link rel="stylesheet" type="text/css" href="css/first-select.css"> 
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet"> 

    <link rel="icon" href="images/icon.jpg" type="image/x-icon">
    <link rel="apple-touch-icon" href="images/icon.jpg" />
  </head>

  <body>
    <section>
        <div class="container">
            <h2>เลือกหมวดหมู่วิชาเลือกที่คุณสนใจ</h2>
            <p class="skip"><a href="index.php">ข้าม>></a></p>
            <form action="editprofile.php" method="post">
            <ul>
                <li>
                    <input type="checkbox" class="selectS" id="myCheckbox1" name="elective_eng1">
                    <label for="myCheckbox1">
                        <i class="fas fa-language"></i>
                        <p class="sub">หมวดภาษา</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox2" name="elective_hu">
                    <label for="myCheckbox2">
                        <i class="fas fa-users"></i>
                        <p class="sub">หมวดมนุษย์ศาสตร์</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox3" name="elective_so1">
                    <label for="myCheckbox3">
                        <i class="fas fa-globe"></i>
                        <p class="sub">หมวดสังคมศาสตร์</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox4" name="elective_sci">
                    <label for="myCheckbox4">
                        <i class="fas fa-atom"></i>
                        <p class="sub">หมวดวิทยาศาสตร์ฯ</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox5" name="elective_free">
                    <label for="myCheckbox5">
                        <i class="fas fa-dove"></i>
                        <p class="sub">หมวดวิชาเลือกเสรี</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox6" name="elective_life">
                    <label for="myCheckbox6">
                        <i class="fas fa-hand-holding-heart"></i>
                        <p class="sub">หมวดคุณค่าแห่งชีวิต</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox7" name="elective_so2">
                    <label for="myCheckbox7">
                        <i class="fas fa-icons"></i>
                        <p class="sub">หมวดวิถีแห่งสังคม</p>
                    </label>                   
                    <input type="checkbox" class="selectS" id="myCheckbox8" name="elective_think">
                    <label for="myCheckbox8">
                        <i class="fas fa-brain"></i>
                        <p class="sub">ศาสตร์แห่งการคิด</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox9" name="elective_manage">
                    <label for="myCheckbox9">
                        <i class="fas fa-chart-line"></i>
                        <p class="sub">ศิลปแห่งการจัดการ</p>
                    </label> 
                    <input type="checkbox" class="selectS" id="myCheckbox10" name=""elective_eng2>
                    <label for="myCheckbox10">
                        <i class="fas fa-comments"></i>
                        <p class="sub">ภาษาและการสื่อสาร</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox11" name="elective_21">
                    <label for="myCheckbox11">
                        <i class="fas fa-vr-cardboard"></i>
                        <p class="sub">หมวดทักษะที่จำเป็นในศตวรรษที่ 21</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox12" name="elective_carrer">
                    <label for="myCheckbox12">
                        <i class="fas fa-user-tie"></i>
                        <p class="sub">ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox13" name="elective_leader">
                    <label for="myCheckbox13">
                        <i class="fas fa-book-reader"></i>
                        <p class="sub">ทักษะด้านการจัดการและภาวะความเป็นผู้นำ</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox14" name="elective_eng3">
                    <label for="myCheckbox14">
                        <i class="fas fa-globe-americas"></i>
                        <p class="sub">หมวดทักษะด้านภาษาและการสื่อสาร</p>
                    </label>
                </li>
            </ul>
            <!--<p class="finish"><a href="index.php" name="select_finish">เสร็จสิ้น</a></p>-->
            <input type="submit" class="finish" name="select_finish" value="เสร็จสิ้น">
</form>
        </div>
    </section>
  </body>
  