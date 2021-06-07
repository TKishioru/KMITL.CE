print("*** multiplication or sum ***")
num1,num2 = map(int,input("Enter num1 num2 : ").split())

if num1*num2 > 1000:
    print("The result is",num1 + num2 )
else:
    print("The result is",num1 * num2 )