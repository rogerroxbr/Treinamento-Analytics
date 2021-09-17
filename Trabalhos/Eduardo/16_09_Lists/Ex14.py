total = 0

while True:
    codigo = int(input("digite o código do produto: "))
    if codigo == 0:
        break
    qntd = int(input("digite a quantidade do produto: "))

    if codigo == 1:
        total += 0.5 * qntd
    elif codigo == 2:
        total += 1 * qntd
    elif codigo == 3:
        total += 4 * qntd
    elif codigo == 5:
        total += 7 * qntd
    elif codigo == 9:
        total += 8 * qntd
    else:
        print("código inválido")

print(f"total: {total:.2f}")