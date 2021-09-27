def teste():
    print('Teste!')

def run_teste(funcao): # Passando uma função como parâmetro!
    funcao()
    print("Teste 2!")

run_teste(teste)

def soma_2(a, b):
    print(a+b)

L = [2,3]
soma_2(*L) # Passando todos os pârametros da lista separadamente!

def soma_lista(L): # Passando uma lista como pârametro!
    soma = 0 
    for x in L:
        soma += x
    print(soma)

L = [1,5,7]
soma_lista(L) 

a = lambda x: x*2
print(a(3))

aumento = lambda a,b: (a*b/100)
print(aumento(100, 5))