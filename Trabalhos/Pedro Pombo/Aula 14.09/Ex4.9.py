valC = float(input("Digite o valor da casa: "))
sal = float(input("Digite o valor do seu salário: "))
qAnos = float(input("Digite a quantidade de anos a pagar: "))

valorMensal = valC / qAnos * 12
if valorMensal > sal * 0.3:
    print("Valor não é valido, seu emprestimo foi negado.")
else:
    print(f"Emprestimo aprovado com valor mensal de R$ {valorMensal:.2f}")
