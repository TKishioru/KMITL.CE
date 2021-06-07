class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)
        if cur.next != None :
            s += "->"
        while cur.next != None:
            s += str(cur.next.value)
            if cur.next.next != None :
                s += "->"
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty() :
            self.head = Node(item)
        else :
            t = self.head
            while t.next :
                t = t.next
            t.next = Node(item)

    def addHead(self, item):
        h = Node(item)
        h.next = self.head
        self.head = h

    def index(self, item):
        itr = self.head
        i = 0
        while itr :
            if str(itr.value) == str(item) :
                return i
            itr = itr.next
            i += 1
        return -1

    def size(self):
        itr = self.head
        i = 0
        while itr :
            itr = itr.next
            i += 1
        return i

    def pop(self, pos) :
        if self.isEmpty() :
            return None
        if pos == 0 :
            self.head = self.head.next
            return "Success"
        itr = self.head
        i = 0
        while itr.next :
            if i + 1 == pos :
                v = itr.next.value
                if itr.next.next == None :
                    itr.next = None
                else :
                    itr.next = itr.next.next
                return v
            itr = itr.next
            i += 1
        return "Out of Range"

    def setNode(self, index1, index2) :
        if self.isEmpty() :
            return "Error! {list is empty}"
        if index1 + 1 > self.size() :
            return "Error! {index not in length}: " + str(index1)
        if index2 + 1 > self.size() :
            self.append(str(index2))
            return "index not in length, append : " + str(index2)
        n1 = Node(None)
        n2 = Node(None)
        itr = self.head
        s = "Set node.next complete!, index:value = " + str(index1) + ":"
        while itr :
            if index1 == 0 :
                n1 = itr
                s += str(n1.value) + " -> " + str(index2) + ":"
            index1 -= 1
            itr = itr.next
        itr = self.head
        while itr :
            if index2 == 0 :
                n2 = itr
                s += str(n2.value)
            index2 -= 1
            itr = itr.next
        n1.next = n2
        return s

    def isLoop(self) :
        if self.isEmpty() :
            return False
        idList = []
        itr = self.head
        while itr.next :
            if id(itr) in idList :
                return True
            idList.append(id(itr))
            itr = itr.next
        return False

x = input("Enter input : ").split(",")
L = LinkedList()
for i in x :
    if i[0] == 'A' :
        L.append(i[2:])
        print(L)
    elif i[0] == 'S' :
        x1, x2 = [int(a) for a in i.split()[1].split(":")]
        print(L.setNode(x1, x2))
if L.isLoop() :
    print("Found Loop")
else :
    print("No Loop")
    print(L)