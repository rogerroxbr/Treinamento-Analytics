import time

x = 0
print('0 a 100: ')
while x <= 100:
    print(x)
    x+= 1

time.sleep(3)

print('\n')
print('50 a 100: ')
x = 50
while x <= 100:
    print(x)
    x+= 1

time.sleep(3)

print('\n')
print('10 a 0: ')
x = 10
while x >= 0:
    print(x)
    x-= 1
    time.sleep(1)
