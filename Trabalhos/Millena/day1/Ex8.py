name = input("What's your name? ")
age = int(input("What's your age? "))
current_year = 2021
height = float(input("What's your height? "))
weight = float(input("What's your weight? "))
yearOfBirth = current_year - age
imc = weight / (height ** 2)

print(f'The year of birth of: {name} is {yearOfBirth}, based on Current year {current_year} and their age {age}.'
      f' Their IMC is {imc:.2f}. Based on the values {height} and {weight}.')

message = ''

if imc < 16.9:
    message = "Muito abaixo do peso"
elif imc < 24.9:
    message = "Peso normal"
elif imc < 29.9:
    message =  "Acima do peso"
elif imc < 34.9:
    message =  "Obesidade Grau I"
elif imc < 40:
    message =  "Obesidade Grau II"
else:
    message = "Obesidade Grau III"


print(f'Result: your IMC result is {message}. ')
