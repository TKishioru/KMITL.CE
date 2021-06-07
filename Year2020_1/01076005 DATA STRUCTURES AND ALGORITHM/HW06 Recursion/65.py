#Draw
def rec_row(number, row):
    print('_'*(number-row), end="")
    print('#'*row, end="")
    print('')

def rec_pattern(number, row):
    if number > 0:
        if row < number:
            row += 1
            rec_row(number, row)
            rec_pattern(number, row)
    elif number == 0:
        print('Not Draw!')
    else:
        if row < abs(number):
            rec_row(abs(number), abs(number)-row)
            row += 1
            rec_pattern(number, row)

rec_pattern(int(input("Enter Input : ")),0)