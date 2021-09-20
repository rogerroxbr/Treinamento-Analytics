L = [15, 7, 27, 39]
p = int(input("Digite o valor a ser pesquisado: "))
x = 0
v = int(input("Digite o valor a ser pesquisado: "))
A = [-1, -1]

while x < len(L):
    if L[x] == p:
        A[0] = x
    if L[x] == v:
        A[1] = x
    x += 1
if A[0] == -1 and A[1] == -1:
    print('Não encontrei nenhum dos valores!')
elif A[0] == -1:
    print(f'Só encontrei o valor {v} na posição {A[-1]}')
elif A[1] == -1:
    print(f'Só encontrei o valor {p} na posição {A[0]}')
elif A[0] <= A[1]:
    print(f"{p} achado primeiro na posição {A[0]}")
    print(f"{v} achado na posição {A[1]}")
elif A[1] < A[0]:
    print(f"{v} achado primeiro na posição {A[1]}")
    print(f"{p} achado na posição {A[0]}")