'''
estoque={"tomate": [1000,2.30],
         "alface": [500, 0.45] }

produto = input("Informe o produto: ")
quantidade = int(input("Informe a quantidade: "))

venda = [[{produto}:{quantidade}]]
total = 0
print("vendas:\n", {venda})
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print("%12s: %3d x %6.2f = %6.2f",
          (produto, quantidade, preco, custo))
    estoque[produto][0] -= quantidade
    total += custo
print("Custo total :21.2f\n", total)
print("estoque \n")
for chave, dados in estoque.items():
    print("descrição : ", chave)
    print("Quantidade : ", dados[0])
    print("preco : %6.2f\n ", dados [1])
'''
'''
glossario = {"Data Science": "Ciencia de Dados", "Machine Learning": "Aprendizado de Maquina"}

for palavra, frase in glossario.items():
    print(f"{palavra.title()}\n {frase.title()}")
'''
'''
Rios = {"Nilo": "Egito"}

for chave, valor in Rios.items():
    print(f"O rio: ", chave, "Corre pelo", valor)
'''
'''
favorit_places = {"joão": "Opera de Arame", "Francine": "Parque Barigui"}

for pessoa, lugar in favorit_places.items():
    print(" ")
    print("O lugar favorito de", pessoa.title(), "é: ", lugar)
    print("* - " * 15)
'''




















