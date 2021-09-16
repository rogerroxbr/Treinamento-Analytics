a = [1, 2, 3, 4, 5]
b = [5, 7, 8, 9, 10]
c = []

for x in a:
    if x not in c:
        c.append(x)

for x in b:
    if x not in c:
        c.append(x)

print(c)
