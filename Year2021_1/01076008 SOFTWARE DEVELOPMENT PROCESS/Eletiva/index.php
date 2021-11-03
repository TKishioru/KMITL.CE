<?php
session_start();
//unset($_SESSION["check"]);

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
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eletiva</title>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
 
    <link rel="stylesheet" type="text/css" href="css/home_index.css"> 

    <!-- add icon link -->
    <link rel="icon" href="images/icon.jpg" type="image/x-icon">
    <!-- specifying a webpage icon for web clip -->
    <link rel="apple-touch-icon" href="images/icon.jpg" />

</head>
<!-- Guest -->
<body>
    <header>
        <nav>
            <div class="navbar">
                <div class="logo">
                    <a href="#">electiva</a>
                </div>

                <ul>
                    <li>
                        <input class="searchbox" id="search" type="text" placeholder="" style="display:none;" />
                        <div class="tabbar" style="position:absolute; right: 210px;" id="searchclass">
                            <i class="fas fa-search" id="search-button"></i>
                            <a href="#" id="searchtext">ค้นหา</a>
                        </div>
                        <div class="tabbar">
                            <i class="fas fa-th-large"></i>
                            <a href="#">หมวดหมู่</a>
                        </div>
                    </li>
                    <div class="btn">
                        <button>Login</button>
                    </div>
                </ul>
            </div>
        </nav>
    </header>

    <section>
        <img class="banner" src="images/home.jpg" alt="Banner" />
        <div class="posttext">
            <i class="fas fa-clock"></i>
            <p>โพสล่าสุด</p>
        </div>

        <div class="postbtn">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post1โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>

        <div class="postbtn">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post2โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>

        <div class="postbtn" style="margin-bottom:50px;">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post3โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>
    </section>

    <section>
        <div class="posttext">
            <i class="fas fa-star"></i>
            <p>โพสยอดนิยม</p>
        </div>

        <div class="postbtn">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post1โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>

        <div class="postbtn">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post2โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>

        <div class="postbtn" style="margin-bottom:50px;">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post3โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>
    </section>

    <section>
        <div class="posttext">
            <i class="fas fa-bookmark"></i>
            <p>โพสแนะนำ</p>
        </div>

        <div class="postbtn">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post1โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>

        <div class="postbtn">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post2โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>

        <div class="postbtn" style="margin-bottom:50px;">
            <i class="fas fa-chevron-circle-right"></i>
            <a href="#">Post3โพส</a>
            <h1>วิชาเลือกกลุ่ม....</h1>
            <p>User:??? Time:???</p>
            <div class="commentfa">
                <i class="far fa-comment-dots"></i>
                <h3>num</h3>
            </div>
        </div>
    </section>

    <div class="blank">
        <span>space</span>
    </div>
    <script>
        const searchBtn = document.getElementById('search-button');
        const search = document.getElementById('search');
        const searchtext = document.getElementById('searchtext');
        const searchCL = document.getElementById('searchclass')

        searchCL.addEventListener('click', () => {
            search.style.display = 'block';
            search.style.width = '30%';
            search.style.paddingRight = '50px';
            search.style.right = '220px';
            searchBtn.style.color = '#FAB23D';
            searchBtn.style.position = 'absolute';
            searchBtn.style.top = '17px';
            searchBtn.style.cursor = 'pointer';
            searchCL.style.pointerEvents = 'none';
            searchtext.style.display = 'none';
        })
    </script>
</body>
</html>