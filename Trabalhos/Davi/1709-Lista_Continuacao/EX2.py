expressao = input("digite uma expressão: ")
controle = 0

for c in expressao:
    if c == '(':
        controle += 1
    elif c == ')':
        controle -= 1

if controle == 0:
    print("parentêses ok")
elif controle < 0:
    print(f"equação errada, {abs(controle)} parentêses foram fechados sem serem abertos")
else:
    print(f"equação errada, falta fechar {controle} parentêses")