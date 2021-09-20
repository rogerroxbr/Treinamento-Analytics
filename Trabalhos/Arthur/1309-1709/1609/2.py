print("Código | Preço")
print("1 | 0.50")
print("2 | 1.00")
print("3 | 4.00")
print("5 | 7.00")
print("9 | 8.00")
print("Informe o código 0 para sair!")
soma = 0
valor = 0

while True:
    codigo = int(input("Informe o código do produto: "))
    if codigo == 0:
        break
    if codigo == 1:    
        valor = 0.50    
    elif codigo == 2:
        valor = 1
    elif codigo == 3:
        valor = 4
    elif codigo == 5:
        valor = 7
    elif codigo == 9:
        valor = 8
    else:
        print("Código inválido!")
        continue

    quantidade = int(input(f"Quantos produtos de código {codigo} foram comprados? "))
    soma = soma + (quantidade * valor)

print(f"O valor total da compra é: {soma}")
