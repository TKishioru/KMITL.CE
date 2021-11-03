<?php
session_start();

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

if(!isset($_SESSION['check'])){
    header('location: index.php');
}
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
            <ul>
                <li>
                    <input type="checkbox" id="myCheckbox1" />
                    <label for="myCheckbox1">
                        <i class="fas fa-language"></i>
                        <p class="sub">หมวดภาษา</p>
                    </label>
                    <input type="checkbox" id="myCheckbox2" />
                    <label for="myCheckbox2">
                        <i class="fas fa-users"></i>
                        <p class="sub">หมวดมนุษย์ศาสตร์</p>
                    </label>
                    <input type="checkbox" id="myCheckbox3" />
                    <label for="myCheckbox3">
                        <i class="fas fa-globe"></i>
                        <p class="sub">หมวดสังคมศาสตร์</p>
                    </label>
                    <input type="checkbox" id="myCheckbox7" />
                    <label for="myCheckbox7">
                        <i class="fas fa-atom"></i>
                        <p class="sub">หมวดวิทยาศาสตร์ฯ</p>
                    </label>
                    <input type="checkbox" id="myCheckbox4" />
                    <label for="myCheckbox4">
                        <i class="fas fa-dove"></i>
                        <p class="sub">หมวดวิชาเลือกเสรี</p>
                    </label>
                    <input type="checkbox" id="myCheckbox5" />
                    <label for="myCheckbox5">
                        <i class="fas fa-hand-holding-heart"></i>
                        <p class="sub">หมวดคุณค่าแห่งชีวิต</p>
                    </label>
                    <input type="checkbox" id="myCheckbox6" />
                    <label for="myCheckbox6">
                        <i class="fas fa-icons"></i>
                        <p class="sub">หมวดวิถีแห่งสังคม</p>
                    </label>                   
                    <input type="checkbox" id="myCheckbox8" />
                    <label for="myCheckbox8">
                        <i class="fas fa-brain"></i>
                        <p class="sub">ศาสตร์แห่งการคิด</p>
                    </label>
                    <input type="checkbox" id="myCheckbox9" />
                    <label for="myCheckbox9">
                        <i class="fas fa-comments"></i>
                        <p class="sub">ภาษาและการสื่อสาร</p>
                    </label>
                    <input type="checkbox" id="myCheckbox10" />
                    <label for="myCheckbox10">
                        <i class="fas fa-chart-line"></i>
                        <p class="sub">ศิลปแห่งการจัดการ</p>
                    </label> 
                    <input type="checkbox" id="myCheckbox11" />
                    <label for="myCheckbox11">
                        <i class="fas fa-vr-cardboard"></i>
                        <p class="sub">หมวดทักษะที่จำเป็นในศตวรรษที่ 21</p>
                    </label>
                    <input type="checkbox" id="myCheckbox12" />
                    <label for="myCheckbox12">
                        <i class="fas fa-user-tie"></i>
                        <p class="sub">ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</p>
                    </label>
                    <input type="checkbox" id="myCheckbox13" />
                    <label for="myCheckbox13">
                        <i class="fas fa-book-reader"></i>
                        <p class="sub">ทักษะด้านการจัดการและภาวะความเป็นผู้นำ</p>
                    </label>
                    <input type="checkbox" id="myCheckbox14" />
                    <label for="myCheckbox14">
                        <i class="fas fa-globe-americas"></i>
                        <p class="sub">หมวดทักษะด้านภาษาและการสื่อสาร</p>
                    </label>
                </li>
            </ul>
            <p class="finish"><a href="index.php">เสร็จสิ้น</a></p>
        </div>
    </section>
  </body>
  