"""
Chapter : 2 - item : 5 - funString
จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

1. หาความยาวของ String
2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)
3. Reverse String (ห้ามใช้คำสั่ง reversed)
4. ลบตัวอักษรที่ปรากฏมาก่อนใน String

    Testcase : #1 1
        Enter String and Number of Function : helloce 1
        7

    Testcase : #2 2
        Enter String and Number of Function : aAaBbBccCDddd 2
        AaAbBbCCcdDDD

    Testcase : #3 3
        Enter String and Number of Function : IloveKMITL 3
        LTIMKevolI

    Testcase : #4 4
        Enter String and Number of Function : BananaBoat 4
        Banot
"""

class funString():
    
    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        s2 = ""
        for i in range(0,len(self.string)):
            x = ord(self.string[i])
            if x >= 65 and x <= 90:
                y = chr(x + 32)
            elif x >= 97 and x <= 112:
                y = chr(x - 32)
            s2 += y
        return s2

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        s4 = ""
        for i in range(0,len(self.string)):
            x = self.string[i]
            if x not in s4:
                s4 += self.string[i]
        return s4

str1,str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)
if str2 == "1" :   print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())