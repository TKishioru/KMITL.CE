'''
Chapter : 9 - item : 1 - หัดใช้ Sort
ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

    Testcase : #1
        Enter Input : -99 -1 0 1 2 3
        Yes

    Testcase : #2
        Enter Input : 5252 -5 2630 -558
        No

    Testcase : #3
        Enter Input : 9 10 99
        Yes
'''

ans = ''
inp = input('Enter Input : ').split()
for i in range(0,len(inp)-1):
    if int(inp[i]) <= int(inp[i+1]):
        ans = 'Yes'
    else:
        ans = 'No'
print(ans)
