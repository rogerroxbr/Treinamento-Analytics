a = []
b = []

print("First list ---")
while True:
    i = int(input("Enter a number (0 to exit): "))
    if i == 0:
        break
    # The append() method appends an element to the end of the list.
    a.append(i)

print("Second list ---")
while True:
    i = int(input("Enter a number (0 to exit): "))
    if i == 0:
        break
    b.append(i)

# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
a.extend(b)

print(a)