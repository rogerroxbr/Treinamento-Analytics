from turtle import Turtle
t = Turtle()
t.speed(1)
while True:
    dir = input('Digite F para anda para frente, T para ir para trás,\n'
                'E para ir para esquerda, D para a direita\n')
    if dir == 'F' or dir == 'T':
        pix = int(input('Quantos pixels? '))
    elif dir == 'E' or dir == 'D':
        angle = int(input('Qual o ângulo? '))

    if dir == 'F':
        t.forward(pix)
    elif dir == 'T':
        t.backward(pix)
    elif dir == 'E':
        t.left(angle)
    elif dir == 'E':
        t.right(angle)
    else:
        print('Opção inválida!')
        # continue

    dir = input('Desenha Sair? ("S" para sair, qualquer outra coisa para continuar)')
    if dir == 'S':
        break