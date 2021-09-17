valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
a_pagar = valor

while True:
    a_pagar = float(format(a_pagar, ".2f"))
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} de R$ {atual}")
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
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas = 0