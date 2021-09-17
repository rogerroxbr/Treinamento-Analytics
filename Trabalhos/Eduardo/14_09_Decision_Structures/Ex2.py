age = int(input("Enter the age of your car: "))
if age <= 3:
    print("Your car is new!")
elif age > 3:
    print("Your car is old!")

velocity = float(input("Vehicle speed: "))
if velocity >= 80:
    print(f"You were fined and must pay R${(velocity-80)/5:.2f}")
else:
    print("All right!")