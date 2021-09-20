valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
a_pagar = valor

if valor != 0:
    while True:
        a_pagar = float(format(a_pagar, ".2f"))
        if atual <= a_pagar:
            a_pagar -= atual
            cedulas += 1
        else:
            if atual >= 1:
                print(f"{cedulas} de R$ {atual}")
            else:
                print(f"{cedulas} de moeda de R$ {atual}")
            if a_pagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.01
            cedulas = 0
else:
    print('Nada a pagar!')