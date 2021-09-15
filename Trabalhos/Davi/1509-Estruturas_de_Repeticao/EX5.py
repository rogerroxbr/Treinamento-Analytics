fim = int(input("Digite oo último número a imprimir: "))
x = 1
i = 0

while x <= fim:
    if x % 3 == 0:
        print(x)
        i += 1
    if i == 10:
        break
    x += 1
