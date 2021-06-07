"""
Chapter : 4 - item : 2 - คอยนาน
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้
แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ
แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ
ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2
จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด

    Testcase : #1
        Enter people : Lorem_Ipsum
        1 ['o', 'r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L'] []
        2 ['r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o'] []
        3 ['e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o', 'r'] []
        4 ['m', '_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e'] []
        5 ['_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm'] []
        6 ['I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm', '_'] []
        7 ['p', 's', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] []
        8 ['s', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p']
        9 ['u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p', 's']
        10 ['m'] ['e', 'm', '_', 'I', 'u'] ['s']
        11 [] ['e', 'm', '_', 'I', 'u'] ['s', 'm']

"""
n = 1
class Queue:
    def __init__(self):
        self.fst = list()
        self.snd = list()
        self.inp = []
        
        self.a = 0
        self.b = 0
    def size(self):
        return len(self.inp)
    def enqueue(self,data):
        self.inp.append(data)    
    def dequeue(self):
        #print('1:',len(self.fst),self.a,'   2:',len(self.snd),self.b)
        if len(self.fst) < 5:
            self.fst.append(self.inp.pop(0))
        elif len(self.fst) == 5 and self.a == 3:
            self.fst.append(self.inp.pop(0))
        elif len(self.snd) < 5:
            if len(self.fst) < 5:
                self.fst.append(self.inp.pop(0))
            else:
                self.snd.append(self.inp.pop(0))
        if len(self.fst) > 0:
            self.a+=1
        if len(self.snd) > 0:
            self.b+=1
        if len(self.fst) > 0 and self.a > 3:
            self.fst.pop(0)
            if len(self.fst) > 0:
                self.a = 1
            else:
                self.a = 0
        if len(self.snd) > 0 and self.b > 2:
            self.snd.pop(0) 
            if len(self.snd) > 0:
                self.b = 1
            else:   
                self.b = 0
        
q = Queue()
txt = input('Enter people : ')
for i in range(0,len(txt)):
    q.enqueue(txt[i])
while q.size() > 0:
    q.dequeue()
    print(f'{n} {q.inp} {q.fst} {q.snd}')
    n+=1