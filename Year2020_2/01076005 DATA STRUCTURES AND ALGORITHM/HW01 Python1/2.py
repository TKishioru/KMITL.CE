"""
Chapter : 1 - item : 2 - multiplication or sum
รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง
    Testcase : 1
        *** multiplication or sum ***
        Enter num1 num2 : 20 30
        The result is 600

    Testcase : 2
        *** multiplication or sum ***
        Enter num1 num2 : 40 60
        The result is 100
"""

print("*** multiplication or sum ***")
inp = input('Enter num1 num2 : ').split()
a = int(inp[0])
b = int(inp[1])
if (a*b) > 1000:
    x = a + b
else:
    x = a* b
print(f'The result is {x}')