'''
Chapter : 7 - item : 3 - Less Than or Equal
ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k

    Testcase : #1
        Enter Input : 10 4 20 1 5/4
            20
        10
                5
            4
                1
        --------------------------------------------------
        2

    Testcase : #2
        Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100/-101
                        100
                75
                        62
            50
                        28
                25
                        13
        0
                        -13
                -25
                        -38
            -50
                        -62
                -75
                        -100
        --------------------------------------------------
        0
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
num = []
inp = []
T = BST()
S = BST()
count = 0
num = input('Enter Input : ').split('/')
inp = [int(i) for i in num[0].split()]
mask = int(num[1])

for i in inp:
        if i <= mask:
                count+=1
        root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(count)