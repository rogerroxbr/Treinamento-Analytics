str = list(input("Digite apenas ( e ): "))
while True:
    first = -1
    second = -1
    i = 0
    while i < len(str):
        if str[i] == '(':
            first = i
            break
        else:
            i += 1
    i = 0
    while i < len(str):
        if str[i] == ')':
            second = i
            break
        else:
            i += 1
    if first != -1 and second != -1:
        str.pop(second)
        str.pop(first)
    else:
        if len(str) == 0:
            print('Ok!')
        else:
            print('ERRO')
        break