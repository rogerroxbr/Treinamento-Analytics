'''
x = 1
while x <= 100:
    print(x)
    x = x + 1
'''
'''
fim = int(input("Digite o ultimo numero a imprimir: "))
x = 0
while x <= fim:
    print(x)
    x = x + 2
'''
'''
fim = int(input("Digite o ultimo numero a imprimir: "))
x = 0
while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1
'''
'''
fim = 30
x = 3
while x <= fim:
    print(x)
    x = x + 3
'''
'''
#tabuada
n = int(input("Tabuada de: "))
x = 1
while x <= 10:
    result = x * n
    print(f'{n} * {x} : {result}')
    x = x + 1
'''
'''
#tabuada escolhendo inicio e fim
n = int(input("Tabuada de: "))
m = int(input("Digite de onde você quer o inicio desta tabuada: "))
tabuada = int(input("Digite até onde você quer ver sua tabuada:"))

while n <= m:
    print(f'{n} * {tabuada} : {n * result}')
    n = n + 1
'''
'''
n = int(input("Digite o primeiro numero: "))
m = int(input("Digite o segundo numero: "))
total = 0
while n > 0:
    total += n
    m = -= 1
print({total})
'''
'''
dividendo = int(input("Digite o primeiro numero: "))
divisor = int(input("Digite o segundo numero: "))
quociente = 0
x = dividendo

while x >= divisor:
    x = x - divisor
    quociente += 1
    resto = x
    print(f"{dividendo}/{divisor}={quociente} resto: {resto}")
'''
'''
pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f'Resposta da questao {questao}: ')
    if questao == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    if questao == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1
    if questao == 3 and resposta == "d" or resposta == "D":
        pontos = pontos + 1
    questao += 1
print(f"O aluno fez {pontos} pontos(s)")
'''
'''
n = 1
soma = 0
while n <= 10:
     x = int(input(f"Digite o {n} numero: "))
     soma = soma + x
     n = n + 1
    print (f"Soma : {soma}")
'''
'''
valor_deposito = float(input("Digite o valor de deposito : "))
taxa_juros = float(input("Digite a taxa de juros :"))/100
mes = 0

while mes < 23:
    valor_deposito = valor_deposito + (valor_deposito*taxa_juros/12)
    mes = mes + 1
    print(f"Valor: {valor_deposito}")
'''
'''
valor_deposito = float(input("Digite o valor de deposito : "))
taxa_juros = float(input("Digite a taxa de juros :"))/100
deposito_mensal = float(input("Digite o valor do deposito mensal :"))
mes = 0
saldo = deposito_mensal

while mes < 23:
    saldo = saldo + (saldo*taxa_juros/12) + deposito mensal
    print(f"Saldo do mês {mes} é de {saldo}")
    mes = mes + 1
    print(f"Valor: {total:.2f}")
print(f"o ganho obtido com os juros foi de {deposito_mensal}")
'''
'''
divida = float(input("Digite o valor da divida : "))
juros = float(input("Digite o valor do juro mensal: "))
pagamento = float(input("Digite o valor que deseja pagar mensalmente:"))
mes = 0

if pagamento < (divida*juros/100):
    print("Voce nao irá conseguir pagar sua divida")
else:
    juros_pago = 0
    saldo = divida

    while saldo > pagamento:
        mes +=1
        juros_mensal = saldo * juros/100
        saldo = saldo + juros_mensal - pagamento
        juros_pago = juros_pago + juros_mensal
        print(f"Seu saldo é {saldo:.2f} no mês {mes} ")

    print(f"Para pagar uma dívida de {divida} voce levará")
'''
"""
s = 0
while True:
    v = int(input("Digite um numero a somar ou 0 para sair :"))
    if v == 0:
        break
    s = s + v
print(s)
"""

for n in "banana":
    print(n)
