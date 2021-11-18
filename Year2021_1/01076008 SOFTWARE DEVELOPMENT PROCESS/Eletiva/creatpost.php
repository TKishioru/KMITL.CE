<title>Eletiva | Creat Post</title>
<link rel="stylesheet " type="text/css " href="css/creatpost.css ">

<?php

//error_reporting(0);

//For Student
require "dbconnect.php";

include "header.php";

//DB : subject
?>
<?php if(isset($_SESSION['status']) && !empty($_SESSION['status']) && ($_SESSION['status'] == 1 || $_SESSION['status'] == 2)) : ?>
<body>
    <div class="container-fluid  pt-5">
        <div class="row">

            <div class="col-lg-2 col-sm-1 "></div>

            <div class="col-lg-8 col-sm-10 ">
                <div class="box-post">
                    <h2>เขียนโพสต์</h2>
                    <form method="POST" action="controllerPostData.php">
                        <label for="Category" class="form-label">รหัสวิชา</label>                        
                        <input class="form-control form-control-sm " list="codes" type="text" id="subject_ID" placeholder="subject ID" name="subject_ID" pattern="(?=.*[0-9]).{8}" title="The course code must be 8 digits only." required>
                            
                        
                        <!--<p id="demo"></p>-->
                        <div class="row ">
                            <div class="col-lg-6 ">
                                <label for="subjectecode " class="form-label ">หมวดหมู่</label>
                                <input class="form-control form-control-sm " type="text" id="Group_subject" placeholder="group name" name="Group_subject" readonly >                                
                            </div>
                            <div class="col-lg-6 ">
                                <label for="subjectename" class="form-label ">ชื่อวิชา</label>
                                <input class="form-control form-control-sm " type="text" id="subjectename" placeholder="subject name" name="subject_Name" readonly >
                            </div>

                            </div>
                            
                            <?php if($_SESSION['status'] == 1): ?>
                                <div class="post-check">
                                    <label class="form-check-label" for="radio0">ประเภทโพสต์</label>
                                    <div class="form-check form-check-inline">
                                        <label class="form-check-label" for="inlineRadio1">
                                        <input class="form-check-input " type="radio" checked="checked"name="post_type" id="inlineRadio1" value="1"> โพสต์ธรรมดา
                                        </label>
                                    </div>
                                    <div class="form-check form-check-inline"><label class="form-check-label" for="inlineRadio2">
                                        <input class="form-check-input" type="radio" name="post_type" id="inlineRadio2" value="2">โพสต์รีวิว
                                        </label>
                                    </div>
                                </div>
                            <?php elseif($_SESSION['status'] == 2): ?>
                                <div class="form-check form-check-inline" style="display:none"><label class="form-check-label" for="inlineRadio3">
                                    <input class="form-check-input " type="radio" checked="checked"name="post_type" id="inlineRadio3" value="3"> โพสต์สอบถาม
                                    </label>
                                </div>
                                <p style="margin-top:-30px; color:transparent;">-</p>
                            <?php endif ?>
                            <div class="row g-2 align-items-center">
                            <div class="col-lg-auto">
                                <label for="instructor" class="form-label">ชื่อเรื่อง</label>
                            </div>
                            <div class="col-lg-10">
                                <input class="form-control form-control-sm " type="text" id="instructor" name="post_topic" placeholder="topic" pattern="[ก-๛0-9a-zA-Z]{5,50}" title="User can type the title in Thai, English, numbers and spaces, 5 - 50 characters." required>
                            </div>
                            </div>
                            <div class="details">
                                <label for="details" class="form-label ">รายละเอียด:</label>
                                <textarea class="form-control form-control-sm " id="details" name="post_details" placeholder="รายละเอียด" rows="4" cols="50" pattern="^[@#$%^*+\\]{10,255}" 
                                title="Users can type the information they want to post. which consists of Thai, English, numbers, special symbols (. : - / ? = ( ) & ' !) and spaces 10 -255 characters long" required></textarea>
                            </div>
                            <div class="d-grid col-lg-6 mx-auto ">
                                <input class="form-control button " type="submit" value="สร้างโพสต์" name="creat_post">
                            </div>
                        </div>
                </form>
            </div>

        </div>

        <div class="col-lg-2 col-sm-1"></div>
    </div>
</body>
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>
<script>
    function FuncGroup(sel) {
    var Group_subject = sel.options[sel.selectedIndex].value; 
    //หรือ document.getElementById("category").value;
    document.getElementById("demo").innerHTML = "You selected: " + x;
    } 
    
</script>

<script>
$(document).ready(function(){
	load_data();
	function load_data(query)
	{
		$.ajax({
			url:"fetch_creatpost.php",
			method:"post",
			data:{query:query},
			success:function(data)
			{		
                document.getElementById("subjectename").value = data;
			}
		});
	}
	
	$('#subject_ID').keyup(function(){
		var search = $(this).val();
		if(search != '')
		{
			load_data(search);
		}
		else
		{
			load_data();			
		}
	});
});
</script>

<script>
$(document).ready(function(){
	load_data();
	function load_data(queryG)
	{
		$.ajax({
			url:"fetch_creatpost.php",
			method:"post",
			data:{queryG:queryG},
			success:function(data)
			{		
                document.getElementById("Group_subject").value = data;
			}
		});
	}
	
	$('#subject_ID').keyup(function(){
		var search = $(this).val();
		if(search != '')
		{
			load_data(search);
		}
		else
		{
			load_data();			
		}
	});
});
</script>