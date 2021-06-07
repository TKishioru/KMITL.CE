def pyramid(x, y):
    if x==1:
        print("#."*(y-1)+"#"+".#"*(y-1))
        return
    
    print("#."*(y-x)+"#"*(1+(x-1)*4)+".#"*(y-x))
    print("#."*(y-x+1)+"."*((x-1)*4-3)+".#"*(y-x+1))
    pyramid(x-1, y)
    print("#."*(y-x+1)+"."*((x-1)*4-3)+".#"*(y-x+1))
    print("#."*(y-x)+"#"*(1+(x-1)*4)+".#"*(y-x))

print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
pyramid(num, num)