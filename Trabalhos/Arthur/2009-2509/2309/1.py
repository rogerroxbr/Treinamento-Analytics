def generate_dict(string):
    dicio = {}
    for numb in range(0, len(string)):
        dicio[numb] = string[numb]
    return dicio

string = input("Digite uma frase/palavra: ")
dicionario_gerado = generate_dict(string)
print(dicionario_gerado)