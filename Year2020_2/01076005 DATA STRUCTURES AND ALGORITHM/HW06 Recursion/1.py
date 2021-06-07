'''
Chapter : 6 - item : 1 - หาค่ามากที่สุด
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
ให้เขียน Recursive หาค่า Max ของ Input

    Testcase : #1
        Enter Input : 8 7 10 1 5 4 2 6 3 9
        Max : 10

    Testcase : #2
        Enter Input : -84 -230 -54845 -6 -1
        Max : -1
'''
n_max = 0
def findmax(i,inp):
    global n_max
    if i == 0:
        n_max = int(inp[0])
    elif i == len(inp):
        return n_max
    else:
        if int(inp[i]) > n_max:
            n_max = int(inp[i])
    i+=1
    return findmax(i,inp)        

inp = input('Enter Input : ').split()
print('Max :',findmax(0,inp))
