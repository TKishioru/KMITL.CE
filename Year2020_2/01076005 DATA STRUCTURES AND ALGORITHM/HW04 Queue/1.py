#By Chay

"""
Chapter : 4 - item : 1 - มาใช้ Queue กันเถอะ
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา

E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue
D   ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลัE1งจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูลปัจจุบันของ Queue

***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty

    Testcase : #1
        Enter Input : E 1,E 2,E 3,D,D,E 4
        1
        1, 2
        1, 2, 3
        1 <- 2, 3
        2 <- 3
        3, 4
        1, 2 : 3, 4

    Testcase : #2
        Enter Input : E 1,E 2,D,D,D
        1
        1, 2
        1 <- 2
        2 <- Empty
        Empty
        1, 2 : Empty

"""

class Queue:
    def __init__(self):
        self.en = list()
        self.de = list()
        self.p_e = []
        self.p_d = []
    def __str__(self):
        x = ''
        if len(self.de) <= 0:
            x += 'Empty'
        else:
            if len(self.de) == 1 or self.de[0]:
                x += self.de[0]
            if len(self.de) > 1:
                for i in range(1,len(self.de)):
                    x = x + ', ' + self.de[i]
        x += ' : '
        if len(self.en) <= 0:
            x += 'Empty'
        elif not(len(self.en) <= 0):
            if len(self.en) == 1 or self.en[0]:
                x += self.en[0]
            if len(self.en) > 1:
                for i in range(1,len(self.en)):
                    x = x + ', ' + self.en[i]
        return x
    def enqueue(self,data):
        self.en.append(data)
        self.p_e.append(data)

    def dequeue(self):
        if len(self.p_e) <= 0:
            e = 'Empty'
        else:
            self.de.append(self.en.pop(0))
            self.p_d.append(self.p_e.pop(0))
            
    def prt(self):    
        if len(self.p_e) <= 0:
            e = 'Empty'
        else:
            if len(self.p_e) == 1 or self.p_e[0]:
                e = self.p_e[0]
            if len(self.p_e) > 1:
                for i in range(1,len(self.p_e)):
                    e = e + ', ' + self.p_e[i]            
        
        if len(self.p_d) <= 0:
            d = 'Empty'
        else:
            d = self.p_d[-1]       

        if len(self.p_e) > 0 and len(self.p_d) <= 0:            
            return e
        elif len(self.p_d) <= 0:                 
            return d 
        else:
            self.p_d.clear()
            return d + ' <- ' + e

q = Queue()
inp = input('Enter Input : ').split(',')
for i in range(0,len(inp)):
    x = inp[i]
    if x[0] == 'E':
        key,num = x.split()
        q.enqueue(num)
    elif x[0] == 'D':  
        q.dequeue()
    print(q.prt())
print(q)