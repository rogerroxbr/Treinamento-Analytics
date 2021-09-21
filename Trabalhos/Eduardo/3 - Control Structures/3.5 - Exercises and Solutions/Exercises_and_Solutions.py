"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""

numero = input("Digite um número: ")

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par!')
    else:
        print(f'{numero} é ímpar!')

except:
    print("A entrada não é um número !")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input("Informe o horário:"))

if hora >= 0 and hora <= 11:
    print("Bom dia!")
elif hora >= 12 and hora <= 17:
    print("Boa tarde!")
else:
    print("Boa noite!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tive 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; 
maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Informe seu nome: ")

if len(nome) <= 4:
    print("Seu nome é curto! ")
elif len(nome) <= 5 and len(nome) <= 6:
    print("Seu nome é normal! ")
else:
    print("Seu nome é grande!")
