<?php
session_start();
require "dbconnect.php";
error_reporting(0);
$errors = array();
$ID = $_SESSION['ID'];


if(isset($_POST['interest_info']) OR isset($_POST['select_finish'])){   
    $elective_eng1 = $_POST['elective_eng1'];    
    $elective_hu = $_POST['elective_hu'];    
    $elective_so1 = $_POST['elective_so1'];    
    $elective_sci = $_POST['elective_sci'];    
    $elective_free = $_POST['elective_free'];    
    $elective_life = $_POST['elective_life'];    
    $elective_so2 = $_POST['elective_so2'];    
    $elective_think = $_POST['elective_think'];    
    $elective_manage = $_POST['elective_manage'];    
    $elective_eng2 = $_POST['elective_eng2'];
    $elective_21 = $_POST['elective_21'];    
    $elective_carrer = $_POST['elective_carrer'];  
    $elective_leader = $_POST['elective_leader'];    
    $elective_eng3 = $_POST['elective_eng3'];  

    //echo "กลุ่มภาษา : $elective_eng1 <br>กลุ่มมนุษย์ศาสตร์ : $elective_hu <br>กลุ่มสังคมศาสตร์ : $elective_so1 <br>กลุ่มวิทยาศาสตร์ฯ : $elective_sci <br>กลุ่มวิชาเลือกเสรี : $elective_free <br>กลุ่มคุณค่าแห่งชีวิต : $elective_life <br>กลุ่มวิถีแห่งสังคม : $elective_so2 <br>";
    //echo "ศาสตร์แห่งการคิด : $elective_think <br>ศิลปแห่งการจัดการ : $elective_manage <br>ภาษาและการสื่อสาร : $elective_eng2 <br>กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21 : $elective_21 <br>ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ : $elective_carrer <br>ทักษะด้านการจัดการและภาวะความเป็นผู้นำ : $elective_leader <br>กลุ่มทักษะด้านภาษาและการสื่อสาร : $elective_eng3 <br>";
        
        if($elective_eng1=="on"){      
            $elective_eng1 = 0;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_eng1 and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_eng1','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        } 
        if($elective_eng1==""){
            $elective_eng1 = 0;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_eng1 and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_hu=="on"){      
            $elective_hu = 1;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_hu and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_hu','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        } 
        if($elective_hu==""){
            $elective_hu = 1;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_hu and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_so1=="on"){      
            $elective_so1 = 2;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_so1 and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_so1','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }
        if($elective_so1==""){
            $elective_so1 = 2;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_so1 and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_sci=="on"){      
            $elective_sci = 3;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_sci and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_sci','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_sci==""){
            $elective_sci = 3;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_sci and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_free=="on"){      
            $elective_free = 4;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_free and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_free','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_free==""){
            $elective_free = 4;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_free and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_life=="on"){      
            $elective_life = 5;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_life and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_life','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_life==""){
            $elective_life = 5;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_life and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_so2=="on"){      
            $elective_so2 = 6;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_so2 and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_so2','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        } 
        if($elective_so2==""){
            $elective_so2 = 6;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_so2 and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_think=="on"){      
            $elective_think = 7;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_think and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_think','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_think==""){
            $elective_think = 7;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_think and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_manage=="on"){      
            $elective_manage = 8;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_manage and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_manage','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        } 
        if($elective_manage==""){
            $elective_manage = 8;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_manage and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_eng2=="on"){      
            $elective_eng2 = 9;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_eng2 and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_eng2','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_eng2==""){
            $elective_eng2 = 9;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_eng2 and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_21=="on"){      
            $elective_21 = 10;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_21 and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_21','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_21==""){
            $elective_21 = 10;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_21 and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_carrer=="on"){      
            $elective_carrer = 11;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_carrer and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_carrer','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_carrer==""){
            $elective_carrer = 11;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_carrer and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_leader=="on"){      
            $elective_leader = 12;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_leader and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_leader','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_leader==""){
            $elective_leader = 12;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_leader and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }

        if($elective_eng3=="on"){      
            $elective_eng3 = 13;      
            $query_check_select_finish = "SELECT ID FROM interest WHERE Group_subject=$elective_eng3 and ID=$ID";
            $run_query_check_select_finish = mysqli_query($connect, $query_check_select_finish);
            $row_query_check_select_finish = mysqli_fetch_assoc($run_query_check_select_finish);            
            if(mysqli_num_rows($run_query_check_select_finish) == 0){
                $query_select_finish = "INSERT INTO interest (Group_subject,ID) VALUES('$elective_eng3','$ID')";
                $run_query_select_finish = mysqli_query($connect, $query_select_finish);
            }  
        }  
        if($elective_eng3==""){
            $elective_eng3 = 13;
            $query_delete_finish = "DELETE FROM interest WHERE Group_subject=$elective_eng3 and ID=$ID";
            $run_query_delete_finish = mysqli_query($connect, $query_delete_finish);
        }
 
    if(isset($_POST['select_finish'])){       
        if(count($errors) == 0){ 
            header('location: index.php');
        }
        else{
            echo"ERROR";
        }
    }
    if(isset($_POST['interest_info'])){  
        if(count($errors) == 0){         
            header('location: profile.php?error=1');
        }
        else{
            header('location: profile.php?error=2');
        }
    }
}

if (isset($_POST['change_info'])) {

    $sex = mysqli_real_escape_string($connect, $_POST['sex']);    
    $major = mysqli_real_escape_string($connect, $_POST['major']);
    $introduce = mysqli_real_escape_string($connect, $_POST['introduce']);
      
    $email = $_SESSION["email"];

    //echo "emaill : $email <br>major : $major <br> introduce : $introduce <br> sex : $sex <br>";
    
    $query = "UPDATE users SET ";  
    if ($major == null) {
        $query .= "major = NULL,";
    } 
    else {
        $query .= "major = '$major',";
    }
    if ($introduce == null) {
        $query .= "introduce = NULL,";
    } 
    else {
        $query .= "introduce = '$introduce',";
    }    
    if ($sex == null) {
        $query .= "sex = NULL";
    } 
    else {
        $query .= "sex = '$sex'";
    } 
    $query .= " WHERE email = '$email'";

    //echo "query : $query";

    $result = mysqli_query($connect, $query);

    if ($_FILES["filUpload"]["name"] != "") {
        if (move_uploaded_file($_FILES["filUpload"]["tmp_name"], "myfile/" . $email . "_" . $_FILES["filUpload"]["name"])) {

            //*** Delete Old File ***//
            if ($_POST["hdnOldFile"] != 'avatar.jpg') {
                @unlink("myfile/" . $_POST["hdnOldFile"]);
            }

            //*** Update New File ***//
            $strSQL = "UPDATE users SET picture = '" . $email . "_" . $_FILES["filUpload"]["name"] . "' WHERE email = '$email'";
            $objQuery = mysqli_query($connect, $strSQL);
        }
    }
    if(count($errors) == 0){         
        header('location: profile.php?error=1');
    }
    else{
        header('location: profile.php?error=2');
    }

}

if (isset($_POST['change_name'])) {

    $name= mysqli_real_escape_string($connect, $_POST['name']);  
      
    $email = $_SESSION["email"];

    //echo "emaill : $email <br>major : $major <br> introduce : $introduce <br> sex : $sex <br>";
    
    $query = "UPDATE users SET name = '$name' WHERE email ='$email'"; 

    //echo "query : $query";

    mysqli_query($connect, $query);
    
    if(count($errors) == 0){         
        header('location: profile.php?error=1');
    }
    else{
        header('location: profile.php?error=2');
    }

}
?>