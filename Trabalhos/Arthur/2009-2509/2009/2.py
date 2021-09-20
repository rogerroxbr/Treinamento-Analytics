produto = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]

compras = [produto, produto2, produto3]

for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]}")