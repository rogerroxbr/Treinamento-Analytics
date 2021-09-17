houseValue = float(input("Digite o valor da casa "))
wage = float(input("Digite o salario "))
yearsToPay = int(input("Digite a quantidade de anos a pagar "))
monthsToPay = yearsToPay * 12

monthlyPayment = houseValue/monthsToPay
limitMonthlyPayment = wage * 0.3

if monthlyPayment < limitMonthlyPayment:
    print(f'O valor da prestacao mensal é de: {monthlyPayment:.2f}')
else:
    print(f'O valor da prestacao mensal não pode ser maior que 30%')
