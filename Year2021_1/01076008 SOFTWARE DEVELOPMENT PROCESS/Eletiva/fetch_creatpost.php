<?php
error_reporting(0);
require "dbconnect.php";
$output = '';
if(isset($_POST["query"]))
{
	$search = mysqli_real_escape_string($connect, $_POST["query"]);
	$query = "
	SELECT Name_subject FROM subject 
	WHERE ID_subject = $search
	";
	//WHERE ID_subject LIKE '%".$search."%'
	$result = mysqli_query($connect, $query);
	if(mysqli_num_rows($result) > 0)
	{
		$row = mysqli_fetch_array($result);
		
			$output = $row["Name_subject"];
		
		echo $output;
	}
	else
	{
		echo 'Data Not Found';
	}
}

if(isset($_POST["queryG"]))
{
	$search = mysqli_real_escape_string($connect, $_POST["queryG"]);
	$query = "
	SELECT Group_subject FROM subject 
	WHERE ID_subject = $search
	";
	//WHERE ID_subject LIKE '%".$search."%'
	$result = mysqli_query($connect, $query);
	if(mysqli_num_rows($result) > 0)
	{
		$row = mysqli_fetch_array($result);
		
			$output = $row["Group_subject"];
		
		echo $output;
	}
	else
	{
		echo 'Data Not Found';
	}
}


?>