distancia = int(input("Informe a distância em KM que o passageiro deseja percorrer: "))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print(f'A viagem com distância: {distancia}km terá um valor de: R${valor} !')
