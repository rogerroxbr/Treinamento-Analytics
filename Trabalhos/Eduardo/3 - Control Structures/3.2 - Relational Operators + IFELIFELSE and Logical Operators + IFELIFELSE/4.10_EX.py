kwh = int(input("Enter the amount of kWh consumed: "))

print('\n')
print("Enter: ")
print("H for homes")
print("I for industries")
print("T for trades")
print('\n')

installation = input("What type of installation?? ")

if installation == "H":
    if kwh <= 500:
        price = kwh * 0.40
    else:
        price = kwh * 0.65
    print(f"The consumption value of {kwh} in the installation type {installation} is: R${price} !")

elif installation == "I":
    if kwh <= 1000:
        price = kwh * 0.55
    else:
        price = kwh * 0.60
    print(f"The consumption value of {kwh} in the installation type {installation} is: R${price} !")

elif installation == "T":
    if kwh <= 5000:
        price = kwh * 0.55
    else:
        price = kwh * 0.60
    print(f"The consumption value of {kwh} in the installation type {installation} is: R${price} !")

else:
    print("Invalid option!")