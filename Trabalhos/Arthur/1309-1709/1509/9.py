deposito_inicial = float(input("Informe o depósito inicial: "))
deposito_mensal = float(input("Informe os valor dos depósitos mensais: "))
juros = float(input("Informe a taxa de juros mensal da poupança: "))

juros_atual = 0
meses = 1
soma = deposito_inicial

print('\n')

while meses <= 24:
    juros_atual = (soma / 100) * juros
    soma = soma + juros_atual + deposito_mensal
    print(f'{deposito_inicial} ~ {meses} mese(s) : {soma:.2f}')
    meses += 1