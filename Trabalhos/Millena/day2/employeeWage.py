wage = float(input("Informe seu salario: "))

if wage >= 1250.0:
    increase = wage * 0.1
else:
    increase = wage * 0.15

print(f'O total do salario é: {wage + increase}')

