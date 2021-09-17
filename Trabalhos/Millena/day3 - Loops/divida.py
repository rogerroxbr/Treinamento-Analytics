divida = float(input("Digite o valor da divida "))
taxa = float(input("Digite a taxa de juros"))/100
pagamento = float(input("Digite o valor do deposito mensal "))

total = 0
i = 0

if pagamento < (divida*taxa):
    print("Voce nao vai conseguir pagar sua divida")
else:
    jurosPago = 0
    saldo = divida
    mes = 1

    while saldo >= 0:
        mes += 1
        jurosMensal = saldo * taxa /100
        saldo = jurosMensal + (taxa/12 * divida) - pagamento
        total += divida
        print(f'Seu saldo é de {saldo} no mes {mes}')

print(f'Para pagar uma divida de: {saldo} voce levara {mes} meses')
