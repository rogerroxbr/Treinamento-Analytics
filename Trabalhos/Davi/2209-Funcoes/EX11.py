def validar_string(valor, min, max):
    return min <= len(valor) <= max


print(validar_string("ola", 1, 4))
