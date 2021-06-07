#by Bassilism
'''
Chapter : 5 - item : 2 - Doubly Linked List(append,insert,remove)
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า

4. def isEmpty(self): return list นั้นว่างหรือไม่

5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

6. def insert(self, index, data): insert data ใน index ที่กำหนด

7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append       ->  A
2. add_before   ->  Ab
3. insert       ->  I
4. remove       ->  R

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    Testcase : #1 1
        Enter Input : A 3,A 4,Ab 0,I 1:2
        linked list : 3
        reverse : 3
        linked list : 3->4
        reverse : 4->3
        linked list : 0->3->4
        reverse : 4->3->0
        index = 1 and data = 2
        linked list : 0->2->3->4
        reverse : 4->3->2->0

    Testcase : #2 2
        Enter Input : I -1:0,I 10:10,I 0:0
        Data cannot be added
        linked list : 
        reverse : 
        Data cannot be added
        linked list : 
        reverse : 
        index = 0 and data = 0
        linked list : 0
        reverse : 0
'''
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += '->' + str(cur.next.value)
            cur = cur.next
        return s

    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur, s = self.tail, str(self.tail.value)
        while cur.prev != None:
            s += '->' + str(cur.prev.value)
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return

        self._size += 1
        cur = self.head
        while(cur.next != None):
            cur = cur.next
        node = Node(item)
        node.prev, cur.next, self.tail  = cur, node, node

    def add_before(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return

        node = Node(item)
        if self.size() == 1:
            node.next, self.tail.prev, self.head  = self.tail, node, node
        else:
            node.next, self.head.prev, self.head = self.head, node, node
        self._size += 1
    
    def insert(self, pos, item):
        if pos > self.size() or pos < 0:
            return print('Data cannot be added')

        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return print(f'index = {pos} and data = {item}')

        node = Node(item)
        if pos == 0:
            self._size += 1
            node.next, self.head.prev, self.head = self.head, node, node
            return print(f'index = {pos} and data = {item}')

        if pos == self.size():
            self._size += 1
            node.prev, self.tail.next, self.tail = self.tail, node, node
            return print(f'index = {pos} and data = {item}')

        cur, index = self.head, 0
        while index != pos-1:
            index += 1
            cur = cur.next
        
        cur.next.prev = node
        node.next = cur.next
        node.prev = cur
        cur.next = node
        self._size += 1

        return print(f'index = {pos} and data = {item}')

    def size(self):
        return self._size

    def remove(self, item):
        if self.isEmpty():
            return print("Not Found!")

        cur = self.head
        if self.size() == 1 and cur.value == item:
            self.head = self.tail = None
            self._size -= 1
            return print(f'removed : {item} from index : 0')

        self._size -= 1
        if item == self.head.value:
            self.head = self.head.next
            self.head.prev = None
            return print(f'removed : {item} from index : 0')

        index = 0
        while cur.next != None:
            if cur.value == item:
                cur.prev.next, cur.next.prev = cur.next, cur.prev
                return print(f'removed : {item} from index : {index}')
            index += 1
            cur = cur.next
        if cur.value == item:
            self.tail = self.tail.prev
            self.tail.next = None
            return print(f'removed : {item} from index : {index}')
        self._size += 1
        return print("Not Found!")

inp = input('Enter Input : ').split(',')

L = LinkedList()
for data in inp:
    data = data.split()
    if data[0] == 'A':
        L.append(data[1])
    elif data[0] == 'Ab':
        L.add_before(data[1])
    elif data[0] == 'I':
        L.insert(int(data[1].split(':')[0]), data[1].split(':')[1])
    else:
        L.remove(data[1])
    print('linked list :', L)
    print('reverse :', L.str_reverse())