name = input("Digite seu nome :")
age = int(input("Digite sua idade "))
height = float(input("Digite sua altura "))
weight = int(input("Digite seu peso "))
thisYear = 2021

birthYear = thisYear - age
IMC = (weight)/(height**2)

print(f"O {name} tem {age} anos, {height}m de altura e seu ano de nascimento é {birthYear}")
print(f"O seu IMC é {IMC}")
