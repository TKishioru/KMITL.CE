"""
Chapter : 3 - item : 1 - สร้าง stack

    Testcase : #1
        *** Stack implement by Python list***
        Enter data to stack : K M I T L C E 2 5 6 3
        11 Data in stack :  ['K', 'M', 'I', 'T', 'L', 'C', 'E', '2', '5', '6', '3']
        0 Data in stack :  []
"""
class Stack:
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

print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)
print(s.size(),"Data in stack : ",s.items)
while not s.isEmpty():
    s.pop()
print(s.size(),"Data in stack : ",s.items)