<title>Eletiva | Search</title>
<link rel="stylesheet" type="text/css" href="css/home_index.css">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<?php
require "dbconnect.php";

include "header.php";
?>
<?php if((isset($_SESSION['status']) && !empty($_SESSION['status']) && $_SESSION['status'] != 3) || empty($_SESSION['status'])) : ?>
<div class="inf">
    <div class="form_find">
    <form class=""> 
    <i class="align_icon fa fa-search"></i>
    <input type="text" class="searchbox A_left" placeholder="Search...  [Subject ID, Subject Name etc.]" name="search_text" id="search_text">
    <!--<button class="btn_find " type="submit">ค้นหา</button>-->
    <!--<button class="btn_find " type="submit"><i class="icon_find fa fa-search"></i></button>-->
    </form>
</div>

<section>
    <!-- โพสล่าสุด -->
    <div class="inf">
        <br>
        <div class="posttext">
            <i class="fas fa-bookmark"></i>
            <p class="mainC">ผลการค้นหา</p>
        </div>
        <!-- -ข้อมูล -->
        <div id="result"></div>
    </div>
</section>

<script>
$(document).ready(function(){
	load_data();
	function load_data(queryS)
	{
		$.ajax({
			url:"fetch_search.php",
			method:"post",
			data:{queryS:queryS},
			success:function(data)
			{
				$('#result').html(data);
			}
		});
	}
	
	$('#search_text').keyup(function(){
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

<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>
