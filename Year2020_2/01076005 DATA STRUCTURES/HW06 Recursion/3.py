'''
Chapter : 6 - item : 3 - ( 2^(input) ) - 1
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 

*** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11

    Testcase : #1
        Enter Number : -1
        Only Positive & Zero Number ! ! !

    Testcase : #2
        Enter Number : 0
        0

    Testcase : #3
        Enter Number : 1
        0
        1

    Testcase : #4
        Enter Number : 4
        0000
        0001
        0010
        0011
        0100
        0101
        0110
        0111
        1000
        1001
        1010
        1011
        1100
        1101
        1110
        1111
'''
sum = 1
m = 0

def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

inp = int(input("Enter Number : "))
if inp < 0:
    print("Only Positive & Zero Number ! ! !")
elif inp == 0:
    print("0")
else:
    n = pow(2, inp)
    for i in range(0,n):    
        if i == 0 or i == 1:        #condition clear
            for k in range(1,inp):
                print("0",end='')
        else:
            while sum <= i:
                sum *= 2
                m += 1
            for r in range(0,inp-m):
                if sum != n:
                    print("0",end='')
        decimalToBinary(i)
        print('')