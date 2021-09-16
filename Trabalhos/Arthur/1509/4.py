numero = int(input("Tabuada de: "))
inicio = int(input("Informe o número inicial: "))
fim = int(input("Informe o último número: "))

while inicio <= fim:
    print(f'{numero} * {inicio} : {numero * inicio}')
    inicio += 1
