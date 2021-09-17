num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
op = input("Digite a operação desejada: ")

if op == "+":
    print(f"O valor final é {num1 + num2}")
elif op == "-":
    print(f"O valor final é {num1 - num2}")
elif op == "*":
    print(f"O valor final é {num1 * num2}")
elif op == "/":
    print(f"O valor final é {num1 / num2}")
else:
    print("A operação é invalida!")

