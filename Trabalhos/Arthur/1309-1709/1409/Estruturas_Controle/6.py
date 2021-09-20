n1 = float(input("Informe o 1o número: "))
n2 = float(input("Informe o 2o número: "))

print("\n")
print("+ para adição")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")
print("\n")
opcao = input("Qual operação você deseja fazer? ")

if len(opcao) > 1 or len(opcao) == 0:
    print("Você não informou a opção, reinicie o programa!")

else:
    if opcao == "+":
        resultado = n1 + n2
    elif opcao == "-":
        resultado = n1 - n2
    elif opcao == "*":
        resultado = n1 * n2
    elif opcao == "/":
        resultado = n1 / n2

    print(f"O resultado de {n1} {opcao} {n2} é: {resultado}")
