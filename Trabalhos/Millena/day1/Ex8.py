name = input("What's your name? ")
age = int(input("What's your age? "))
current_year = 2021
height = float(input("What's your height? "))
weight = float(input("What's your weight? "))
yearOfBirth = current_year - age
IMC = weight / (height ** 2)

print(f'The year of birth of: {name} is {yearOfBirth}, based on Current year {current_year} and their age {age}.'
      f' Your IMC is {IMC:.2f}. Based on the values {height} and {weight}.')


def weight_range(imc):
    if imc < 16.9:
        return "Muito abaixo do peso"
    if imc < 24.9:
        return "Peso normal"
    if imc < 29.9:
        return "Acima do peso"
    if imc < 34.9:
        return "Obesidade Grau I"
    if imc < 40:
        return "Obesidade Grau II"
    return "Obesidade Grau III"


print(f'Result: your IMC result is {weight_range(IMC)}. ')
