estoque = {
    "tomate":[1000 , 2.30],
    "alface":[500, 0.45],
    "batata":[2001, 1.20],
    "feijão":[100, 1.50]
}

print("\n")
produto_vendido = input("Informe o produto vendido: ")
print("\n")

if produto_vendido in estoque.keys():
    quantidade_vendida = int(input("Informe a quantidade vendida: "))
    estoque[produto_vendido][0] -= quantidade_vendida
    valor_produto_vendido = estoque[produto_vendido][1]
    total = valor_produto_vendido * quantidade_vendida
    print(f"{produto_vendido}: {quantidade_vendida} * {valor_produto_vendido}")
    print("O total da compra foi: ", total)
    print("\n")
    print("***********************************")
    print("\n")
    print("Estoque: \n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print("Preço: ", dados[1])
        print("\n")
    print("***********************************")

else:
    print("Produto não encontrado!")
