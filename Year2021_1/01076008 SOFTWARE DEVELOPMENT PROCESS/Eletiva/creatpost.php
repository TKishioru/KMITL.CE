<title>Eletiva | Creat Post</title>
<link rel="stylesheet " type="text/css " href="css/creatpost.css ">
<?php
//For Student
include "header.php";
?>
<!DOCTYPE html>
<html lang="en">
</html>
<body>
    <div class="container-fluid  pt-5">
        <div class="row">

            <div class="col-lg-2 col-sm-1 "></div>

            <div class="col-lg-8 col-sm-10 ">
                <div class="box-post">
                    <h2>เขียนโพสต์</h2>
                    <form>
                        <label for="Category" class="form-label">หมวดหมู่</label>
                        <select class="form-select form-select-sm">
                            <option selected>-- เลือกหมวดหมู่ --</option>
                            <option>กลุ่มวิชาภาษา</option>
                            <option>กลุ่มวิชามนุษย์ศาสตร์</option>
                            <option>กลุ่มวิชาสังคมศาสตร์</option>
                            <option>กลุ่มวิชาวิทยาศาสตร์กับคณิตศาสตร์</option>
                            <option>วิชาเลือกเสรี</option>
                            <option>กลุ่มคุณค่าแห่งชีวิต</option>
                            <option>กลุ่มวิถีแห่งสังคม</option>
                            <option>กลุ่มศาสตร์แห่งการคิด</option>
                            <option>กลุ่มภาษาและการสื่อสาร</option>
                            <option>กลุ่มศิลปแห่งการจัดการ</option>
                            <option>กลุ่มทักษะที่จำเป็นในศตวรรษที่ 21</option>
                            <option>กลุ่มทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</option>
                            <option>กลุ่มทักษะด้านการจัดการและภาวะความเป็นผู้นำ</option>
                            <option>กลุ่มทักษะด้านภาษาและการสื่อสาร</option>
                        </select>

                        <div class="row ">

                            <div class="col-lg-6 ">
                                <label for="subjectecode " class="form-label ">รหัสวิชา</label>
                                <input class="form-control form-control-sm " list="codes" type="text" id="code" placeholder="" required>
                                <datalist id="codes">
                                    <option value="xxxxxx"></option>
                                    <option value="yyyyyy"></option>
                                </datalist>
                            </div>
                            <div class="col-lg-6 ">
                                <label for="subjectename " class="form-label ">ชื่อวิชา</label>
                                <input class="form-control form-control-sm " type="text" id="subject " placeholder=" " required>
                            </div>

                        </div>


                        <label for="instructor " class="form-label ">อาจารย์ผู้สอน</label>
                        <input class="form-control form-control-sm " type="text" id="instructor " placeholder=" " required>


                        <label for="details " class="form-label ">รายละเอียด:</label>
                        <textarea class="form-control form-control-sm " id="details " placeholder="" rows="3" required></textarea>

                        <div class="d-grid col-lg-6 mx-auto ">
                            <input class="form-control button " type="submit" value="สร้างโพสต์">
                        </div>
                </div>
                </form>
            </div>

        </div>

        <div class="col-lg-2 col-sm-1"></div>
    </div>

</body>

</html>