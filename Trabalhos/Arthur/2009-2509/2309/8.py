pessoas = {}

print("\n")
print("Digite 0 em qualquer campo para sair do programa!")
print("\n")

while True:
    name = input("Informe seu nome: ")
    if name == "0":
        break

    favorite_language = input("Informe sua linguagem favorita: ")
    if favorite_language == "0":
        break

    pessoas[name] = favorite_language


for key, item in pessoas.items():
    print(f"{key} : {item}")