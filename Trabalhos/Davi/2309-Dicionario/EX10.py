pessoas = {
    "João": ['Jardim Botânico', 'Opera de Arame'],
    "Maria": ['Bairro Liberdade', 'Av. Paulista', 'MASP'],
    "George": ['Central Park']
}

for chave, dados in pessoas.items():
    lugares = ""
    for lugar in dados:
        if lugar == dados[0]:
            lugares += lugar
        elif lugar == dados[-1]:
            lugares += " e " + lugar
        else:
            lugares += ", " + lugar

    print(f"{chave} gosta do(s) lugar(es) {lugares}")
