# EX5.14
count = 0
soma = 0

while True:
    numero = int(input("Escreva um número inteiro: "))
    count +=1
    if numero == 0:
        break
    soma = soma + numero

print(f'Você digitou {count} números, a soma desses números é igual: {soma} e média deles: {soma/count:.2f}')

# EX5.15

preco_final = 0
preco = 0

while True:
    cod = int(input("Informe o código do produto (0 para sair): "))

    if cod == 0:
        break
    elif cod == 1:
        preco = 0.5
    elif cod == 2:
        preco = 1.0
    elif cod == 3:
        preco = 4.0
    elif cod == 5:
        preco = 7.0
    elif cod == 9:
        preco = 8.0
    else:
        print('Código inválido!')
    if preco != 0:
        qtd = int(input("Informe a quantidade: "))
        preco_final = preco_final + (preco * qtd)
print(f'Total a pagar: {preco_final}')

# EX5.15 - 5.19

valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100.0
a_pagar = valor

while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas +=1
    else:
        print(f"{cedulas} de R$ {atual}")
        if a_pagar == 0.0:
            break
        if atual == 100.0:
            atual = 50.0
        if atual == 50.0:
            atual = 20.0
        elif atual == 20.0:
            atual = 10.0
        elif atual == 10.0:
            atual = 5.0
        elif atual == 5.0:
            atual = 1.0
        cedulas = 0

# EX5.15 - 5.19

valor = float(input("Digite o valor a pagar: "))
cedulas = 0
moedas = 0
atual = 100.0
a_pagar = valor

while True:
    a_pagar = float(format(a_pagar, ".2f"))
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas +=1
    else:
        if atual >= 1:
            print(f"{cedulas} de R$ {atual}")
        else:
            print(f"{moedas} de R$ {atual}")
        if a_pagar == 0:
            break
        if atual == 100.0:
            atual = 50.0
        if atual == 50.0:
            atual = 20.0
        elif atual == 20.0:
            atual = 10.0
        elif atual == 10.0:
            atual = 5.0
        elif atual == 5.0:
            atual = 1.0
        elif atual == 1.0:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual == 0.05
        cedulas = 0

# EX3.8

notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"Nota {x}: "))
    soma += notas[x]
    x +=1
x = 0
while x < 7:
    print(f"Nota {x}: {notas[x]:.2f}")
    x +=1
print(f"Média: {soma/x:.2f}")

# EX6.2
list1 = []
list2 = []

while True:
    num = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if num == 0:
        break
    list1.append(num)
while True:
    num = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if num == 0:
        break
    list2.append(num)

list3 = []

for i in list1:
    if i not in list2:
        list3.append(i)

for x in list2:
    if x not in list2:
        list3.append(x)

print(f"\n{list3}")
