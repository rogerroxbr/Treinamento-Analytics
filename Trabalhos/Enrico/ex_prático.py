nome = input("Nome da pessoa: ")
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura(em cm): "))
ano_atual = int(input("Informe o ano atual: "))
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

if imc <= 18.5:
    status = "Peso baixo"

if imc > 18.5 and imc <= 24.9:
    status = "Peso normal"

if imc > 24.9:
    status = "Sobrepeso"

print(f'\nNome da pessoa: {nome}\nIdade {idade}\nPeso {peso}\nAltura {altura }\nAno de nascimento {ano_nascimento}\nTem um IMC de: {imc:.2f} e seu status é: {status}')
