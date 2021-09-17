deposito = float(input("Digite o deposito inicial "))
taxa = float(input("Digite a taxa de juros "))
porcentagemTaxa = taxa / 100
investimento = float(input("Digite o valor do deposito mensal "))

total = 0
i = 0
while i <= 24:
    deposito = deposito + (porcentagemTaxa/12 * deposito) + investimento
    total += deposito
    i += 1
    print(f'Valor por mes: {deposito:.2f}')

print(f'Valor total: {total:.2f}')
