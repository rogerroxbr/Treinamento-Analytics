distance = float(input("Distance to go (in km): "))

if distance <= 200:
    value = distance * 0.5
else:
    value = distance * 0.45

print(f"The value of your {distance}km trip will be R${value:.2f}")