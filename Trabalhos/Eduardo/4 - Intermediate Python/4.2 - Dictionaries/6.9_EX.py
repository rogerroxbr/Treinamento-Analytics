favorite_numbers = {}

while True:
    name = input("Enter your name or out: ")
    list_numbers = []

    if name == "out":
        break

    while True:
        number = input("Enter your favorite number: ")
        if number != "out":
            list_numbers.append(number)
        else:
            break

    favorite_numbers.update({name: list_numbers})

for key, values in favorite_numbers.items():
    print(f"{key.title()}'s favorite numbers are:")
    for number in values:
        print("\t- " + str(number))

print(favorite_numbers)