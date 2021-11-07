<title>Eletiva | Admin Home</title>
<?php
require "dbconnect.php";

include "header.php";
?>


<body>
   
    <section class="main">
        <div class="post">
            <div class="postName">
                <i class="fas fa-pen"></i>
                <p>Post1โพส</p>
            </div>
            <div class="btnPost" style="margin-left: 47px;">
                <button>รหัสวิชา</button>
                <button>วิชาเลือกกลุ่ม....</button>
            </div>
            <div class="user">
                <img class="pic" src="images/login.png" alt="user profile">
                <div class="profile">
                    <a href="#">User:???</a>
                    <p>Time:???</p>
                </div>
            </div>
        </div>

        <div class="btn">
            <a href="#" class="cd-popup-notify" style="margin-left: 20px; margin-right: 20px;">แจ้งเตือนผู้ใช้</a>
            <a href="#" class="cd-popup-delete" style="margin-left: 20px; margin-right: 20px;">ลบโพสต์</a>

            <div class="cd-popup" role="alert">
                <div id="notifyConfirm" class="cd-popup-container hidden">
                    <p>ต้องการแจ้งเตือนผู้ใช้หรือไม่?</p>
                    <ul class="cd-buttons">
                        <li><a class="yes" href="#">ต้องการ</a></li>
                        <li><a href="#">ไม่ต้องการ</a></li>
                    </ul>
                    <a href="#" class="cd-popup-close img-replace">Close</a>
                </div>
                <div id="deleteConfirm" class="cd-popup-container hidden">
                    <p>ต้องการลบโพสต์หรือไม่?</p>
                    <ul class="cd-buttons">
                        <li><a class="yes" href="#">ต้องการ</a></li>
                        <li><a href="#">ไม่ต้องการ</a></li>
                    </ul>
                    <a href="#" class="cd-popup-close img-replace">Close</a>
                </div>
            </div>
        </div>

    </section>

   
</body> 
<script src="javascript/pop-up.js"></script>