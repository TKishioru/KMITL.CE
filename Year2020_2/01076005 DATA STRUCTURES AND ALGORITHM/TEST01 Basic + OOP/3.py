#โจทย์ให้หาความถี่โดยถ้าให้นำข้อมูลก่อนเจอ -1 มาหาฐานนิยม แต่จะต้องมีค่ามากกว่า "ครึ่งหนึ่งของจำนวนที่รับมา ซึ่งไม่รวม -1"

num = list()
x = []
y = []
sum = 0
inp = input('Enter number end with (-1) : ').split()
if '-1' not in inp:
    print('Invalid INPUT !!!')
elif inp[0] == '-1':
    print('Not found')
else:
    for i in range(0,len(inp)):
        #print(inp[i])
        if inp[i] != '-1' and int(inp[i]) > 0:
            num.append(int(inp[i]))
            sum += int(inp[i])
            nerr = True
        elif '.' in inp[i] or int(inp[i]) < -1:
            nerr = False
            break
        else:
            break
    if nerr:
        freq = sum/len(num)
        num.sort()
        num.reverse()
        for i in range(0,len(num)):
            if num[i] not in x:
                x.append(num[i])
        for i in range(0,len(x)):
            n = 0
            for j in range(0,len(num)):
                if x[i] == num[j]:
                    n+=1
            y.append(n)
        #print(x)    #เซ็คค่า
        #print(y)    #เซ็คจำนวน
        max = 0
        check = 0
        equ = 1
        for i in range(0,len(y)-1):
            #print(y[i] , y[i+1])
            if y[i] < y[i+1]:
                max = i+1
                check = y[i+1]
            elif y[i] == y[i+1]:
                equ += 1
                check = y[i]
            else:
                max = i
        #print(equ)
        #print(len(num)/2 , y[max],x[max])
        if equ == len(y) or y[max] < (len(num)/2):
            print('Not found')
        else:
            print(x[max])
    else:
        print('Invalid INPUT !!!')