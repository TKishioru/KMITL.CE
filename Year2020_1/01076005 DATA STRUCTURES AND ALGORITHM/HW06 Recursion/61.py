#หาค่ามากที่สุด
a = b = 0

def Max(i,inp):

    global a,b

    if i == len(inp):
        print("Max :",b)
    else:
        if i == 0:
            b = int(inp[0])
            a = int(inp[0])
        else:
            a = int(inp[i])

        if a <= b:
            b = b
        else:
            b = a
        i += 1
        return Max(i,inp)
        
inp = input('Enter Input : ').split()
Max(0,inp)