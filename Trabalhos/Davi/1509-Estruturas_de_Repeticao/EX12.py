deposito = float(input("depósio inicial: "))
mensal = float(input("depósio mensal: "))
juros = float(input("taxa de juros: ")) / 100
meses = 1
investimento = deposito

while meses <= 24:
    investimento += mensal
    deposito += deposito * (juros / 12) + mensal
    print(f"valor acumulado no {meses}° mês: {deposito:.2f}")
    meses += 1
