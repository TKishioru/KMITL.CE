#Manchester United,30,3,5,88,20/Arsenal,24,6,8,98,29/Chelsea,22,8,8,98,29
#Manchester City,30,8,0,67,20/Liverpool,34,2,2,118,29/Leicester City,22,8,8,98,29
#Manchester United,30,8,0,67,20/New Castle United,34,2,2,118,36/Leicester City,34,2,2,108,21

def Bubble(m,i,c):
    n = list(int(m))
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
a = list()
b = list()
k = list()
m = list()
T = dict()
U = dict()
inp = input("Enter Input : ").split('/')
print("== results ==")
for i in range(0,len(inp)):
    x = inp[i].split(',')
    #cal
    points = (3 * int(x[1])) + (0 * int(x[2])) + (1 * int(x[3]))
    gd = int(x[4]) - int(x[5])
    txt = '[\'' + x[0] + '\', {\'points\': ' + str(points) + '}, {\'gd\': ' + str(gd) + '}]'
    y = str(points) + ' ' + str(gd)
    T[y] = txt
for i in T.keys():
    k.append(i)
z = Bubble(k,0,0)
for i in range(0,len(z)):
    print(T.get(z[i]))