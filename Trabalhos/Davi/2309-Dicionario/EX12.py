cities = {
    'cwb': {
        'país': 'Brazil',
        'população': '2 milhões',
        'temperatura': 'frio'
    }
}

for chave, valor in cities.items():
    print(f"{chave} está no {valor['país']}, tem a população de {valor['população']} e é {valor['temperatura']}")
