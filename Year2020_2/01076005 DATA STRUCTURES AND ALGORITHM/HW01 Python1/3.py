"""
Chapter : 1 - item : 3 - loop
จงเขียนโปรแกรมรับตัวเลขจำนวนเต็ม ไม่เกิน 9 หลัก แล้วหาผลรวมของเลขโดด แต่ละหลัก 
รับตัวเลข 123 => 1+2+3=6
รับตัวเลข 7892 => 7+8+9+2=26 
รับตัวเลข 32189657 => 3+2+1+8+9+6+5+7=41
    Testcase : #1 1
        *** Summation of each digit ***
        Enter a positive number : 123
        Summation of each digit =  6

    Testcase : #2 2
        *** Summation of each digit ***
        Enter a positive number : 7892
        Summation of each digit =  26

    Testcase : #3 3
        *** Summation of each digit ***
        Enter a positive number : 32189657
        Summation of each digit =  41

    Testcase : #4 4
        *** Summation of each digit ***
        Enter a positive number : 987654321987654321
        Summation of each digit =  90
"""

x = 0
print(" *** Summation of each digit ***")
inp = input('Enter a positive number : ')
for i in range(0,len(inp)):
    x += int(inp[i])
print(f'Summation of each digit =  {x}')