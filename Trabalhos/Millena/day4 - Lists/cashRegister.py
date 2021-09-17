def find_price(x):
    return {
        1: 0.50,
        2: 1.00,
        3: 4.00,
        5: 7.00,
        9: 8.00
    }.get(x, None)


soma = 0

while True:
    code = int(input('Type the code '))
    if code == 0:
        break
    price = find_price(code)
    soma += price
    if not price:
        print(f'Invalid code!')
    print(f'The price is: {price}')

print(f'The total price is: {soma}')
