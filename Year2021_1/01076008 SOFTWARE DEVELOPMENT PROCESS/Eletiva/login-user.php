<?php
  require('dbconnect.php');
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eletiva | Login & Regieter</title>
  <link rel="stylesheet" type="text/css" href="css/login-user.css"> 

  <!-- add icon link -->
  <link rel="icon" href="images/icon.jpg" type="image/x-icon">
  <!-- specifying a webpage icon for web clip -->
  <link rel="apple-touch-icon" href="images/icon.jpg" />
  </head>

  <body>
    <section>
      <div class="container">
        <!-- login -->
        <div class="user signinBx">
          <div class="imgBx"><img src="images/4.jpg"></div>
          <div class="formBx">
            <form action="controllerUserData.php" method="post" autocomplete="">
              <h2>เข้าสู่ระบบ</h2>
              <input class="form-control" type="text" placeholder="อีเมล" name="email">
              <input class="form-control" type="password" placeholder="รหัสผ่าน" name="password">
              <a class="forget" href="forgot-password.php">Forget Password?<br></a>
              <input type="submit" name="login_user" value="เข้าสู่ระบบ" >
              <p class="singup" align ='center'>ยังไม่ได้เป็นสมาชิก? <a href="#" onclick="toggleForm();">คลิกเพื่อสมัคร</a></p>
            </form>
          </div>
        </div>

        <!-- regieter -->
        <div class="user singupBx">
          <div class="formBx">
            <form action="controllerUserData.php" method="post" name="R_form" autocomplete="">
              <h2>ลงทะเบียน</h2>
              <?php include('errors.php'); ?>
              <?php if (isset($_SESSION['error'])) : ?>
                <div class="error">
                  <h3>
                      <?php 
                        echo $_SESSION['error'];
                        unset($_SESSION['error']);
                      ?>
                  </h3>
                </div>
               <?php endif ?>
              <input class="form-control" type="email" placeholder="อีเมล" name="email">
              <input class="form-control" type="password" placeholder="รหัสผ่าน" name="First_password" id="First_password" onChange="onChange()" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
              <input class="form-control" type="password" placeholder="ยืนยันรหัสผ่าน" name="confirm_password" id="confirm_password" onChange="onChange()">
              
              <!-- pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required -->
              <p class="I_status">สถานะ</p>
              <label class="container">
                <div class="student">นักเรียน
                  <input type="radio" checked="checked" value="0" name="status">
                  <span class="checkmark"></span>
                </div>
              </label>
              <label class="container">
                <div class="teacher">อาจารย์
                  <input type="radio" value="1" name="status">
                  <span class="checkmark"></span>
                </div>
              </label>


              <input type="submit" name="reg_user" value="ลงทะเบียน">
              <p class="singup" align ='center'>เป็นสมาชิกแล้ว? <a href="#" onclick="toggleForm();">คลิกเพื่อเข้าสู่ระบบ</a></p>
            </form>
          </div>
          <div class="imgBx"><img src=images/3.jpg></div>
        </div>
      </div>
    </section>

    <script>
      function toggleForm(){
        section = document.querySelector('section');
        container = document.querySelector('.container');
        container.classList.toggle('active');
        section.classList.toggle('active');
      }
      function onChange() {
  const password = document.querySelector('input[name=First_password]');
  const confirm = document.querySelector('input[name=confirm_password]');
  
  if (confirm.value === password.value) {
    confirm.setCustomValidity('');
  } else {
    confirm.setCustomValidity('Passwords do not match');
  }
}
    </script>
    <script type="text/javascript" src="javascript/Jquery.js"></script>
  </body>
</html>
