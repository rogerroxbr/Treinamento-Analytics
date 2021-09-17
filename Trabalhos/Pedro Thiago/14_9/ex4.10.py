def ex10():
    try:
        consumo = float(input('Qual a quantidade consumida?\n'))
    except:
        print('Digite apenas números!')
        return 'error'
    tipo = input('Qual o tipo de instalação? (R, I, C)\n')

    if tipo == 'R':
        if consumo <= 500:
            multiplicador = 0.4
        else:
            multiplicador = 0.65
    elif tipo == 'I':
        if consumo <= 1000:
            multiplicador = 0.55
        else:
            multiplicador = 0.60
    elif tipo == "C":
        if consumo <= 5000:
            multiplicador = 0.55
        else:
            multiplicador = 0.60
    else:
        print('Tipo Inválido!')
        return 'error'

    print(f'O custo da fatura é de: {consumo * multiplicador}')
    return 'sucess'

ex10()

