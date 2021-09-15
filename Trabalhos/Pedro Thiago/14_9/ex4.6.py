dist = float(input('Digite a distância que você quer percorrer: \n'))

if dist < 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45

print(f'\nO custo da viagem é de: R${preço}')