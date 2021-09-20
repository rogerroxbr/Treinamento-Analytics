# Com frequência, a programação envolve analisar um conjunto de condições e decidir qual ação deve
# ser executada de acordo com essas condições. A instrução if de Python permite analisar o estado
# atual de um programa e responder de forma apropriada a esse estado.

a = int(input("First value: "))
b = int(input("Second value: "))

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

if a > b:
    print("The first number is the higher!")
elif b > a:
    print("The second number is the higher!")
else:
    print("The numbers are the same!")