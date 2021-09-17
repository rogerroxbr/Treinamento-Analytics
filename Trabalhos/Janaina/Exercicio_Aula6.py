'''
ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print(f'Existem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print(f'Digite F para adicionar um cliente ao fim da fila,\n'
          f'ou A para realizar o atendimento, \n'
          f'ou S para sair')
    op = input('Operação F, A ou S:')
    if op == 'A':
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print(f'Cliente{atendido}')
        else:
            print(f'Fila vazia ! Ninguem para atender.')
    elif op == 'F':
        ultimo += 1 # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif op == 'S':
        break
    else:
        print(f'Operação inválida! Digite apenas F, A ou S')
'''
'''
prato = 5
pilha = list(range(1, prato+1))
while True:
    print(f'Existem {len(pilha)} pratos na pilha')
    print(f'Pilha atual: {pilha}')
    print(f'Digite E para empilhar um prato,\n'
          f'ou D para desempilhar \n'
          f'ou S para sair:')
    op = input('Operação E, D ou S:')
    if op == 'D':
        if (len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print(f'Prato {lavado}')
        else:
            print(f'Pilha vazia ! Nada para lavar.')
    elif op == 'E':
        prato += 1  # Novo prato
        pilha.append(prato)
    elif op == 'S':
        break
    else:
        print(f'Operação inválida! Digite apenas D, E ou S')
'''

l = [15, 7, 27, 39]
p = int(input("Digite o valor a ser pesquisado"))
achou = False
x = 0

while x < len(l):
    if l[x] == p:
        achou = True
        break
    x += 1
    if achou:
        print(f'{p} achado na posição {x}')
    else:
        print((f'{p} não encontrado'))














