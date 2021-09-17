ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = []

while True:
    print(f"Existem {len(fila1)} clientes na fila 1")
    print(f"Fila atual: {fila1}")
    print(f"Existem {len(fila2)} clientes na fila 2")
    print(f"Fila atual: {fila2}")
    print(f"Digite F para adicionar um cliente ao fim da fila 1,"
          f"ou A para realizar o atendimento da fila 1.")
    print(f"Digite G para adicionar um cliente ao fim da fila 2,"
          f"ou B para realizar o atendimento da fila 2.")
    print("S para sair")
    ops = input("operações F, A ou S: ")

    for op in ops:
        if op == 'A':
            if (len(fila1)) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido}")
            else:
                print(f"Fila vazia 1! Ninguém para atender.")
        elif op == 'F':
            ultimo += 1
            fila1.append(ultimo)
        elif op == 'B':
            if (len(fila2)) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido}")
            else:
                print(f"Fila vazia 2! Ninguém para atender.")
        elif op == 'G':
            ultimo += 1
            fila2.append(ultimo)
        elif op == 'S':
            break
        else:
            print(f"Operação inválida! Digite apenas F, A, G, B ou S")
