a = []
b = []

print("primeira lista ---")
while True:
    i = int(input("digite um número (0 para sair): "))
    if i == 0:
        break
    a.append(i)

print("segunda lista ---")
while True:
    i = int(input("digite um número (0 para sair): "))
    if i == 0:
        break
    b.append(i)

a.extend(b)

print(a)
