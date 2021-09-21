'''
compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    quantidade = int(input("Quantidade: "))
    price = float(input("Preço: "))
    compras.append([produto, quantidade, price])
soma = 0.0
for e in compras:
    print(f"{e[0]} x {e[1]}, {e[2]:5.2f} = {e[1]} * {e[2]:6.2f}")
    soma += e[1] * e[2]
print(f"Total: [soma:7.2f")
'''
import turtle

'''
L = [7, 4, 3, 7, 12, 8]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim-1):
        if L[x] > L[x+1]:
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)
'''
'''
lista = ['Luiz', 'Joao', 1, 2, 3]
n1, n2, * outra = lista
print(lista)
'''
'''
y = 10

for x in range(0, 11):
    print(f"{x} {y - x}")
'''
'''
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
'''
'''
palavras = ["abacaxi", "banana"]
indice = int(input("Digite um numero: "))
palavra = palavras[(indice * 776) % len(palavras)]

for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha=""
    for letra in palavra:
        senha +=letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX : ")
    print("X O " if erros >= 1 else "X")
    linha2=""
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " \| "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3=""
    if erros == 5:
        linha3+=" / "
    elif erros>=6:
        linha3+=" / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
'''
'''
palavras = [
    "casa",
    "bola",
    "mangueira",
    "uva",
    "quiabo",
    "computador",
    "cobra",
    "lentilha",
    "arroz"
]
índice = int(input("Digite um numero:"))
palavra = palavras[(índice * 776) % len(palavras)]
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
linhas_txt = """
X==:==
X  :
X
X
X
X
=======
"""
linhas = []
for linha in linhas_txt.splitlines():
    linhas.append(list(linha))
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            if erros == 1:
                linhas[3][3] = "O"
            elif erros == 2:
                linhas[4][3] = "|"
            elif erros == 3:
                linhas[4][2] = "\\"
            elif erros == 4:
                linhas[4][4] = "/"
            elif erros == 5:
                linhas[5][2] = "/"
            elif erros == 6:
                linhas[5][4] = "\\"
    for l in linhas:
        print("".join(l))
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
'''

from turtle import Turtle
t = turtle.Turtle()
t.speed(1)
t.forward(100)
t.right(200)
#t.left(90)
#t.back(200)











