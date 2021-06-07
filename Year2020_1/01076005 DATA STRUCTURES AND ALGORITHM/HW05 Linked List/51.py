class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for item in lst:
                self.push_back(item)

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

    def push_front(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            buf = Node(value, self.head)
            self.head.prev = buf
            self.head = buf

    def push_back(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            self.tail.next = Node(value, prev =self.tail)
            self.tail = self.tail.next

    def is_in(self, value):
        if self.isEmpty():
            return False
        buf = self.head
        while buf is not None:
            if buf.val == value:
                return True
            buf = buf.next
        return False

    def index(self):
        pass

    def pop_back(self):
        if self.isEmpty():
            print('List is empty')
            return -1
        last = self.tail
        self.tail = last.prev
        if self.tail is not None:
            self.tail.next = None
        last.prev = None
        if self.tail is None: 
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
            print('Empty linked list')
        if rev:
            buf = self.tail
            out = 'The reversed list contains :'
            while buf is not None:
                out += ' ' + str(buf.val)
                buf = buf.prev
            print(out)
        else:
            buf = self.head
            out = 'The list contains :'
            while buf is not None:
                out += ' ' + str(buf.val)
                buf = buf.next
            print(out)

    def remove(self, value):
        if self.isEmpty() or not self.is_in(value):
            print("Value not found in list")
            return -1
        else:
            buf = self.head
            while buf is not None:
                if buf.val == value:
                    break
                buf = buf.next
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
                    next.prev = prev
                return val

    def insert(self, index, value):  
        if 0 <= index <= self.size():
            if index == 0:
                print(f"index = {index} and data = {value}")
                self.push_front(value)
            elif index == self.size():
                print(f"index = {index} and data = {value}")
                self.push_back(value)
            else:
                print(f"index = {index} and data = {value}")
                count = 0
                buf = self.head
                while buf is not None and count != index:
                    buf = buf.next
                    count += 1
                prev = buf.prev
                new = Node(value, buf, prev)
                prev.next = new
                buf.prev = new
        else:
            print('Data cannot be added')

    def __str__(self):
        if self.isEmpty():
            return 'List is empty'
        else:
            buf = self.head
            out = 'link list : '
            while buf is not None:
                out += str(buf.value)
                if buf.next is not None:
                    out += '->'
                buf = buf.next
            return out

class Node:
    def __init__(self, value, next = None, prev =None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


inp = input('Enter Input : ').split(',')
lst = inp[0].split()
insert = list(map(lambda text: text.strip(), inp[1:]))
l = LinkedList(lst)
print(l)
for items in insert:
    pos, val = items.split(':')
    pos = int(pos)
    val = int(val)

    l.insert(pos, val)
    print(l)

