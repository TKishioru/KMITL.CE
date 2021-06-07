#palindrome
check = 0
def palindrome(i,inp):

    global check
    
    if i < len(inp):
        j = (i + 1) * -1
        if inp[i] == inp[j]:
            check += 1
        i += 1
        return palindrome(i,inp)

    if check == len(inp):
        print(f'\'{inp}\' is palindrome')
    else:
        print(f'\'{inp}\' is not palindrome')
     
inp = input("Enter Input : ")
palindrome(0,inp)