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

l3.extend(l1)
l3.extend(l2)
print('\n')
print(l3)