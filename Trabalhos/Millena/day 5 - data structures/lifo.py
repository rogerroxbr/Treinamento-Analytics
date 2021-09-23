
parentesisList = ['(())']
i = 0
stack = []
while i < len(parentesisList):
    if parentesisList[i] == '(':
        stack.append(')')
    if parentesisList[i] == ')':
        if len(stack) > 0:
            stack.pop(-1)
        else:
            stack.append(")")  # FOrca a mensagem de erro
            break

if len(pilha) == 0:
    print('Ok')
else:
    print('Erro')
print(stack)
