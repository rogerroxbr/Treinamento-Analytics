L, L1, L2 = [], [], []

i=0
L1 += [0]
while L1[i] != "END":
    x = input("L2: Informe um valor (END p/ fim):")
    if x != "END":
        L1.append(x)
        i += 1

i=0
L2 += [0]
while L2[i] != "END":
    x = input("L2: Informe um valor (END p/ fim):")
    if x != "END":
        L2.append(x)
        i += 1

L = L1 + L2
print(L)