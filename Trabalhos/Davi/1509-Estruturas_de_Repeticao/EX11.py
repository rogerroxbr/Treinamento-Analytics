deposito = float(input("depósio inicial: "))
juros = float(input("taxa de juros: ")) / 100
meses = 1

while meses <= 24:
    deposito += deposito * (juros / 12)
    print(f"valor acumulado no {meses}° mês: {deposito:.2f}")
    meses += 1
