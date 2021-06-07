class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == 0

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

score = n_pl = n_act = 0
I = []
U = []
A_I = []
A_P = []
U_I = []
U_P = []
I_pl = U_pl = I_ac = U_ac = 0
#activity
active = ["Eat","Game","Learn","Movie"]
#place
place = ["Res.","ClassR.","SuperM.","Home"]

q = Queue()
inpQ = input('Enter Input : ').split(',')
for i in range(0,len(inpQ)):
    x = inpQ[i].split()
    I.append(x[0])
    U.append(x[1])
print("My   Queue = ",end='')
print(*I ,sep=', ')
print("Your Queue = ",end='')
print(*U ,sep=', ')
for j in range(0,len(I)):
    y = I[j]
    z = U[j]
    I_ac,I_pl,U_ac,U_pl = int(y[0]),int(y[2]),int(z[0]),int(z[2])
    for k in range(0,4): 
        if int(y[0]) == k:          
            A_I.append(active[k])
        if int(y[2]) == k:
            A_P.append(place[k])
        if int(z[0]) == k:          
            U_I.append(active[k])
        if int(z[2]) == k:
            U_P.append(place[k])
            
    if I_pl == U_pl and I_ac == U_ac:
        score += 4
    elif I_pl == U_pl and I_ac != U_ac:
        score += 2
    elif I_pl != U_pl and I_ac == U_ac:
        score += 1
    else:
        score -= 5
print("My   Activity:Location =",end=' ')
for i in range(len(I)):    
    if(i==len(I)-1):
        print(A_I[i],A_P[i],sep=':')
    else:
        print(A_I[i],A_P[i],sep=':',end=', ')
print("Your Activity:Location =",end=' ')
for i in range(len(U)):    
    if(i==len(I)-1):
        print(U_I[i],U_P[i],sep=':')
    else:
        print(U_I[i],U_P[i],sep=':',end=', ')
if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif 0 < score < 7:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")