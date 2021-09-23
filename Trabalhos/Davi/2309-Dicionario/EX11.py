numero_favorito = {}

while True:
    name = input("Informe seu nome (0 para sair): ")
    if name == "0":
        break

    numbers = []
    while True:
        number = input("Informe seu número favorito (A para parar de adicionar números): ")
        if number == "A":
            print("")
            break
        numbers.append(number)

    numero_favorito[name] = numbers

print("")

for chave, dados in numero_favorito.items():
    numeros = ""
    for num in dados:
        if num == dados[0]:
            numeros += num
        elif num == dados[-1]:
            numeros += " e " + num
        else:
            numeros += ", " + num

    print(f"{chave} gosta do(s) número(s) {numeros}")


