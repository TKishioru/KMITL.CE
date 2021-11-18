<title>Eletiva | Setting</title>
<?php
require "dbconnect.php";

require('inc_header.php');
include "header.php";
?>
<?php if((isset($_SESSION['status']) && !empty($_SESSION['status']) && (($_SESSION['status'] == 1) || $_SESSION['status'] == 2))) : ?>
<style>
  .BO{
    border: 2px solid black;
  }
</style>
<body>
    <div class="">
        <div class="container py-4">
           <div class="card card-dark mb-4 rounded-0">
              <div class="card-header rounded-0">
                ตั้งค่า
              </div>
              <div class="card-body pt-0 pb-0">
                  <form>
                      <div class="row">
                        <div class="col-sm-2 px-0 borderAccNav">
                            <nav class="nav nav-pill flex-column" id="accountNav">
                              <a class="nav-link active" aria-current="page" href="setting.php" style="color:white;">บัญชี</a>
                            </nav>
                        </div>
                        <div class="col-sm-10 pt-2">
                            <div class="px-md-3">
                                <div class="row mb-3">
                                    <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">อีเมล</label>
                                    <div class="col-sm-10">
                                      <p class="form-control-plaintext text-white"><?php echo $email ?></p>
                                    </div>
                                </div>
                                <div class="row mb-3">
                                    <label for="inputEmail3" class="col-sm-2 col-form-label fw-normal text-white">รหัสผ่าน</label>
                                    <div class="col-sm-10">
                                      <p class="form-control-plaintext text-white"><a href="new-password.php">changed password</a></p>
                                    </div>
                                </div>
                                <div class="row mb-3">
                                    <div class="col-sm-12 text-center py-3">
                                      <button class="btn btn-orange BO">บันทึกข้อมูล</button>
                                    </div>
                                </div>
                            </div>
                        </div>  
                      </div> 
                  </form>
              </div>
            </div>
        </div>
    </div>
<!-- Modal -->
<div class="modal fade" id="changeUserNameModal" tabindex="-1" aria-labelledby="changeUserNameModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <form>  
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="changeUserNameModalLabel">เปลี่ยนชื่อนามแฝง</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row mb-3">
                <label for="inputEmail3" class="col-sm-2 col-form-label">นามแฝง</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" value="Big O">
                </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">ยกเลิก</button>
            <button type="button" class="btn btn-success">บันทึกการแก้ไข</button>
          </div>
        </div>
    </form>
  </div>
</div>   
<!-- Modal -->
<div class="modal fade" id="changeEmailModal" tabindex="-1" aria-labelledby="changeEmailModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <form>  
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="changeEmailModalLabel">เปลี่ยนอีเมล</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row mb-3">
                <label for="inputEmail3" class="col-sm-2 col-form-label">อีเมล์</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" value="65010345@kmitl.ac.th">
                </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">ยกเลิก</button>
            <button type="button" class="btn btn-success">บันทึกการแก้ไข</button>
          </div>
        </div>
    </form>
  </div>
</div>
<!-- Modal -->
<div class="modal fade" id="changePassModal" tabindex="-1" aria-labelledby="changePassModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <form>  
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="changePassModalLabel">เปลี่ยนรหัสผ่าน</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row mb-3">
                <label for="inputEmail3" class="col-sm-2 col-form-label">รหัสผ่านใหม่</label>
                <div class="col-sm-10">
                  <input type="password" class="form-control" value="">
                </div>
            </div>  
            <div class="row mb-3">
                <label for="inputEmail3" class="col-sm-2 col-form-label">ยืนยันรหัสผ่านใหม่</label>
                <div class="col-sm-10">
                  <input type="password" class="form-control" value="">
                </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">ยกเลิก</button>
            <button type="button" class="btn btn-success">บันทึกการแก้ไข</button>
          </div>
        </div>
    </form>
  </div>
</div>    
</body>
<?php else: ?>
<?php include "logout.php"; ?>
<?php endif ?>