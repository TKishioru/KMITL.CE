"""
Chapter : 1 - item : 4 - Game Minesweeper
สร้างฟังก์ชันที่รับ input เป็น list(5x5) ของ # และ - โดยแต่ละแฮช (#) แทนทุ่นระเบิดและแต่ละขีด (-) แทนจุดที่ไม่มีทุ่นระเบิด ให้ return list ที่แต่ละขีดถูกแทนที่ด้วยตัวเลขที่ระบุจำนวนของทุ่นระเบิดที่อยู่ติดกับจุดนั้น (แนวนอนแนวตั้งและแนวทแยงมุม)
    Testcase : #1 1
        *** Minesweeper ***
        Enter input(5x5) : - - - - -,- - - - -,- - # - -,- - - - -,- - - - -

        ['-', '-', '-', '-', '-']
        ['-', '-', '-', '-', '-']
        ['-', '-', '#', '-', '-']
        ['-', '-', '-', '-', '-']
        ['-', '-', '-', '-', '-']

        ['0', '0', '0', '0', '0']
        ['0', '1', '1', '1', '0']
        ['0', '1', '#', '1', '0']
        ['0', '1', '1', '1', '0']
        ['0', '0', '0', '0', '0']

    Testcase : #2 2
        *** Minesweeper ***
        Enter input(5x5) : - - - # -,- # - - -,- - # - -,- - - - -,- # - - -

        ['-', '-', '-', '#', '-']
        ['-', '#', '-', '-', '-']
        ['-', '-', '#', '-', '-']
        ['-', '-', '-', '-', '-']
        ['-', '#', '-', '-', '-']

        ['1', '1', '2', '#', '1']
        ['1', '#', '3', '2', '1']
        ['1', '2', '#', '1', '0']
        ['1', '2', '2', '1', '0']
        ['1', '#', '1', '0', '0']
"""


def num_grid(lst):
    new = []
    for i in range(0,len(lst_input)):
        lst = lst_input[i]
        new.append(lst[0])
        new.append(lst[1])
        new.append(lst[2])
        new.append(lst[3])
        new.append(lst[4])
    x = 0
    for i in range(0,5):
        for j in range(0,5):
            field[i][j] = new[x]
            x += 1
    i = 0
    j = 0
    for j in range(0,5):
        for i in range(0,5):
            if field[i][j] == '-':                              field[i][j] = 0
            if field[i-1][j-1] == '#' and field[i][j] != '#':   field[i][j]+=1
            if field[i-1][j] == '#' and field[i][j] != '#':     field[i][j]+=1
            if field[i][j-1] == '#' and field[i][j] != '#':     field[i][j]+=1
            if field[i-1][j+1] == '#' and field[i][j] != '#':   field[i][j]+=1
            if field[i+1][j-1] == '#' and field[i][j] != '#':   field[i][j]+=1
            if field[i+1][j] == '#' and field[i][j] != '#':     field[i][j]+=1
            if field[i][j+1] == '#' and field[i][j] != '#':     field[i][j]+=1
            if field[i+1][j+1] == '#' and field[i][j] != '#':   field[i][j]+=1
    lst.clear()
    for a in range(0,5):
        R_small = []
        for b in range(0,5):
            R_small.append(str(field[a][b]))
        lst.append(R_small)
    return lst

w = 6
h = 6
lst_input = []
field = [[0 for x in range(w)] for y in range(h)] 
print('*** Minesweeper ***')
input_list = input('Enter input(5x5) : ').split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])
print("\n",*lst_input,sep = "\n")               #print ปกติเป็นช่อง
print("\n",*num_grid(lst_input),sep = "\n")