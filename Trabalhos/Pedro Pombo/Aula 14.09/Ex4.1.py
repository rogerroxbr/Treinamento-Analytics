vel = int(input("Digite a velocidade do seu carro: "))

if vel > 80:
    acima = vel - 80
    print(f"Você foi multado, sua multa é de R$ {acima * 5}")
    