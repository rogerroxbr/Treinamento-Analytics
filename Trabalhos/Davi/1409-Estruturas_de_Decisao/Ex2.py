idade = int(input("digite a idade do seu carro: "))
if idade <= 3:
    print("seu carro é novo")
elif idade> 3:
    print("seu carro é velho")

velocidade = float(input("velocidade do veículo: "))
if velocidade >= 80:
    print(f"você foi multado e deverá pagar R${(velocidade-80)/5:.2f}")
else:
    print("tudo certo")
