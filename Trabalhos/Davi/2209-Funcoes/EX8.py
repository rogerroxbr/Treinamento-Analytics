def mdc(num1, num2):
    if num2 == 0:
        return num1
    return mdc(num2, num1 % num2)


def mmc(num1, num2):
    return abs(num1 * num2) / mdc(num1, num2)


print(mdc(10, 5))
print(mmc(32, 24))
print(mdc(5, 3))
