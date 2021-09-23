pets = []
print("Informe 0 no nome do animal para sair!\n")

while True:
    animal_name = input("Informe o nome do animal: ")
    if animal_name == "0":
        break

    animal_type = input("Informe o tipo de animal: ")
    owner = input("Informe o nome do dono: ")
    print("")
