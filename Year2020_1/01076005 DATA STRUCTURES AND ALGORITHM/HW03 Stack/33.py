class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop(-1)
    def size(self):
        return len(self.items)
    def show(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []  

def CheckOperator(a, b):
    oper = '()+-*/^'
    try:
        return oper.index(a) // 2 >= oper.index(b) // 2
    except ValueError:  
        return False          

inp = input("Enter Infix : ")
st = Stack()

postfix = ""
for i in inp:
    if i in '()+-*/^':
        if i == '(':
            st.push(i)
        elif i == ')':
            while st.show() != '(':
                postfix += st.pop()
            st.pop()    
        elif i in '+-*/^':
            if st.isEmpty():
                st.push(i)
            else:
                while st.size() != 0 and CheckOperator(st.show(), i):
                    postfix += st.pop()
                st.push(i)                  
    else:
        postfix += i    

for k in range(st.size()):
        postfix += st.pop()


print("Postfix : " + postfix)