num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Operation: ")

if operation == "+":
    value = num1 + num2
elif operation == "-":
    value = num1 - num2
elif operation == "*":
    value = num1 * num2
elif operation == "/":
    value = num1 / num2
else:
    value = 0
    print("Invalid operation")

print(f"Operation results {num1} {operation} {num2} = {value}")