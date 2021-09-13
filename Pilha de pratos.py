prato = 5
pilha = list(range(1, prato+1))
while True:
    print(f"Existem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print(f"Digite E para empilhar um novo prato,"
          f" ou D para desempilhar. S para sair")
    op = input("Operação E, D ou S: ")
    if op == 'D':
        if (len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print(f"Pilha vazia ! Nada para lavar.")
    elif op == 'E':
        prato += 1  # Novo prato
        pilha.append(prato)
    elif op == 'S':
        break
    else:
        print(f"Operação inválida! Digite apenas D, E ou S! ")
