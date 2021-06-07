merge = []

inp = input("Enter Input (L1,L2) : ").split()
L1 = inp[0].split("->")
L2 = inp[1].split("->")

print("L1    :" , end= ' ')
for i in range(0,len(L1)):
    print(L1[i],end=' ')

print("\nL2    :" , end= ' ')
for j in range(0,len(L2)):
    print(L2[j],end=' ')
    
L2.reverse()
merge.append(L1 + L2)

print("\nMerge :" , end= ' ')
for i in range(0,len(merge)):
    print(*merge[i],end=' ')