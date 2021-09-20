palavras = ["abacaxi", "banana"]
indice = int(input("digite um número: "))

palavra = palavras[(indice * 776) % len(palavras)]

for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    print("X==:==\nX : ")
    print("X O " if erros >= 1 else "X")
    linha2 = ["", "", " | ", " \| ", " \|/ "]
    if erros > 4:
        print("X%s" % linha2[3])
    else:
        print("X%s" % linha2[erros])

    linha3 = ["", " / ", " / \ "]
    if erros < 4:
        print("X")
    else:
        print("X%s" % linha3[erros-4])

    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra era {palavra}")
        break
