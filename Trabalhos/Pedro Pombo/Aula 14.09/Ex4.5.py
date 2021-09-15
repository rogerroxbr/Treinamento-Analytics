dist = float(input("Digite a distância que deseja percorrer: "))
if dist <= 200:
    print(f"Sua passagem custara: R$:{dist * 0.5}")
if dist > 200:
    print(f"Sua passagem custara: R${dist * 0.45}")
