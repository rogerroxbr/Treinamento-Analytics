def function():
    start = int(input('Digite o começo da tabuada\n'))
    i = int(input('Digite um número\n'))
    end = int(input('Digite o fim da tabuada\n'))
    print('')

    if start > end:
        print('O começo deve ser menor que o final!')
        return 'err'

    while start <= end:
        print(f'{start} x {i} = {start * i}')
        start = start + 1


function()
