#By ApexTone
'''
Chapter : 10 - item : 4 - Rehashing
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด

    Testcase : #1
        ***** Rehashing *****
        Enter Input : 5 1 67/1 6
        Initial Table :
        #1	None
        #2	None
        #3	None
        #4	None
        #5	None
        ----------------------------------------
        Add : 1
        #1	None
        #2	1
        #3	None
        #4	None
        #5	None
        ----------------------------------------
        Add : 6
        collision number 1 at 1
        ****** Max collision - Rehash !!! ******
        #1	None
        #2	1
        #3	None
        #4	None
        #5	None
        #6	None
        #7	6
        #8	None
        #9	None
        #10	None
        #11	None
        ----------------------------------------

    Testcase : #2
        ***** Rehashing *****
        Enter Input : 5 1 10/1 6
        Initial Table :
        #1	None
        #2	None
        #3	None
        #4	None
        #5	None
        ----------------------------------------
        Add : 1
        ****** Data over threshold - Rehash !!! ******
        #1	None
        #2	1
        #3	None
        #4	None
        #5	None
        #6	None
        #7	None
        #8	None
        #9	None
        #10	None
        #11	None
        ----------------------------------------
        Add : 6
        ****** Data over threshold - Rehash !!! ******
        #1	None
        #2	1
        #3	None
        #4	None
        #5	None
        #6	None
        #7	6
        #8	None
        #9	None
        #10	None
        #11	None
        #12	None
        #13	None
        #14	None
        #15	None
        #16	None
        #17	None
        #18	None
        #19	None
        #20	None
        #21	None
        #22	None
        #23	None
        ----------------------------------------
'''
import math

class Hash:
    def __init__(self, table_size, max_collision, threshold=70):
        self.threshold = threshold
        self.max_collision = max_collision
        self.table_size = table_size
        self.element = []   # use this to store inserted element in table instead!
        self.table = []
        for _ in range(table_size):
            self.table.append(None)

    def get_hash(self, key):
        return key % self.table_size

    def number_of_elements(self):
        number = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                number += 1
        return number

    def is_full(self):
        return self.number_of_elements() == self.table_size

    def rehash(self, adding=None):
        if adding is not None:
            self.element.append(adding)

        self.table = []

        for possible_prime in range(self.table_size*2, 99999999999999):  # get new prime table size
            for i in range(2, int(math.sqrt(self.table_size*2))+1):
                if possible_prime % i == 0:
                    break
            else:
                self.table_size = possible_prime
                break

        for i in range(self.table_size):
            self.table.append(None)
        for val in self.element:
            retry = 0
            hashed_index = self.get_hash(val)
            while retry < self.max_collision:
                i = (hashed_index + retry ** 2) % self.table_size
                if self.table[i] is None:
                    # print(value, index)
                    self.table[i] = val
                    break
                retry += 1
                print(f'collision number {retry} at {i}')


    def insert(self, val):
        print("Add :", val)

        retry = 0
        hashed_index = self.get_hash(val)
        while retry < self.max_collision:
            i = (hashed_index + retry ** 2) % self.table_size
            if self.table[i] is None:
                if (self.number_of_elements()+1) * 100 / self.table_size > self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehash(val)
                else:
                    self.element.append(val)
                    self.table[i] = val
                return
            retry += 1
            print(f'collision number {retry} at {i}')

        print("****** Max collision - Rehash !!! ******")
        self.rehash(val)

    def __str__(self):
        out = ''
        for i in range(self.table_size):
            out += f"#{i+1}\t{self.table[i]}\n"
        out += '----------------------------------------'
        return out

print(" ***** Rehashing *****")
control, lst = input("Enter Input : ").split('/')
table_size, max_collision, threshold = list(map(int, control.split()))
lst = list(map(int, lst.split()))
print("Initial Table :")
hash = Hash(table_size, max_collision, threshold)
print(hash)
for item in lst:
    hash.insert(item)
    print(hash)