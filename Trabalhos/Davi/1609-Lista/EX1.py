soma = 0
quantidade = 0

while True:
    num = int(input("digite um número: "))
    if num == 0:
        break
    quantidade += 1
    soma += num

print(f"qntd de números: {quantidade} / total: {soma} / média {soma / quantidade}")