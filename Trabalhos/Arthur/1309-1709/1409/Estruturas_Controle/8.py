kwh = int(input("Informe a quantidade de kWh consumida: "))

print('\n')
print("Informe: ")
print("R para residências")
print("I para indústrias")
print("C para comércios")
print('\n')

instalacao = input("Qual é o tipo de instalação? ")

if instalacao == "R":
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
    print(f"O valor do consumo de {kwh} no tipo de instalação {instalacao} é: R${preco} !")

elif instalacao == "I":
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
    print(f"O valor do consumo de {kwh} no tipo de instalação {instalacao} é: R${preco} !")

elif instalacao == "C":
    if kwh <= 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
    print(f"O valor do consumo de {kwh} no tipo de instalação {instalacao} é: R${preco} !")

else:
    print("Opção inválida!")
