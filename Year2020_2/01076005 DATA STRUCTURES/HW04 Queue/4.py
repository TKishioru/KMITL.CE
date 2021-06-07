#BY https://github.com/ApexTone/DataStructAlgo-Grader-KMITL/blob/master/Week4/canteen.py

"""
Chapter : 4 - item : 4 - Canteen
โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input : จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

    Testcase : #1
        Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
        Empty
        101
        201

    Testcase : #2
        Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,E 102,D,D,D,D
        Empty
        101
        102
        201
        Empty
"""

class Queue:
    def __init__(self):
        self.item = list()
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        if len(self.item) > 0:
            return self.item.pop(0)
        else:
            return -1
    def is_empty(self):
        if len(self.item) <= 0:
            return True
        return False
    def dep(self, dep):
        for item in self.item:
            if dep == item[0]:
                return True
        return False

    def Qin(self, val):
        if (len(self.item) <= 0) or not self.dep(val[0]):
            self.enqueue(val)
        else:
            for i in range(len(self.item)-1, -1, -1):
                if self.item[i][0] == val[0]:  
                    self.item.insert(i+1, val)
                    return
            self.enqueue(val)

    def __str__(self):
        prt = ""
        if len(self.item) > 0:
            for i in range(0,len(self.item)):
                prt += str(self.item[i]) + ' '
        else:
            prt = 'Empty'
        return prt

worker = dict()
def allworker(tag,human):
    worker[human] = tag

q = Queue()
inp,command = input('Enter Input : ').split('/')
x = inp.split(',')
for i in range(0,len(x)):
    y = x[i].split()
    allworker(y[0],y[1])
a = command.split(',')
for item in a:
    if item[0] == 'D':
        if not q.is_empty():
            print(q.dequeue()[1])
        else:
            print('Empty')
    if item[0] == 'E':
        que = item.split()
        val = que[1]
        q.Qin((worker[val], val))

