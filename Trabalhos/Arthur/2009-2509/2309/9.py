pets = []
print("Informe 0 no nome do animal para sair!")

while True:
    print("\n")
    animal_name = input("Informe o nome do animal: ")
    if animal_name == "0":
        break

    animal_type = input("Informe o tipo de animal: ")
    owner = input("Informe o nome do dono: ")
    print("\n")
    
    dicionario = {
        "animal_name": animal_name.title(),
        "animal_type":animal_type,
        "owner":owner.title()
    }

    pets.append(dicionario)


for pet in pets:
    print("\n")
    print(f"Nome: {pet['animal_name']}")
    print(f"Tipo de Animal: {pet['animal_type']}")
    print(f"Dono: {pet['owner']}")
    print("\n")