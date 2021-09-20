def function():
    num = int(input("Quantos números? "))
    i = 0
    l = [0] * num

    while i < len(l):
        l[i] = int(input(f"Digite o elemento {i} da Lista: "))
        i += 1

    return l

L3 = []
x = 0
holder = function() + function()

while x < len(holder):
    if L3.count(holder[x]) == 0:
        L3.append(holder[x])
    x += 1

print(L3)
