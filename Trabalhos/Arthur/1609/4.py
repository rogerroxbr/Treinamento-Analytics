notas = [0]*7
soma = 0
x = 0

while x < 7:
    notas[x] = float(input(f"Nota {x + 1}: "))
    soma += notas[x]
    x += 1

x = 0
print("\n")

while x < 7:
    print(f"Nota {x + 1}: {notas[x]:.2f}")
    x += 1

print("\n")
print(f"Média: {soma/x:.2f}")
