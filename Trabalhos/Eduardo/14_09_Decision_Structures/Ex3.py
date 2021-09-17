a = int(input("Value A: "))
b = int(input("Value B: "))
c = int(input("Value C: "))

if a > b and a > c:
    print(f"Value A is the highest. Value: {a}")
elif b > c:
    print(f"Value B is the highest. Value: {b}")
else:
    print(f"Value C is the highest. Value: {c}")

if a < b and a < c:
    print(f"Value A is the lowest. Value: {a}")
elif b < c:
    print(f"Value B is the lowest. Value: {b}")
else:
    print(f"Value C is the lowest. Value: {c}")