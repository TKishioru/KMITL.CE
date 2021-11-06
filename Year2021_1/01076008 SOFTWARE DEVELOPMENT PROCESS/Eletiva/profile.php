<head>
    <meta charset="UTF-8">
    <title>Profile</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="">

    <!-- add icon link -->
    <link rel="icon" href="images/icon.jpg" type="image/x-icon">
    <!-- specifying a webpage icon for web clip -->
    <link rel="apple-touch-icon" href="images/icon.jpg" />

</head>
<?php
session_start();
require "dbconnect.php";
$email = $_SESSION["email"];

$query = "SELECT * FROM users WHERE email = '$email'";
$result = mysqli_query($connect, $query);
$row = mysqli_fetch_assoc($result);
$name = $row["name"];
$faculty = $row["faculty"];
$major = $row["major"];
$img = (empty($row['picture'])) ? 'test.jpg' : $row["picture"];
$introduce = $row["introduce"];

?>

    <form action="editprofile.php" method="post" id="form" enctype="multipart/form-data">
        <label>เมล</label><input type="email" value="<?php echo $email ?>" readonly><br>
        <label>ชื่อ</label><input type="text" placeholder="ชื่อ" name="name" value="<?php echo $name ?>"><br>
        <label>คณะ</label><input type="text" placeholder="คณะ" name="faculty" value="<?php echo $faculty ?>"><br>
        <label>สาขา</label><input type="text" placeholder="สาขา" name="major" value="<?php echo $major ?>"><br>
        <img src="myfile/<?php echo $img; ?>" width="200" height="200"></center></td><br>
        <label for="img">Select image:</label>
        <input type="file" id="filUpload" name="filUpload"><br>
		<input type="hidden" name="hdnOldFile" value="<?php echo $img; ?>">
        <label>แนะนำตัว</label><input type="text" placeholder="แนะนำตัว" name="introduce" value="<?php echo $introduce ?>"><br>

        <input type="checkbox" name="elective_eng1"> <label> 1. elective_eng1</label><br>
        <input type="checkbox" name="elective_hu"> <label> 2. elective_hu</label><br>
        <input type="checkbox" name="elective_so1"> <label> 3. elective_so1</label><br>
        <input type="checkbox" name="elective_sci"> <label> 4. elective_sci</label><br>
        <input type="checkbox" name="elective_free"> <label> 5. elective_free</label><br>
        <input type="checkbox" name="elective_life"> <label> 6. elective_life</label><br>
        <input type="checkbox" name="elective_so2"> <label> 7. elective_so2</label><br>
        <input type="checkbox" name="elective_think"> <label> 8. elective_think</label><br>
        <input type="checkbox" name="elective_manage"> <label> 9. elective_manage</label><br>
        <input type="checkbox" name="elective_eng2"> <label> 10. elective_eng2</label><br>
        <input type="checkbox" name="elective_21"> <label> 11. elective_21</label><br>
        <input type="checkbox" name="elective_carrer"> <label> 12. elective_carrer</label><br>
        <input type="checkbox" name="elective_leader"> <label> 13</label><br>
        <input type="checkbox" name="elective_eng3"> <label> 14. elective_eng3</label><br>

        <input type="submit" name="change_info">
    </form>

    <p><a href="index.php">index page</a></p>

<p><a href="new-password.php">changed password</a></p>

<?php  
 
if($_GET['error']==1){
    echo '<script type="text/javascript">';
    echo ' alert("Change Complete!!"); ';  //not showing an alert box.
    echo '</script>';
}
else if ($_GET['error']==2){
    echo '<script type="text/javascript">';
    echo ' alert("Change Fail!!"); ';  //not showing an alert box.
    echo '</script>';
}

?>