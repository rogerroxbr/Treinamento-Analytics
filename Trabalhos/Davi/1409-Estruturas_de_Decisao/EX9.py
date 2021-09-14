valorCasa = float(input("valor da casa: "))
salario = float(input("salário: "))
anos = int(input("quantidade de anos a pagar: "))

prestacao = valorCasa / (anos * 12)

if prestacao > salario * 0.3:
    print("não é possível fazer esse empréstimo")
else:
    print(f"é possível fazer esse empréstimo com {anos*12} prestações de R${prestacao:.2f}")
