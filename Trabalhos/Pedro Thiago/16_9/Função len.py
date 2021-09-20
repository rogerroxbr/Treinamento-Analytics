import random

x = 0
Tamanho = int(input('Quantos números você quer? '))
L = [0] * Tamanho

while x < Tamanho:
    L[x] = random.randint(0, 99)
    x += 1

x = 0

while x < len(L):
    print(L[x])
    x += 1