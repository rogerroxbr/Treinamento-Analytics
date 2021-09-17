"""
soma = 0
quantidade = 0

while True:
    num1 = int(input("Digite o numero:   ou 0 para sair"))
    if num1 == 0:
        break
    quantidade += 1
    soma = soma + num1

print(f"O total de numeros digitados é: {quantidade}  a soma desses "
      f"numeros é: {soma}  e a média é: {soma/quantidade}")
"""
"""
preco = 0
apagar = 0
while True:
    codigo = int(input("Codigo da mercadoria (0 sair)"))
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido!")
    if preco != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preco * quantidade)
print(f"Total a pagar R$ {apagar:8.2f}")
"""
'''
valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
a_pagar = valor

while True:
    pagar = float(format(pagar, ".2f"))
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print(f"{cedulas} de cedulas R$ {atual}")
        else:
            print(f"{cedulas} de moedas R$ {atual}")
        if a_pagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        cedulas = 0
'''
'''
lista = [1,2,3,4,5]
lista[1] = 9
print(lista)
'''
'''
notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Nota {x}: "))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f"Nota {x}: {notas[x]:6.2f}")
    x =+ 1
print(f"Média: {soma/x:5.2f}")
'''
'''
L = [1,2,3,4,5]
L[0:5]

L[:5]

L[:-1]

L[3:]

L[-1]
'''
'''
lista1 = [15, 8, 5]
lista2 = []

print(len(lista1))
print(len(lista2))
'''
'''
L = [7,8,9,10,11,12,13,14,15]
x = 0

while x < len(L):
     print(L[x])
     x += 1
'''
primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if e == 0:
        break
    primeira.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if e == 0:
        break
    segunda.append(e)
terceira = []
duas_listas = primeira[:]
duas_listas.extend(segunda)
x = 0
while x < len(duas_listas):
    y = 0
    while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break
        y = y + 1
    if y == len(terceira):
        terceira.append(duas_listas[x])
    x = x + 1
x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x = x + 1








