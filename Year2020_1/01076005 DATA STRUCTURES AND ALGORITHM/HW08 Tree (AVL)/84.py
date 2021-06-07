class BST:
    def __init__(self, lst1 = None):
        if lst1 is None:
            self.item = []
        else:
            self.item = lst1

    def __str__(self):
        return str(self.item)

    def size(self):
        return len(self.item)

    def LC(self, index):
        left = index*2+1
        return left if left < self.size() else -1

    def RC(self, index):
        right = index*2+2
        return right if right < self.size() else -1

    def sum(self, num = 0):
        S = []
        count = 0
        S.append(num)
        while len(S) > 0:
            POP = S.pop(0)
            if 0 <= POP < self.size():
                count += self.item[POP]
                L = self.LC(POP)
                R = self.RC(POP)
                if L != -1:
                    S.append(L)
                if R != -1:
                    S.append(R)
        return count

    def compare(self, x, y):
        X = self.sum(x)
        Y = self.sum(y)
        if X > Y:
            print(f'{x}>{y}')
        elif X < Y:
            print(f'{x}<{y}')
        else:
            print(f'{x}={y}')


inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
T = BST(lst)
oper = inp[1].split(',')
print(T.sum())
for i in oper:
    x, y = tuple(map(int, i.split()))
    T.compare(x, y)