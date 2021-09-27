def validate_string(string, min, max):
    largura = len(string)
    if(largura >= min and largura <= max):
        return True
    else:
        return False

teste_1 = validate_string("String", 1, 6)
teste_2 = validate_string("Função", 1, 5)
teste_3 = validate_string("Def", 0, 2)

print(teste_1)
print(teste_2)
print(teste_3)

def validate_list(string, lista):
    if string in lista:
        return True
    else:
        return False

lista = ['Arthur', 'Gabriel', 'Matheus']
string_1 = 'Arthur'
string_2 = 'Leonardo'

teste_1 = validate_list(string_1, lista)
teste_2 = validate_list(string_2, lista)

print(teste_1)
print(teste_2)