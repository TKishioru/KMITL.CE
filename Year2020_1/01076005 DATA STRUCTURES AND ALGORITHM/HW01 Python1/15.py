num = int(input('Enter Input : '))
y = 0
while y < num+1:
    i = 0
    while i < 1+num-y:
        print('.',end='')
        i+=1
    
    j = 0
    while j < 1+y:
        print('#',end='')
        j+=1
    if y == 0:
        i = 0
        while i < 2+num:
            print('+',end='')
            i+=1
    else:
        print('+',end='')
        i = 0
        while i < num:
            print('#',end='')
            i+=1
        print('+',end='')
    print()
    y += 1
a = 0
while a < 2:
    z = 0
    while z < 2+num:
        print('#',end='')
        z+=1
    b = 0
    while b < 2+num:
        print('+',end='')
        b+=1
    print()
    a+=1

c = 0
while c < 1+num:
    if c == num:
        i = 0
        while i < 2+num:
            print('#',end='')
            i+=1
    else:
        print('#',end='')
        i = 0
        while i < num:
            print('+',end='')
            i+=1
        print('#',end='')
    i = 0
    while i < 1+num-c:
        print('+',end='')
        i+=1
    
    j = 0
    while j < 1+c:
        print('.',end='')
        j+=1
    print()
    c += 1
