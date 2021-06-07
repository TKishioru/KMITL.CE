def Queue(inpQ):
    return list(inpQ)
def encodemsg(q1, q2):
    de = []
    lst = []
    j = 0
    for k in range(0,len(q1)):
        if q1[k] != ' ':
            lst.append(q1[k])
    for i in range(0,len(lst)):
        if j == len(q2):
            j = 0
        st = ord(lst[i])
        n = int(q2[j])
        if st+n > 122: #z
            x = 122 - st
            n -= x
            en = chr(96 + n)
        elif st+n > 90 and st + n < 97: #Z
            x = 90 - st
            n -= x
            en = chr(64 + n)
        else:    
            en = chr(st + n)
        de.append(en)
        j += 1
    print("Encode message is : " , de)

def decodemsg(q1, q2):
    lst = []
    for k in range(0,len(q1)):
        if q1[k] != ' ':
            lst.append(q1[k])
    print("Decode message is : " , lst)

inpQ = input('Enter String and Code : ').split(',')
string = inpQ[0]
number = inpQ[1]

#อาจารย์ให้มา
q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)