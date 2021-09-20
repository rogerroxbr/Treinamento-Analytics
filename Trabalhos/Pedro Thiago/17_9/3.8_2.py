L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a ser pesquisado: "))
v = int(input("Digite o segundo valor a ser pesquisado: "))
pPosicao = -1
vPosicao = -1
x = 0

while x < len(L):
    if L[x] == p:
        pPosicao = x
    if L[x] == v:
        vPosicao = x
    x += 1

if pPosicao != -1 and vPosicao != -1:
    print(f"{p} achado na posição {pPosicao}")
    print(f"{v} achado na posição {vPosicao}")
elif pPosicao != -1:
    print(f"{p} achado na posição {pPosicao}")
    print(f"{v} não foi encontrado")
elif vPosicao != -1:
    print(f"{p} não foi encontrado")
    print(f"{v} achado na posição {vPosicao}")
else:
    print(f"nenhum valor encontrado")
