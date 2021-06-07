"""
Chapter : 4 - item : 3 - code with queue
รับ string มาเข้าคิวหา secret code โดยรับ input คือ code เป็น string ยาว hint คือตัวแรกของรหัสที่ถูกต้อง

    **คำใบ้**
    **หาความต่างของ hint กับตัวแรกของประโยคแล้วนำมา +/- ตัวต่อไป
    ascii ของ "f" มีค่า = 102
    ascii ของ "g" มีค่า = 103
    ascii ของ "h" มีค่า = 104
    ascii ของ "i" มีค่า = 105
    ascii ของ "j" มีค่า = 106
    
    Testcase : #1 :
        Enter code,hint : gjstu`uftu,f
        ['f']
        ['f', 'i']
        ['f', 'i', 'r']
        ['f', 'i', 'r', 's']
        ['f', 'i', 'r', 's', 't']
        ['f', 'i', 'r', 's', 't', '_']
        ['f', 'i', 'r', 's', 't', '_', 't']
        ['f', 'i', 'r', 's', 't', '_', 't', 'e']
        ['f', 'i', 'r', 's', 't', '_', 't', 'e', 's']
        ['f', 'i', 'r', 's', 't', '_', 't', 'e', 's', 't']

    Testcase : #2 : 
        Enter code,hint : AforY((/,I
        ['I']
        ['I', 'n']
        ['I', 'n', 'w']
        ['I', 'n', 'w', 'z']
        ['I', 'n', 'w', 'z', 'a']
        ['I', 'n', 'w', 'z', 'a', '0']
        ['I', 'n', 'w', 'z', 'a', '0', '0']
        ['I', 'n', 'w', 'z', 'a', '0', '0', '7']

    Testcase : #3 :
        Enter code,hint : hiMf__jNcfGilhcha,n
        ['n']
        ['n', 'o']
        ['n', 'o', 'S']
        ['n', 'o', 'S', 'l']
        ['n', 'o', 'S', 'l', 'e']
        ['n', 'o', 'S', 'l', 'e', 'e']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l', 'M']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l', 'M', 'o']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l', 'M', 'o', 'r']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l', 'M', 'o', 'r', 'n']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l', 'M', 'o', 'r', 'n', 'i']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l', 'M', 'o', 'r', 'n', 'i', 'n']
        ['n', 'o', 'S', 'l', 'e', 'e', 'p', 'T', 'i', 'l', 'M', 'o', 'r', 'n', 'i', 'n', 'g']

"""
class Queue:
    def __init__(self):
        self.inp = list()
        self.prt = list()
        self.x = []
    def enqueue(self,data):
        self.inp.append(txt[i])
    def dequeue(self):
        for i in range(0,len(self.inp)):
            y = ord(self.inp[i]) + self.x
            self.prt.append(chr(y))
            print(self.prt)
    def peak(self):
        return self.inp.pop(0)
    def size(self):
        return len(self.inp)
    def isEmpty(self):
        if q.size <= 0:
            return False
        return True

q = Queue()
txt,hint = input('Enter code,hint : ').split(',')
for i in range(0,len(txt)):
    q.enqueue(txt[i])
    q.x = ord(hint) - ord(txt[0])
q.dequeue()