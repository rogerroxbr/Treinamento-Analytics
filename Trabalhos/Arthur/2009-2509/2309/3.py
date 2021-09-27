pessoa = {"pessoas": []}

print("\n")
print("Digite 0 em qualquer campo para sair do programa!")
print("\n")

while True:
    first_name = input("Informe seu primeiro nome: ")
    if first_name == "0":
        break

    last_name = input("Informe seu último nome: ")
    if last_name == "0":
        break

    age = int(input("Informe sua idade: "))
    if age == 0:
        break

    city = input("Informe sua cidade: ")
    if city == "0":
        break            

    objeto = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city
    }
    pessoa["pessoas"].append(objeto)

for x in pessoa["pessoas"]:
    print("\n")
    print(f"Nome: {x['first_name']} {x['last_name']}")
    print(f"Idade: {x['idade']}")
    print(f"Cidade: {x['city']}")
    print("\n")