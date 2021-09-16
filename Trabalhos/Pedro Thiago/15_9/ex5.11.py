start = int(input("Qual o deposito inicial? \n"))
tax = 1 + float(input("Qual o juros? (de forma decimal, ex: 0.03 para 3%)\n"))
i = 0

while i <= 24:
    start = start * tax
    i += 1

print(start)
