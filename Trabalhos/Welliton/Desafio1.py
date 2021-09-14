nome = str(input("nome:"))
idade = int(input("idade:"))
altura = float(input("altura:"))
peso = float(input("peso:"))
ano = int(input("ano:"))

nasc = ano - idade
print(f'Ano de Nascimento: {nasc}')

imc = peso / altura **2
print(f'IMC: {imc:.2f}')

