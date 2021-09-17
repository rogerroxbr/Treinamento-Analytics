divida = float(input("dívida: "))
juros_mensal = float(input("juros mensal: ")) / 100
valor_mensal = float(input("valor da parcela: "))

juros_acumulado = 0
divida_inicial = divida
meses = 1

while divida > 0:
    if divida * juros_mensal > valor_mensal:
        print("não será possível pagar a dívida")
        break
    juros_acumulado += divida * juros_mensal
    divida += divida * juros_mensal - valor_mensal
    meses += 1

print(f"valor total pago: {divida_inicial + juros_acumulado:.2f} / juros totais: {juros_acumulado:.2f} "
      f"/ qntd de meses: {meses}")
