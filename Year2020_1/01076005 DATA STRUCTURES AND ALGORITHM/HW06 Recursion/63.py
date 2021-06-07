#( 2^(input) ) - 1

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