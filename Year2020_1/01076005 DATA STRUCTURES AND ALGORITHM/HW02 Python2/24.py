def zero(lis):
    if len(lis) < 3:
        return "Array Input Length Must More Than 2"
    shownum = list()
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            for k in range(j+1, len(lis)):
                if lis[i]+lis[j]+lis[k] == 0 and [lis[i], lis[j], lis[k]] not in shownum:
                    shownum.append([lis[i], lis[j], lis[k]])
    return shownum

if __name__ == '__main__':
    num = list(map(int, input("Enter Your List : ").split()))
    print(zero(num))