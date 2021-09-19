# EX MAIOR/MENOR listas
t = [-10, -8, 0, 2, 5, -2, -4]
maior = 0
menor = 0
count = 0
media = 0

for i in t:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
    count += 1
    media += i

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {media/count:.2f}')

# Mini-game turtle
from turtle import Turtle

t = Turtle()
t.speed(1)
while True:
    direction = input('Qual direção a tartaruga deve andar(frente/tras) : ')
    pixelsD = int(input(f'Quantos pixels quer andar para {direction}: '))
    rotation = input('Qual rotação a tartaruga deve andar(esquerda/direita): ')
    pixelsR = int(input(f'Quantos pixels quer andar para {rotation}: '))
    if direction == 'frente' and rotation == 'esquerda':
        t.forward(pixelsD)
        t.left(pixelsR)
    elif direction == 'frente' and rotation == 'direita':
            t.forward(pixelsD)
            t.right(pixelsR)
    if direction == 'tras' and rotation == 'esquerda':
        t.backward(pixelsD)
        t.left(pixelsR)
    elif direction == 'tras' and rotation == 'direita':
            t.backward(pixelsD)
            t.right(pixelsR)
    stats = input('Deseja continuar(S ou N): ')
    if stats == 'N':
        break

'''Exercícios complementares'''
# 1°
for x in range(9):
    print(x)
print('\n')

# 2°
for y in range(10,1,-1):
    print(y)
# 3°
for i in range(1,21):
    print(i)
# 4°
list = []

for i in range(1,100001):
    list.append(i)
print(list)

# 5°
list = []

for i in range(1,100001):
    list.append(i)
print(f'Valor máximo: {max(list)}')
print(f'Valor mínimo: {min(list)}')
print(f'Soma da lista: {sum(list)}')

# 6°
list = list(range(1,20,2))
for i in list:
    print(i)

# 7°
list = list(range(3,31,3))
for i in list:
    print(i)

# 8°
list = []
for i in range(1,11):
    list.append(i**3)
print(list)
