letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = [letra.lower() for letra in letras_maiusculas]
print(letras_minusculas)

print("\n")

dobros = [i * 2 for i in range(10)]
print(dobros)

print("\n")

dobro_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro_dos_pares)

print("\n")