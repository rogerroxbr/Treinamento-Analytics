import turtle

print("Direção | Código")
print(" /\     | 1")
print(" \/     | 2") 
print(" ->     | 3")
print(" <-     | 4")
print(" Salvar | 5")
print(" Sair   | 0")

defined_turtle = turtle.Turtle()
defined_turtle.speed(1)
graus = 0

def move_forward():
    pixels = int(input("Informe a quantidade de pixels a serem percorridos: "))
    defined_turtle.forward(pixels)


def move_backward():
    pixels = int(input("Informe a quantidade de pixels a serem percorridos: "))
    defined_turtle.backward(pixels)


def move_right():
    graus = int(input("Informe a quantidade de graus a serem rotacionados: "))
    defined_turtle.right(graus)


def move_left():
    graus = int(input("Informe a quantidade de graus a serem rotacionados: "))
    defined_turtle.left(graus)


while True:

    decision = int(input("Informe a direção da tartaruga: "))

    if decision == 0:
        print("Obrigado por jogar!")
        break

    elif decision == 1:
        move_forward()

    elif decision == 2:
        move_backward()

    elif decision == 3:
        move_right()

    elif decision == 4:
        move_left()

    else:
        print("Código não encontrado!")
        print("Informe o código novamente!")
        continue
