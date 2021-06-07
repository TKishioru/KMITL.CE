import statistics
from collections import Counter
from itertools import groupby

print("*** Election ***")

people = int(input('Enter a number of voter(s) : '))
inputList = input().split()
newList = []
count = 0
for i in range(people) :
    inputList[i]= int(inputList[i])
    if inputList[i]<1 or inputList[i] >20:
        count+=1
    else : newList.append(inputList[i])

freqs = groupby(Counter(newList).most_common(), lambda x:x[1])

if count == people or len([val for val,count in next(freqs)[1]]) >1 or people < 1 or people !=len(inputList):
    print("*** No Candidate Wins ***")
else :
    print(statistics.mode(newList))