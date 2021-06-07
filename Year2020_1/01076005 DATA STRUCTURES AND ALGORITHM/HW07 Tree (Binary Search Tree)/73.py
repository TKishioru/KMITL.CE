#ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

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
num = input('Enter Input : ').split('/')
inp = [int(i) for i in num[0].split()]
mask = int(num[1])

for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
for i in inp:
    if i > mask:
        i *= 3
    new = S.insert(i)
S.printTree(new)
