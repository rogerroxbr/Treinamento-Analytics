def maximo(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

teste_1 = maximo(5,6)
teste_2 = maximo(2,1)
teste_3 = maximo(7,7)

print(teste_1)
print(teste_2)
print(teste_3)

print('\n')

def multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

test_1 = multiplo(8,4)
test_2 = multiplo(7,3)
test_3 = multiplo(5,5)

print(test_1)
print(test_2)
print(test_3)
