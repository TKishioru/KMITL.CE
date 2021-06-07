#ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree
#***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()

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

    def maxTree(self):
        if self.root is None:
            return
        T = self.root
        while T.right is not None:
            T = T.right
        return T.data

    def minTree(self):
        if self.root is None:
            return
        T = self.root
        while T.left is not None:
            T = T.left
        return T.data

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min :", T.minTree())
print("Max :", T.maxTree())