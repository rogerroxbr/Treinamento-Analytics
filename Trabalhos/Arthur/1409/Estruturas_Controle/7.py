valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o valor do salário: "))
quantidade_anos = int(input("Informe o valor de anos necessários para comprar a casa: "))

quantidade_meses = quantidade_anos * 12
trinta_porcento_salario = (salario / 100) * 30
valor_prestacao = valor_casa / quantidade_meses

if valor_prestacao > trinta_porcento_salario:
    print("O valor da prestação é superior a 30% do salário do usuário!")
else:
    print("O usuário pode comprar a casa!")
