'''
Chapter : 9 - item : 4 - Sort by alphabet
ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

    Testcase : #1
        Enter Input : 932c 832u32 2344b
        2344b 932c 832u32

    Testcase : #2
        Enter Input : 99a 78b c2345 11d
        99a 78b c2345 11d

    Testcase : #3
        Enter Input : 572z 5y5 304q2
        304q2 5y5 572z
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