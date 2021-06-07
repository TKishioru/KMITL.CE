"""
Chapter : 2 - item : 3 - New Range
ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function

ถ้าหากเป็น 1 argument -> range(a)          | start = 0 , end = a , step = 1
ถ้าหากเป็น 2 argument -> range(a, b)       | start = a , end = b , step = 1
ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = c

    Testcase : #1 1
        *** New Range ***
        Enter Input : 10
        (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)

    Testcase : #2 2
        *** New Range ***
        Enter Input : 3.2 6.32
        (3.2, 4.2, 5.2, 6.2)

    Testcase : #3 3
        *** New Range ***
        Enter Input : 0.112 6.45 1.35
        (0.112, 1.462, 2.812, 4.162, 5.512)
"""

prt = list()
print("*** New Range ***")
num = input('Enter Input : ').split()

if(len(num)==3):
    x = 0
    y = 0
    if '.' in num[0]:
        x = len(num[0].split('.')[1])
    if '.' in num[2]:
        y = len(num[2].split('.')[1])
    
    a = float(num[0])
    b = float(num[1])
    c = float(num[2])
    
    if x < y:    l = y
    else:        l = x

    while a < b:
        a = round(a,l)
        prt.append(a)
        a = a + c

elif(len(num)==2):
    a = float(num[0])
    b = float(num[1])
    while a < b:
        prt.append(a)
        a = a + 1.0
elif(len(num)==1):
    a = int(num[0])
    i = 0.0
    while i < a:
        prt.append(i)
        i = i + 1.0

print(tuple(prt))
"""
print('(',end='')
for i in range(0,len(prt)-1):
    print(prt[i],end=', ')
print(f'{prt[-1]})')
"""