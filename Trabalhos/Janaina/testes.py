"""
a = int(input("primeiro valor: "))
b = int(input("segunto valor: "))

if a > b:
    print("O primeiro é maior!")
if b > a:
    print("O segundo é maior!")
"""
"""
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("seu carro é novo ")
if idade > 3:
    print("seu carro é velho")
"""
"""
valor1 = input("Digite o primeiro numero: ")
valor2 = input("Digite o segundo numero: ")
valor3 = input("Digite o terceiro numero: ")
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3

menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3

print(f"O menor valor digitado: {menor}")
print(f"O maior valor digitado: {maior}")
"""
"""
distancia = float(input("Digite a distancia a ser percorrida: "))
if distancia < 200:
    valor_cobrado = distancia * 0.50
else:
    valor_cobrado = distancia * 0.45

print(f"O valor a ser cobrado é: {valor_cobrado}")
"""
"""
num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o Segundo numero: ")
operador = input("Qual operação deseja realizar: + - * / ")

if operador == '+':
    valor_calculado = num1+num2
elif operador == '-':
    valor_calculado = num1-num2
elif operador == '*':
    valor_calculado = num1*num2
elif operador == '/':
    valor_calculado = num1/num2
print(f"O resultado desta operação é: {valor_calculado}")
"""
"""
valor_casa = float(input("Digite o valor do imovel: "))
valor_salario = float(input("Digite o valor refrente ao salario: "))
anos_a_pagar = int(input("Digite o total de anos a pagar: "))
meses_a_pagar = anos_a_pagar * 12
prestacao = valor_casa / meses_a_pagar

if prestacao > valor_salario * 0.3:
    print("Emprestimo Negado")
else:
    print(f"Emprestimo aceito, valor a pagar: {prestacao:.2f}")
"""


