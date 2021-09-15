name = input("Digite seu nome:\n")
age = int(input("Digite sua idade:\n"))
height = float(input("Digite sua altura:\n"))
weight = int(input("Digite seu peso:\n"))
current_year = int(input("Digite o ano atual:\n"))

birth_year = current_year - age
IMC = weight / height**2

category = 'peso ideal'

if IMC < 18.5:
    category = 'abaixo do peso'
elif IMC >= 25:
    category = 'acima do peso'

print(f'Olá {name}, seu IMC é: {IMC}, o que te coloca na categoria: {category} \ne seu ano de nascimento é: {birth_year}')
