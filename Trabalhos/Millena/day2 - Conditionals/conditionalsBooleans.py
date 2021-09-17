speedOfcar = float(input('Digite a velocidade do seu carro: '))

if speedOfcar > 80:
    print("Voce foi multado, cara")
    ticket = (speedOfcar-80)*5
    print(f'O valor da multa é: {ticket:.2f} >:(')
else:
    print("Muito bao, sem multa por hoje")
