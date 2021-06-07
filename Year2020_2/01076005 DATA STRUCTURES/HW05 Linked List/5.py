#By ApexTone.
'''
Chapter : 5 - item : 5 - Radix Sort (มากไปน้อย)
ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย
โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

    Testcase : #1
        Enter Input : 64 8 216 512 27 729 0 1 343 125
        ------------------------------------------------------------
        Round : 1
        0 : 0 
        1 : 1 
        2 : 512 
        3 : 343 
        4 : 64 
        5 : 125 
        6 : 216 
        7 : 27 
        8 : 8 
        9 : 729 
        ------------------------------------------------------------
        Round : 2
        0 : 8 1 0 
        1 : 512 216 
        2 : 729 125 27 
        3 : 
        4 : 343 
        5 : 
        6 : 64 
        7 : 
        8 : 
        9 : 
        ------------------------------------------------------------
        Round : 3
        0 : 64 27 8 1 0 
        1 : 125 
        2 : 216 
        3 : 343 
        4 : 
        5 : 512 
        6 : 
        7 : 729 
        8 : 
        9 : 
        ------------------------------------------------------------
        Round : 4
        0 : 729 512 343 216 125 64 27 8 1 0 
        1 : 
        2 : 
        3 : 
        4 : 
        5 : 
        6 : 
        7 : 
        8 : 
        9 : 
        ------------------------------------------------------------
        3 Time(s)
        Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
        After  Radix Sort : 729 -> 512 -> 343 -> 216 -> 125 -> 64 -> 27 -> 8 -> 1 -> 0

    Testcase : #2
        Enter Input : -123 456 -789 0 27 3645 133 -142 -5038594 15615 668 2 -1 72
        ------------------------------------------------------------
        Round : 1
        0 : 0 
        1 : -1 
        2 : 72 2 -142 
        3 : 133 -123 
        4 : -5038594 
        5 : 15615 3645 
        6 : 456 
        7 : 27 
        8 : 668 
        9 : -789 
        ------------------------------------------------------------
        Round : 2
        0 : 2 0 -1 
        1 : 15615 
        2 : 27 -123 
        3 : 133 
        4 : 3645 -142 
        5 : 456 
        6 : 668 
        7 : 72 
        8 : -789 
        9 : -5038594 
        ------------------------------------------------------------
        Round : 3
        0 : 72 27 2 0 -1 
        1 : 133 -123 -142 
        2 : 
        3 : 
        4 : 456 
        5 : -5038594 
        6 : 15615 3645 668 
        7 : -789 
        8 : 
        9 : 
        ------------------------------------------------------------
        Round : 4
        0 : 668 456 133 72 27 2 0 -1 -123 -142 -789 
        1 : 
        2 : 
        3 : 3645 
        4 : 
        5 : 15615 
        6 : 
        7 : 
        8 : -5038594 
        9 : 
        ------------------------------------------------------------
        Round : 5
        0 : 3645 668 456 133 72 27 2 0 -1 -123 -142 -789 
        1 : 15615 
        2 : 
        3 : -5038594 
        4 : 
        5 : 
        6 : 
        7 : 
        8 : 
        9 : 
        ------------------------------------------------------------
        Round : 6
        0 : 15615 3645 668 456 133 72 27 2 0 -1 -123 -142 -789 -5038594 
        1 : 
        2 : 
        3 : 
        4 : 
        5 : 
        6 : 
        7 : 
        8 : 
        9 : 
        ------------------------------------------------------------
        5 Time(s)
        Before Radix Sort : -123 -> 456 -> -789 -> 0 -> 27 -> 3645 -> 133 -> -142 -> -5038594 -> 15615 -> 668 -> 2 -> -1 -> 72
        After  Radix Sort : 15615 -> 3645 -> 668 -> 456 -> 133 -> 72 -> 27 -> 2 -> 0 -> -1 -> -123 -> -142 -> -789 -> -5038594
'''

class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = node()

    def __str__(self):
        return " -> ".join(str(i) for i in self.display())

    def addList(self,data):
        self.head = node()
        for i in data:
            self.append(i)

    def append(self,data):
        new_node,cur = node(data),self.head
        while cur.next != None:
            cur = cur.next
        new_node.prev = cur
        cur.next = new_node

    def display(self):
        elems,cur = [],self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems

    def lenght(self):
        cur,total = self.head,0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def sort(self):
        cur = self.display()
        ls,strList = [],[]
        for i in cur:
            ls.append(int(i))
        ls = sorted(ls)
        ls.reverse()
        for i in ls:
            strList.append(str(i))
        self.addList(strList)

def getDigit(pos,data): #return int from round position
    pos = pos*-1
    try:
        digit = data[pos]
        return int(digit) if digit != '-' else 0
    except IndexError:
        return 0

def redixSort(useList):
    round,nInput = 0,len(useList)
    subList = list(LinkedList() for _ in range(10))
    while True:
        round += 1
        for i,data in enumerate(useList):
            num = getDigit(round,data)
            for j in range(10):
                if num == j:
                    subList[j].append(data)
                    break

        #sub-sorted
        for i in range(10):
            subList[i].sort()
            
        print('------------------------------------------------------------')
        print('Round :',round)

        for i,data in enumerate(subList):
            print(i,':',' '.join(data.display()))

        useList = []
        for i in subList:                               #update data from round sort
            for j in i.display():
                useList.append(j)
        if subList[0].lenght() == nInput: 
            break   
        subList = list(LinkedList() for _ in range(10)) #Clear sub list
        
    return round-1,useList


inp = input('Enter Input : ').split()
round,result = redixSort(inp)
print('------------------------------------------------------------')
print(round,'Time(s)')
print('Before Radix Sort :',' -> '.join(inp))
print('After  Radix Sort :',' -> '.join(result))