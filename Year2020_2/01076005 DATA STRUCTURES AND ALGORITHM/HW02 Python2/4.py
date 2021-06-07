"""
Chapter : 2 - item : 4 - 3 SUM
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

    Testcase : #1 1
        Enter Your List : -25 -10 -7 -3 2 4 8 10
        [[-10, 2, 8], [-7, -3, 10]]

    Testcase : #2 2
        Enter Your List : -3 2 4 6 8 10
        []

    Testcase : #3 3
        Enter Your List : -100 100
        Array Input Length Must More Than 2
"""

show = list()
lst = [int(e) for e in input('Enter Your List : ').split()]
if len(lst) < 3:
    print('Array Input Length Must More Than 2')
else:
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                if (lst[i] + lst[j] + lst[k] == 0) and [lst[i] , lst[j] , lst[k]] not in show:
                    #s = "[" + str(lst[i]) + ', ' + str(lst[j]) + ', ' + str(lst[k]) + "]"
                    show.append([lst[i] , lst[j] , lst[k]])
    print(show)