<title>Eletiva | Admin Page</title>

<link rel="stylesheet" href="css/admin-post.css">
<link rel="stylesheet" href="css/pop-up.css">

<?php
require "dbconnect.php";

include "header.php";
?>
<?php if(isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] == 3 && $_GET['id']) : ?>
<body>
    <section class="main">
        <div class="post">
            <?php
                $_SESSION['postnow']  = $_GET['id'];
                $x = $_GET['id'];
                $query = "SELECT * FROM post WHERE ID_post = '$x'";
                $result = mysqli_query($connect, $query);
                while($row =  mysqli_fetch_assoc($result)){
                    echo '<div class="postName">';
                    echo '<i class="fas fa-pen"></i>';
                    echo '<p>'.$row['title_post'].'</p>';
                    echo '</div>';
                    echo '<div class="btnPost" style="margin-left: 47px;">';
                    echo '<button>'.$row['ID_subject'].'</button>';
                    echo '<button>'.$row['Group_subject'].'</button>';
                    echo '</div>';
                    echo '<div class="postDetail">';
                    echo '<p>'.$row['msg_post'].'</p>';
                    echo '</div>';
                    echo '<div class="user">';
                    echo '<img class="pic" src="images/login.png" alt="user profile">';
                    echo '<div class="profile">';
                    echo '<a href="#">User:'.$row['create_by'].'</a>';
                    echo '<p>Time:'.$row['time_post'].'</p>';
                    echo '</div>';
                    echo '</div>';
                    echo '</div>';   
                }
            ?>
        </div>
        <form action="controllerPostData.php" method="POST">
         <div class="btn">
            <p class="cd-popup-notify" style="margin-left: 20px; margin-right: 20px;">แจ้งเตือนผู้ใช้</p>
            <p class="cd-popup-delete" style="margin-left: 20px; margin-right: 20px;">ลบโพสต์</p>
            <div class="cd-popup" role="alert">
                <div id="notifyConfirm" class="cd-popup-container hidden">
                    <p>ต้องการแจ้งเตือนผู้ใช้หรือไม่?</p>
                    <ul class="cd-buttons">
                        <li><a href="controllerPostData.php?notify_id=<?php echo $x?>" class="yes" ><button type="button" class="btnlink" name="yesnotify">ต้องการ</button></a></li>
                        <li><a id="notnotify">ไม่ต้องการ</a></li>
                    </ul>
                    <a class="cd-popup-close img-replace">Close</a>
                </div>
                <div id="deleteConfirm" class="cd-popup-container hidden">
                    <p>ต้องการลบโพสต์หรือไม่?</p>
                    <ul class="cd-buttons">
                        <li><a href="controllerPostData.php?del_P_id=<?php echo $x?>" class="yes" ><button type="button" class="btnlink" name="del_P_id">ต้องการ</button></a></li>
                        <li><a id="notdel">ไม่ต้องการ</a></li>
                    </ul>
                    <a class="cd-popup-close img-replace">Close</a>
                </div>
            </div>
        </div>
        </form>
    </section>
</body> 
<script src="javascript/pop-up.js"></script>
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>