<div>
    <!-- logged in user information -->
    <?php if(isset($_SESSION["email"])) : ?>
        <p>Welcome <strong><?php echo $_SESSION["email"]; ?></strong></p>
        <p>status : 
            <?php 
                if($_SESSION["status"] == 0){
                    echo "student"; 
                }
                else if ($_SESSION["status"] == 1){
                    echo "teacher";
                }
                else if ($_SESSION["status"] == 2){
                    echo "admin";
                    echo '<p><a href="admin.php">admin page</a></p>';
                }
            ?>
        </p>
        <p><a href="logout.php">Logout</a></p>
    <?php endif ?>
</div>