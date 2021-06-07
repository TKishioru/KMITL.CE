class Bus:
    def __init__(self,people, fare):
        self.people = people
        self.fare = fare
    def __str__(self):
        return 'this bus has ' + str(people) \
        + ' people with fare = ' + str(fare)
    def __lt__(self,rhs):
        return self.people*self.fare < \
                 rhs.people*rhs.fare
    def people_in(self,k):
        return self.people += k
    def people_out(self,k):
        return self.people -= k
    def change_fare(self,new_fare):
        return fare = new_fare

#โปรแกรม(อย่าแก้)
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