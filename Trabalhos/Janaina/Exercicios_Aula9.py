'''
def display_message():
    print("Estou aprendendo Funções")

display_message()


def favorito_book():
    book = "A metamorfose"
    print(f"Meu livro favorito é {book}")

favorito_book()
'''
'''
def maior(x, y):
    if(x > y):
        print(x)
    else:
        print(y)

maior(6,9)
'''
'''
def multiplo(x, y):
    if (x % y):
        print(x)
    else:
        print(y)

multiplo(6,9)
'''
'''
def area(x):
    resultado = x * x
    print(f"A area é : {resultado}")

area(5)
'''
'''
def area_triangulo( b, h):
    area = (b * h)/ 2
    return area
teste = area_triangulo(5, 8)
print(teste)
'''
'''
def gerar_objeto_personalinado(cor,*, altura, formato):
    print(cor, altura, formato)

gerar_objeto_personalinado("branco", altura=2, formato="redondo")
'''
'''
def pesquise(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None

L=[10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
'''
'''
def soma(L):
    total=0
    x = 0
    for x in range(0, len(L)):
        total +=L[x]
        x += 1
    return total
L = [1, 2, 3, 4, 5]

print(soma(L))
'''
'''
def mdc(x, y):
    mdc = x
    while x % mdc != 0 or y % mdc != 0:
        mdc = mdc - 1

    print("MDC(%d,%d)=%d" % (x, y, mdc))

mdc(315, 125)
'''
''' revisar
def mmc(x, y):
    if num1 > num2:
        maior = num1
    else:
    maior = num2
while True:
    if maior % num1 == 0 and maior % num2 == 0:
        print(maior)
    else:
        maior += 1
'''
'''
def fatorial(n):
    print("Calculando o fatorial de %d" %n)
    if n == 0 or n == 1:
        print("Fatorial de %d = 1" % n)
        return 1
    else:
        fat = n*fatorial(n-1)
        print("fatorial de %d = %d" % (n, fat))
    return fat
fatorial(4)
'''
def validar_string(string, min, max):
    largura = len(string)
    if(largura >= min and largura <= max):
        return True
    else:
        return False

teste1 = validar_string("string", 1, 6)

print(teste1)













