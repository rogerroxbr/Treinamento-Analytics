def valida_lista(string, lista):
    return string in lista


lista = ['python', 'java', 'javascript']

print(valida_lista('python', lista))
print(valida_lista('ola', lista))
