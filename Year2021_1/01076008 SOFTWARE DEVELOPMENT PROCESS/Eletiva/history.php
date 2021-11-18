<title>Eletiva | My post</title>
<?php
require "dbconnect.php";

require('inc_header.php');
include "header.php";

    $check = "SELECT ID FROM users WHERE email = '$email ' AND password = '$password' AND status = '$status'";
    $result = mysqli_query($connect, $check);
    $row = mysqli_fetch_assoc($result);
    $iduser = $row['ID'];

    $queryA = "SELECT * FROM post WHERE create_by = '$iduser'";
    $resultbulid = mysqli_query($connect, $queryA);
?>
<body>
    <div class="">
        <div class="container py-4">
            <ul class="nav nav-pills nav-fill" id="tabHistory" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="pills-create-tab" data-bs-toggle="pill" data-bs-target="#pills-create" type="button" role="tab" aria-controls="pills-create" aria-selected="true">โพสที่ฉันสร้าง</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="pills-answer-tab" data-bs-toggle="pill" data-bs-target="#pills-answer" type="button" role="tab" aria-controls="pills-answer" aria-selected="false">โพสที่ฉันตอบ</button>
              </li>
            </ul>
            <div class="tab-content" id="tabHistory-Content">
              <div class="tab-pane fade show active" id="pills-create" role="tabpanel" aria-labelledby="pills-create-tab">
                  <ul class="list-group list-group-flush">
                  <?php
                      while($row = mysqli_fetch_assoc($resultbulid)){
                        echo'<li class="list-group-item">';
                        echo'  <div class="row">';
                        echo'     <div class="col-sm-9">';
                        echo'         <a href="post.php?id='.$row['ID_post'].'"><i class="fas fa-chevron-circle-right" style="margin-right"></i>'.$row['title_post'].'</a>';
                        echo'    </div> ';
                        echo'    <div class="col-sm-3 text-md-end">'.$row['time_post'].'</div> ';
                        echo'</div>';
                        echo'</li>';
                      }                        
                      ?>
                  </ul>
              </div>
              <div class="tab-pane fade" id="pills-answer" role="tabpanel" aria-labelledby="pills-answer-tab">
                  <ul class="list-group list-group-flush">
                      <?php
                        $queryB = "SELECT from_post FROM comment WHERE create_by = '$iduser'";
                        $x = mysqli_query($connect, $queryB);
                        while($row = mysqli_fetch_assoc($x)){
                            //เช็คว่าเขียนโพสไหน แล้วนำมาเช็คชื่อเรื่อง
                            $y = $row["from_post"];
                            $queryC = "SELECT * FROM post WHERE ID_post = '$y'";
                            $resultans = mysqli_query($connect, $queryC);
                            if($row = mysqli_fetch_assoc($resultans)){
                                echo'<li class="list-group-item">';
                                echo'  <div class="row">';
                                echo'     <div class="col-sm-9">';
                                echo'         <a href="post.php?id='.$row['ID_post'].'"><i class="fas fa-chevron-circle-right"></i>'.$row['title_post'].'</a>';
                                echo'    </div> ';
                                echo'    <div class="col-sm-3 text-md-end">'.$row['time_post'].'</div> ';
                                echo'</div>';
                                echo'</li>';
                            }
                      }             
                      ?>
                  </ul>
              </div>
            </div>
            
        </div>
    </div>
   
</body>