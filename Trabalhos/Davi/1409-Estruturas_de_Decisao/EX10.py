kwh = float(input("kWh consumida: "))
instalacao = input("tipo de instalação: ")

if instalacao == "R":
    if kwh <= 500:
        valor = kwh * 0.4
    else:
        valor = kwh * 0.65
elif instalacao == "I":
    if kwh <= 1000:
        valor = kwh * 0.55
    else:
        valor = kwh * 0.6
elif instalacao == "C":
    if kwh <= 5000:
        valor = kwh * 0.55
    else:
        valor = kwh * 0.6
else:
    valor = 0
    print("tipo de instalação inválida")

print(f"valor a pagar: R${valor:.2f}")
