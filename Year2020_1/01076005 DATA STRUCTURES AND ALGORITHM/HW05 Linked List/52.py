class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for item in lst:
                self.p_back(item)

    def isEmpty(self):
        return self.head is None or self.tail is None  

    def size(self):
        buf = self.head
        count = 0
        while buf is not None:
            count += 1
            buf = buf.next
        return count

    def __len__(self):
        return self.size()

    def p_front(self, val):
        if self.isEmpty():
            self.head = Node(val)
            self.tail = self.head
            return
        else:
            buf = Node(val, self.head)
            self.head.prev = buf
            self.head = buf

    def p_back(self, val):
        if self.isEmpty():
            self.head = Node(val)
            self.tail = self.head
            return
        else:
            new = Node(val, prev=self.tail)
            self.tail.next = new
            self.tail = new

    def is_in(self, val):
        if self.isEmpty():
            return 'Not Found'
        buf = self.head
        while buf is not None:
            if buf.val == val:
                return 'Found'
            buf = buf.next
        return 'Not Found'

    def index(self, val):
        buf = self.head
        count = 0
        while buf is not None:
            if buf.val == val:
                return count
            count += 1
            buf = buf.next
        return -1

    def pop_back(self):
        if self.isEmpty():
            print('List is empty')
            return -1
        last = self.tail
        self.tail = last.prev
        if self.tail is not None:
            self.tail.next = None
        last.prev = None
        if self.tail is None:  # list is now empty
            self.head = None
        return last.val

    def pop_front(self):
        if self.isEmpty():
            print('List is empty')
            return -1
        first = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        first.next = None
        return first.val

    def traverse(self, rev=False):
        if self.isEmpty():
            out = 'Empty'
            return out
        if rev:
            buf = self.tail
            out = ''
            while buf is not None:
                out += str(buf.val) + ' '
                buf = buf.prev
        else:
            buf = self.head
            out = ''
            while buf is not None:
                out += str(buf.val) + ' '
                buf = buf.next
        return out

    def remove(self, val):
        if self.isEmpty() or not self.is_in(val):
            print("Value not found in list")
            return -1
        else:
            buf = self.head
            while buf is not None:
                if buf.val == val:
                    break
                buf = buf.next_node
            if buf is self.head:
                return self.pop_front()
            elif buf is self.tail:
                return self.pop_back()
            else:
                prev = buf.prev
                next = buf.next
                val = buf.val
                buf.prev = None
                buf.next = None
                if prev is not None:
                    prev.next = next
                if next is not None:
                    next.prev= prev
                return val

    def pop(self, pos):
        if self.isEmpty() or not (0 <= pos <= self.size()-1):
            return 'Out of Range'
        else:
            if pos == 0:
                self.pop_front()
            elif pos == self.size()-1:
                self.pop_back()
            else:
                buf = self.head
                count = 0
                while buf is not None and count != pos:
                    count += 1
                    buf = buf.next
                prev = buf.prev
                next = buf.next
                buf.prev = None
                buf.next = None
                if prev is not None:
                    prev.next = next
                if next_node is not None:
                    next_node.prev = prev
            return 'Success'

    def insert(self, index, val): 
        if index == 0 or self.isEmpty():
            self.p_front(val)
        elif index >= self.size():
            self.p_back(val)
        elif index < 0: 
            index = abs(index)
            count = 0
            buf = self.tail
            while buf is not None and count < index:
                
                buf = buf.prev
                count += 1
            if buf is None:
                self.p_front(val)
            else:
                
                next = buf.next
                new = Node(val, next, buf)
                buf.next = new
                next.prev = new
        else:  
            count = 0
            buf = self.head
            while buf is not None and count != index:
                buf = buf.next
                count += 1
            prev = buf.prev
            new = Node(val, buf, prev)
            prev.next = new
            buf.prev = new

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        else:
            buf = self.head
            out = ''
            while buf is not None:
                out += str(buf.val) + ' '
                buf = buf.next
            return out



L = LinkedList()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AP":
        L.p_back(i[3:])
    elif i[:2] == "AH":
        L.p_front(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.is_in(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.traverse(rev=True))
