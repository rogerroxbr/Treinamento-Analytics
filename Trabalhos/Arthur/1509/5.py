n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
contador = 0
total = 0

while contador != n2:
    total += n1
    contador += 1

print(f'{n1} * {n2}: {total}')