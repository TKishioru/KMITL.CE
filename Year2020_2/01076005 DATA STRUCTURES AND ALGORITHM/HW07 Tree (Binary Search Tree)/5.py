'''
Chapter : 7 - item : 5 - Expression Tree
ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

    Testcase : #1
        Enter Postfix : ab+cde+**
        Tree :
                        e
                +
                        d
            *
                c
        *
                b
            +
                a
        --------------------------------------------------
        Infix : ((a+b)*(c*(d+e)))
        Prefix : *+ab*c+de

    Testcase : #2
        Enter Postfix : abc*+de*f+g*+
        Tree :
                g
            *
                        f
                +
                            e
                        *
                            d
        +
                        c
                *
                        b
            +
                a
        --------------------------------------------------
        Infix : ((a+(b*c))+(((d*e)+f)*g))
        Prefix : ++a*bc*+*defg

    Testcase : #3
        Enter Postfix : ab+c*de-fg+*-
        Tree :
                        g
                +
                        f
            *
                        e
                -
                        d
        -
                c
            *
                        b
                +
                        a
        --------------------------------------------------
        Infix : (((a+b)*c)-((d-e)*(f+g)))
        Prefix : -*+abc*-de+fg
'''
text_in = "Infix : "
text_pre = "Prefix : "

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            root = self.root
            while True:
                if data < root.data:
                    if root.left is None:
                        root.left = Node(data)
                        break
                    root = root.left
                else:
                    if root.right is None:
                        root.right = Node(data)
                        break
                    root = root.right
        return self.root
    def num_multi(self, k, multi): 
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            T = q.dequeue()
            if T.data > k:
                T.data = T.data*multi
            if T.left is not None:
                q.enqueue(T.left)
            if T.right is not None:
                q.enqueue(T.right)
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
def inorder(T):
    global text_in
    if T is not None:
        if T.left is not None or T.right is not None:  
            text_in += "("
        inorder(T.left)
        text_in += str(T.data)
        inorder(T.right)
        if T.left is not None or T.right is not None: 
            text_in += ")"
def preorder(T):
    global text_pre
    if T is not None:
        text_pre += str(T.data)
        preorder(T.left)
        preorder(T.right)

inp = input("Enter Postfix : ")
T = BST()
s = Stack()
for character in inp:
    if character in '+-*/':
        op1 = s.pop()
        op2 = s.pop()
        s.push(Node(character, op2, op1))
    else:
        s.push(Node(character))
print("Tree :")
T.root = s.pop()
T.printTree(T.root)
print("--------------------------------------------------")
inorder(T.root)
print(text_in)
preorder(T.root)
print(text_pre)
