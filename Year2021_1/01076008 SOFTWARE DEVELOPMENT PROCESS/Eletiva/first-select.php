<?php
session_start();
error_reporting(0);
require "dbconnect.php";
$ID = $_SESSION["ID"];
$query3 = "SELECT Group_subject FROM interest WHERE ID = '$ID'";
$result3 = mysqli_query($connect, $query3);
while($row3_Resuut = mysqli_fetch_assoc($result3))
{
  if($row3_Resuut["Group_subject"]==0){
    $elective_eng1 = "on";    
  }
  if($row3_Resuut["Group_subject"]==1){
    $elective_hu = "on";    
  }
  if($row3_Resuut["Group_subject"]==2){  
    $elective_so1 = "on";   
  }
  if($row3_Resuut["Group_subject"]==3){  
    $elective_sci = "on";    
  }
  if($row3_Resuut["Group_subject"]==4){ 
    $elective_free = "on";     
  }
  if($row3_Resuut["Group_subject"]==5){
    $elective_life = "on";    
  }
  if($row3_Resuut["Group_subject"]==6){ 
    $elective_so2 = "on";   
  }
  if($row3_Resuut["Group_subject"]==7){  
    $elective_think = "on";   
  }
  if($row3_Resuut["Group_subject"]==8){ 
    $elective_manage = "on";    
  }
  if($row3_Resuut["Group_subject"]==9){ 
    $elective_eng2 = "on";  
  }
  if($row3_Resuut["Group_subject"]==10){
    $elective_21 = "on";    
  }
  if($row3_Resuut["Group_subject"]==11){  
    $elective_carrer = "on";    
  }
  if($row3_Resuut["Group_subject"]==12){
    $elective_leader = "on";    
  }
  if($row3_Resuut["Group_subject"]==13){ 
    $elective_eng3 = "on";    
  }                        
}
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
            <h2>เลือกกลุ่มวิชาเลือกที่คุณสนใจ</h2>
            <p class="skip"><a href="index.php">ข้าม>></a></p>
            <form action="controllerProfile.php" method="post">
            <ul>
                <li>
                    <input type="checkbox" class="selectS" id="myCheckbox1" name="elective_eng1" <?php if ($elective_eng1 == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox1">
                        <i class="fas fa-language"></i>
                        <p class="sub">กลุ่มภาษา</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox2" name="elective_hu" <?php if ($elective_hu == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox2">
                        <i class="fas fa-users"></i>
                        <p class="sub">กลุ่มมนุษย์ศาสตร์</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox3" name="elective_so1" <?php if ($elective_so1 == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox3">
                        <i class="fas fa-globe"></i>
                        <p class="sub">กลุ่มสังคมศาสตร์</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox4" name="elective_sci" <?php if ($elective_sci == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox4">
                        <i class="fas fa-atom"></i>
                        <p class="sub">กลุ่มวิทยาศาสตร์ฯ</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox5" name="elective_free" <?php if ($elective_free == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox5">
                        <i class="fas fa-dove"></i>
                        <p class="sub">กลุ่มวิชาเลือกเสรี</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox6" name="elective_life" <?php if ($elective_life == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox6">
                        <i class="fas fa-hand-holding-heart"></i>
                        <p class="sub">กลุ่มคุณค่าแห่งชีวิต</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox7" name="elective_so2" <?php if ($elective_so2 == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox7">
                        <i class="fas fa-icons"></i>
                        <p class="sub">กลุ่มวิถีแห่งสังคม</p>
                    </label>                   
                    <input type="checkbox" class="selectS" id="myCheckbox8" name="elective_think" <?php if ($elective_think == "on") { echo "checked='checked'"; } ?>> 
                    <label for="myCheckbox8">
                        <i class="fas fa-brain"></i>
                        <p class="sub">ศาสตร์แห่งการคิด</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox9" name="elective_manage" <?php if ($elective_manage == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox9">
                        <i class="fas fa-chart-line"></i>
                        <p class="sub">ศิลปแห่งการจัดการ</p>
                    </label> 
                    <input type="checkbox" class="selectS" id="myCheckbox10" name="elective_eng2" <?php if ($elective_eng2 == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox10">
                        <i class="fas fa-comments"></i>
                        <p class="sub">ภาษาและการสื่อสาร</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox11" name="elective_21" <?php if ($elective_21 == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox11">
                        <i class="fas fa-vr-cardboard"></i>
                        <p class="sub">กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox12" name="elective_carrer" <?php if ($elective_carrer == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox12">
                        <i class="fas fa-user-tie"></i>
                        <p class="sub">ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox13" name="elective_leader" <?php if ($elective_leader == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox13">
                        <i class="fas fa-book-reader"></i>
                        <p class="sub">ทักษะด้านการจัดการและภาวะความเป็นผู้นำ</p>
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox14" name="elective_eng3" <?php if ($elective_eng3 == "on") { echo "checked='checked'"; } ?>>
                    <label for="myCheckbox14">
                        <i class="fas fa-globe-americas"></i>
                        <p class="sub">กลุ่มทักษะด้านภาษาและการสื่อสาร</p>
                    </label>
                </li>
            </ul>
            <!--<p class="finish"><a href="index.php" name="select_finish">เสร็จสิ้น</a></p>-->
            <input type="submit" class="finish" name="select_finish" value="เสร็จสิ้น">
</form>
        </div>
    </section>
  </body>
  