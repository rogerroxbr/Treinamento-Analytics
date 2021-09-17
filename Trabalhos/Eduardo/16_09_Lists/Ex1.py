# Lists are used to store multiple items in a single variable.

grades = [0] * 7
sum = 0
x = 0

while x < 7:
    grades[x] = float(input(f"Grade {x}: "))
    sum += grades[x]
    x += 1

x = 0
while x < 7:
    print(f"Grade {x}: {grades[x]:6.2f}")
    x += 1

print(f"Average: {sum/x:5.2f}")