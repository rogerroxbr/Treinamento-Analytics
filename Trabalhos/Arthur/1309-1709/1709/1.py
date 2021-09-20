ultimo = 10
fila = list(range(1, ultimo+1))
print(f"Digite F para adicionar um cliente ao fim da fila ou A para realizar o atendimento e S para sair!")

while True:
    print(f"Existem {len(fila)} clientes na fila!")
    print(f"Existem atual: {fila}!")
    op = input("Informe F, A ou S: ")
    op = op.upper()
    if op == 'A':
        if len(fila) >= 1:
            atendido = fila.pop(0)
            print(f"Cliente {atendido}")
        else:
            print("\n")
            print(f"Fila vazia!")
            print("\n")
    elif op == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif op == 'S':
        break
    else:
        print(f"Operação inválida!")