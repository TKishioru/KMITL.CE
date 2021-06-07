#โจทย์ให้ทำกรอบสี่เหลี่ยมโดยแสดงเป็นเลขฐาน 16 >> ("%X" %(input))

num = list()
inp = int(input('Enter a positive number : '))
if inp < 1:
    print(inp,'is too low.')
elif inp > 15:
    print(inp,'is too high.')
else:
    for i in range(1,inp):
        print("%X" %(i),end=' ')
    print("%X" %(inp))
    for i in range(1,inp-1):            #กว้าง 
        for j in range(1,inp+1):        #ยาว
            if j == 1:
                print("%X" %(i+1),end=' ')
            elif j == inp:
                print("%X" %(i),end=' ')
            else:
                print('  ',end='')
        print('')
    print("%X" %(inp),end=' ')
    for i in range(1,inp):
        print("%X" %(i),end=' ')