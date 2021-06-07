"""
Chapter : 3 - item : 5 - แปลงเลขฐาน 10 เป็น เลขฐาน 2 ด้วย STACK
จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง

    Testcase : #1
    ***Decimal to Binary use Stack***
    Enter decimal number : 10
    Binary number : 1010

    Testcase : #2
    ***Decimal to Binary use Stack***
    Enter decimal number : 255
    Binary number : 11111111

    Testcase : #3
    ***Decimal to Binary use Stack***
    Enter decimal number : 32340
    Binary number : 111111001010100

"""

class Stack :
    def __init__(self):    #ใช้สำหรับสร้าง list ว่าง
        self.items = []
    def push(self,i):       #เก็บข้อมูลลง stack
        return self.items.append(i)
    def pop(self):         #นำข้อมูลออกจาก stack
        return self.items.pop()
    def isEmpty(self):     #ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        if len(self.items) != 0:
            return False
        return True
    def size(self):        #ตรวจสอบจำนวนข้อมูลใน stack
        return len(self.items)

def dec2bin(decnum):
    s = Stack()
    while decnum > 0:
        s.push(decnum%2)
        decnum = decnum//2
    
    txt = ""
    for i in range(0,s.size()):
        txt += str(s.pop())
    return txt

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))
