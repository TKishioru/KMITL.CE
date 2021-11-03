<?php 

use PHPMailer\PHPMailer\PHPMailer;

session_start();
require "dbconnect.php";
$errors = array();
$email = '';

    //if user click register
    if (isset($_POST['reg_user'])) {
        // รับค่าที่ส่งมาจากฟอร์มลงในตัวแปร
        $email = mysqli_real_escape_string($connect, $_POST["email"]); 
        $password_1 = mysqli_real_escape_string($connect, $_POST['First_password']);
        $password_2 = mysqli_real_escape_string($connect, $_POST['confirm_password']);
        $status = mysqli_real_escape_string($connect, $_POST["status"]);

        if (empty($email)) {
            array_push($errors, "Email is required");
            $_SESSION['error'] = "Email is required";
        }
        if (empty($password_1)) {
            array_push($errors, "Password is required");
            $_SESSION['error'] = "Password is required";
        }
        if ($password_1 != $password_2) {
            array_push($errors, "The two passwords do not match");
            $_SESSION['error'] = "The two passwords do not match";
        }
        
        // บันทึกข้อมูล
        $user_check_query = "SELECT * FROM users WHERE email = '$email' LIMIT 1";
        $query = mysqli_query($connect, $user_check_query);
        $result = mysqli_fetch_assoc($query);
        //$interest = array('elective_eng1'=>0,'elective_hu'=>0,'elective_so1'=>0,'elective_sci'=>0,'elective_free'=>0,'elective_life'=>0,'elective_so2'=>0,'elective_think'=>0,'elective_manage'=>0,'elective_eng2'=>0,'elective_21'=>0,'elective_carrer'=>0,'elective_eng3'=>0);
        //{"elective_eng1":0,"elective_hu":0,"elective_so1":0,"elective_sci":0,"elective_free":0,"elective_life":0,"elective_so2":0,"elective_think":0,"elective_manage":0,"elective_eng2":0,"elective_21":0,"elective_carrer":0,"elective_eng3":0}

        if ($result) { // if user exists
            if ($result['email'] === $email) {
                array_push($errors, "email already exists");
            }
        }
        //var_dump($errors);

        if (count($errors) == 0) {
            $password = md5($password_1);

            $sql = "INSERT INTO users(email,password,status) VALUES('$email','$password','$status')";
            mysqli_query($connect,$sql); // สั่งรันคำสั่ง sql

            $_SESSION['email'] = $email;
            $_SESSION['success'] = "You are now logged in";
            $_SESSION['check'] = "first login";

            header('location: first-select.php');
        } else {
            header("location: login-user.php");
            //echo myqli_errors($connect);
        }
    }
    
    //if user click login
    if (isset($_POST['login_user'])) {
        $email = mysqli_real_escape_string($connect, $_POST['email']);
        $password = mysqli_real_escape_string($connect, $_POST['password']);

        if (empty($email)) {
            array_push($errors, "Email is required");
        }

        if (empty($password)) {
            array_push($errors, "Password is required");
        }

        if (count($errors) == 0) {
            $password = md5($password);

            $query = "SELECT * FROM users WHERE email = '$email' AND password = '$password' ";
            $result = mysqli_query($connect, $query);
            $row = mysqli_fetch_assoc($result);

            if (mysqli_num_rows($result) == 1) {
                $_SESSION['email'] = $email;
                $_SESSION['status'] = $row['status'];
                $_SESSION['success'] = "Your are now logged in";
                if($_SESSION['status'] == 2){
                    header("location: admin.php");
                }
                else{
                    header("location: index.php");
                }
            } else {
                array_push($errors, "Wrong Email or Password");
                $_SESSION['error'] = "Wrong Email or Password!";
                header("location: login-user.php");
            }
        } else {
            array_push($errors, "Email & Password is required");
            $_SESSION['error'] = "Email & Password is required";
            header("location: login-user.php");
        }
    }

    //if user click continue button in forgot password form
    if(isset($_POST['check-email'])){
        $email = mysqli_real_escape_string($connect, $_POST['email']);
        $check_email = "SELECT * FROM users WHERE email='$email'";
        $run_sql = mysqli_query($connect, $check_email);
        if(mysqli_num_rows($run_sql) > 0){
            $code = rand(999999, 111111);
            $insert_code = "UPDATE users SET code = $code WHERE email = '$email'";
            $run_query =  mysqli_query($connect, $insert_code);
            if($run_query){
               
                require_once "PHPMailer/PHPMailer.php";
                require_once "PHPMailer/SMTP.php";
                require_once "PHPMailer/Exception.php";
        
                $mail = new PHPMailer();
        
                // SMTP Settings
                $mail->isSMTP();
                $mail->Host = "smtp.gmail.com";
                $mail->SMTPAuth = true;
                $mail->Username = "eletiva.forgetp@gmail.com"; // enter your email address
                $mail->Password = "eletiva.00"; // enter your password
                $mail->Port = 465;
                $mail->SMTPSecure = "ssl";        
        
                //Email Settings
                $mail->isHTML(true);
                $mail->setFrom($email, "Member Eletiva");
                $mail->addAddress($email); // Send to mail
                $mail->Subject = "Eletiva | Reset Password";
                $mail->Body = "Reset Password : ".$code;
                //"Reset Password : http://127.0.0.1/eletiva/id=$email&id2=".$code

                if($mail->send()) {
                    $info = "We've sent a passwrod reset otp to your email - $email";
                    $_SESSION['info'] = $info;
                    $_SESSION['email'] = $email;
                    header('location: reset-code.php');
                    exit();
                    //$status = "success";
                    //$response = "Email is sent";
                } else {
                    $status = "failed";
                    $response = "Something is wrong" . $mail->ErrorInfo;
                }
                
                exit(json_encode(array("status" => $status, "response" => $response)));
            }
        }
    }

    //if user click check reset otp button
    if(isset($_POST['check-reset-otp'])){
        $_SESSION['info'] = "";
        $otp_code = mysqli_real_escape_string($connect, $_POST['otp']);
        $check_code = "SELECT * FROM users WHERE code = $otp_code";
        $code_res = mysqli_query($connect, $check_code);
        if(mysqli_num_rows($code_res) > 0){
            $fetch_data = mysqli_fetch_assoc($code_res);
            $email = $fetch_data['email'];
            $_SESSION['email'] = $email;
            $info = "Please create a new password that you don't use on any other site.";
            $_SESSION['info'] = $info;
            header('location: new-password.php');
            exit();
        }else{
            $errors['otp-error'] = "You've entered incorrect code!";
        }
    }

    //if user click change password button
    if(isset($_POST['change-password'])){
        $_SESSION['info'] = "";
        
        $password = mysqli_real_escape_string($connect, $_POST['password']);
        $cpassword = mysqli_real_escape_string($connect, $_POST['cpassword']);
        
        if($password !== $cpassword){
            $errors['password'] = "Confirm password not matched!";
        }else{
            $email = $_SESSION['email']; //getting this email using session
            //$encpass = password_hash($password, PASSWORD_BCRYPT);
            $encpass = md5($password);
            $update_pass = "UPDATE users SET code = NULL, password = '$encpass' WHERE email = '$email'";
            $run_query = mysqli_query($connect, $update_pass);
            if($run_query){
                $info = "Your password changed. Now you can login with your new password.";
                $_SESSION['info'] = $info;
                header('Location: password-changed.php');
            }else{
                $errors['db-error'] = "Failed to change your password!";
            }
        }
    }
    
   //if login now button click
    if(isset($_POST['login-now'])){
        header('Location: login-user.php');
    }
?>
