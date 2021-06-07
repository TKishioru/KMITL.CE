"""
Chapter : 3 - item : 4 - Stack Calculator
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
    +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
    -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
    *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
    /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
    DUP: Duplicate (not double) ค่าบนสุดของ stack
    POP: Pop ค่าบนสุดออกจาก stack และ discard.
    PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************

    Testcase : #1
        * Stack Calculator *
        Enter arguments : 5 6 +
        11

    Testcase : #2
        * Stack Calculator *
        Enter arguments : 3 DUP +
        6

    Testcase : #3
        * Stack Calculator *
        Enter arguments : 6 5 5 7 * - /
        5

    Testcase : #4
        * Stack Calculator *
        Enter arguments : a b c +
        Invalid instruction: a

"""
class StackCalc:
    def __init__(self):    #ใช้สำหรับสร้าง list ว่าง
        self.items = []
        self.s = ''
    def isEmpty(self):     #ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        if len(self.items) != 0:
            return False
        return True
    def size(self):        #ตรวจสอบจำนวนข้อมูลใน stack
        return len(self.items)
    def run(self,arg):
        for i in range(0,len(arg)):
            if arg[i].isnumeric():          #แทนฟังก์ชั่น PSH
                self.items.append(int(arg[i]))
            elif arg[i] in '+-*/':
                if arg[i] == '+':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(x+y)
                elif arg[i] == '-':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(x-y)
                elif arg[i] == '*':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(x*y)
                elif arg[i] == '/':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(int(x/y))
            elif arg[i] == 'DUP':           #Duplicate (not double) ค่าบนสุดของ stack
                self.items.append(int(self.items[-1]))
            elif arg[i] == 'POP':           #Pop ค่าบนสุดออกจาก stack และ discard.
                self.items.pop()
            #elif arg[i] == 'PSH':           #ทำการ push ตัวเลขลง stack
                #self.items.append(arg[i])
            else:
                self.s = "Invalid instruction: " + arg[i]
                break
    def getValue(self):
        if len(self.items):
            return self.items[-1]
        elif len(self.s):
            return self.s
        else:
            return "0"

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())