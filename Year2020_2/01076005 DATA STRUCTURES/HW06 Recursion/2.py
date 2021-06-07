'''
Chapter : 6 - item : 2 - Palindrome
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่
    Testcase : #1
        Enter Input : abba
        'abba' is palindrome

    Testcase : #2
        Enter Input : abgba
        'abgba' is palindrome

    Testcase : #3
        Enter Input : abcdefkgfedfe
        'abcdefkgfedfe' is not palindrome
'''
check = 'T'
def palindrome(i,txt):
    n = len(txt)-1
    if txt[i] != txt[n-i]:
        return '\'' + txt + '\'' + ' is not palindrome'
    if i == n:
        return '\'' + txt + '\'' + ' is palindrome'
    return palindrome(i+1,txt)
inp = input('Enter Input : ')
print(palindrome(0,inp))