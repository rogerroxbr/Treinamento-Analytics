salario = float(input("Informe o valor do salário do funcionário: "))

if salario > 1250:
    aumento = round((salario / 100) * 10, 2)

else:
    aumento = round((salario / 100) * 15, 2)

print(f"O salário é: R${salario} !")
print(f"O aumento é: R${aumento} !")
print(f"O salario após o aumento é: R${salario + aumento} !")
