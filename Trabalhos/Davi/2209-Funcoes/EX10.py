def fibonacci(n):
    p = 0
    s = 1
    while n > 0:
        p = s
        s = s + p
        n -= 1
        print(p)
    return p


fibonacci(10)
