guests = ['Moraes Moreira', 'Michael Jackson', 'Galadriel']

for i in guests:
    print(f'Hi dear {i}. Would you like to have dinner?')

j = 0

while j < len(guests):
    if guests[j] == 'Michael Jackson':
        guests[j] = 'Amy Winehouse'
    j += 1

print(f"Michael Jackson isn't coming. Inviting new guests: \n")

for g in guests:
    print(f'Hi dear {g}. Would you like to have dinner?')
