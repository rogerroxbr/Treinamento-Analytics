lista_valores = []

for i in range(3):
    valor = int(input("Digite um valor: "))
    lista_valores.append(valor)
valor_max = 0
valor_min = 100
for i in lista_valores:
    if i > valor_max:
        valor_max = i
    if i < valor_min:
        valor_min = i
print(f"O menor valor digitado foi: {valor_min}\nO maior valor digitado foi: {valor_max}")
