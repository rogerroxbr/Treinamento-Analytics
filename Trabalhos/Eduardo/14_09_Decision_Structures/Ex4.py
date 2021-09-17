wage = float(input("Current wage: "))

if wage > 1250.0:
    print(f"Increase of {wage * 0.1} totalizing {wage + wage * 0.1}")
else:
    print(f"Increase of {wage * 0.15} totalizing {wage + wage * 0.15}")