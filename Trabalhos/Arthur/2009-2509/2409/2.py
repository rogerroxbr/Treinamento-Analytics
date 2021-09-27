lista = []
string = '01234567890123456789012345678901234567890123456789'
string_auxiliar = ''

for letra in string:

    if letra != '9':
        string_auxiliar += letra

    else:
        string_auxiliar += letra + '.'
        lista.append(string_auxiliar)    
        string_auxiliar = ''

print(lista)