class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.index = None
        self.level = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 1

    def setCount(self,count):
        if count > 5:
            for i in range(count//2):
                self.blank('blank',i+1)
        else:
            self.root = Node('blank')
            self.root.level = 1
            self.root.index = 1
            self.count +=1
            self.root.left = Node('blank')
            self.root.left.level = self.root.level+1
            self.root.left.index = self.count 
            self.root.right = Node('blank')
            self.count +=1
            self.root.right.level = self.root.level+1
            self.root.right.index = self.count 

            if count == 5:
                nodeLeft = self.root.left
                nodeLeft.left = Node('blank')
                self.count +=1
                nodeLeft.left.index = self.count 
                nodeLeft.left.level = 2
                nodeLeft.right = Node('blank')
                self.count +=1
                nodeLeft.right.index = self.count 
                nodeLeft.right.level = 2

    def blank(self, data,index):
        if index == 1: 
            self.root = Node('blank')
            self.root.index = 1
            self.root.level = 0
        else: 
            Q = [] 
            Q.append(self.root)     
            while len(Q) != 0:
                curr = Q.pop(0)
                if curr.left is None:
                    curr.left = Node(data)
                    self.count +=1
                    curr.left.parent = curr
                    curr.left.index = self.count
                    curr.left.level = curr.level + 1
                else: 
                    Q.append(curr.left)

                if curr.right is None:
                    curr.right = Node(data)
                    self.count += 1
                    curr.right.parent = curr
                    curr.right.index = self.count
                    curr.right.level = curr.level + 1
                else: 
                    Q.append(curr.right)

    def insertAt(self,data,index):
        Q = []
        Q.append(self.root)
        while len(Q) != 0:
            curr = Q.pop(0)
            if curr.left is not None:
                if curr.left.index == index: 
                    currentLevel = curr.left.level
                    curr.left = Node(data)
                    curr.left.index = index
                    curr.left.parent = curr
                    curr.left.level = currentLevel
                    break
                else: 
                    Q.append(curr.left)
            if curr.right is not None:
                if curr.right.index == index: 
                    currentLevel = curr.right.level
                    curr.right = Node(data)
                    curr.right.index = index
                    curr.right.parent = curr
                    curr.right.level = currentLevel
                    break
                else: 
                    Q.append(curr.right)
        
    def setLevel(self,level):
        minData = 0
        if self.count < 6:
            if self.count == 5 and level == 0:
                if self.root.left.left.data < self.root.left.right.data: minData = self.root.left.left.data
                else: minData = self.root.left.right.data 
                self.root.left.data = minData
                self.root.left.left.data -= minData
                self.root.left.right.data -= minData
                if self.root.left.data < self.root.right.data: minData = self.root.left.data
                else: minData = self.root.right.data
                self.root.data = minData
                self.root.left.data -= minData
                self.root.right.data -= minData
            elif self.count == 3 and level == 0:
                if self.root.left.data < self.root.right.data: minData = self.root.left.data
                else: minData = self.root.right.data
                self.root.data = minData
                self.root.left.data -= minData
                self.root.right.data -= minData
        else:
            Q = []
            Q.append(self.root)
            minData = 0
            while len(Q) != 0:
                curr = Q.pop(0)
                if curr.left is not None or curr.right is not None:
                    if level == curr.level + 1:
                        if curr.left.data < curr.right.data: 
                            minData = curr.left.data
                        else: 
                            minData = curr.right.data
                if curr.left is not None:
                    if curr.left.level == level:
                        index = curr.left.index
                        curr.data = minData
                        left = curr.left.left
                        right = curr.left.right
                        curr.left = Node(curr.left.data-minData)
                        curr.left.index = index
                        curr.left.level = level
                        curr.left.parent = curr
                        curr.left.left = left
                        curr.left.right = right 
                    else: 
                        Q.append(curr.left)
                if curr.right is not None:
                    if curr.right.level == level:
                        index = curr.right.index
                        curr.data = minData
                        left = curr.right.left
                        right = curr.right.right
                        curr.right = Node(curr.right.data-minData)
                        curr.right.left = left
                        curr.right.right = right 
                        curr.right.index = index
                        curr.right.level = level
                        curr.right.parent = curr
                    else: 
                        Q.append(curr.right)

    def countNode(self,node):
        Q = [] 
        count = node.data
        Q.append(self.root)     
        while len(Q) != 0:
            curr = Q.pop(0) 
            if curr.left is not None: 
                count += curr.left.data
                Q.append(curr.left)
            if curr.right is not None: 
                count += curr.right.data
                Q.append(curr.right)
        return count

T = BST()
inp = input('Enter Input : ').split('/')
inp[1] = [int(i) for i in inp[1].split()]
if int(inp[0]) < 3 or int(inp[0]) % 2 == 0 or len(inp[1]) != (int(inp[0]) // 2 + 1): 
    print('Incorrect Input')
else: 
    T.setCount(int(inp[0]))
    for i in range(int(inp[0])-len(inp[1])+1):
        T.insertAt(inp[1][i],int(inp[0])-len(inp[1])+i+1) 
    for i in range(int(inp[0])-len(inp[1])):
        T.setLevel(int(inp[0])-len(inp[1])-1-i)
    print(T.countNode(T.root))