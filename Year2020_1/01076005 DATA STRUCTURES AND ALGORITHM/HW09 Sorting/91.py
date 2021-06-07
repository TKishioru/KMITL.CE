def Bubble(n,i,c):
    l = len(n)
    count = l * l
    if c <= count:
        if i <= l-2:
            if n[i] > n[i+1]:
                n[i],n[i+1] = n[i+1],n[i]
            i += 1
        else:
            i = 0
        Bubble(n,i,c+1)
    return n
prt = '['
inp = input("Enter Input : ").split()
txt = (Bubble(inp,0,0))
for i in range(0,len(txt)-1):
    prt+= txt[i] + ', '
prt += txt[-1] + ']'
print(prt)