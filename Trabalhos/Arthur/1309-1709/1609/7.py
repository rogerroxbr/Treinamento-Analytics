print("Digite 0 para sair!")

l1 = []
l2 = []
l3 = []

print('\n')
print("*** 1a Lista ***")
print('\n')

while True:
    elemento = input("Informe um elemento: ")
    if elemento == "0":
        break
    else:
        l1.append(elemento)

print('\n')
print("*** 2a Lista ***")
print('\n')

while True:
    elemento = input("Informe um elemento: ")
    if elemento == "0":
        break
    else:
        l2.append(elemento)

for elemento in l1:
    if elemento not in l3:
        l3.append(elemento)
    else:
        continue

for elemento in l2:
    if elemento not in l3:
        l3.append(elemento)
    else:
        continue

print('\n')
print(l3)
