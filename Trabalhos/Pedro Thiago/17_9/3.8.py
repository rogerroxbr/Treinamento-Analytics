ultimo = 10
fila = list(range(1, ultimo +1))

while True:
    print(f"Existem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"Digite F para adiconar um cliente ao fim da Fila,"
          f"ou A para realizar o atendimento. S para sair")
    op = input('Operação F, A ou S: ')
    if op == 'A':
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print(f"cliente {atendido}")
        else:
            print(f"Fila vazia! Ninguém pra atender.")
    elif op == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif op == 'S':
        break
    else:
        print(f'Operação inválida! Digite apenas F, A ou S')