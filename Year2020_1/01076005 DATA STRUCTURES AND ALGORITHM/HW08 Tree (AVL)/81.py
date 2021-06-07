class Node:
    def __init__(self, data, freq, left = None, right = None):
        self.data = data 
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class Huffman:
    def __init__(self):
        self.root = None

    def out(self, node):
        if not node:
            return []
        st = self.out(node.right) + [Node(node.data, node.freq)] + self.out(node.left)
        return st

    def insert(self, node, data, freq):
        if not node:
            return Node(data, freq)
        elif freq == node.freq:
            if data < node.data:
                node.left = self.insert(node.left, data, freq)
            else:
                node.right = self.insert(node.right, data, freq)
        elif freq < node.freq:
            node.left = self.insert(node.left, data, freq)
        else:
            node.right = self.insert(node.right, data, freq)
        return node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def haffC(node, code):
    s = ''
    if node:
        s = haffC(node.right, code + '1')
        if node.data != '*':
            s += "'" + str(node.data) + "': '" + code + "'";
        a = haffC(node.left, code + '0')
        if a != '':
            s += ', ' + a
    return s

def search(node, data, code): 
    if not node:
        return None
    if data == node.data:
        return code
    if node:
        s = search(node.right, data, code + '1')
        if s != None:
            return s
        s = search(node.left, data, code + '0')
        return s


inp = list(input('Enter Input : '))
S = set(inp)
H = Huffman()

for data in S:
    H.root = H.insert(H.root, data, inp.count(data))

data = H.out(H.root)
dP = [data.pop()]

while len(data) != 0 or len(dP) != 1:
    if len(dP) > 1:
        if data == [] or (data[-1].freq >= dP[0].freq + dP[1].freq):
            a, b =  dP.pop(0), dP.pop(0)
            dP.append(Node('*', a.freq + b.freq, a, b))
        else:
            dP.append(data.pop())
    else:
        dP.append(data.pop())

print('{' + f'{haffC(dP[0], "")}' + '}')
printTree90(dP[0])

print('Encoded! : ', end = '')
for i in inp:
    print(search(dP[0], i, ''), end = '')