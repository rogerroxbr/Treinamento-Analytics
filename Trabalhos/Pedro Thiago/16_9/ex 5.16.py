valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
a_pagar = valor

if valor != 0:
    while True:
        if atual <= a_pagar:
            a_pagar -= atual
            cedulas += 1
        else:
            print(f"{cedulas} de R$ {atual}")
            if a_pagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0
else:
    print('Nada a pagar!')