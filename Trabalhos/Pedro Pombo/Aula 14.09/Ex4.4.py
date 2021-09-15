salario = float(input("Digite o seu salario: "))

if salario >= 1250:
    print(f"O seu aumento foi de: R${salario * 0.1:.2f}. E o seu salário final é de : R${salario * 1.1:.2f}")
if salario < 1250:
    print(f"O seu aumento foi de: R${salario * 0.15:.2f}. E o seu salário final é de : R${salario * 1.15:.2f}")

