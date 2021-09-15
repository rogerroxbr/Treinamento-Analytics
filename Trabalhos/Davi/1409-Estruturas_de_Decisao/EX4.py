salario = float(input("salário atual: "))

if salario > 1250.0:
    print(f"aumento de {salario * 0.1} totalizando {salario + salario * 0.1}")
else:
    print(f"aumento de {salario * 0.15} totalizando {salario + salario * 0.15}")
