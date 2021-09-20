from turtle import Turtle

t = Turtle()

t.speed(1)

while True:
    sentido = input("diga o sentido: ").lower().strip()
    angulo = int(input("diga o ângulo: "))
    direcao = input("diga a direção: ").lower().strip()

    if sentido == "direita":
        t.right(angulo)
    elif sentido == "esquerda":
        t.left(angulo)
    elif sentido == "fim":
        break
    else:
        print("não houveram mudanças no sentido")

    if direcao == "frente":
        t.forward(100)
    elif direcao == "trás":
        t.backward(100)
    elif direcao == "fim":
        break
    else:
        print("a tartaruga não se movimentou")

    print("----------------")
    print("")
