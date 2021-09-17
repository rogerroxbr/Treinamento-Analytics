num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))
operador = input("Qual operação deseja fazer? ")

if operador == '+':
    print(num1 + num2)
elif operador == '-':
    print(num1 - num2)
elif operador == '/':
    print(num1 / num2)
elif operador == '*':
    print(num1 * num2)
else:
    print("Operação inválida!")
