<?php
error_reporting(0);
require "dbconnect.php";
$output = '';
if(isset($_POST["query"]))
{
	$search = mysqli_real_escape_string($connect, $_POST["query"]);
	$query = "
	SELECT * FROM subject 
	WHERE ID_subject = $search
	";
	//SELECT COUNT(ID_notify) FROM notify;
}

$result = mysqli_query($connect, $query);
if(mysqli_num_rows($result) > 0)
{
	$row = mysqli_fetch_array($result);
	
		$output = $row["COUNT(ID_notify)"];
		//echo $row['COUNT(*)'];
	echo $output;
}
?>