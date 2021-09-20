def function():
    num = int(input("Quantos números? "))
    x = 0
    l = [0] * num

    while x < len(l):
        l[x] = int(input(f"Digite o elemento {x} da Lista: "))
        x += 1

    return l

L1 = function()
L2 = function()

L1.extend(L2)

print(L1)