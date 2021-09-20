print("Códigos: ")
print("1 | (")
print("2 | )")
print("3 | Sair")

lista = []
cont_esquerda = 0
cont_direita = 0

while True:
    for y in lista:
        print(y, end="")
    print('\n')
    op = int(input(f"Informe a opção que deseja utilizar: "))
    if op == 1:
        lista.append('(')
    elif op == 2:
        lista.append(')')
    elif op == 3:
        break
    else:
        print("Operação inválida!")
        continue

for x in lista:
    if x == '(':
        cont_esquerda += 1
    elif x == ')':
        cont_direita += 1

if cont_esquerda == cont_direita:
    print("OK!")
    print(lista)  
      
else:
    print("Erro!")