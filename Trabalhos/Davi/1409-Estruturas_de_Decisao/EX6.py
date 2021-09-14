distancia = float(input("distancia a percorrer (em km): "))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print(f"o valor de sua viagem de {distancia}km será de R${valor:.2f}")
