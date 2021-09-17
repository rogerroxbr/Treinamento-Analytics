a = int(input("First value: "))
b = int(input("Second value: "))

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

if a > b:
    print("The first number is the higher!")
elif b > a:
    print("The second number is the higher!")
else:
    print("The numbers are the same!")