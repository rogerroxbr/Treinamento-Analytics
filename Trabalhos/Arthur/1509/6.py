dividendo = int(input("Informe um número: "))
divisor = int(input("Informe outro número: "))
quociente = 0

x = dividendo

while x >= divisor:
    x -= divisor
    quociente += 1
    resto = x

print(f'{dividendo}/{divisor}: {quociente}')
print(f'resto: {resto}')