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
  
  1.10 กด Continue / Done ไปเร่ือยๆ
  
  1.11 เมื่อถึงหน้า Profile setup
  
    - Your name : spa_assignment
    
    - Your server's name : spa_server
    
    - Pick a username : spa_admin
    
    - Choose a password : admin
    
    - Confirm your password : admin
    
  1.12 ตกลงแล้ว Reboot Now
  
  1.13 เมื่อโหลดถึง [OK] Reached target Cloud-init target. กด Enter!
    
    - login : ชื่อ username ที่ตั้งไว้
    
    - Password : password ที่ตั้งไว้
  
2. ตั้งค่าให้เวลาเดินตรงกับมาตรฐานโลก

3. อัปเดต/แพตช์ระบบปฏิบัติการ

4. เพิ่มยูสเซอร์ webadmin และ dbadmin เข้าสู่ระบบ พร้อมการกำกับดูแลที่ดีให้ปลอดภัย

5. เปิดให้เข้าถึงได้จากระยะไกลด้วย ssh หรือ remote desktop หรือเทียบเท่า

6. เปิดบริการเป็นเว็บแอพพลิเคชันได้ (Web+DB+Server-Side Script) แบบปลอดภัย

7. กำกับดูแลด้วยยูสเซอร์ webadmin สำหรับงานเว็บ และ dbadmin สำหรับงานฐานข้อมูล

8. คำสั่งที่จำเป็นต่อผู้ดูแลระบบไม่ต่ำกว่า 30 คำสั่ง



