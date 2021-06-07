'''
Chapter : 9 - item : 2 - เรียงลำดับโดยไม่สนจำนวนเต็มลบ
ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

    Testcase : #1
        Enter Input : 6 3 -2 5 -8 2 -2
        2 3 -2 5 -8 6 -2

    Testcase : #2
        Enter Input : 6 5 4 -1 3 0 2 -99 1
        0 1 2 -1 3 4 5 -99 6
'''

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
