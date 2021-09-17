a = []
b = []
c = []

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

for x in a:
    if x not in c:
        c.append(x)

for x in b:
    if x not in c:
        c.append(x)

print(c)
