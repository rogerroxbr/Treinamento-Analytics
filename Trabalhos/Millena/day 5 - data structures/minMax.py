L = [4,2,1,7]

maximo = L[0]
minimo = L[0]

for e in L:
    if e > maximo:
        maximo = e
    if e < minimo:
        minimo = e
print(f"O valor maximo é: {maximo} e o valor minimo é {minimo}")
