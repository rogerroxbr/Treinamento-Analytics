L = [15, 7, 27, 39]

x = int(input("Digite o valor a ser pesquisado: "))
# segundo = int(input("Digite o valor a ser pesquisado: "))

x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posicao {x}")
        break
    x += 1

if x == len(L):
    print(f"{p} não encontrado")