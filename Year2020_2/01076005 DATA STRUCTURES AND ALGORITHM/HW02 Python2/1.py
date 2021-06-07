"""
Chapter : 2 - item : 1 - Rshift
สร้างฟังชั่น right shift 
เช่น     = 8 right shift 1
        = 1000 (ฐาน 2) right shift 1 (ฐาน 2)
        = 100 (ฐาน 2)
        = 4

    Testcase : #1 1
        Enter number and shiftcount : 3888 4
        243
    Testcase : #2 2
        Enter number and shiftcount : 5 6
        0
    Testcase : #3 3
        Enter number and shiftcount : -320 6
        -5
    Testcase : #4 5
        Enter number and shiftcount : -4 4
        -1
"""

def Rshift(num,shift):
    #แปลง num เป็นเลขฐาน 2 แล้ว shift ตามจำนวนแล้วแปลงกลับเป็นเลขฐานสิบ
    return num >> shift

n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))