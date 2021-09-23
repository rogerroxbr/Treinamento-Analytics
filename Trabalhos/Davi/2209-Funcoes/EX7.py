def soma(L):
    total = 0
    for x in range(0, len(L)):
        total += L[x]
    return total


L = [1, 7, 2, 9, 15]

print(soma(L))
