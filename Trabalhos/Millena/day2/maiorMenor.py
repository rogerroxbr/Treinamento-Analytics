a = input(f'Digite o primeiro numero ')
b = input(f'Digite o segundo numero ')
c = input(f'Digite o terceiro numero ')

if a > b:
    print('A é o maior' if a > c else 'C é o maior')
else:
    print('B é o maior' if b > c else 'C é o maior')

if a < b:
    print('A é o menor' if a < c else 'C é o menor')
else:
    print('B é o menor' if b < c else 'C é o menor')


# ou

if b > a and b > c:
    greatest = b
if c > a and c > b:
    greatest = c

if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c

