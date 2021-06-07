'''
Chapter : 6 - item : 4 - ไปเที่ยวแบบชาว Pantip
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 ) ******

หลังจากที่กฤษฎาสอบมิดเทอมเสร็จ กำลังเดินทางกลับบ้านก็ได้หยิบโทรศัพท์ขึ้นมาเช็คข่าวสารต่างๆ แต่ก็ต้องสะดุดสิ่งที่เพื่อนของกฤษฎานั้นแชร์มาให้ นั่นคือกระทู้ที่มีหัวข้อว่า "ทริปไปเที่ยวโดยใช้ตังน้อยที่สุด" by Pantip กฤษฎาก็ได้เข้ากระทู้ไปอ่านจึงได้สะดุดกับบางประโยคของกระทู้นี้  นั่นคือการคำนวณว่าถ้าหากเรามีเงิน k บาท เราสามารถซื้อของให้เงินหมดพอดี (ไม่เหลือไม่ขาด) ได้หรือไม่ ถ้าได้จะได้สินค้าราคาเท่าใดบ้าง (หาทุกค่าที่ซื้อได้)  ถึงแม้ว่าของจะมีราคาเท่ากันก็ถือว่าเป็นของคนละชิ้นอยู่ดี  กฤษฎาจึงได้อยากไหว้วานน้องๆปีสอง วิศวกรรมคอมพิวเตอร์ ในการช่วยเขียนโปรแกรมแบบ Recursive ในการช่วยหาว่ากฤษฎาจะซื้อของได้ทั้งหมดกี่แบบและแต่ละแบบมีราคาของเท่าไหร่บ้าง
****** รายละเอียด Input ******
โดย Input จะแบ่งเป้นทั้งหมด 2 ฝั่ง ได้แก่   ซ้าย : จำนวนเงินที่กฤษฎามี   |    ขวา : ราคาของสินค้าแต่ละชิ้น

****** Output ******
รับประกันว่ากฤษฎาจะซื้อของได้อย่างน้อย 1 pattern

    Testcase : #1
        Enter Input (Money, Product) : 20/20 10 5 5 3 2 20 10
        20
        10 5 5
        10 5 3 2
        10 5 3 2
        10 10
        5 5 10
        5 3 2 10
        5 3 2 10
        20
        Krisada can purchase Product: [20, 10, 5, 5, 3, 2, 20, 10] with: 20 Baht | 9 Pattern

    Testcase : #2
        Enter Input (Money, Product) : 3/3 1 1 4 1 2 2 3
        3
        1 1 1
        1 2
        1 2
        1 2
        1 2
        1 2
        1 2
        3
        Krisada can purchase Product: [3, 1, 1, 4, 1, 2, 2, 3] with: 3 Baht | 9 Pattern

    Testcase : #3
        Enter Input (Money, Product) : 3/5 10 9 1 28 9 2 12 1 98 723 3
        1 2
        2 1
        3
        Krisada can purchase Product: [5, 10, 9, 1, 28, 9, 2, 12, 1, 98, 723, 3] with: 3 Baht | 3 Pattern

    Testcase : #4
        Enter Input (Money, Product) : 99/216 67 59602 20 523 5 2545 2 97 99 32 515
        67 32
        2 97
        99
        Krisada can purchase Product: [216, 67, 59602, 20, 523, 5, 2545, 2, 97, 99, 32, 515] with: 99 Baht | 3 Pattern
'''
count = 0
def printSack(path, maxi):
  global arr, count
  count += 1
  for i in range(maxi+1):
    print(arr[path[i]], end = ' ')
  print()

def pantip(path, i, k, n):
  global N, arr

  if n< N:    
    price = arr[n]   

    if k < price:               # ถ้าเงินไม่พอให้ไป index ต่อไป
      pantip(path, i, k, n+1) 
    else:                       # ถ้าซื้อได้
      k -= price  
      path[i] = n 

      if k == 0:                # ซื้อครบ
        printSack(path, i)
      else:           
        pantip(path, i+1, k, n+1)   # ถ้าเงินยังเหลือ
        
      pantip(path, i, k+price, n+1)   
  return count


inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
N = len(arr)         # จำนวนสินค้า
path = N*[-1]        # ข้อมูลที่เก็บมา (ว่าง)
k = int(inp[0])      # จำนวนเงิน
i = 0                # index ข้อมูล
n = 0                # index สินค้า

pattern = pantip(path, i, k,n)
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))