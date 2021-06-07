import statistics

print("*** Election ***")

people = int(input('Enter a number of voter(s) : '))
inputList = input().split()
newList = []
count = 0
for i in range(people) :
    inputList[i]= int(inputList[i])
    if inputList[i]>0 and inputList[i] <21:
        newList.append(inputList[i])
    else:
        count+=1

if count==people: 
    print("*** No Candidate Wins ***")
else :
    print(statistics.mode(newList))