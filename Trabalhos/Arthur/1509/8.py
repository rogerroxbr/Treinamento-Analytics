deposito_inicial = float(input("Informe o depósito inicial: "))
juros = float(input("Informe o juros da poupança: "))

soma = deposito_inicial
juros_atual = 0
meses = 0

print('\n')

while meses <= 24:
    juros_atual = (soma / 100) * juros
    soma += juros_atual
    print(f'{deposito_inicial} ~ {meses} meses : {soma:.2f}')
    meses += 1