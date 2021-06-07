"""
Chapter : 3 - item : 2 - Parenthesis Matching
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา
โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด
1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด
2. วงเล็บปิดเกิน
3. วงเล็บเปิดเกิน

    Testcase : #1 
        Enter expresion : [[)))))
        [[))))) Unmatch open-close  

    Testcase : #2 
        Enter expresion : [[))
        [[)) Unmatch open-close  

    Testcase : #3
        Enter expresion : (())))
        (()))) close paren excess

    Testcase : #4 
        Enter expresion : )}]
        )}] close paren excess

    Testcase : #5 
        Enter expresion : (((
        ((( open paren excess   3 : (((

    Testcase : #6 
        Enter expresion : (a+c)(a-b)*c(-a
        (a+c)(a-b)*c(-a open paren excess   1 : (

"""
op = list()
ed = list()
k = 0
txt = input('Enter expresion : ')
for i in range(0,len(txt)):
    if txt[i] in '({[':
        op.append(txt[i])
    elif txt[i] in ')}]':
        ed.append(txt[i])

for i in range(len(op)-1,-1,-1):
    for j in range(len(ed)-1,-1,-1):
        #print(op[i],ed[j])
        if len(op)>0 and len(ed)>0:
            #print(i,j)
            if op[i] == '(' and ed[j] == ')':
                op.pop(i)
                ed.pop(j)
                k += 1
                break
            elif op[i] == '{' and ed[j] == '}': 
                op.pop(i)
                ed.pop(j)
                k += 1
                break
            elif op[i] == '[' and ed[j] == ']':
                op.pop(i)
                ed.pop(j)
                k += 1
                break
        
#print(op)
#print(ed)
if len(op) == 0 and len(ed) == 0:
    print(f'{txt} MATCH')
elif k == 0 and len(op) > 0 and len(ed) > 0:
    print(f'{txt} Unmatch open-close')
elif k > 0 and len(op) == 0 and len(ed) > 0:
    print(f'{txt} close paren excess')
elif len(op) == 0 and len(ed) > 0:
    print(f'{txt} close paren excess')
elif len(op) > 0 and len(ed) >= 0:
    s = ""
    for i in range(0,len(op)):
        s += op[i]
    print(f'{txt} open paren excess   {len(op)} : {s}')