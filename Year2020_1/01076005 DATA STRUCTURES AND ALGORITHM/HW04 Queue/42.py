class Queue:
    def __init__(self):
        self.items = list()
    def enqueue(self, value):
        self.items.append(value)
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return -1
    def cut_in(self, value):
        if self.is_empty():
            self.items.append(value)
        elif self.peek()[0] == 'EN':
            self.items.insert(0, value)
        else:
            for i in range(self.size()):
                if self.items[i][0] == 'EN':
                    self.items.insert(i, value)
                    return
            self.items.append(value)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return -1
    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output

inp = input('Enter Input : ').split(',')
q = Queue()
for i in inp:
    show = i.split()
    if len(show) == 1:
        if not q.is_empty():
            print(q.dequeue()[1])
        else:
            print('Empty')
    else:
        if show[0] == 'EN':
            q.enqueue((show[0], show[1]))
        elif show[0] == 'ES':
            q.cut_in((show[0], show[1]))