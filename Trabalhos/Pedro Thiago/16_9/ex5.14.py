soma = 0
media = 0
i = 0
num = 0

while True:
    num = int(input("Digite um número, ou 0 para sair: "))
    if num == 0:
        break
    soma = soma + num
    i = i + 1

media = soma / i

print(f'sua soma é: {soma}')
print(f'E a média é: {media}')
