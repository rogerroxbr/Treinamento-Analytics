start = int(input('Digite um número\n'))
end = int(input('Digite outro número\n'))
count = 0

while start >= end:
    start = start - end
    count += 1

print('')
print(f'\n{count}')
