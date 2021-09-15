'''
x = 1
while x <= 100:
    print(x)
    x = x + 1
'''
'''
fim = int(input("Digite o ultimo numero a imprimir: "))
x = 0
while x <= fim:
    print(x)
    x = x + 2
'''
fim = int(input("Digite o ultimo numero a imprimir: "))
x = 0
while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1
