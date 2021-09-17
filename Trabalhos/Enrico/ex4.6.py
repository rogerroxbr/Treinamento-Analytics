percorrer = float(input("Informe a distância pretende percorre: "))

if percorrer <= 200.0:
    valor = percorrer * 0.69
else:
    valor = percorrer * 0.5

print(f"Valor a pagar: {valor:.2f}")