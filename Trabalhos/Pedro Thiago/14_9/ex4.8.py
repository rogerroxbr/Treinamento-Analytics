num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))

operation = input('Qual operação você deseja fazer? (+ , -, /)\n')

if operation[0] == '+':
    var = num1 + num2
elif operation[0] == '-':
    var = num1 - num2
elif operation[0] == '/':
    var = num1 / num2
elif operation[0] == '*':
    var = num1 * num2
else:
    print('Operação inválida!')

print(f'seu resultado é: {var}')