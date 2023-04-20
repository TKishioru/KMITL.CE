# SPA Assignment 2023

1. ติดตั้งระบบปฏิบัติการตระกูลยูนิกซ์ระดับเซิร์ฟเวอร์ Ubuntu Server หรือ FreeBSD/OpenBSD หรือเทียบเท่า

**ขั้นตอน**

  1.1 โหลดโปรแกรม Oracle VM VirtualBox
  
  1.2 โหลด Ubuntu Server จาก https://ubuntu.com/download
  
  1.3 ไปที่ VirtualBox กดสร้าง Virtual machine Name
  
    - ชื่อ : spa_2565
    
    - ชนิด : Linux
    
    - รุ่น : Ubuntu เวอร์ชันที่เราโหลดมา
    
  1.4 กด next ไปเรื่อยๆ (ใช้ค่า default)
  
  1.5 กด finish
  
  1.6 (ณ Virtual machine Name ที่เราสร้าง) ไปที่ตั้งค่า > เครือข่าย > เลือกเชื่อมต่อกับ "แผนวงจรแบบบริดจ์" > ตกลง
  
  1.7 เปิด Virtual machine (ดับเบิ้ลคลิก!)
  
  1.8 เมื่อมีหน้าต่าง VirtualBox VM ขึ้นมา ให้เลือกไฟล์ที่เราโหลดจากข้อ 1.2 > Mount and Retry Boot
  
  1.9 เซ็ทค่าภาษาเป็น English
  
  1.10 กด Continue / Done ไปเร่ือยๆ //ต้องต่อกับเน็ตที่สามารถแจก IPv4 ได้นะ
  
  1.11 เมื่อถึงหน้า Profile setup
  
    - Your name : spa_assignment
    
    - Your server's name : spa_server
    
    - Pick a username : spa_admin
    
    - Choose a password : admin
    
    - Confirm your password : admin
    
  **อย่าลืม** Install SSH ด้วยนะ กดเลือก
  
  1.12 ตกลงแล้ว Reboot Now
  
  1.13 เมื่อโหลดถึง [OK] Reached target Cloud-init target. กด Enter!
    
    - login : ชื่อ username ที่ตั้งไว้
    
    - Password : password ที่ตั้งไว้
  
2. ตั้งค่าให้เวลาเดินตรงกับมาตรฐานโลก

  2.1 แสดงเวลามาดูก่อน
  
  ```
  $ date  
  
  หรือ
  
  $ timedatectl
  คำสั่ง timedatectl ใน Ubuntu ใช้เพื่อแสดงการตั้งค่าเวลาและวันที่ปัจจุบัน 
  คำสั่งนี้ใช้เพื่อควบคุมเวลาและวันที่ของระบบ
  ```
  
  2.2 ตั้งค่าเวลาตามเวลากทม.
  
  ```
  $ timedatectl set-timezone Asia/Bangkok
  ```
  
3. อัปเดต/แพตช์ระบบปฏิบัติการ
  
  3.1 พิมพ์คำสั่งแล้วใส่รหัสผ่าน
  
  ```
  $ sudo apt update
  ```

4. เพิ่มยูสเซอร์ webadmin และ dbadmin เข้าสู่ระบบ พร้อมการกำกับดูแลที่ดีให้ปลอดภัย

  4.1 เพิ่ม user คือ webadmin และ dbadmin > ตั้งรหัสเฉพาะแต่ละ user
  
  ```
  $ sudo adduser ชื่อที่จะเพิ่ม (ยืนยันด้วยรหัส user)
  ```
    - webadmin ใช้รหัสผ่าน webadmin
    
    - dbadmin ใช้รหัสผ่าน dbadmin
    
  4.2 กด Enter ข้ามการกรอก value ไปเลย "แล้วกด Y"
  
  4.3 ดูว่ามี user อะไรบ้าง
  
  ```
  $ compgen -u
  ```
  
  4.4 ดูว่ามี group อะไรบ้าง

  ```
  $ compgen -g
  ```
  **หมายเหตุ** ในการสร้าง 1 user จะถูกสร้าง group สำหรับ user นั้นขึ้นมา
  
  **หมายเหตุ** adduser มีตั้งค่า รหัสผ่าน/สร้าง directory/เก็บข้อมูล _ซึ่งตรงข้ามกับ_ useradd
    
  4.5 เหลือ "กำกับดูแลที่ดีให้ปลอดภัย"
  
5. เปิดให้เข้าถึงได้จากระยะไกลด้วย ssh หรือ remote desktop หรือเทียบเท่า

  5.0 คำสั่งที่น่าสนใจ
  
  ```
  $ ssh -v ดูว่ามีการติดตั้ง ssh ไหม
  
  $ sudo apt-get install openssh-server ติดตั้ง ssh
  
  $ sudo systemctl status ssh เช็คว่าทำงานไหม
  
  $ ip a เช็คว่า เครื่องนี้เป็น ip อะไร
  
  $ ssh ชื่อ username@เลข ip ของเครื่อง
  ```
  
  5.1 ใส่คำสั่ง ifconfig ใช้ในการแสดงข้อมูลและเปลี่ยนค่า interface server
  
  5.2 เมื่อคำสั่ง ifconfig ใช้งานไม่ได้ จึงจำเป็นต้องโหลด
  
  ```
  $ sudo apt install net-tools
  ```
  
  5.3 เปิด cmd (window) ใช้คำสั่ง
  
  ```
  $ ssh-keygen -b 4096
  ```
  
6. เปิดบริการเป็นเว็บแอพพลิเคชันได้ (Web+DB+Server-Side Script) แบบปลอดภัย

7. กำกับดูแลด้วยยูสเซอร์ webadmin สำหรับงานเว็บ และ dbadmin สำหรับงานฐานข้อมูล

8. คำสั่งที่จำเป็นต่อผู้ดูแลระบบไม่ต่ำกว่า 30 คำสั่ง



