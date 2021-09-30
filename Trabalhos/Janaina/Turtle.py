import turtle

from turtle import Turtle

t = Turtle()

t.left(20)
t.right(40)
t.forward(100)
t.backward



while True:
    direcao = input("Para qual direção devemos ir? "f:frente " ou " t:tras")
    if direcao == "f":
        distancia = int(input("Quantos pixels devemos movimentar para frente? "))
        movimentar_para_lado = input("Rotacionar para a d:direita, e:esquerda n:nao rotacionar")
        if movimentar_para_lado == "d":
            angulo = int(input("Quanto para a direita devemos rotacionar?"))
            t.right(angulo)
        elif movimentar_para_lado == "e":
            angulo = int(input("Quanto para a esquerda devemos rotacionar?"))
            t.left(angulo)
        t.forward(distancia)
    if direcao == "t":
        distancia = int("Quantos pixels devemos movimentar para tras?")
        movimentar_para_lado = input("Rotacionar para a d:direita, e:esquerda n:nao rotacionar")
        if movimentar_para_lado == "d":
            angulo = int(input("Quanto para a direita devemos rotacionar?"))
        t.right(angulo)
        elif movimentar_para_lado == "e":
        angulo = int(input("Quanto para a esquerda devemos rotacionar?"))
        t.left(angulo)
        t.backward(distancia)
    resposta = input(("Continuar andando?"))
    if resposta not in ("sim", "s"):
        break


