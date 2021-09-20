apagar = 0

while True:
    codigo = int(input("Digite o código da mercadoria ou 0 para sair: "))
    preco = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.5
    elif codigo == 2:
        preco = 1.0
    elif codigo == 3:
        preco = 4.0
    elif codigo == 5:
        preco = 7.0
    elif codigo == 9:
        preco = 8.0
    else:
        print('Código inválido!')
    if preco != 0:
        quantidade = int(input("Qual a quantidade? "))
        apagar = (quantidade * preco) + apagar

print(f'você deve pagar {apagar:.2f}')
