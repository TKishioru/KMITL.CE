'''
Chapter : 7 - item : 4 - สนุกไปกับ Binary Search Tree
ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ

    Testcase : #1
        Enter Input : 10 4 20 1 5
        Preorder : 10 4 1 5 20 
        Inorder : 1 4 5 10 20 
        Postorder : 1 5 4 20 10 
        Breadth : 10 4 20 1 5 

    Testcase : #2
        Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100
        Preorder : 0 -50 -75 -100 -62 -25 -38 -13 50 25 13 28 75 62 100 
        Inorder : -100 -75 -62 -50 -38 -25 -13 0 13 25 28 50 62 75 100 
        Postorder : -100 -62 -75 -38 -13 -25 -50 13 28 25 62 100 75 50 0 
        Breadth : 0 -50 50 -75 -25 25 75 -100 -62 -38 -13 13 28 62 100 
'''
text_pre = "Preorder : "
text_in = "Inorder : "
text_post = "Postorder : "
text_pr = "Breadth : "

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            T = self.root
            while True:
                if data < T.data:
                    if T.left is None:
                        T.left = Node(data)
                        break
                    T = T.left
                else:
                    if T.right is None:
                        T.right = Node(data)
                        break
                    T = T.right
        return self.root
    
    def printTree(self, node, level = 0):
        global text_curr
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
def preorder(root):
    global text_pre  
    if root:  
        text_pre += str(root.data) + " "
        preorder(root.left)  
        preorder(root.right)  
def inorder(root):  
    global text_in
    if root:  
        inorder(root.left)  
        text_in += str(root.data) + " "
        inorder(root.right)  
def postorder(root):  
    global text_post
    if root:  
        postorder(root.left)   
        postorder(root.right)
        text_post += str(root.data) + " "
def bread(root):
    global text_pr
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        dQ = q.dequeue()
        text_pr += str(dQ.data) + ' '
        if dQ.left is not None:
            q.enqueue(dQ.left)
        if dQ.right is not None:
            q.enqueue(dQ.right)
    return text_pr

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
preorder(T.root)
print(text_pre)
inorder(T.root)
print(text_in)
postorder(T.root)
print(text_post)
bread(T.root)
print(text_pr)
