houseValue = float(input("House value: "))
wage = float(input("Wage: "))
years = int(input("Number of years to pay: "))

installment = houseValue / (years * 12)

if installment > wage * 0.3:
    print("It is not possible to make this loan")
else:
    print(f"It is possible to make this loan with {years*12} installment of R${installment:.2f}")