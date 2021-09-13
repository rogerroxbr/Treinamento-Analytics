nome = input("digite o seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
ano = int(input("digite o ano atual: "))

ano_nascimento = ano - idade
imc = peso / altura ** 2

print(f"nome: {nome} / idade: {idade} / altura: {altura} peso: {peso} / ano atual: {ano} \n"
      f"ano de nascimento: {ano_nascimento} / imc: {imc:.2f}")

if imc > 40.0:
    print("obesidade III")
elif imc > 35.0:
    print("obesidade II")
elif imc > 30:
    print("obesidade I")
elif imc > 25.0:
    print("sobrepeso")
elif imc > 18.5:
    print("peso normal")
else:
    print("abaixo do peso")
