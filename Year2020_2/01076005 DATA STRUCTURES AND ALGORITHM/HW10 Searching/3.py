#By radsadorn
'''
Chapter : 10 - item : 3 - Fun with hashing
 ส่งมาแล้ว 0 ครั้ง
ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ

    Testcase : #1
        ***** Fun with hashing *****
        Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
        #1	(1+1, I)
        #2	None
        #3	None
        ---------------------------
        collision number 1 at 0
        #1	(1+1, I)
        #2	(OnE, Love)
        #3	None
        ---------------------------
        collision number 1 at 0
        collision number 2 at 1
        Max of collisionChain
        #1	(1+1, I)
        #2	(OnE, Love)
        #3	None
        ---------------------------
        #1	(1+1, I)
        #2	(OnE, Love)
        #3	(#$ew2, KMITL)
        ---------------------------
        This table is full !!!!!!

    Testcase : #2
        ***** Fun with hashing *****
        Enter Input : 5 5/one Un,two Deux,three Trois,four Quatre,five Cinq,ten Dix,eleven Onze
        #1	None
        #2	None
        #3	(one, Un)
        #4	None
        #5	None
        ---------------------------
        #1	None
        #2	(two, Deux)
        #3	(one, Un)
        #4	None
        #5	None
        ---------------------------
        collision number 1 at 1
        collision number 2 at 2
        #1	(three, Trois)
        #2	(two, Deux)
        #3	(one, Un)
        #4	None
        #5	None
        ---------------------------
        #1	(three, Trois)
        #2	(two, Deux)
        #3	(one, Un)
        #4	None
        #5	(four, Quatre)
        ---------------------------
        collision number 1 at 1
        collision number 2 at 2
        collision number 3 at 0
        collision number 4 at 0
        collision number 5 at 2
        Max of collisionChain
        #1	(three, Trois)
        #2	(two, Deux)
        #3	(one, Un)
        #4	None
        #5	(four, Quatre)
        ---------------------------
        collision number 1 at 2
        #1	(three, Trois)
        #2	(two, Deux)
        #3	(one, Un)
        #4	(ten, Dix)
        #5	(four, Quatre)
        ---------------------------
        This table is full !!!!!!
'''
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:

    def __init__(self, tb):
        self.table_size, self.max_colision = map(int, tb.split())
        self.table = [None] * self.table_size

    def hashing(self, data):
        data = data.split()
        asc = 0
        for txt in list(data[0]):
            asc += ord(txt)    
        asc %= self.table_size     
        count = 0                  
        while True:
            i = (asc + count ** 2) % self.table_size   
            if count == self.max_colision:                
                print('Max of collisionChain')
                return False
            if self.table[i] is None:                 
                self.table[i] = Data(data[0], data[1])
                if None not in self.table:              
                    return True
                return False
            count += 1
            print(f"collision number {count} at {i}")

    def printHASH(self):
        for i, data in enumerate(self.table):
            print(f'#{i + 1}\t{data}')
        print('---------------------------')

print(" ***** Fun with hashing *****")
tb, data = input("Enter Input : ").split('/')

table = Hash(tb)
for d in data.split(','):
    check = table.hashing(d)
    table.printHASH()
    if check:
        print('This table is full !!!!!!')
        quit()