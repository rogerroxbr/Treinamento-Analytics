dividendo = int(input("número 1: "))
divisor = int(input("número 2: "))
quociente = 0
resto = dividendo

while resto >= divisor:
    resto -= divisor
    quociente += 1

print(f"{dividendo} / {divisor} = {quociente} resto: {resto}")
