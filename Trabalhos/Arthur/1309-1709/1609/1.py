soma = 0
media = 0
contador = 0

while True:
    numero = int(input("Informe um número: "))
    if numero <= 0:
        print("Você digitou 0 ou um número menor que 0!")
        break
    soma += numero
    contador += 1

if soma > 0:
    media = soma/contador
    print(f"Foi/Foram digitado(s) {contador} número(s)!")
    print(f"A soma é: {soma}")
    print(f"Média: {media:.2f}")