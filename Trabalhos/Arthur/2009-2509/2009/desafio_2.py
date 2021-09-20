import turtle

print("\n")
print("Direção | Código")
print(" /\     | 1")
print(" \/     | 2") 
print(" ->     | 3")
print(" <-     | 4")
print(" Salvar | 5")
print(" Sair   | 0")

t = turtle.Turtle()
t.speed(1)
graus = 0

while True:

    # t.forward(100) // Anda 100 pixels para frente!
    # t.left(90) // Ajusta o Ângulo 90 graus p/ esquerda!
    # t.right(90) // Ajusta o Ângulo 90 graus p/ direita!
    # t.backward(100)  // Anda 100 pixels para trás!

    print("\n")
    d = int(input("Informe a direção da tartaruga: "))

    if d == 0:
        print("\n")
        print("Obrigado por jogar!")
        print("\n")
        break

    elif d >= 1 and d <= 4:
        print("\n")
        if d == 1:
            p = int(input("Informe a quantidade de pixels a serem percorridos: "))
            t.forward(p)

        elif d == 2:
            p = int(input("Informe a quantidade de pixels a serem percorridos: "))
            t.backward(p)

        elif d == 3:
            g = int(input("Informe a quantidade de graus a serem rotacionados: "))
            t.right(g)

        elif d == 4:
            g = int(input("Informe a quantidade de graus a serem rotacionados: "))
            t.left(g)

    elif d == 5:
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="duck.eps")

    else:
        print("\n")
        print("Código não encontrado!")
        print("Informe o código novamente!")
        print("\n")
        continue