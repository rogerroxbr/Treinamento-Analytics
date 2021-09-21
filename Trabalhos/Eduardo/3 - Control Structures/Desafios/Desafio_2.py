from turtle import Turtle

# Inicializa uma turtle
t = Turtle()
t.shape("turtle")

while True:
    print("-------------------------------")
    print("Direções: ")
    print("F = Para frente | B = Para trás")
    print("-------------------------------")
    D = input("Informe a direção que a tartaruga vai andar: ")

    if D == "F":
        Pixel = int(input("Para frente, então! Informe a distância em pixel: "))
        print("------------------------------------")
        print("R = Para direita | L = Para esquerda")
        print("------------------------------------")
        L = input("Rotacionar para direita ou esquerda: ")
        PixelR = int(input("Informe a rotação em pixel: "))
        if L == "R":
            t.speed(1)
            t.right(PixelR)
            t.forward(Pixel)
        elif L == "L":
            t.speed(1)
            t.left(90)
            t.forward(Pixel)

    elif D == "B":
        Pixel = int(input("Para trás, então! Informe a distância em pixel: "))
        L = input("Rotacionar para direita ou esquerda: ")
        print("------------------------------------")
        print("R = Para direita | L = Para esquerda")
        print("------------------------------------")
        PixelR = int(input("Informe a rotação em pixel: "))
        if L == "R":
            t.speed(1)
            t.right(PixelR)
            t.backward(Pixel)
        elif L == "L":
            t.speed(1)
            t.left(PixelR)
            t.backward(Pixel)

    print("------------------------------------")
    print("S = Sim | N = Não")
    print("------------------------------------")
    Sair = input("Continuar andando? ")

    if Sair not in "S":
        break

print("Volte logo!")