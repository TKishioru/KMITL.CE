"""
Chapter : 2 - item : 2 - Class BUS

การทำงานไม่ถูกต้อง มีจุดผิดดังนี้
- ไม่มีการใช้ self
- เมท็อด people_in, people_out และ change_fare ต้องไม่คืนค่า
- เมท็อด people_out ไม่ได้ตรวจสอบว่า จำนวนคนน้อยกว่าศูนย์หรือไม่

    Testcase : #1 1
        Enter people in Bus1, Bus2, fare Bus1, Bus2 : 10 8 7 3
        this bus has 8 people with fare = 3
        this bus has 7 people with fare = 12

    Testcase : #2 2
        Enter people in Bus1, Bus2, fare Bus1, Bus2 : 1 4 3 6
        this bus has 1 people with fare = 3
        this bus has 0 people with fare = 12
"""

class Bus:
    #สร้างรถเมล์ 1 คัน รับพารามิเตอร์ จำนวนคนบนรถ people และค่าโดยสาร fare
    def __init__(self, people, fare):
        self.people = people
        self.fare = fare
    
    #คืนค่าสตริงซ่ึงบอกจำนวนคนบนรถและค่าโดยสาร
    def __str__(self):
        return 'this bus has ' + str(self.people) \
        + ' people with fare = ' + str(self.fare)

    #เปรียบเทียบรถเมล์โดยพิจารณาค่าโดยสารรวมของรถ (จำนวนคนบนรถคูณค่าโดยสารต่อคน)
    def __lt__(self,rhs):
        return self.people*self.fare < \
                 rhs.people*rhs.fare

    #เพิ่มจำนวนคนบนรถ k คน ไม่คืนค่า
    def people_in(self,k):
        self.people += k
        return self.people
    
    #ลดจำนวนคนบนรถ k คน (หากจำนวนคนน้อยกว่า 0 จะต้องแก้ไขจำนวนคนเป็น 0) ไม่คืนค่า
    def people_out(self,k):
        self.people -= k
        if self.people <= 0:
            self.people = 0
        return self.people
    
    #เปลี่ยนค่าโดยสารเป็นค่าโดยสารใหม่ new_fare ไม่คืนค่า
    def change_fare(self,new_fare):
        self.fare = new_fare
        return self.fare

b1, b2, f1, f2 = input("Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()
b1 = Bus(int(b1), int(f1))
b2 = Bus(int(b2), int(f2))
if b1 < b2:
    print(b1)
else:
    print(b2)
b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)