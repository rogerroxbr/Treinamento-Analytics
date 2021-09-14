a = int(input("valor a: "))
b = int(input("valor b: "))
c = int(input("valor c: "))

if a > b and a > c:
    print(f"valor A é o maior. Valor: {a}")
elif b > c:
    print(f"valor B é o maior. Valor: {b}")
else:
    print(f"valor C é o maior. Valor: {c}")

if a < b and a < c:
    print(f"valor A é o menor. Valor: {a}")
elif b < c:
    print(f"valor B é o menor. Valor: {b}")
else:
    print(f"valor C é o menor. Valor: {c}")
