code = int(input("Insira o código: "))
qtd = int(input("Insira a quantidade: "))

while True:
    if code == 1:
        valor = qtd * 0.5
    if code == 2:
        valor = qtd * 1
    if code == 3:
        valor = qtd * 4
    if code == 5:
        valor = qtd * 7
    if code == 9:
        valor = qtd * 8
    break
print(f"O valor da sua compra foi de R${valor}")