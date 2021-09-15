velocidade = int(input("Informe a velocidade do carro: "))
limite = 80
if velocidade > limite:
    print("MULTADO!")
    velocidade_acima_limite = velocidade - limite
    valor_km_acima = velocidade_acima_limite * 5
    print(f"O usuário recebeu uma multa de R${valor_km_acima}.00!")
