#โจทย์ให้ทำคลาสที่สามารถบวกเลขได้ และเปลี่ยนเป็นเลขโรมันได้

class MyInt:
    def __init__(self, num):
        self.num = num
    def toRoman(self):
        cal = self.num
        rm = ''
        while cal >= 1000:  #"M" = 1000
            rm += 'M'
            cal -= 1000
        while cal >= 900:   #"CM" = 900
            rm += 'CM'
            cal -= 900
        while cal >= 500:  #"D" = 500
            rm += 'D'
            cal -= 500     
        while cal >= 400:   #"CD" = 400
            rm += 'CD'
            cal -= 400
        while cal >= 100:  #"C" = 100
            rm += 'C'
            cal -= 100
        while cal >= 90:   #"XC" = 90
            rm += 'XC'
            cal -= 90
        while cal >= 50:  #"L" = 50
            rm += 'L'
            cal -= 50
        while cal >= 40:   #"XL" = 40
            rm += 'XL'
            cal -= 40
        while cal >= 10:  #"X" = 10
            rm += 'X'
            cal -= 10
        while cal >= 9:   #"IX" = 9
            rm += 'IX'
            cal -= 9
        while cal >= 5:  #"V" = 5
            rm += 'V'
            cal -= 5
        while cal >= 4:   #"IV" = 4
            rm += 'IV'
            cal -= 4
        while cal >= 1:  #"I" = 1
            rm += 'I'
            cal -= 1
        s = str(self.num) + ' convert to Roman : ' + rm
        return s
    def __add__(self,other):    # + เพิ่มอีกครึ่งนึงด้วย
        s = str(self.num) +' + '+ str(other.num) + ' = ' + str(self.num + other.num + int((self.num + other.num)/2))
        return s

print(' *** class MyInt ***')
inp = input('Enter 2 number : ').split()
a = MyInt(int(inp[0]))
b = MyInt(int(inp[1]))
print(a.toRoman())
print(b.toRoman())
print(a+b)

