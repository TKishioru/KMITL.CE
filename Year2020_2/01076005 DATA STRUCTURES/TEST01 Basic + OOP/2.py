#โจทย์ให้ทำ Perfect Number

print(' *** Perfect Number Verification ***')
inp = int(input('Enter number : '))
num = 0
fac = list()
if inp <= 0:
    print('Only positive number !!!')
else:
    for i in range(1,inp):
        if (inp%i)==0:
            num += i
            fac.append(i)
    if num == inp:
        print(inp,'is a PERFECT NUMBER.')
        print('Factors :',fac)
    else: 
        print(inp,'is NOT a perfect number.')
        print('Factors :',fac)