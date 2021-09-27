rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'yangtz': 'china' 
}

for key, value in rios.items():
    print(f"O rio {key.title()} corre pelo {value.title()}.")

for key in rios.keys():
    print(key.title())

for item in rios.values():
    print(item.title())