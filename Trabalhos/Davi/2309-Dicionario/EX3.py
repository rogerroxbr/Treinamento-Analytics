users = {
    "dbpombeiro": {
        "first_name": "Davi",
        "last_name": "Barreto Pombeiro",
        "age": 20,
        "city": "Curitiba"
    },
    "amarques": {
        "first_name": "Anthony",
        "last_name": "Marques",
        "age": 35,
        "city": "New York"
    }
}

for chave, dados in users.items():
    print("User: ", chave)
    print(" First name: ", dados["first_name"])
    print(" Last name: ", dados["last_name"])
    print(" Age: ", dados["age"])
    print(f" City: {dados['city']}\n")
