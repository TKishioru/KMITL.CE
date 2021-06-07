'''
Chapter : 10 - item : 2 - First Greater Value
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

    Testcase : #1
    Enter Input : 3 2 7 6 8/5
    6

    Testcase : #2
    Enter Input : 3 2 7 6 8/5 6 12
    6
    7
    No First Greater Value
'''

def FGV(data,key):
    data = sorted(data)
    for j in range(0,len(data)):
        if data[j] > key:
            return data[j]
    return "No First Greater Value"

inp = input('Enter Input : ').split('/')
data = list(map(int, inp[0].split()))
key = list(map(int, inp[1].split()))
for i in range(0,len(key)):
    print(FGV(data,key[i]))