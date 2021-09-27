tupla = (100,200,300)
tupla_vazia = ()

for elemento in tupla:
    print(elemento)

# Para fazer a modificação precisamos definir o objeto novamente!

tupla = ("A", ["B","C","D"])
len(tupla)

tupla[1] # ['B','C','D']
tupla[1].append('e')

# A tupla é imutável mas os seus elementos não.

L = [1,2,3]

T = tuple(L)

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2 # 1,2,3,4,5,6