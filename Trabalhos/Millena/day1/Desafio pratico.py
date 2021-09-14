name = "Millena"
age = 23
current_year = 2021
height = 1.71
weight = 79.0
yearOfBirth = current_year - age
IMC = weight / (height ** 2)

print(f'The year of birth of: {name} is {yearOfBirth}, based on Current year {current_year} and their age {age}.'
      f' Their IMC is {IMC:.2f}. Based on the values {height} and {weight}.')

