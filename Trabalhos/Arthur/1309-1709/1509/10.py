valor_divida_inicial = float(input("Informe o valor inicial da dívida: "))
juros_mensal = float(input("Informe a taxa de juros mensal: "))
valor_mensal_pago = float(input("Informe o valor mensal a ser pago: "))

valor_total = 0
quantidade_meses = 0

while(valor_divida > 0):
    juros = (valor_divida / 100) * juros_mensal
    if valor_mensal_pago <= juros:
        print("Sua dívida nunca será paga!")
        break
    else:
        valor_divida = valor_divida + juros - valor_mensal_pago 
        quantidade_meses += 1

if quantidade_meses > 0:
    print(f"O valor de R${valor_divida_inicial} será pago em: {quantidade_meses} meses!")
else:
    print("Aumente o valor mensal pago!")