## ฟังก์ชันเช็คชนิดตัวแปร
def check_type(i = null):
  while True:
    print("Enter Number [" , i, "] : ")
    inp = input()
    try:
      num = int(inp)
      break;
    except ValueError:
      try:
        num = float(inp)
        break;
      except ValueError:
        print("ไม่สามารถดำเนินการได้") #ERROR TYPE
  return num

##  ฟังก์ชันหาประเภทสามเหลี่ยม
def find_triangular(triangular_side):
if triangular_side[0] == triangular_side[1] == triangular_side[2]:
  print("Equilateral Triangle")
elif (triangular_side[0] == triangular_side[1]) or (triangular_side[0] == triangular_side[2]) or (triangular_side[1] == triangular_side[2]):
  print("Isosceles triangle")
elif ((pow(triangular_side[0],2) + pow(triangular_side[1],2)) == pow(triangular_side[2],2)) or ((pow(triangular_side[0],2) + pow(triangular_side[2],2)) == pow(triangular_side[1],2)) or ((pow(triangular_side[1],2) + pow(triangular_side[2],2)) == pow(triangular_side[0],2)):
  print("Right Triangle")
else:
  print("Scalene Triangle")

## ประกาศตัวแปร
triangular_side = list()

## MAIN
### รับตัวเลข (แบบรับแล้วเช็คทีละตัว)
for i in range(1, 4):
  num = check_type(i)
  while num <= 0:
    print("ไม่สามารถดำเนินการได้") #ERROR NUMBER
    num = check_type(i)
  triangular_side.append(num)
find_triangular(triangular_side)
