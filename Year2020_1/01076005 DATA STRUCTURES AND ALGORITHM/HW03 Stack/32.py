class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return (999999999, 0)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return (999999999, 0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':
    dishes = input('Enter Input : ').split(',')
    s = Stack()
    for i in range(0, len(dishes)):
        weight, frequency = map(int, dishes[i].split())
        if s.is_empty():
            s.push((weight, frequency))
        else:
            while weight > s.peek()[0]:
                dish = s.pop()
                print(dish[1])
            s.push((weight, frequency))



##ทำเอง
class Stack:

     def __init__(self):
        self.items = []

     def is_empty(self):
        return len(self.items) == 0

     def push(self, item):
        self.items.append(item)

     def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
        else:
            return 0

     def peek(self):
        if not self.is_empty():
           return self.items[-1]
        else:
           return 0

if __name__ == "__main__":
    inp = input("Enter Input : ").split(',')
    s = Stack()
    i = 0
    ins = []
    re = []
    re1 = []
    for i in range(len(inp)):
        weight,freq = map(int,inp[i].split())
        if s.is_empty():
            s.push((weight,freq))
        else:
            
            if weight >= s.peek()[0]:
               ins = s.pop()
               s.push((ins[0],ins[1]))  
               if weight!=s.peek()[0]:
                  print(ins[1])  
               if re==s.peek()[0]:
                  print(re1)    
               if weight==s.peek()[0]:
                  re,re1=ins 
               s.pop()
            s.push((weight,freq))
