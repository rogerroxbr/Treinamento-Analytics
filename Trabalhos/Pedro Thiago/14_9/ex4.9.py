salario = float(input('Digite o salário da pessoa: \n'))
valor_da_casa = float(input('Digite o valor da casa: \n'))
quantidade_de_meses = 12 * float(input('Digite a quantidade de anos para o pagamento: \n'))

prestacao_mensal = valor_da_casa / quantidade_de_meses

if salario * 0.3 < prestacao_mensal:
    print('Não aprovado!')
else:
    print(f'Aprovado! valor a pagar: {prestacao_mensal:.2f}')