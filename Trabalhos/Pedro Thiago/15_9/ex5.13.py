start = int(input("Qual o valor da dívida? \n"))
tax = float(input("Qual o juros? (de forma decimal, ex: 0.03 para 3%)\n"))
month = int(input("Qual o valor pago mensal?\n"))
i = 0
taxtotal = 0
total = start

if (total * tax) > month:
    print('Você nunca conseguirá pagar!')
else:
    while total >= 0:
        taxtotal = taxtotal + (total * tax)
        total = (total * (tax + 1)) - month
        i += 1

    print(f'Demorará {i} mes(es) para pagar a dívida, com um total de {taxtotal:.2f} de taxa, pagando um total de: {start + taxtotal}')
