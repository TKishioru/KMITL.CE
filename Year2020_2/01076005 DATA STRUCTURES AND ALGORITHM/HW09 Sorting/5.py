#BY ApexTone
'''
Chapter : 9 - item : 5 - Sort Subset
ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /

1. ด้านซ้าย เป็นผลลัพธ์
2. ด้านขวา เป็น list ของจำนวนเต็ม

โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้

1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก

ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import

อธิบาย Test Case 1:

[2]
[-1, 3]
[0, 2]  # [-1, 3] กับ [0, 2] มีขนาดเท่ากัน แต่ -1 < 0 ดังนั้น [-1, 3] จึงแสดงผลก่อน [0, 2]
[-3, 2, 3]
[-2, 1, 3]
[-1, 0, 3]
[-1, 1, 2]
[-3, 0, 2, 3]
[-2, -1, 2, 3]
[-2, 0, 1, 3]   # [-2, -1, 2, 3] กับ [-2, 0, 1, 3] มีขนาดและตัวแรกสุดเท่ากัน แต่ตัวที่สอง -1 < 0 ดังนั้น [-2, -1, 2, 3] จึงแสดงผลก่อน [-2, 0, 1, 3]
[-1, 0, 1, 2]
[-3, -1, 1, 2, 3]
[-2, -1, 0, 2, 3]
[-3, -1, 0, 1, 2, 3]

    Testcase : #1
        Enter Input : 2/-2 3 1 -1 0 -3 2
        [2]
        [-1, 3]
        [0, 2]
        [-3, 2, 3]
        [-2, 1, 3]
        [-1, 0, 3]
        [-1, 1, 2]
        [-3, 0, 2, 3]
        [-2, -1, 2, 3]
        [-2, 0, 1, 3]
        [-1, 0, 1, 2]
        [-3, -1, 1, 2, 3]
        [-2, -1, 0, 2, 3]
        [-3, -1, 0, 1, 2, 3]

    Testcase : #2
        Enter Input : 2/1 0 2 -1
        [2]
        [0, 2]
        [-1, 1, 2]
        [-1, 0, 1, 2]

    Testcase : #3 3
        Enter Input : 3/-1 0 1 2
        [1, 2]
        [0, 1, 2]
'''

def bubble_sort(lst):
    result = lst.copy()
    for i in range(len(result)-1):
        swapped = False
        for j in range(len(result)-1-i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def get_subsets(target, lst, left=0, res=[], carry=[]):  # knapsack style
    if left >= len(lst):
        return res
    carry.append(lst[left])
    if sum(carry) == target:
        res.append(carry.copy())
    res = get_subsets(target, lst, left+1, res, carry)
    carry.pop()
    res = get_subsets(target, lst, left+1, res, carry)
    return res


def list_sorting(lst):
    # sort by length
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

inp = input("Enter Input : ").split('/')
k = int(inp[0])
num = [int(i) for i in inp[1].split()]
num = bubble_sort(num)
allset = get_subsets(k, num)
if len(allset) == 0:
    print("No Subset")
else:
    allset = list_sorting(allset)
    for item in allset:
        print(item)