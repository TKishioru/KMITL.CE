<title>Eletiva | Post</title>
<link rel="stylesheet " type="text/css " href="css/post-reveiw.css ">
<link rel="stylesheet " type="text/css " href="css/bootstrap1.css ">
<!--<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">-->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
   
<?php
require "dbconnect.php";
error_reporting(0);
include "header.php";
if ($_GET['id']){
    //echo $_GET['id'];
    $x = $_GET['id'];
    $_SESSION['postnow']  = $_GET['id'];
    $queryP = "SELECT create_by FROM post WHERE ID_post = '$x'";
    $resultpost = mysqli_query($connect, $queryP);
    $rowpost = mysqli_fetch_assoc($resultpost);
    $IDpost = $rowpost["create_by"];

    $queryC = "SELECT * FROM comment WHERE from_post = '$x'";
    $resultcom = mysqli_query($connect, $queryC);    
    
    $queryU = "SELECT * FROM users WHERE ID = '$IDpost'";
    $resultU = mysqli_query($connect, $queryU);
    $rowUser = mysqli_fetch_assoc($resultU);
    $name = (empty($rowUser['name'])) ? 'ไม่ระบุ' : $rowUser["name"];
    $sex = $rowUser["sex"];
    $major = $rowUser["major"];
    $img = (empty($rowUser['picture'])) ? 'avatar.jpg' : $rowUser["picture"];
    $introduce = $rowUser["introduce"];
   
}
?>
<?php if((isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] != 3) || empty($_SESSION['status'])) : ?>
    <style>
        .badge{
            color:black;
        }
    </style>
<body class="post">
    <div class="container-fluid mt-5">
        <!-- หน้าโพสต์รีวิว -->
        <div class="row">
            <div class="col-lg-3 col-sm-2"></div>

            <div class="col-lg-5 col-sm-8">
                <div class="post-review">
                    <div class="review-box">

                        <i class="fas fa-ellipsis-h " id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false"></i>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <li> <a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#staticBackdrop">รายงานโพสต์</a></li>
                            <?php if ($_SESSION['ID']==$IDpost){
                            echo '<li><a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#modaldel">ลบโพสต์</a></li>';
                            }
                            ?>
                        </ul>
                        <?php 
                        $queryP = "SELECT * FROM post WHERE ID_post = '$x'";
                        $resultpost = mysqli_query($connect, $queryP);
                        while($row = mysqli_fetch_assoc($resultpost)){
                            $form_post = $row["ID_post"];
                            echo '<p class="title"><i class="fas fa-pen"></i>'.$row["title_post"].'
                            <br><span class="badge rounded-pill " id="code">'.$row["ID_subject"].'</span><span class="badge rounded-pill" id="category">'.$row["Group_subject"].'</span>
                            </p>';
                            echo '<p class="post-item">'.$row["msg_post"].'</p>';
                            echo '<div class="d-flex align-items-center ">';
                            echo '  <div class="d-inline ">';
                            echo '  <img src="myfile/'.$img.'" alt="Avatar" class="avatar">';
                            echo '</div>';
                            echo '<div class="d-inline col-sm-6">';
                            echo '  <strong>'.$name.'</strong>';
                            echo '  <span class="d-block" id="time">'.$row["time_post"].'></span>';
                            echo '</div>';
                            if(($_SESSION['status'] == 1) || ($_SESSION['status'] == 2)){
                            echo '<div class="d-grid col-lg-5 col-md-5 col-sm-4 float-end">';
                            echo '  <button type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">แสดงความคิดเห็น</button>';
                            echo '  <i class="fas fa-comment-dots" data-bs-toggle="modal" data-bs-target="#exampleModal"></i>';
                            echo '</div>';
                            }
                            echo '</div>';
                        }                        
                        ?>
                    </div>
                </div>
            </div>
            <div class=" col-lg-4 col-sm-2"></div>
        </div>

        <!-- โพสต์ comment โพสต์รีวิว -->
        <?php 
        while($row = mysqli_fetch_assoc($resultcom)){
            $IDuser = $row["create_by"];
            $IDcomment = $row["ID_comment"];
            $querycU = "SELECT * FROM users WHERE ID = '.$IDuser.'";
            $resultcU = mysqli_query($connect, $querycU);
            $rowcUser = mysqli_fetch_assoc($resultcU);
            $name = (empty($rowcUser['name'])) ? 'ไม่ระบุ' : $rowUser["name"];
            $sex = $rowcUser["sex"];
            $major = $rowcUser["major"];
            $img = (empty($rowcUser['picture'])) ? 'avatar.jpg' : $rowcUser["picture"];
            $introduce = $rowcUser["introduce"];
            echo '<div class="row ">';
            //echo '<div class="col-lg-4 col-sm-3"></div>'; //*
            echo '<div class="col-lg-3 col-sm-2"></div>';
            echo '<div class="col-lg-5 col-sm-8">'; //*
            //echo '<div class="col-lg-4 col-sm-7">';
            echo '<div class="comment-review">';
            echo '<div class="comment-box">';
            if ($_SESSION['ID']==$IDuser OR $_SESSION['ID']==$IDpost){
                echo '<i class="fas fa-ellipsis-h " id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false"></i>';
                echo '<ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">';
                echo '<li><a class="dropdown-item" href="controllerPostData.php?del_C_id='.$IDcomment.'">ลบโพสต์</a></li>';
                echo '</ul>';
            }
            echo'<div class="d-flex align-items-center ">';
            echo    '<div class="d-inline ">';
            echo        '<img src="myfile/'.$img.'" alt="Avatar" class="avatar">';
            echo    '</div>';
            echo    '<div class="d-inline ">';
            echo        '<strong>'.$name.'</strong>';
            echo        '<span class="d-block" id="time">'.$row["time_comment"].'</span>';
            echo    '</div>';
            echo'</div>';
            echo'<div class="d-block text-start ">';
            echo    '<p class="comment">'.$row["msg_comment"].'</p>';
            echo'</div>';
            echo '</div>';
            echo '<div class="col-lg-2 col-sm-2"></div>';
            echo '</div>';
            echo '</div>';
            echo '</div>';        
        }
        ?>
        <!--
        <div class="star-review ">
            <span class="heading">คะแนน</span>
            <span class="fa fa-star checked "></span>
            <span class="fa fa-star checked "></span>
            <span class="fa fa-star checked "></span>
            <span class="fa fa-star "></span>
            <span class="fa fa-star "></span>
        </div>
        -->
        <!-- modal box -->
        
            <!-- modal comment รีวิว -->
            <div class="modal fade " id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered ">
                    <div class="modal-content ">
                        
                  
                        <div class="modal-header ">
                            <h5 class="modal-title " id="exampleModalLabel">แสดงความคิดเห็น</h5>
                            <button type="button " class="btn-close btn-close-white " data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <form method="POST" action="controllerPostData.php" id="comment_post" enctype="multipart/form-data">
                            <div class="modal-body ">
                                <textarea class="form-control form-control-sm " id="comment-item" placeholder="แสดงความคิดเห็น" name='msg_comment' rows="5" required></textarea>
                                
                                <!--
                                <input type="text" style="display:none;" name="comment_post">                                
                                <div class="review-choose float-end ">
                                    <span class="heading">ให้คะแนน</span>
                                    <span class="fa fa-star "></span>
                                    <span class="fa fa-star "></span>
                                    <span class="fa fa-star "></span>
                                    <span class="fa fa-star "></span>
                                    <span class="fa fa-star "></span>
                                </div>
                                -->
                            </div>
                            <input type="hidden" name="post_id" value="<?php echo $form_post; ?>">    
                            <div class="modal-footer ">
                                <button type="submit" name="comment_post">ส่งความคิดเห็น</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
       
        <!-- modal รายงานโพสต์ -->
        <div class="modal fade " id="staticBackdrop" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class=" modal-dialog modal-dialog-centered ">
                <div class="modal-content">
                    <div class="modal-body ">
                        <p class="modal-title text-center mx-5 my-2 " id="staticBackdropLabel">เนื่องจากโพสต์ดังกล่าวมีการใช้ถ้อยคำที่ไม่สุภาพ และไม่ให้เกียรติซึ่งกันและกัน เพื่อรักษาบรรยากาศของเว็บไซต์ ข้าพเจ้าจึงขอให้มีการตรวจสอบโพสต์ดังกล่าว</p>
                        <p class="text-center">ต้องการรายงานโพสต์นี้ใช่หรือไม่</p>
                        <form method="POST" action="controllerPostData.php">
                        <div class="row">
                            <div class=" col-lg-3 col-sm-3"></div>
                            <div class=" col-lg-6 col-sm-6">
                                <a href="controllerPostData.php?report_P_id=<?php echo $x ?>"><button type="button" class="btn text-center float-start" id="yes" data-bs-toggle="modal" data-bs-target="#need" name="report_P">ต้องการ</button></a>
                                <button type="button" class="btn text-center float-end " id="no" data-bs-dismiss="modal">ไม่ต้องการ</button>
                            </div>
                            <div class=" col-lg-3 col-sm-3"></div>
                        </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>        
        <!-- modal P ลบ -->
        <div class="modal fade " id="modaldel" data-bs-keyboard="false" tabindex="-1" aria-labelledby="modaldel" aria-hidden="true">
            <div class=" modal-dialog modal-dialog-centered ">
                <div class="modal-content">
                    <div class="modal-body ">
                        <p class="text-center">ต้องการลบโพสต์นี้ใช่หรือไม่</p>
                        <div class="row">
                            <div class=" col-lg-3 col-sm-3"></div>
                            <div class=" col-lg-6 col-sm-6">
                                <a href="controllerPostData.php?del_P_id=<?php echo $x ?>"><button type="button" class="btn text-center float-start" id="yes" data-bs-toggle="modal" name="del_P">ต้องการ</button></a>
                                <button type="button" class="btn text-center float-end " id="no" data-bs-dismiss="modal">ไม่ต้องการ</button>
                            </div>
                            <div class=" col-lg-3 col-sm-3"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>                
        
    </div>
</body>
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>