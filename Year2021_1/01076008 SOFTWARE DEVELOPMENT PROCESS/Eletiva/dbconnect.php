<?php

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "db_eletiva";

        // Create Connection
        $connect = mysqli_connect($servername, $username, $password, $dbname);

        // Check connection
        if (!$connect) {
            die("Connection failed" . mysqli_connect_error());
            //หรือย่อเป็น $conn = mysqli_connect($servername, $username, $password, $dbname) or die("Connection failed");
        } 
    
?>