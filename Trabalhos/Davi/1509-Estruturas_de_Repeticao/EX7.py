n = int(input("Tabuada de: "))
inicio = int(input("Começo da Tabuada: "))
fim = int(input("Fim da Tabuada: "))

while inicio <= fim:
    print(f"{n}x{inicio} = {n*inicio}")
    inicio += 1

if inicio > fim:
    print("inicio maior que o fim")
