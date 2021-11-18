<?php 

session_start();
require "dbconnect.php";
$errors = array();

    $id_notify = $_REQUEST['id_notify'];
    $sql = "UPDATE notify SET status_notify = '0' WHERE ID_notify='$id_notify'";    
    mysqli_query($connect,$sql); // สั่งรันคำสั่ง sql

    $SQL = "SELECT from_post FROM notify WHERE ID_notify='$id_notify'";
    $Query = mysqli_query($connect,$SQL);
    $Resuut = mysqli_fetch_assoc($Query);   
    $from_post = $Resuut['from_post'];
    
    header("location: post.php?id=$from_post");
?>
