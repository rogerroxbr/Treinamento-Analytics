ano_atual = int(input("Qual é o ano atual? "))
nome = str(input("Qual é seu nome? "))
idade = int(input("Quantos anos você tem? "))
altura = float(input("Qual é sua altura? "))
peso = float(input("Qual é seu peso? "))

ano_nascimento = ano_atual - idade
imc = peso/altura ** 2

print('\n')
print(f"Ano Atual: {ano_atual}")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Peso: {peso}")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Sua classificação de IMC é Baixo peso!")

if imc >= 18.6 and imc <= 24.9:
    print("Seu peso está normal!")

if imc >= 25 and imc <= 29.9:
    print("Sua classificação de IMC é Sobrepeso!")

if imc >= 30 and imc <= 34.9:
    print("Sua classificação de IMC é Obesidade grau I!")

if imc >= 35 and imc <= 39.9:
    print("Sua classificação de IMC é Obesidade grau II!")

if imc >= 40:
    print("Sua classificação de IMC é Obesidade grau III!")