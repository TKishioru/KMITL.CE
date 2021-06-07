จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้
1. หาความยาวของ String len(s)
2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)
3. Reverse String (ห้ามใช้คำสั่ง reversed)
4. ลบตัวอักษรซ้ำใน String

class funString:
    def LenStr(lstr):
        ns = len(lstr)
        print(ns)
    def LowUpStr(lustr):
        print()
    def RevStr(restr):
        print()
    def DelStr(destr):
        print()

str,n = input("Enter String and Number of Function : ").split()
n = int(n)
fs = funString()
if n ==1:
    fs.LenStr(str)
elif n==2:
    fs.LowUpStr(str)
elif n==3:
    fs.RevStr(str)
elif n==4:
    fs.DelStr(str)