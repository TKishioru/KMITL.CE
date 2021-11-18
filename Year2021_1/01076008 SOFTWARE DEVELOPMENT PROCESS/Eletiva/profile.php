<title>Eletiva | Profile</title>
<?php
require "dbconnect.php";
error_reporting(0);
include "inc_header.php";
include "header.php";
$email = $_SESSION["email"];
$ID = $_SESSION["ID"];
$query = "SELECT * FROM users WHERE email = '$email'";
$result = mysqli_query($connect, $query);
$row = mysqli_fetch_assoc($result);
$name = $row["name"];
$sex = $row["sex"];
$major = $row["major"];
$img = (empty($row['picture'])) ? 'avatar.jpg' : $row["picture"];
$introduce = $row["introduce"];

$query2 = "SELECT * FROM education WHERE major = '$major'";
$result2 = mysqli_query($connect, $query2);
$row2 = mysqli_fetch_assoc($result2);
$faculty = $row2["faculty"];

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

//echo "กลุ่มภาษา : $elective_eng1 <br>กลุ่มมนุษย์ศาสตร์ : $elective_hu <br>กลุ่มสังคมศาสตร์ : $elective_so1 <br>กลุ่มวิทยาศาสตร์ฯ : $elective_sci <br>กลุ่มวิชาเลือกเสรี : $elective_free <br>กลุ่มคุณค่าแห่งชีวิต : $elective_life <br>กลุ่มวิถีแห่งสังคม : $elective_so2 <br>";
//echo "ศาสตร์แห่งการคิด : $elective_think <br>ศิลปแห่งการจัดการ : $elective_manage <br>ภาษาและการสื่อสาร : $elective_eng2 <br>กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21 : $elective_21 <br>ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ : $elective_carrer <br>ทักษะด้านการจัดการและภาวะความเป็นผู้นำ : $elective_leader <br>กลุ่มทักษะด้านภาษาและการสื่อสาร : $elective_eng3 <br>";
      
//echo "emaill : $email <br>major : $major <br> introduce : $introduce <br>faculty : $faculty <br>img : $img <br> introduce : $name <br> sex : $sex";
?>
<style>
  .BO{
    border: 2px solid black;
  }
  .form-check-label{
    margin-top:7px;
  }
</style>
<body>
    <div class="">
        <div class="container py-4">
           <div class="card card-dark mb-4 rounded-0">
              <div class="card-header rounded-0">
                หน้าของฉัน
              </div>
              <div class="card-body">
                  <form action="controllerProfile.php" method="post" id="change_info" enctype="multipart/form-data">
                      <div class="row">
                        <div class="col-sm-3 text-center">
                            <div class="box-browse">
                                <img src="myfile/<?php echo $img; ?>" width="200" height="200"></center></td><br>
                                <label for="img">Select image:</label>
                                <input type="file" id="filUpload" name="filUpload"><br>
                                <input type="hidden" name="hdnOldFile" value="<?php echo $img; ?>">
                            </div>
                        </div>
                        <div class="col-sm-7">
                            <div class="row mb-3">
                                <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">ชื่อผู้ใช้</label>
                                <div class="col-sm-10">
                                  <p class="form-control-plaintext text-white"><?php echo $email ?></p>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">นามแฝง</label>
                                <div class="col-sm-10">
                                  <p class="form-control-plaintext text-white"><?php echo $name ?><button type="button" class="btn btn-link text-orange p-0" data-bs-toggle="modal" data-bs-target="#changeUserNameModal"><i class="fas fa-pen-square"></i></button></p>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">เพศ</label>
                                <div class="col-sm-10">
                                <select class="form-select" name="sex" placeholder="แนะนำตัว">
                                      <option value="<?php echo $sex ?>"><?php 
                                      if ($sex=='M'){
                                        $sex_value = "ผู้ชาย";
                                      } 
                                      else if ($sex=='F'){
                                        $sex_value = "ผู้หญิง";
                                      }
                                      else{
                                        $sex_value = "ไม่ระบุ";
                                      }
                                      echo  $sex_value;
                                      ?>
                                      </option>                                       
                                      <?php
                                      $sex_Resuut = array('','M','F');
                                      for($x = 0; $x < 3; $x++)
                                      {  
                                        if ($sex=='M'&&$sex_Resuut[$x]=='M'){
                                            continue;
                                        } 
                                        else if ($sex=='F'&&$sex_Resuut[$x]=='F'){
                                            continue;
                                        }
                                        else if ($sex==''&&$sex_Resuut[$x]==''){
                                            continue;
                                        }
                                        if ($sex_Resuut[$x]=='M'){
                                          $sex_value2 = "ผู้ชาย";
                                        }                                         
                                        else if ($sex_Resuut[$x]=='F'){
                                          $sex_value2 = "ผู้หญิง";
                                        }                                        
                                        else if ($sex_Resuut[$x]==''){
                                          $sex_value2 = "ไม่ระบุ";
                                        }
                                      ?>                                      
                                      <option value="<?php echo $sex_Resuut[$x]; ?>"><?php echo $sex_value2;?></option>
                                      <?php
                                      }
                                      ?> 
                                  </select>                                
                                </div>
                            </div>
                            
                            <div class="row mb-3">
                                <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">คณะ</label>
                                <div class="col-sm-10">
                                <input type="text" name="faculty" value="<?php if ($faculty == null){echo "ไม่ระบุ";}else {echo $faculty;}?>" class="form-control" readonly>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">ภาควิชา</label>
                                <div class="col-sm-10">
                                  <select class="form-select" name="major">
                                        <option value="<?php echo $major; ?>">
                                          <?php if ($major == null) 
                                          {
                                            echo "ไม่ระบุ";                                                      
                                          } 
                                          else {
                                            echo $major; 
                                          }?></option>
                                        <?php
                                        $major_SQL = "SELECT major FROM education";
                                        $major_Query = mysqli_query($connect,$major_SQL);
                                        while($major_Resuut = mysqli_fetch_assoc($major_Query))
                                        {
                                            if($major_Resuut["major"]==$major){
                                                continue;
                                            }
                                        ?>
                                        <option value="<?php echo $major_Resuut["major"]; ?>"><?php echo $major_Resuut["major"]; ?></option>
                                        <?php
                                        }
                                        ?>
                                    </select>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">แนะนำตัว</label>
                                <div class="col-sm-10">
                                    <textarea rows="3" class="form-control" id="inputEmail3" placeholder="แนะนำตัว" name="introduce" ><?php echo $introduce ?></textarea>
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label for="inputEmail3" class="col-sm-2 col-form-label">&nbsp;</label>
                                <div class="col-sm-10 text-center">
                                  <button class="btn btn-orange BO" name="change_info">บันทึกข้อมูล</button>
                                </div>
                            </div>
                        </div>  
                      </div>
                  </form>
              </div>
            </div>
            
            <div class="card card-dark mb-3 rounded-0">
              <div class="card-header rounded-0">
                หมวดหมู่ที่สนใจ
              </div>
              <div class="card-body">
                  <form action="controllerProfile.php" method="post" id="interest_info" enctype="multipart/form-data">
                      <div class="row">
                        <div class="col-sm-6">
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck1" name="elective_eng1" <?php if ($elective_eng1 == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck1">กลุ่มวิชาภาษา</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck2" name="elective_hu" <?php if ($elective_hu == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck2">กลุ่มวิชามนุษย์ศาสตร์</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck3" name="elective_so1" <?php if ($elective_so1 == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck3">กลุ่มวิชาสังคมศาสตร์</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck4" name="elective_sci" <?php if ($elective_sci == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck4">กลุ่มวิชาวิทยาศาสตร์กับคณิตศาสตร์</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck5" name="elective_free" <?php if ($elective_free == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck5">วิชาเลือกเสรี</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck6" name="elective_life" <?php if ($elective_life == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck6">กลุ่มคุณค่าแห่งชีวิต</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck7" name="elective_so2" <?php if ($elective_so2 == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck7">กลุ่มวิถีสังคม</label>
                            </div>
                        </div>  
                        <div class="col-sm-6">
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck8" name="elective_think" <?php if ($elective_think == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck8">กลุ่มศาสตร์แห่งการคิด</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck9" name="elective_manage" <?php if ($elective_manage == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck9">ศิลปแห่งการจัดการ</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck10" name="elective_eng2" <?php if ($elective_eng2 == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck10">กลุ่มภาษาและการสื่อสาร</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck11" name="elective_21" <?php if ($elective_21 == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck11">กลุ่มทักษะที่จำเป็นในศตวรรษที่21</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck12" name="elective_carrer" <?php if ($elective_carrer == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck12">กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck13" name="elective_leader" <?php if ($elective_leader == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck13">กลุ่มทักษะด้านการจัดการและภาวะความเป็นผู้นำ</label>
                            </div>
                            <div class="form-check mb-2">
                              <input class="form-check-input" type="checkbox" id="defaultCheck14" name="elective_eng3" <?php if ($elective_eng3 == "on") { echo "checked='checked'"; } ?>>
                              <label class="form-check-label" for="defaultCheck14">กลุ่มทักษะด้านภาษาและการสื่อสาร</label>
                            </div>
                        </div>
                        <div class="col-sm-12 text-center">
                            <hr>
                            <button type="submit" class="btn btn-orange BO" name="interest_info">บันทึกข้อมูล</button>  
                        </div>  
                      </div>
                  </form>
              </div>
            </div>
        </div>
    </div>
<!-- Modal -->
<div class="modal fade" id="changeUserNameModal" tabindex="-1" aria-labelledby="changeUserNameModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <form action="controllerProfile.php" method="post" id="change_name" enctype="multipart/form-data">  
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="changeUserNameModalLabel">เปลี่ยนชื่อนามแฝง</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row mb-3">
                <label for="inputEmail3" class="col-sm-2 col-form-label">นามแฝง</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" name="name" value="<?php echo $name ?>">
                </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">ยกเลิก</button>
            <button type="summit" class="btn btn-success" name="change_name">บันทึกการแก้ไข</button>
          </div>
        </div>
    </form>
  </div>
</div>    
</body>
<?php  
 
if($_GET['error']==1){
    echo '<script type="text/javascript">';
    echo ' alert("Change Complete!!"); ';  //not showing an alert box.
    echo '</script>';
}
else if ($_GET['error']==2){
    echo '<script type="text/javascript">';
    echo ' alert("Change Fail!!"); ';  //not showing an alert box.
    echo '</script>';
}

?>