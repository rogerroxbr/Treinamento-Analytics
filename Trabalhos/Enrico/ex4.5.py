salario = float(input("Informe seu salário: "))

if salario >= 1250.0:
    aumento = salario * 0.1
if salario < 1250.0:
    aumento = salario * 0.15

print(f"O seu aumento foi de: R${aumento:.2f}. E o seu salário final é de: R${aumento + salario:.2f}")