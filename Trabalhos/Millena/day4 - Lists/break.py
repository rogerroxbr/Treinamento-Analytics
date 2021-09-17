amount = 0
sum = 0
while True:
    number = int(input("Digite um numero ou zero para sair "))
    if number == 0:
        break
    print(f'Numero: {number}')
    amount += 1
    sum += number

print(f'The amount of numbers is: {amount}, their sum: {sum} and their mean is: {sum/amount}')
