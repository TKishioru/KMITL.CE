"""
Chapter : 3 - item : 3 - Postfix Calculator
จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 

    Testcase : #1
        ***Postfix expression calcuation***
        Enter Postfix expression : 6 5 2 3 + 8 * - 3 + *
        Answer :  -192.00

    Testcase : #2
        ***Postfix expression calcuation***
        Enter Postfix expression : 4 22 * 89 / 98 * 21 - 32 2 / 4 * 10 / 23 * + 23 -48 * -
        Answer :  1327.10

    Testcase : #3
        ***Postfix expression calcuation***
        Enter Postfix expression : 5 8 * 5 6 * 6 6 4 * - 5 6 * 6 / + - -
        Answer :  -3.00

    Testcase : #4
        ***Postfix expression calcuation***
        Enter Postfix expression : 3 8 2 / 6 * 5 6 - + 6 6 -5 5 * 2 - - + + +
        Answer :  65.00

"""
class Stack():

    def __init__(self, ls = None):  #ใช้สำหรับสร้าง list ว่าง
        self.ls = []
    def push(self,i):
        self.ls.append(i)
    def pop(self):
        if len(self.ls) != 0:
            return self.ls.pop()
        return 0
    def isEmpty(self):              #ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        if len(self.ls) != 0:
            return False
        return True
    def size(self):                 #ตรวจสอบจำนวนข้อมูลใจ stack
        return len(self.ls)

txt = list()
def postFixeval(st):
    s = Stack()
    for i in range(0,len(st)):
        #print(txt)
        if st[i] in '+-*/':
            if st[i] == '+':
                x = s.pop()
                y = s.pop()
                ans = x + y
                s.push(ans)
            elif st[i] == '-':
                x = s.pop()
                y = s.pop()
                ans = y-x
                s.push(ans)
            elif st[i] == '*':
                x = s.pop()
                y = s.pop()
                ans = x*y
                s.push(ans)
            elif st[i] == '/':
                x = s.pop()
                y = s.pop()
                ans = y/x
                s.push(ans)
        else:
            #txt.append(int(st[i]))
            s.push(int(st[i]))
    return s.pop()
    
print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))