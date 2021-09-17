num1 = int(input("Digite o primeiro numero "))
num2 = int(input("Digite o segundo numero "))
operation = input("Digite a operacao desejada ")

result = None
if operation == 'soma' or operation == '+':
    result = num1 + num2
elif operation == 'subtracao' or operation == '-':
    result = num1 - num2
elif (operation == 'divisao' or operation == '/') and num2 != 0:
    result = num1 / num2
elif operation == 'multiplicacao' or operation == '*':
    result = num1 * num2
else:
    print("Operacao invalida")

    print(f'O resultado da operação é {result}')
