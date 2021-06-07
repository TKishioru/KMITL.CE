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
prt = ''
s = list()
txt = dict()
k = list()
inp = input("Enter Input : ").split()
for i in range(0,len(inp)):
    s = inp[i]
    for j in range(0,len(s)):
        if s[j] >= 'a' and s[j] <= 'z':
            txt[s[j]] = s
for x in txt.keys():
    k.append(x)
z = Bubble(k,0,0)
for i in range(0,len(z)):
    prt += txt.get(z[i]) + ' '
print(prt)