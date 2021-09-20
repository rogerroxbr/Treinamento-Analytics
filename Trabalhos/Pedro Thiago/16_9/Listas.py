num = int(input("Quantas notas? "))
notas = [0]*num
soma = 0
x = 0

while x < len(notas):
    notas[x] = float(input(f"Nota {x}: "))
    soma += notas [x]
    x += 1
x = 0

while x < len(notas):
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1

print(f"Soma: {soma}")
print(f"Média: {soma/x:5.2f}")
