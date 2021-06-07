"""
Chapter : 1 - item : 5 - vickrey auction
จงสร้าง vickrey auction แบบจำลอง
Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา

word
"Enter All Bid : "
"not enough bidder"
"error : have more than one highest bid"
"winner bid is $ need to pay $"
    Testcase : 1
        Enter All Bid : 5
        not enough bidder

    Testcase : 2
        Enter All Bid : 5 10 20 5 16
        winner bid is 20 need to pay 16

    Testcase : 3
        Enter All Bid : 5 10 20 20 10
        error : have more than one highest bid
"""


x = []
inp = input('Enter All Bid : ').split()
for i in range(0,len(inp)):
    x.append(int(inp[i]))
x.sort(reverse = True)
    #เป็นการเรียงข้อมูลแบบนึง (ไม่ใช้คำสั่งลัด)
    #def Bubble(n,i,c):
    #    l = len(n)
    #    count = l * l
    #    if c <= count:
    #        if i <= l-2:
    #            if n[i] > n[i+1]:
    #                n[i],n[i+1] = n[i+1],n[i]
    #            i += 1
    #        else:
    #            i = 0
    #        Bubble(n,i,c+1)
    #    return n
if len(x) <= 1:
    print("not enough bidder")
elif x[0] == x[1]:
    print("error : have more than one highest bid")
else:
    print(f"winner bid is {x[0]} need to pay {x[1]}")