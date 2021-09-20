L = [1,2,3,4,5]
V = L[:] # P/ Copiar uma lista sem copiar o endereço de memória!

X = L[1:3] # 2,3,4

Y = L[3:] # 4,5
B = L[:3] # 1,2,3

Z = L[:-1] # 1,2,3,4

O = L[-1] # 5
P = L[-2] # 4

L.extend([6, 7]) # L = [1,2,3,4,5,6,7]
L.append([6,7]) # L = [1,2,3,4,5,[6,7]]

del L[0] # 2,3,4,5