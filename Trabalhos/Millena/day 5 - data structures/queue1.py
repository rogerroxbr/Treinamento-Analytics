ultimo = 10
fila = list(range(1, ultimo+1))

# instructions = input("Digite as operações desejadas F, A, S:")
# print(instructions[0])

while True:
    print(f"Existem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila} ")
    print(f"Digite F para adicionar um cliente ao fim da fila, ou A para realizar"
          f" o atendimento. S para sair")
    op = input("Operacao F, A ou S:")
    x = 0
    sair = False

    while x < len(op):
        if op[x] == 'A':
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print(f"Cliente: {atendido}")
            else:
                print(f"Fila vazia! Ninguem para atender.")
        elif op[x] == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif op[x] == 'S':
            sair = True
            break
        else:
            print(f"Operacao inválida! Digite apenas F, A ou S")
        x +=1
    if sair:
        break
