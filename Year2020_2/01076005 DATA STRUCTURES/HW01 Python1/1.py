"""
Chapter : 1 - item : 1 - radius and area of circle
เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล
    #Testcase : 1
        r=1.1
        Area=3.8013271108436504
"""

import math

r = float(input('r='))
print("Area=",end='')
print(r * r * math.pi)   #สูตรพื้นที่วงกลม pi * r * r