'''
Chapter : 6 - item : 5 - วาดภาพแสนสุข
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

    Testcase : #1
        Enter Input : 3
        __#
        _##
        ###

    Testcase : #2
        Enter Input : 7
        ______#
        _____##
        ____###
        ___####
        __#####
        _######
        #######

    Testcase : #3
        Enter Input : -8
        ########
        _#######
        __######
        ___#####
        ____####
        _____###
        ______##
        _______#

    Testcase : #4
        Enter Input : 2
        _#
        ##

    Testcase : #5
        Enter Input : 0
        Not Draw!
'''
s = ''
num = 0
def pos_case(i,j):
    global num,s
    if i <= num:
        if j <= num:
            if j < (num+1-i):
                s += '_'
            else:
                s += '#'
            #print('j :',j)
            return pos_case(i,j+1)
        #print('i :',i)
        print(s)
        s = ''
        return pos_case(i+1,1)
    '''
    for i in range(1,n+1):
        s = ''
        for j in range(1,n+1):
            if j < (n+1-i):
                s += '#'
            else:
                s += '_'
        print(s)
    '''
def neg_case(i,j):
    global num,s
    if i <= num:
        if j <= num:
            if j <= i-1:
                s += '_'
            else:
                s += '#'
            #print('j :',j)
            return neg_case(i,j+1)
        #print('i :',i)
        print(s)
        s = ''
        return neg_case(i+1,1)
    '''
    for i in range(1,abs(n)+1):
        s = ''
        for j in range(1,abs(n)+1):
            if j < i-1:
                s += '_'
            else:
                s += '#'
        print(s)
    '''
def staircase(i,n):
    global num
    if n>0:
        num = n
        pos_case(1,1)
    elif n ==0:
        print('Not Draw!')
    elif n<0:
        num = abs(n)
        neg_case(1,1)
staircase(1,int(input("Enter Input : ")))
