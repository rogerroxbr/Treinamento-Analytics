distance = float(input("Qual a distancia em km ? "))

if distance <= 200.0:
    cost = distance * 0.5
else:
    cost = distance * 0.45

print(f'O preco da passagem é de: R$ {cost}')

