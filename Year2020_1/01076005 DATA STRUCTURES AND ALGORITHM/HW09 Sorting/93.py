def Metadrome(inp): #เรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำ
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            #print(inp[i],"-------",inp[j])
            if inp[i] >= inp[j]:
                return 0
    return 1
def Plaindrome(inp): #เรียงลำดับจากน้อยไปมาก และมีตัวซ้ำ
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            #print(inp[i],"-------",inp[j])
            if inp[i] > inp[j]:
                return 0
    return 2
def Katadrome(inp): #เรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำ
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            #print(inp[i],"-------",inp[j])
            if inp[i] <= inp[j]:
                return 0
    return 3
def Nialpdrome(inp): #เรียงลำดับจากมากไปน้อย
    for i in range(0,len(inp)-1):
        for j in range(i+1,len(inp)):
            #print(inp[i],"-------",inp[j])
            if inp[i] < inp[j]:
                return 0
    return 4
def Repdrome(inp): #ทุกหลักเป็นเลขเดียวกันหมด
    for i in range(0,len(inp)-1):
        for j in range(i+1,len(inp)):
            #print(inp[i],"-------",inp[j])
            if inp[i] == inp[j]:
                c = 1
            else:
                return 0
    if c == 1:  return 5

inp = input("Enter Input : ")
e = Repdrome(inp)
a = Metadrome(inp)
b = Plaindrome(inp)
c = Katadrome(inp)
d = Nialpdrome(inp)

if e == 5:      print("Repdrome")
elif a == 1:    print("Metadrome")
elif b == 2:    print("Plaindrome")
elif c == 3:    print("Katadrome")
elif d == 4:    print("Nialpdrome")
else:           print("Nondrome")