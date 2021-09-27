l1 = [1,2,3,4,5,6]
ex1 = [variavel for variavel in l1]
print(ex1)
print("*" * 20)

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex2)
print(ex3)
print("*" * 20)

l2 = ["Luis", "Mauro", "Maria"]
ex4 = [v.replace("a", "@").upper() for v in l2]
print(ex4)
print("*" * 20)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)
print("*" * 20)

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)
print("*" * 20)

string = "01234567890123456789012345678901234567890123456789"
n=10
list = [string [i:i+n] for i in range(0,len(string),n)]
retorno = ".".join(list)
print(list)
print(retorno)
print("*" * 20)

x = 4
[(print(f'{x} x {i} = {x*i}')) for i in range(11)]
print("*" * 20)

tabuada = [f'{x} x {i} = {x*i}' for i in range(11)]
print(tabuada)
print("*" * 20)
'''
lista_mdc = [1,34,56,73,98,45]
def mdc(lista_mdc):
    for x in range(lista_mdc):
        mdc = x
        while x % mdc != 0 or y % mdc != 0:

    print("MDC(%d,%d)=%d" % (x, y, mdc))
mdc()
'''
import functools
def mdc(args):
    def cal(divisor):
        return divisor if sum(map(lambda x: x % divisor, args)) == 0 else cal(divisor - 1)
    return cal(min(args))

print(mdc([21, 7]))