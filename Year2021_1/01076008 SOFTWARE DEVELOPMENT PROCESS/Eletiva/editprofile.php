<?php
session_start();
require "dbconnect.php";
$errors = array();
if(isset($_POST['select_finish'])){
    $E[0] = (empty($_POST['elective_eng1'])) ? 0 : 1;
    $E[1] = (empty($_POST['elective_hu'])) ? 0 : 1;
    $E[2] = (empty($_POST['elective_so1'])) ? 0 : 1;
    $E[3] = (empty($_POST['elective_sci'])) ? 0 : 1;
    $E[4] = (empty($_POST['elective_free'])) ? 0 : 1;
    $E[5] = (empty($_POST['elective_life'])) ? 0 : 1;
    $E[6] = (empty($_POST['elective_so2'])) ? 0 : 1;
    $E[7] = (empty($_POST['elective_think'])) ? 0 : 1;
    $E[8] = (empty($_POST['elective_manage'])) ? 0 : 1;
    $E[9] = (empty($_POST['elective_eng2'])) ? 0 : 1;
    $E[10] = (empty($_POST['elective_21'])) ? 0 : 1;
    $E[11] = (empty($_POST['elective_carrer'])) ? 0 : 1;
    $E[12] = (empty($_POST['elective_leader'])) ? 0 : 1;
    $E[13] = (empty($_POST['elective_eng3'])) ? 0 : 1;
    
    $interest = "{\"elective_eng1\":\"$E[0]\",\"elective_hu\":\"$E[1]\",\"elective_so1\":\"$E[2]\",\"elective_sci\":\"$E[3]\",\"elective_free\":\"$E[4]\",\"elective_life\":\"$E[5]\",\"elective_so2\":\"$E[6]\",\"elective_think\":\"$E[7]\",\"elective_manage\":\"$E[8]\",\"elective_eng2\":\"$E[9]\",\"elective_21\":\"$E[10]\",\"elective_carrer\":\"$E[11]\",\"elective_leader\":\"$E[12]\",\"elective_eng3\":\"$E[13]\"}";
   
    $query = "UPDATE users SET interest = '$interest'";
    $run_query = mysqli_query($connect, $query);

    if(count($errors) == 0){         
        //echo " $interest ";
        header('location: index.php');
    }
    else{
        echo"ERROR";
    }
}
if (isset($_POST['change_info'])) {

    $name = mysqli_real_escape_string($connect, $_POST['name']);
    $faculty = mysqli_real_escape_string($connect, $_POST['faculty']);
    $major = mysqli_real_escape_string($connect, $_POST['major']);
    $introduce = mysqli_real_escape_string($connect, $_POST['introduce']);

    $E[0] = (empty($_POST['elective_eng1'])) ? 0 : 1;
    $E[1] = (empty($_POST['elective_hu'])) ? 0 : 1;
    $E[2] = (empty($_POST['elective_so1'])) ? 0 : 1;
    $E[3] = (empty($_POST['elective_sci'])) ? 0 : 1;
    $E[4] = (empty($_POST['elective_free'])) ? 0 : 1;
    $E[5] = (empty($_POST['elective_life'])) ? 0 : 1;
    $E[6] = (empty($_POST['elective_so2'])) ? 0 : 1;
    $E[7] = (empty($_POST['elective_think'])) ? 0 : 1;
    $E[8] = (empty($_POST['elective_manage'])) ? 0 : 1;
    $E[9] = (empty($_POST['elective_eng2'])) ? 0 : 1;
    $E[10] = (empty($_POST['elective_21'])) ? 0 : 1;
    $E[11] = (empty($_POST['elective_carrer'])) ? 0 : 1;
    $E[12] = (empty($_POST['elective_leader'])) ? 0 : 1;
    $E[13] = (empty($_POST['elective_eng3'])) ? 0 : 1;
    
    $interest = "{\"elective_eng1\":\"$E[0]\",\"elective_hu\":\"$E[1]\",\"elective_so1\":\"$E[2]\",\"elective_sci\":\"$E[3]\",\"elective_free\":\"$E[4]\",\"elective_life\":\"$E[5]\",\"elective_so2\":\"$E[6]\",\"elective_think\":\"$E[7]\",\"elective_manage\":\"$E[8]\",\"elective_eng2\":\"$E[9]\",\"elective_21\":\"$E[10]\",\"elective_carrer\":\"$E[11]\",\"elective_leader\":\"$E[12]\",\"elective_eng3\":\"$E[13]\"}";
    $email = $_SESSION["email"];

    //echo "emaill : $email <br>name : $name <br>faculty : $faculty <br>major : $major <br> introduce : $introduce <br> interest : $interest";
    
    $query = "UPDATE users ";
    if ($name == null) {
        $query .= "SET name = NULL,";
    } 
    else {
        $query .= "SET name = '$name',";
    }
    if ($faculty == null) {
        $query .= "faculty = NULL,";
    } 
    else {
        $query .= "faculty = '$faculty',";
    }
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
        $query .= "introduce='$introduce',";
    }
    if ($interest == null) {
        $query .= "interest = NULL,";
    } 
    else {
        $query .= "interest='$interest'";
    }

    $query .= "WHERE email = '$email'";

    $result = mysqli_query($connect, $query);

    if ($_FILES["filUpload"]["name"] != "") {
        if (move_uploaded_file($_FILES["filUpload"]["tmp_name"], "myfile/" . $email . "_" . $_FILES["filUpload"]["name"])) {

            //*** Delete Old File ***//
            if ($_POST["hdnOldFile"] != 'test.jpg') {
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
?>