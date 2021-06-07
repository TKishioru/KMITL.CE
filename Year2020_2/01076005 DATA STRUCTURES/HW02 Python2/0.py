"""
Chapter : 2 - item : 1 - print N
ส่งมาแล้ว 0 ครั้ง
จงเขียนฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n และฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1 โดยแสดงผลตามตัวอย่าง
****ห้ามใช้คำสั่ง len, for, while, do while, split*****
หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

def print1ToN(n):    #code here
def printNto1(n):    #code here
n = int(input("Enter Input : "))
print1ToN(n)
printNto1(n)

    Testcase : #1
        Enter Input : 6
        1 2 3 4 5 6 6 5 4 3 2 1 
    Testcase : #2
        Enter Input : -1
        1 1 
    Testcase : #3
        Enter Input : 1
        1 1 
"""

i = 1
def print1ToN(n):
    global i
    if(i < n):
        print(i,end='')
        i+=1
        print1ToN(n)
    else:
        print(i)

def printNto1(n):
    if(n>=1):
        print(n,end='')
        n = n - 1
        printNto1(n)

n = int(input("Enter Input : "))
print1ToN(n)
printNto1(n)