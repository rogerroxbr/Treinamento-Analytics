ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print(f"Existem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"Digite F para adicionar um cliente ao fim da fila,"
          f" ou A para realizar o atendimento. S para sair")
    op = input("Operação F, A ou S: ")
    if op == 'A':
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido}")
        else:
            print(f"Fila vazia ! Ninguem para atender.")
    elif op == 'F':
        ultimo += 1 # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif op == 'S':
        break
    else:
        print(f"Operação inválida! Digite apenas F, A ou S")

