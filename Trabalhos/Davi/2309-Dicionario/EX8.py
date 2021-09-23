pessoas = {}

while True:
    answer = input("\nDeseja inserir mais uma pessoa (S ou N): ")
    if answer == "N":
        break
    elif answer != "S":
        print("Resposta inválida\n")
        continue

    first_name = input("nome: ")
    last_name = input("sobrenome: ")
    age = input("idade: ")
    city = input("cidade: ")

    user = first_name[0] + last_name.split()[-1]

    pessoas[user] = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'city': city
    }

for chave, dados in pessoas.items():
    print("User: ", chave)
    print(" First name: ", dados["first_name"])
    print(" Last name: ", dados["last_name"])
    print(" Age: ", dados["age"])
    print(f" City: {dados['city']}\n")
