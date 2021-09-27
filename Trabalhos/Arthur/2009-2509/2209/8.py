tabela = {
    "Alface":0.45,
    "Batata":1.20,
    "Tomate":2.30,
    "Feijão":1.50
}

for key in tabela:
    print(f"{key} : {tabela[key]}")

print("\n")

for key, value in tabela.items():
    print(f"{key} : {value}")

print("\n")

print('Alface' in tabela)
print('Batata' in tabela)

print("\n")

print(tabela.keys())
print("\n")
print(tabela.values())

print("\n")

print(tabela.get("Alface", 0)) # Get é usado p/ verificar se um dicionário possui um valor,
# se possuir, retorna o valor da chave, se não possuir, retorna o valor pré-definido!

print("\n")

