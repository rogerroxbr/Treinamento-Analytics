name = input('What is your name? ')
age = int(input('What is your age? '))
height = float(input('What is your height? '))
weight = float(input('What is your weight? '))
current_year = int(input('What is the current year? '))

def get_person_birth_year(age, current_year):
  return current_year - age

def get_person_IMC(weight, height):
  return weight / height **2

def get_person_info():
  return f'Your name is {name}, you\'re {age} years old, actually you\'re {height} tall, weigh {weight} KG and were born in {get_person_birth_year(age=age, current_year=current_year)}'

def get_IMC_rating(personIMC):
  if (personIMC < 18.5):
    return 'thinness'
  elif (personIMC > 18.5 and personIMC < 25):
    return 'regular'
  elif (personIMC > 25 and personIMC < 30):
    return 'overweight'
  elif (personIMC > 30 and personIMC < 40):
    return 'obesity'
  else:
    return 'severe obesity'

print(get_person_info())
person_IMC = get_person_IMC(weight, height)
print(f'Your current IMC is {get_IMC_rating(personIMC=person_IMC)}')