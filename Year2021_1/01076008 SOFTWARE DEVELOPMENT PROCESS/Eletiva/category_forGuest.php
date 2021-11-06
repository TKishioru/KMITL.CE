
<section>
    <div class="inf">
    <div id="myBtnContainer">
        <button class="btn active" onclick="filterSelection('all')"> Show all</button>
        <button class="btn" onclick="filterSelection('cars')"> Cars</button>
        <button class="btn" onclick="filterSelection('animals')"> Animals</button>
        <button class="btn" onclick="filterSelection('fruits')"> Fruits</button>
        <button class="btn" onclick="filterSelection('colors')"> Colors</button>
        </div>

        <div class="show_elective">
      <button name="show_eng1"><i class="fas fa-language"></i><p class="sub">หมวดภาษา</p></button>
      <button name="show_hu"><i class="fas fa-users"></i><p class="sub">หมวดมนุษย์ศาสตร์</p></button>
      <button name="show_so1"><i class="fas fa-globe"></i><p class="sub">หมวดสังคมศาสตร์</p></button>
      <button name="show_sci"><i class="fas fa-atom"></i><p class="sub">หมวดวิทยาศาสตร์ฯ</p></button>
      <button name="show_free"> <i class="fas fa-dove"></i><p class="sub">หมวดวิชาเลือกเสรี</p></button>
      <button name="show_life"><i class="fas fa-hand-holding-heart"></i><p class="sub">หมวดคุณค่าแห่งชีวิต</p></button>
      <button name="show_so2"><i class="fas fa-icons"></i><p class="sub">หมวดวิถีแห่งสังคม</p></button>
      <button name="show_think"><i class="fas fa-brain"></i><p class="sub">ศาสตร์แห่งการคิด</p></button>
      <button><i class="fas fa-chart-line"></i>
                        <p class="sub">ศิลปแห่งการจัดการ</p></button>
      <button><i class="fas fa-comments"></i>
                        <p class="sub">ภาษาและการสื่อสาร</p></button>
      <button><i class="fas fa-vr-cardboard"></i>
                        <p class="sub">หมวดทักษะที่จำเป็นในศตวรรษที่ 21</p></button>
      <button><i class="fas fa-user-tie"></i>
                        <p class="sub">ทักษะด้านบุคคลและทักษะส่งเสริมวิชาชีพ</p></button>
      <button><i class="fas fa-book-reader"></i>
                        <p class="sub">ทักษะด้านการจัดการและภาวะความเป็นผู้นำ</p></button>
      <button><i class="fas fa-globe-americas"></i>
                        <p class="sub">หมวดทักษะด้านภาษาและการสื่อสาร</p></button>
      <button></button>
        </div>
                    <input type="checkbox" class="selectS" id="myCheckbox9" name="show_manage">
                    <label for="myCheckbox9">
                        
                    </label> 
                    <input type="checkbox" class="selectS" id="myCheckbox10" name="show_eng2">
                    <label for="myCheckbox10">
                        
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox11" name="show_21">
                    <label for="myCheckbox11">
                        
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox12" name="show_carrer">
                    <label for="myCheckbox12">
                        
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox13" name="show_leader">
                    <label for="myCheckbox13">
                        
                    </label>
                    <input type="checkbox" class="selectS" id="myCheckbox14" name="show_eng3">
                    <label for="myCheckbox14">
                        
                    </label>
    </div>
    </div>
    <!-- โพสล่าสุด -->
    <div class="inf">
        <div class="posttext">
            <i class="fas fa-bookmark"></i>
            <p class="mainC">ผลการค้นหา</p>
        </div>
        <!-- -ข้อมูล -->
        <?php              
        echo '<a href="#Test1" class="Content">';
        echo '    <div class="post_btn">';
        echo '        <div class="A_left">';
        echo '            <i class="icon_next fas fa-chevron-circle-right"></i>';
        echo '            <h4 class="textC" name="Post">Post1โพส</h4>';
        echo '            <h6 class="textS" name="subject">วิชาเลือกกลุ่ม....</h6>';
        echo '            <br><p class="Timestamp">User:??? Time:???</p>';
        echo '        </div>';
        echo '        <div  class="A_right">';
        echo '            <i class="iconcomment far fa-comment-dots"></i>';
        echo '            <h5 class="commentN">num</h5>';
        echo '        </div>';
        echo '    </div>';
        echo '</a>';
        ?>
    </div>
</section>
<script src="javascript/navbar.js"></script>