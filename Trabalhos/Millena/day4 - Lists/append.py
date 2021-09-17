firstList = []
secondList = []

elem = int(input('Type the element to insert into the first list '))
while elem != 0:
    firstList.append(elem)
    elem = int(input())

elem = int(input('Type the element to insert into the second list '))
while elem != 0:
    secondList.append(elem)
    elem = int(input())

firstList.extend(secondList)
print(firstList)

newList = []
for elem in firstList:
    if elem not in newList:
        newList.append(elem)

print(newList)
