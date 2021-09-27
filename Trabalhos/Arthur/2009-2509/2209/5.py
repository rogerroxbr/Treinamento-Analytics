def fibonacci_recursiva(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    a = 0
    b = 1
    contador = 1
    soma = 0
    while(contador <= n):
        contador += 1
        a = b
        b = soma
        soma = a + b
    return soma

print("\n")

print(fibonacci_recursiva(5))
print(fibonacci_recursiva(7))

print("\n")

print(fibonacci(5))
print(fibonacci(7))