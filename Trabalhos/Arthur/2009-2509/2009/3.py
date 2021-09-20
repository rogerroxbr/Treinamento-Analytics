"""
Bubble Sort é um algoritmo de ordenação que pode ser aplicado em Arrays e 
Listas dinâmicas. Se o objetivo é ordenar os valores em forma decrescente, 
então, a posição atual é comparada com a próxima posição e, se a posição 
atual for maior que a posição posterior, é realizada a troca dos valores 
nessa posição. Caso contrário, não é realizada a troca, apenas passa-se 
para o próximo par de comparações.
"""

L = [7,4,3,12,8]
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
        print(L)
        x += 1
    if not trocou:
        break
    fim -= 1

for e in L:
    print(e)