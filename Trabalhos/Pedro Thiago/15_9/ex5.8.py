start = int(input('Digite um número\n'))
end = int(input('Digite outro número\n'))
i = start

while end > 1:
    i = start + i
    end -= 1

print('')
print(i)
