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
numP = list()
numN = list()
inp = list()
prt = ''
inp = input("Enter Input : ").split()
for i in range(0,len(inp)):
    if int(inp[i]) >= 0:
        numP.append(int(inp[i]))
    elif int(inp[i]) < 0:
        numN.append(int(inp[i]))
        numN.append(i)
        #print(inp[i],"---------",str(i))
txt = (Bubble(numP,0,0))
for i in range(0,len(numN),2):
    txt.insert(numN[i+1],numN[i])
for i in txt:
    print(i,end = ' ')
