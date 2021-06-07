print('******** Parking Lot ********')
s = input('Enter max of car,car in soi,operation : ').split()
max_car = int(s[0])
n_car = list(map(int, s[1].split(',')))
move_car = s[2]
id_car = int(s[3])

#new
if len(n_car) == 1 and n_car[0] == 0:
   n_car = []

if move_car == 'arrive':
   if id_car in n_car:
      print("car",id_car,"already in soi")
   elif len(n_car) >= max_car:
      print("car",id_car,"cannot arrive : Soi Full")
   else:
      print("car",id_car,"arrive! : Add Car",id_car)
      n_car.append(id_car)

elif move_car == 'depart':
   if len(n_car) == 0:
      print("car",id_car,"cannot depart : Soi Empty")
   elif id_car in n_car:
      print("car",id_car,"depart ! : Car",id_car,"was remove")
      n_car.remove(id_car)
   else:
      print("car",id_car,"cannot depart : Dont Have Car",id_car)

print(n_car)