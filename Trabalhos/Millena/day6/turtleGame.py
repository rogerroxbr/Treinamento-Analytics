from turtle import Turtle
t = Turtle()
t.speed(1)

while True:
    direction = input("Move the turtle backward or forward?")
    pixels = int(input("Move the turtle for how many pixels?"))
    if direction == 'forward':
        t.forward(pixels)
    else:
        t.backward(pixels)

    orientation = input("Move the turtle left of right?")
    degrees = int(input("How many degrees? "))
    if orientation == 'left':
        t.left(degrees)
    else:
        t.right(degrees)

    keepMoving = input("Keep moving? (y or n)")
    if keepMoving == 'n':
        break
print("You've arrived")
