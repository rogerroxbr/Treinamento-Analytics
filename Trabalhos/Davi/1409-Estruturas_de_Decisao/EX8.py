num1 = float(input("primeiro número: "))
num2 = float(input("segundo número: "))
operacao = input("operação: ")

if operacao == "+":
    valor = num1 + num2
elif operacao == "-":
    valor = num1 - num2
elif operacao == "*":
    valor = num1 * num2
elif operacao == "/":
    valor = num1 / num2
else:
    valor = 0
    print("operação inválida")

print(f"Resultado da operação {num1} {operacao} {num2} = {valor}")
