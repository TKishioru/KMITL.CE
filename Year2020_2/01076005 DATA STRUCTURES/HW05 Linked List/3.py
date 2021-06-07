#By ApexTone.
'''
Chapter : 5 - item : 3 - รวม Linked List
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง

    Testcase : #1
        Enter Input (L1,L2) : 1 2
        L1    : 1 
        L2    : 2 
        Merge : 1 2 

    Testcase : #2
        Enter Input (L1,L2) : 1->2->3 4->5
        L1    : 1 2 3 
        L2    : 4 5 
        Merge : 1 2 3 5 4 

    Testcase : #3
        Enter Input (L1,L2) : I->Love->KMITL Datastruct->and
        L1    : I Love KMITL 
        L2    : Datastruct and 
        Merge : I Love KMITL and Datastruct 
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):         #สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
        self.head = None

    def __str__(self):          #คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    def isEmpty(self):          #เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
        if self.head is None:
            return True
        return False
    def append(self, item):     #add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node

l = LinkedList()
L1,L2 = input('Enter Input (L1,L2) : ').split()
txt1 = L1.split('->')
s = 'L1    : '
for i in range(0,len(txt1)):
    s += txt1[i] + ' '
    l.append(txt1[i])
print(s)
txt2 = L2.split('->')
s = 'L2    : '
for i in range(0,len(txt2)):
    s += txt2[i] + ' '
for i in range(len(txt2)-1,-1,-1):
    l.append(txt2[i])
print(s)
print('Merge :' , l)
